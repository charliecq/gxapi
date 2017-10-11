import os
from gen import CodeGeneratorBase
from spec import Type, Availability, Constant, Define, Parameter, Method, Class
import textwrap

class GXLibConstant(Constant):
    def __init__(self, other):
        super().construct_copy(other)

    def render(self):
        if self.type == Type.STRING:
            return self.generator.get_template('#define {{ constant.name }} "{{ constant.value }}"').render(constant=self)
        else:
            return self.generator.get_template('#define {{ constant.name }} {{ constant.value }}').render(constant=self)

class GXLibDefine(Define):
    def __init__(self, other):
        super().construct_copy(other)

    def render(self):
        return self.generator.get_template("""
//===========================================================================================================
//
// Define {{ define.name }}
//
// {% if define.doc %}{{ define.doc | doc_sanitize | comment }}{% endif %}
//
{%- for constant in define.constants %}
// {{ constant.name }}
// {% if constant.doc %}{{ constant.doc | doc_sanitize | comment }}{% endif %}
//
{%- endfor %}
//===========================================================================================================
{% for constant in define.constants %}
{{ constant.render() }}
{%- endfor %}

""").render(define=self)

def get_GXLib_type(type):
    if type == Type.DOUBLE:
        return "real"
    elif type == Type.INT32_T:
        return "int"
    elif type == Type.STRING:
        return "string"
    else:
        if '0' <= type[0] and type[0] <= '9':
            return "H" + type
        else:
            return type


class GXLibParameter(Parameter):
    def __init__(self, other):
        super().construct_copy(other)

    @property
    def GXLib_type(self):
        if self.is_ref:
            return 'var {}'.format(get_GXLib_type(self.type))
        else:
            return get_GXLib_type(self.type)

    def render_GXLib_doc(self, indent_spaces):
        if self.doc:
            return self.generator.get_template(
                '{% set type_len = param.GXLib_type|length %}{{ param.doc | doc_sanitize | comment(comment_first_line=True) | indent(indent_spaces-type_len, True) | indent(indent_spaces+1) }}'
            ).render(param=self, indent_spaces=indent_spaces)
        else:
            return self.generator.get_template(
                '{% set type_len = param.GXLib_type|length %}{{ "//" | indent(indent_spaces-type_len, True) }}').render(param=self, indent_spaces=indent_spaces)



class GXLibMethod(Method):
    def __init__(self, other):
        super().construct_copy(other)

    def render(self):
        return self.generator.get_template("""{% set name_len = method.exposed_name|length %} {% set ret_len = method.GXLib_return_type|length %} {% set avail_len = method.availability_prefix|length %}
//-----------------------------------------------------------------------------------------------------------
// {{ method.exposed_name }} {%if method.doc %}{{ method.doc | doc_sanitize | comment(extra_spaces=name_len+1) }}{% endif %}
{% if method.return_doc %}//
// Returns {{ ' ' * (name_len - 7) }}{{ method.return_doc | doc_sanitize | comment(extra_spaces=name_len+1) }}
{% endif %}{% if method.notes %}//
// Notes {{ ' ' * (name_len - 5) }}{{ method.notes | doc_sanitize | comment(extra_spaces=name_len+1) }}
{% endif %}{% if method.see_also %}//
// See also {{ ' ' * (name_len - 8) }}{{ method.see_also | doc_sanitize | comment(extra_spaces=name_len+1) }}
{% endif %}//
// Available {{ ' ' * (name_len - 9) }}{{ method.version }}
//-----------------------------------------------------------------------------------------------------------

{{ method.availability_prefix }} {{ method.GXLib_return_type }} {{ method.exposed_name }}{{ method.render_parameters() | indent(avail_len+name_len + ret_len + 2) }}
{{ method.string_macro }}""").render(method=self)

    @property
    def string_macro(self):
        method_name = self.exposed_name
        param_replacements = {p.size_of_param: p.name for p in self.parameters if p.size_of_param}
        if len(param_replacements) > 0:

            if method_name.startswith('I') or method_name.startswith('_'):
                macro_name = method_name[1:]
            elif method_name.startswith('iI'):
                macro_name = 'i{}'.format(method_name[2:])
            elif method_name.startswith('Gt'):
                macro_name = 'Get{}'.format(method_name[2:])
            else:
                macro_name = '_{}'.format(method_name)
            macro_params = ''
            method_params = ''

            for param in self.parameters:
                if method_params:
                    method_params += ', '
                if param.name in param_replacements:
                    method_params += 'sizeof({})'.format(param_replacements[param.name])
                else:
                    if macro_params:
                        macro_params += ', '
                    macro_params += param.name
                    method_params += param.name
            return '#define {}({}) {}({})\n'.format(macro_name, macro_params, method_name, method_params)
        else:
            return ''

    def render_parameters(self):
        max_type_len = 0
        for param in self.parameters:
            max_type_len = max(max_type_len, len(param.GXLib_type))
        return self.generator.get_template("""{% for param in parameters %}{% if loop.first %}({% else %} {% endif %}{{ param.GXLib_type }}{% if not loop.last %}, {{ param.render_GXLib_doc(max_type_len + 2) }}
{% else %});{{ param.render_GXLib_doc(max_type_len + 2) }}{% endif %}{% else %}();{% endfor %}""").render(parameters=self.parameters, max_type_len=max_type_len)

    @property
    def GXLib_return_type(self):
        return get_GXLib_type(self.return_type)

    @property
    def availability_prefix(self):
        if self.availability == Availability.PUBLIC:
            prefix = 'public'
        elif self.availability == Availability.EXTENSION:
            prefix = 'extended'
        else:
            prefix = 'licensed'
        if self.is_app:
            prefix += '_app'
        return '[_{}]'.format(prefix)


