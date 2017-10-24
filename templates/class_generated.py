{{ "### extends 'class_cur.gen.py'" }}
{% set class_name = "GX" ~ cl.name %}

### block ClassImplementation
{{ "### block ClassImplementation" }}
# NOTICE: Do not edit anything here, it is generated code
class {{ class_name }}:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.Wrap{{ cl.name }}(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> '{{ class_name }}':
        """
        A null (undefined) instance of :class:`{{ class_name }}`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`{{ class_name }}` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`{{ class_name }}`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle

{% for key, method_group in cl.method_groups.items() %}
# {{ key }}
{% for method in method_group %}
{% if not method.is_destroy_method %}
{% if method.is_static %}    @classmethod{% endif %}
    def {{ method.ext_method_name }}({{ method.py_first_parm }}{% for param in method.py_parameters %}, {{ param.name }}: {{ param.py_type_hint }}{% endfor %}) -> {{ method.return_hint }}:
        {{ method.assign_return_values }}{{ method.call_wrapper }}({{ method.pass_py_parameters }})
        {{ method.py_return }}
{% endif %}
{% endfor %}

{% endfor %}

{{ "### endblock ClassImplementation" }}
### endblock ClassImplementation
