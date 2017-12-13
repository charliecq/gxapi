{{ "//*** extends 'class_cur.gen.gxh'" }}

//*** block Header
{{ "//*** block Header" }}
// NOTICE: Do not edit anything here, it is generated code
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

{{ "//*** endblock Header" }}
//*** endblock Header


//*** block Generated
{{ "//*** block Generated" }}
// NOTICE: Do not edit anything here, it is generated code

{% for _, define in cl.defines.items() %}
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
#define {{ constant.name }} {{ constant.gxh_value }}
{%- endfor %}

{% endfor %}


{% for key, method_group in cl.method_groups.items() %}
//===========================================================================================================
//
// {{ key }}
//
//===========================================================================================================

{% for method in method_group %}
{% set name_len = method.exposed_name|length %} {% set ret_len = method.gxh_return_type|length %} {% set avail_len = method.availability_prefix|length %}
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

{{ method.availability_prefix }} {{ method.gxh_return_type }} {{ method.exposed_name }}{{ method.render_parameters() | indent(avail_len+name_len + ret_len + 2) }}
{{ method.string_macro }}
{% endfor %}
{% endfor %}


{{ "//*** endblock Generated" }}
//*** endblock Generated

#endif