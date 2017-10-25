{{ "### extends 'init_cur.gen.py'" }}

### block Constants
{{ "### block Constants" }}
# NOTICE: Do not edit anything here, it is generated code
### for cl in classes

# BEGIN GX{{ cl }} Constants
# NOTICE: Do not edit anything here, it is generated code

{% for name, define in classes[cl].defines.items() %}{% if not name == "GEO_BOOL" and not define.is_null_handle %}
{% for constant in define.constants %}
{{ constant.name }} = {{ constant.python_value }}
{% endfor %}
{% endif %}{% endfor %}	

# BEGIN GX{{ cl }} Constants

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


