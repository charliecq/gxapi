{{ "//*** extends 'gxlib_cur.gen.h'" }}

//*** block Header
{{ "//*** block Header" }}
//** NOTICE: Do not edit anything here, it is generated code

/**
* @file {{ cl.name.lower() }}_gxlib.h
* @date {{ date.date().isoformat() }}
* @brief File containing {{ cl.name }} GX C API constant and function declarations
*/

/**
* @defgroup {{ cl.name }}_Module {{ cl.name }}
* {{ cl.doc | doc_sanitize | comment(prefix="* ") }}
{% if cl.notes %}*
* Notes:
*
* {{ cl.notes | doc_sanitize | comment(prefix="* ") }}
*
{% endif %}* @{
*/

#pragma once
#ifndef H{{ cl.name }}_H_DEFINED
#define H{{ cl.name }}_H_DEFINED

#ifdef __cplusplus
extern "C" {
#endif
{{ "//*** endblock Header" }}
//*** endblock Header


//*** block Generated
{{ "//*** block Generated" }}
//** NOTICE: Do not edit anything here, it is generated code

{% for _, define in cl.defines.items() %}{% if not define.is_null_handle %}
/**
* @name {{ define.name }} Definitions{% if define.doc %}
* 
* {{ define.doc | doc_sanitize | comment(prefix="* ") }}{% endif %}
*/
///@{
{%-for constant in define.constants %}
/** 
* {{ constant.name }}{% if constant.doc %}
* 
* {{ constant.doc | doc_sanitize | comment(prefix="* ") }}{% endif %}
*/
#define {{ constant.name }} {{ constant.gxlib_value }}{%- endfor %}
///@}
{% else %}
/**
* {{ define.name }}{% if define.doc %}
*
* {{ define.doc | doc_sanitize | comment(prefix="* ") }}{% endif %}
*/
#define {{ define.name }} 0
{% endif %}{% endfor %}
{% for key, method_group in cl.method_groups.items() %}
/**
* @name {{ key }} Functions 
*/
///@{
{% for method in method_group %}
/**{%if method.doc %}
* {{ method.doc | doc_sanitize | comment(prefix="* ") }}{% endif %}
*
* @param[in]  p_geo GX Context Pointer{% for param in method.parameters %}
* {{ param.doxy_param }} TODO{% endfor %}{% if method.return_doc %}
* @return {{ method.return_doc | doc_sanitize | comment(prefix="* ") }}{% endif %}
*{% if method.notes %}*
* @par Note 
*      {{ method.notes | doc_sanitize | comment(prefix="* ", extra_spaces=5) }}
*{% endif %}{% if method.see_also %}
* @par See also 
*      {{ method.see_also | doc_sanitize | comment(prefix="* ", extra_spaces=5) }}
*{% endif %}
* @par License 
*      {{ method.availability_info_html }}{% if method.limitations_info %}
* @par Limitations 
*      {{ method.limitations_info }}
{% endif %}
* @version {{ method.version }}
*/
GX_EXPORT {{ method.c_return_type }} {{ method.exposed_name }}(void* p_geo{% for param in method.parameters %}, {{ param.c_type }} {{ param.name }}{% endfor %});
{% endfor %}
///@}
{% endfor %}

{{ "//*** endblock Generated" }}
//*** endblock Generated

//*** block Footer
{{ "//*** block Footer" }}
#ifdef __cplusplus
}
#endif

/** @} */

#endif
{{ "//*** endblock Footer" }}
//*** endblock Footer
