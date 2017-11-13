{{ "### extends 'init_cur.gen.py'" }}

### block Constants
{{ "### block Constants" }}
# NOTICE: Do not edit anything here, it is generated code

import struct

### for cl in classes

#
# GX{{ cl }} Constants
# 

{% for name, define in classes[cl].defines.items() %}{% if not define.is_null_handle %}
{% if define.doc %}
#
# {{ define.name }} constants
#
# {{ define.doc | doc_sanitize(cl) | comment(prefix="# ") }}{% endif %}
{% for constant in define.constants %}{% if constant.doc %}
#: {{ constant.doc | doc_sanitize(cl) | comment(prefix="#: ") }}
{% else %}
#: {{ constant.doc_name }}
{% endif %}{{ constant.name }} = {{ constant.python_value }}{% endfor %}{% endif %}{% endfor %}	

### endfor
{{ "### endblock Constants" }}
### endblock Constants

### block ClassImports
{{ "### block ClassImports" }}
# NOTICE: Do not edit anything here, it is generated code

__all__ = [

    'GXContext',
### for cl in classes
{% if not classes[cl].no_cpp and not cl == 'GEO' %}    'GX{{ cl }}',{% endif %}
### endfor
]

from .GXContext import GXContext
### for cl in classes
{% if not classes[cl].no_cpp and not cl == 'GEO' %}from .GX{{ cl }} import GX{{ cl }}{% endif %}
### endfor

{{ "### endblock ClassImports" }}
### endblock ClassImports


