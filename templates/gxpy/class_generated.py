{{ "### extends 'class_cur.gen.py'" }}
{% set class_name = "GX" ~ cl.name %}
### block ClassImports
{{ "### block ClassImports" }}
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
{% for i in cl.gxapi_imports %}from .{{ i }} import {{ i }}
{% endfor %}

{{ "### endblock ClassImports" }}
### endblock ClassImports


### block ClassImplementation
{{ "### block ClassImplementation" }}
# NOTICE: Do not edit anything here, it is generated code
class {{ class_name }}(gxapi_cy.Wrap{{ cl.name }}):
    """
    {{ class_name }} class.

    {{ cl.doc | doc_sanitize(cl.name) | indent }}{% if cl.notes %}

    **Note:**

    {{ cl.notes | doc_sanitize(cl.name) | indent }}{% endif %}
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `{{ class_name }} <geosoft.gxapi.{{ class_name }}>`
        
        :returns: A null `{{ class_name }} <geosoft.gxapi.{{ class_name }}>`
        :rtype:   {{ class_name }}
        """
        return {{ class_name }}()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0


{% for key, method_group in cl.method_groups.items() %}
# {{ key }}
{% for method in method_group %}
{% if not method.is_destroy_method %}
{% if method.is_static %}    @classmethod{% endif %}
    def {{ method.ext_method_name }}({{ method.py_first_parm }}{% for param in method.py_parameters %}, {{ param.name }}{% endfor %}):
        """
        {{ method.doc | doc_sanitize(cl.name) | indent(8) }}
        {% for param in method.py_parameters %}{% if param.doc %}
        :param {{ param.name }}: {{ method.param_indent_start(param) }} {{ param.doc | doc_sanitize(cl.name) | indent(method.param_indent) }}{% endif %}{% endfor %}{% for param in method.py_parameters %}
        :type  {{ param.name }}: {{ method.param_indent_start(param) }} {{ param.py_type }}{% endfor %}{% if not method.returns_void %}{% if method.return_doc %}

        :returns:   {{ method.return_indent_start }} {{ method.return_doc | doc_sanitize(cl.name) | indent(method.param_indent) }}{% endif %}
        :rtype:     {{ method.return_indent_start }} {{ method.py_return_type }}{% endif %}

        .. versionadded:: {{ method.version }}

        **License:** {{ method.availability_info_rst }}{% if method.limitations_info %}

        **Limitations:** {{ method.limitations_info }}{% endif %}{% if method.notes %}

        **Note:** {{ method.notes | doc_sanitize(cl.name) | indent(8) }}{% endif %}{% if method.see_also %}

        .. seealso::

            {{ method.see_also | doc_sanitize(cl.name) | indent(12) }}{% endif %}
        """
        {{ method.assign_return_values }}{{ method.call_wrapper }}({{ method.pass_py_parameters }})
        {{ method.py_return }}
{% endif %}
{% endfor %}

{% endfor %}

{{ "### endblock ClassImplementation" }}
### endblock ClassImplementation
