from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('LL2',
                 doc="""
                 local datum lookup creator
                 ll2 methods are used to create :class:`LL2` objects.  :class:`LL2` objects contain
                 latitude, longitude correction lookup tables to convert between datums.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('Create_LL2', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create an empty :class:`LL2` table to be filled",
               see_also=":func:`Destroy_LL2`, :func:`SetRow_LL2`, :func:`Save_LL2`",
               return_type="LL2",
               return_doc=":class:`LL2` Object",
               parameters = [
                   Parameter('lon0', type=Type.DOUBLE,
                             doc="Longitude origin"),
                   Parameter('lat0', type=Type.DOUBLE,
                             doc="Latitude origin"),
                   Parameter('lon', type=Type.DOUBLE,
                             doc="Longitude increment"),
                   Parameter('lat', type=Type.DOUBLE,
                             doc="Latitude increment"),
                   Parameter('lon', type=Type.INT32_T,
                             doc="# longitudes"),
                   Parameter('lat', type=Type.INT32_T,
                             doc="# latitudes"),
                   Parameter('in_ipj', type="IPJ",
                             doc="Input projection"),
                   Parameter('out_ipj', type="IPJ",
                             doc="Output projection")
               ]),

        Method('Destroy_LL2', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ll2_ll', type="LL2",
                             doc="Projection to Destroy")
               ]),

        Method('Save_LL2', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Save an :class:`LL2` to a named resource",
               notes="""
               The named resource is the name of the datum transform define
               inside square brackets in the datum transform name in the
               datumtrf table.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ll2_ll', type="LL2",
                             doc=":class:`LL2` object"),
                   Parameter('name', type=Type.STRING,
                             doc="Named resource")
               ]),

        Method('SetRow_LL2', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Define a row of the :class:`LL2`",
               notes="""
               The correction data is in degrees, added to the input
               datum to product output datum results.
               
               The :class:`VV` lengths must be equal to #longitudes defined
               by :func:`Create_LL2`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ll2_ll', type="LL2",
                             doc=":class:`LL2` object"),
                   Parameter('row', type=Type.INT32_T,
                             doc="The row to set"),
                   Parameter('lon_vv', type="VV",
                             doc="Longitude corrections"),
                   Parameter('lat_vv', type="VV",
                             doc="Latitude corrections")
               ])
    ]
}

