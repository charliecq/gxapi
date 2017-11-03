{{ "//*** extends 'gxlib_empty.h'" }}

#pragma once
#ifndef H{{ cl.name }}_H_DEFINED
#define H{{ cl.name }}_H_DEFINED

#ifdef __cplusplus
extern "C" {
#endif

{{ "//*** block Header" }}
//*** block Header
//*** endblock Header
{{ "//*** endblock Header" }}

{{ "//*** block Editable" }}
//*** block Editable
//** NOTICE: The code generator will not replace the code in this block
//*** endblock Editable
{{ "//*** endblock Editable" }}

{{ "//*** block Generated" }}
//*** block Generated
//*** endblock Generated
{{ "//*** endblock Generated" }}

#ifdef __cplusplus
}
#endif

#endif