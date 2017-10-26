from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('3DV',
                 doc="TODO...")


gx_defines = [
    Define('GEO3DV_OPEN',
           doc="Open Modes",
           constants=[
               Constant('GEO3DV_MVIEW_READ', value='0', type=Type.INT32_T),
               Constant('GEO3DV_MVIEW_WRITEOLD', value='2', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('OpenMVIEW_3DV', module='geoengine.map', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Open :class:`3DV`'s 3D :class:`MVIEW`",
               return_type="MVIEW",
               return_doc=":class:`MVIEW`, aborts on failure",
               parameters = [
                   Parameter('o3dv', type="3DV",
                             doc=":class:`3DV` Object"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`GEO3DV_OPEN`")
               ]),

        Method('ICopyToMAP_3DV', module='geoengine.map', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy the :class:`3DV`'s 3D :class:`MVIEW` into a map.",
               notes="""
               A :class:`3DV` packs all source files. This functions creates an unpacked map and
               unpacks the packed files in the same way that UnPackFilesEx in the :class:`MAP` class does.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dv', type="3DV",
                             doc=":class:`3DV` Object"),
                   Parameter('map', type="MAP",
                             doc=":class:`MAP` Object"),
                   Parameter('mview', type=Type.STRING,
                             doc="Desired new view name"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="X minimum in mm"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Y minimun in mm"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="X maximum in mm"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Y maximum in mm"),
                   Parameter('force_overwrite', type=Type.INT32_T,
                             doc="(0 - Produce errors for conflicting unpacked files, 1 - Force overwrites of conflicting unpacked files)"),
                   Parameter('new_view', type=Type.STRING, is_ref=True, size_of_param='new_view_size',
                             doc="New view name created"),
                   Parameter('new_view_size', type=Type.INT32_T, default_length='MVIEW_NAME_LENGTH',
                             doc="Length of new view name"),
                   Parameter('problem_files', type=Type.STRING, is_ref=True, size_of_param='problem_files_size',
                             doc="List of files that are problematic returned"),
                   Parameter('problem_files_size', type=Type.INT32_T, default_length='STR_MULTI_FILE',
                             doc="Length of problematic files buffer")
               ]),

        Method('CreateNew_3DV', module='geoengine.map', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a new :class:`3DV`.",
               return_type="3DV",
               return_doc=":class:`3DV` Object",
               parameters = [
                   Parameter('file_name', type=Type.STRING,
                             doc=":class:`3DV` file name"),
                   Parameter('mview', type="MVIEW",
                             doc="3D :class:`MVIEW` to create new :class:`3DV` from")
               ]),

        Method('Open_3DV', module='geoengine.map', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Open an existing :class:`3DV`.",
               return_type="3DV",
               return_doc=":class:`3DV` Object",
               parameters = [
                   Parameter('file_name', type=Type.STRING,
                             doc=":class:`3DV` file name")
               ]),

        Method('FromMap_3DV', module='geoengine.map', version='9.2.0',
               availability=Availability.PUBLIC, 
               doc="Get an :class:`3DV` from :class:`MAP` handle (e.g. from :func:`Lock_EMAP` on open geosoft_3dv document in project)",
               return_type="3DV",
               return_doc=":class:`3DV` Object",
               parameters = [
                   Parameter('map', type="MAP",
                             doc=":class:`MAP` Object")
               ]),

        Method('CRC3DV_3DV', module='geoengine.map', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Generate an XML CRC of a :class:`3DV`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dv', type="3DV",
                             doc=":class:`3DV` object"),
                   Parameter('crc', type=Type.INT32_T, is_ref=True,
                             doc="CRC returned"),
                   Parameter('file', type=Type.STRING,
                             doc="Name of xml to generate (.zip added)")
               ])
    ]
}

