{% set class_name = "GX" ~ cl.name %}
.. _{{ class_name }}:

 
{{ class_name }} class
==================================

{% if cl.name == 'GEOSOFT' %}
{{ cl.doc | doc_sanitize(cl.name) }}
{% else %}.. autoclass:: geosoft.gxapi.{{ class_name }}
   :members:{% endif %}

{% for name, define in cl.defines.items() %}{% if not define.is_null_handle %}
.. _{{ name }}:

{{ name }} constants
-----------------------------------------------------------------------
{% if define.doc %}
{{ define.doc | doc_sanitize(cl.name) }}{% endif %}

{% for constant in define.constants %}.. autodata:: geosoft.gxapi.{{ constant.name }}
    :annotation:
    
    .. autoattribute:: geosoft.gxapi.{{ constant.name }}
{% endfor %}
{% endif %}{% endfor %}	