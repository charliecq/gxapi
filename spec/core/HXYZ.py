from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('HXYZ',
                 doc="""
                 High Performance Data Point Storage. This is used
                 to put Point data on a DAP server. It is compressed
                 and uses a Quad-Tree design to allow very high speed
                 data extraction. It is also multi-threaded.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('Create_HXYZ', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Create a handle to an :class:`HXYZ` object",
               return_type="HXYZ",
               return_doc=":class:`HXYZ` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('Destroy_HXYZ', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`HXYZ`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('hxyz', type="HXYZ",
                             doc=":class:`HXYZ` to destroy.")
               ]),

        Method('GetMETA_HXYZ', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Get the metadata of a grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('hxyz', type="HXYZ",
                             doc=":class:`HXYZ` object"),
                   Parameter('meta', type="META",
                             doc=":class:`META` object to save :class:`HXYZ`'s meta to")
               ]),

        Method('hCreateDB_HXYZ', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Make an :class:`HXYZ` from GDB",
               return_type="HXYZ",
               return_doc=":class:`HXYZ` object",
               parameters = [
                   Parameter('db', type="DB",
                             doc=":class:`DB` handle"),
                   Parameter('gvv', type="VV",
                             doc=":class:`VV` of channels to export"),
                   Parameter('name', type=Type.STRING,
                             doc="Name of :class:`HXYZ` object")
               ]),

        Method('hCreateSQL_HXYZ', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Make an :class:`HXYZ` from SQL Query",
               return_type="HXYZ",
               return_doc=":class:`HXYZ` object",
               parameters = [
                   Parameter('template', type=Type.STRING,
                             doc="Template File Name"),
                   Parameter('x', type=Type.STRING,
                             doc="X field name"),
                   Parameter('y', type=Type.STRING,
                             doc="Y field name"),
                   Parameter('z', type=Type.STRING,
                             doc="Z field name"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection of data values"),
                   Parameter('name', type=Type.STRING,
                             doc="Name of :class:`HXYZ` object")
               ]),

        Method('SetMETA_HXYZ', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Set the metadata of a grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('hxyz', type="HXYZ",
                             doc="Source :class:`HXYZ`"),
                   Parameter('meta', type="META",
                             doc=":class:`META` object to add to :class:`HXYZ`'s meta")
               ])
    ]
}