class GXLibClass(Class):
    def __init__(self, other):
        super().construct_copy(other)

    def render(self):
        return self.generator.get_template("""
{{- cl.header -}}
{{- cl.GXLib_definitions -}}
{{- cl.GXLib_methods -}}
{{- cl.footer -}}
""").render(cl=self)

    @property
    def header(self):
        return self.generator.get_template("""
//===========================================================================================================
//
// Class {{ cl.name }}
//
//-----------------------------------------------------------------------------------------------------------
//
// {{ cl.doc | doc_sanitize | comment }}
//
{% if cl.notes %}//-----------------------------------------------------------------------------------------------------------
// Notes
//
// {{ cl.notes | doc_sanitize | comment }}
//
{% endif %}//-----------------------------------------------------------------------------------------------------------

#ifndef H{{ cl.name }}_GXLib_DEFINED
#define H{{ cl.name }}_GXLib_DEFINED

{% if cl.verbatim_GXLib_defines %}{{ cl.verbatim_GXLib_defines }}{% endif %}

""").render(cl=self)

    @property
    def footer(self):
        return self.generator.get_template('#endif').render(cl=self)

    @property
    def GXLib_definitions(self):
        return self.generator.get_template("""
{% for _, define in cl.defines.items() %}
{{ define.render() }}
{% endfor %}
""").render(cl=self)

    @property
    def gxlib_methods(self):
        if len(self.method_groups) == 1:
            method_group = next(iter(self.method_groups.values()))
            return self.render_method_group(method_group)
        else:
            return self.generator.get_template("""
{% for key, method_group in cl.method_groups.items() %}
//===========================================================================================================
//
// {{ key }}
//
//===========================================================================================================

{{ cl.render_method_group(method_group) }}
{% endfor %}
""").render(cl=self)

    def render_method_group(self, method_group):
        return self.generator.get_template("""
{% for method in methods %}
{{ method.render() }}
{% endfor %}
""").render(methods=method_group)


class GXLibCodeGenerator(CodeGeneratorBase):
    def doc_sanitize(self, s):
        s = self.re_class.sub(r'\1', s)
        s = self.re_def.sub(r'\1', s)
        s = self.re_func.sub(r'\1', s)
        s = self.re_def_val.sub(r'\1', s)

        return textwrap.dedent(s).strip()


    @property
    def header(self):
        return """
#pragma once
/*
=====================================================================
Geosoft GX Wapper Function Headers
=====================================================================
*/

// Legacy defines

#define GX_WRAPPER_FUNC  __declspec(dllexport)
#define GX_STANDARD_FUNC
#define GX_WRAPPER_CALL  _cdecl
#define GX_STANDARD_CALL _stdcall

#define GX_OBJECT_PTR    void*

#define GX_VAR
#define GX_CONST         const

#define GX_VOID          void
#define GX_LONG          int32_t
#define GX_DOUBLE        double
#define GX_HANDLE        int32_t

#define GX_LONG_PTR      int32_t*
#define GX_DOUBLE_PTR    double*
#define GX_HANDLE_PTR    int32_t*
#define GX_ASTR_PTR      char*
#define GX_WSTR_PTR      wchar_t*
#if GEO_UTF8
   #define GX_STR_PTR       GX_ASTR_PTR
#elif _UNICODE
   #define GX_STR_PTR       GX_WSTR_PTR
#else
   #define GX_STR_PTR       GX_ASTR_PTR
#endif

#ifdef __cplusplus
   extern "C" {
#endif

"""
    def __init__(self):
        super().__init__(constant_type=GXLibConstant, define_type=GXLibDefine, parameter_type=GXLibParameter,
                         method_type=GXLibMethod, class_type=GXLibClass)
        self._remove_no_gxlib_classes_and_methods()
        self.j2env.filters['doc_sanitize'] = self.doc_sanitize

    def _remove_no_gxlib_classes_and_methods(self):
        classes_to_remove = [ key for key, cl in self.classes.items() if cl.no_GXLib ]
        for key in classes_to_remove:
            self.classes.pop(key, None)
        for _, cl in self.classes.items():
            for g_k, methods in cl.method_groups.items():
                cl.method_groups[g_k] = [m for m in methods if not m.no_GXLib]
