from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('USERMETA',
                 doc="""
                 The :class:`USERMETA` class handles user style metadata tied to real
                 data.
                 """)


gx_defines = [
    Define('USERMETA_FORMAT',
           doc=":class:`USERMETA` Format Types",
           constants=[
               Constant('USERMETA_FORMAT_DEFAULT', value='-1', type=Type.INT32_T,
                        doc="Use the standard type for the system"),
               Constant('USERMETA_FORMAT_ISO', value='0', type=Type.INT32_T,
                        doc="ISO 19139 standard"),
               Constant('USERMETA_FORMAT_FGDC', value='1', type=Type.INT32_T,
                        doc="FGDC Metadata Standard")
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates an empty :class:`USERMETA` object",
               return_type="USERMETA",
               return_doc=":class:`USERMETA` Object",
               parameters = [
                   Parameter('format', type=Type.INT32_T,
                             doc=":def:`USERMETA_FORMAT` Type of Meta to create")
               ]),

        Method('CreateS_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`USERMETA` from a file",
               return_type="USERMETA",
               return_doc=":class:`USERMETA` Object",
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('Destroy_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroyes the :class:`USERMETA` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA",
                             doc="Projection to Destroy")
               ]),

        Method('GetDataCreationDate_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Data Creation Date",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('date', type=Type.DOUBLE, is_ref=True,
                             doc="Date")
               ]),

        Method('GetExtents2d_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the 2d Extents",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="MinX"),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="MinY"),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="MaxX"),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="MaxY")
               ]),

        Method('GetExtents3d_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the 3d Extents",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="MinX"),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="MinY"),
                   Parameter('min_z', type=Type.DOUBLE, is_ref=True,
                             doc="MinZ"),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="MaxX"),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="MaxY"),
                   Parameter('max_z', type=Type.DOUBLE, is_ref=True,
                             doc="MaxZ")
               ]),

        Method('GetIPJ_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`IPJ`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('ipj', type="IPJ",
                             doc="Date")
               ]),

        Method('GetMetaCreationDate_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Meta Creation Date",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('date', type=Type.DOUBLE, is_ref=True,
                             doc="Date")
               ]),

        Method('GetXMLFormat_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the XML Format",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('format', type=Type.INT32_T, is_ref=True,
                             doc=":def:`USERMETA_FORMAT`")
               ]),

        Method('iCompare_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Compare 2 :class:`USERMETA`'s",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('usermeta1', type="USERMETA",
                             doc="First :class:`USERMETA`"),
                   Parameter('usermeta2', type="USERMETA",
                             doc="Second UERMETA")
               ]),

        Method('IGetDataCreator_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Data Creator",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('data_creator', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="DataCreator returned"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Maximum name size")
               ]),

        Method('IGetFormat_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the File Format",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('format', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Title returned"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Maximum name size")
               ]),

        Method('IGetMetaCreator_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Meta Creator",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('meta_creator', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="MetaCreator returned"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Maximum name size")
               ]),

        Method('IGetProject_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the File Project",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('project', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Title returned"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Maximum name size")
               ]),

        Method('IGetTitle_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Title",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('title', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Title returned"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Maximum name size")
               ]),

        Method('Serial_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Serialize :class:`USERMETA` to a :class:`BF`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('save_geo', type=Type.BOOL,
                             doc="Output Geosoft Metadata?"),
                   Parameter('file', type=Type.STRING,
                             doc="File name to save to")
               ]),

        Method('SetDataCreationDate_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Data Creation Date",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('date', type=Type.DOUBLE,
                             doc="Date")
               ]),

        Method('SetDataCreator_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Data Creator",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('data_creator', type=Type.STRING,
                             doc="DataCreator")
               ]),

        Method('SetExtents2d_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the 2d Extents",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="MinX"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="MinY"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="MaxX"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="MaxY")
               ]),

        Method('SetExtents3d_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the 3d Extents",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="MinX"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="MinY"),
                   Parameter('min_z', type=Type.DOUBLE,
                             doc="MinZ"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="MaxX"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="MaxY"),
                   Parameter('max_z', type=Type.DOUBLE,
                             doc="MaxZ")
               ]),

        Method('SetFormat_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the File Format",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('format', type=Type.STRING,
                             doc="Format")
               ]),

        Method('SetIPJ_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the :class:`IPJ`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('ipj', type="IPJ",
                             doc="Date")
               ]),

        Method('SetMetaCreationDate_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Meta Creation Date",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('date', type=Type.DOUBLE,
                             doc="Date")
               ]),

        Method('SetMetaCreator_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Meta Creator",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('meta_creator', type=Type.STRING,
                             doc="MetaCreator")
               ]),

        Method('SetProject_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the File Project",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('project', type=Type.STRING,
                             doc="Project")
               ]),

        Method('SetTitle_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Title",
               return_type=Type.VOID,
               parameters = [
                   Parameter('usermeta', type="USERMETA"),
                   Parameter('title', type=Type.STRING,
                             doc="Title")
               ]),

        Method('UpdateExtents2D_USERMETA', module='geoengine.core', version='7.0.1',
               availability=Availability.PUBLIC, 
               doc="""
               Edit an existing XML metadata file by
               changing the extents and projection data
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('filename', type=Type.STRING,
                             doc="Filename of existing metadata to update"),
                   Parameter('ipj', type="IPJ",
                             doc="New projection"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="New MinX value"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="New MinY value"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="New MaxX value"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="New MaxY value")
               ]),

        Method('UpdateFileType_USERMETA', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="""
               Edit an existing XML metadata file by
               changing the file type
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('file_name', type=Type.STRING,
                             doc="Filename of existing metadata to update"),
                   Parameter('new_file_type', type=Type.STRING,
                             doc="New file type")
               ]),

        Method('SaveFileLineage_USERMETA', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Add lineage to XML",
               return_type=Type.VOID,
               parameters = [
                   Parameter('file_name', type=Type.STRING,
                             doc="Filename of existing metadata to update"),
                   Parameter('save_geo', type=Type.BOOL,
                             doc="Output Geosoft Metadata?")
               ])
    ]
}

