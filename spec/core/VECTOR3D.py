from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('VECTOR3D',
                 doc=":class:`VECTOR3D` Display object.")





gx_methods = {
    'Miscellaneous': [

        Method('Destroy_VECTOR3D', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`VECTOR3D`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vector_3d', type="VECTOR3D",
                             doc=":class:`VECTOR3D` to destroy.")
               ]),

        Method('GetITR_VECTOR3D', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`ITR` of the :class:`VECTOR3D`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vector_3d', type="VECTOR3D",
                             doc=":class:`VECTOR3D` object"),
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object")
               ]),

        Method('SetITR_VECTOR3D', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Set the :class:`ITR` of the :class:`VECTOR3D`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vector_3d', type="VECTOR3D",
                             doc=":class:`VECTOR3D` object"),
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object")
               ])
    ]
}

