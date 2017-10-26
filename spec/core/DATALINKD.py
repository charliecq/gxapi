from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DATALINKD',
                 doc="DATALINK Display object.")





gx_methods = {
    'Miscellaneous': [

        Method('CreateArcLYR_DATALINKD', module='geoengine.map', version='6.4.0',
               availability=Availability.LICENSED, 
               doc="Create an :class:`DATALINKD` object from a ArcGIS LYR file",
               notes="Needs ArcEngine licence.",
               return_type="DATALINKD",
               return_doc=":class:`DATALINKD` handle, terminates if creation fails",
               parameters = [
                   Parameter('arc_lyr_file', type=Type.STRING,
                             doc="Arc LYR file name")
               ]),

        Method('CreateArcLYREx_DATALINKD', module='geoengine.map', version='9.0.0',
               availability=Availability.LICENSED, 
               doc="Create an :class:`DATALINKD` object from a ArcGIS LYR file",
               notes="Needs ArcEngine licence.",
               return_type="DATALINKD",
               return_doc=":class:`DATALINKD` handle, terminates if creation fails",
               parameters = [
                   Parameter('arc_lyr_file', type=Type.STRING,
                             doc="Arc LYR file name"),
                   Parameter('o3d_group', type=Type.INT32_T,
                             doc="Display as 3D Group? (as opposed to bitmap on plane)")
               ]),

        Method('CreateArcLYRFromTMP_DATALINKD', module='geoengine.map', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Create an :class:`DATALINKD` object from a temporary ArcGIS LYR file",
               notes="Needs ArcEngine licence.",
               return_type="DATALINKD",
               return_doc=":class:`DATALINKD` handle, terminates if creation fails",
               parameters = [
                   Parameter('arc_lyr_file', type=Type.STRING,
                             doc="Arc LYR file name")
               ]),

        Method('CreateArcLYRFromTMPEx_DATALINKD', module='geoengine.map', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Create an :class:`DATALINKD` object from a temporary ArcGIS LYR file",
               notes="Needs ArcEngine licence.",
               return_type="DATALINKD",
               return_doc=":class:`DATALINKD` handle, terminates if creation fails",
               parameters = [
                   Parameter('arc_lyr_file', type=Type.STRING,
                             doc="Arc LYR file name"),
                   Parameter('o3d_group', type=Type.INT32_T,
                             doc="Display as 3D Group? (as opposed to bitmap on plane)")
               ]),

        Method('CreateBING_DATALINKD', module='geoengine.map', version='8.0.0',
               availability=Availability.LICENSED, 
               doc="Create an :class:`DATALINKD` object for a BING dataset",
               return_type="DATALINKD",
               return_doc=":class:`DATALINKD` handle, terminates if creation fails",
               parameters = [
                   Parameter('layer', type=Type.INT32_T,
                             doc="0 = Aerial, 1 = Road")
               ]),

        Method('Destroy_DATALINKD', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`DATALINKD`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('datalinkd', type="DATALINKD",
                             doc=":class:`DATALINKD` to destroy.")
               ]),

        Method('GetExtents_DATALINKD', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the data extents of the DATALINK Display object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('datalinkd', type="DATALINKD",
                             doc=":class:`DATALINKD` object"),
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="Min X"),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="Max X"),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="Min Y"),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="Max Y")
               ]),

        Method('GetIPJ_DATALINKD', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the projection of the DATALINK Display object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('datalinkd', type="DATALINKD",
                             doc=":class:`DATALINKD` object"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` object to set the projection to")
               ])
    ]
}

