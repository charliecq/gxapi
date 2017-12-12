<h1 id="spec">spec</h1>


<h2 id="spec.gxclass">spec.gxclass</h2>


<h3 id="spec.gxclass.Class">Class</h3>

```python
Class(self, name, doc=None, notes=None, see_also=None, handle_name=None, no_gxh=False, no_csharp=False, no_cpp=False, next_gen=False)
```

API specification for a GX class. 

A specification module should have at least one of these assigned to 
an attribute called __gx_class__.

__Arguments__

- __name (str)__: Class name
- __doc (str)__: Doc string with class summary
- __notes (str)__: Doc string containing verbose notes (optional)
- __see_also (str)__: Doc string containing see-also type references (optional)
- __handle_name (str)__: GXC API variable type override (does not affect other languages)
- __no_gxh (bool)__: Not available in GXC API when 'True'
- __no_csharp (bool)__: Not available in .Net API when 'True' (nor Python)
- __no_cpp (bool)__: Not available in C++ API when 'True' (nor Python)
- __next_gen (bool)__: Not a legacy class. Implies __no_gxh__

__Example__

```python
from .. import Class

# This is a very simple example class with only a doc string
gx_class = Class('GXSOMECLASS',
             doc="""
             This class' can be used to...
             It isdirectly related to the :class:`GXSOMEOTHERCLASS` class.
             """)
```
See also: `spec.gxmethod`

<h2 id="spec.gxdefs">spec.gxdefs</h2>


<h2 id="spec.gxmethod">spec.gxmethod</h2>


