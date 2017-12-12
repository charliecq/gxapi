from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('SURFACE',
                 doc="""
                 The :class:`SURFACE` class allows you to create, read and alter Geosurface files (``*.geosoft_surface``).
                 A Geosurface file can contain one or more surface items (see :class:`SURFACEITEM` class). In turn each item can
                 contains one or more triangular polyhedral meshes.
                 """)


gx_defines = [
    Define('SURFACE_OPEN',
           doc="Open Modes",
           constants=[
               Constant('SURFACE_OPEN_READ', value='0', type=Type.INT32_T),
               Constant('SURFACE_OPEN_READWRITE', value='1', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Create a new Geosurface file",
               return_type="SURFACE",
               return_doc=":class:`SURFACE` Object",
               parameters = [
                   Parameter('surface_file', type=Type.STRING,
                             doc="Geosurface file name"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` containing coordinate system of the Geosurface")
               ]),

        Method('Open_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Open a Geosurface file",
               return_type="SURFACE",
               return_doc=":class:`SURFACE` Object",
               parameters = [
                   Parameter('surface_file', type=Type.STRING,
                             doc="Geosurface file name"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`SURFACE_OPEN`")
               ]),

        Method('Destroy_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`SURFACE` Object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surface', type="SURFACE",
                             doc=":class:`SURFACE` Object")
               ]),

        Method('GetIPJ_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the coordinate system of the :class:`SURFACE`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surface', type="SURFACE",
                             doc=":class:`SURFACE` Object"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` in which to place the Geosurface coordinate system")
               ]),

        Method('SetIPJ_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Change the coordinate system of the :class:`SURFACE`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surface', type="SURFACE",
                             doc=":class:`SURFACE` Object"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` containing the new coordinate system of the Geosurface")
               ]),

        Method('GetSurfaceItems_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the surfaces items in a Geosurface file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surface', type="SURFACE",
                             doc=":class:`SURFACE` Object"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetSurfaceItem_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the an existing surface item from the :class:`SURFACE`",
               return_type="SURFACEITEM",
               return_doc=":class:`SURFACEITEM` Object",
               parameters = [
                   Parameter('surface', type="SURFACE",
                             doc=":class:`SURFACE` Object"),
                   Parameter('guid', type=Type.STRING,
                             doc="Item GUID")
               ]),

        Method('AddSurfaceItem_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Add a new surface item to the :class:`SURFACE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surface', type="SURFACE",
                             doc=":class:`SURFACE` Object"),
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` to add")
               ]),

        Method('GetSurfaceNames_SURFACE', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the surface item names in a Geosurface file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surface_file', type=Type.STRING,
                             doc="Geosurface file"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetClosedSurfaceNames_SURFACE', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the names of closed surface items in a Geosurface file (may return an empty list)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surface_file', type=Type.STRING,
                             doc="Geosurface file"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` to fill (may return an empty :class:`LST` if none of the surfaces are closed)")
               ]),

        Method('GetExtents_SURFACE', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the spatial range of all surface items.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surface', type="SURFACE",
                             doc=":class:`SURFACE` object"),
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum valid data in X."),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum valid data in Y."),
                   Parameter('min_z', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum valid data in Z."),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum valid data in X."),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum valid data in Y."),
                   Parameter('max_z', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum valid data in Z.")
               ]),

        Method('CRC_SURFACE', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Compute an XML CRC of a Geosurface file.",
               return_type="CRC",
               return_doc="CRC Value (always 0)",
               parameters = [
                   Parameter('surface_file', type=Type.STRING,
                             doc="Geosurface file"),
                   Parameter('output', type=Type.STRING,
                             doc="Output file"),
                   Parameter('crc', type=Type.INT32_T, is_ref=True,
                             doc="CRC (unused, always set to 0)")
               ]),

        Method('Sync_SURFACE', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Syncronize the Metadata for this Geosurface",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Geosurface file")
               ]),

        Method('CreateFromDXF_SURFACE', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Create Geosurface file from DXF file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ipj', type="IPJ"),
                   Parameter('surface_file', type=Type.STRING,
                             doc="Geosurface file"),
                   Parameter('dxf_file', type=Type.STRING,
                             doc="DXF file")
               ]),

        Method('CreateFromVulcanTriangulation_SURFACE', module='geoengine.interoperability', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Create Geosurface file from a Maptek Vulcan triangulation file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('triangulation_file', type=Type.STRING,
                             doc="00t file"),
                   Parameter('ipj', type="IPJ"),
                   Parameter('surface_file', type=Type.STRING,
                             doc="Geosurface file")
               ]),

        Method('AppendVulcanTriangulation_SURFACE', module='geoengine.interoperability', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Create new surface from a Maptek Vulcan triangulation file and add to an existing geosurface.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('triangulation_file', type=Type.STRING,
                             doc="00t file"),
                   Parameter('ipj', type="IPJ"),
                   Parameter('surface_file', type=Type.STRING,
                             doc="Geosurface file")
               ]),

        Method('DumpGeometryToTextFile_SURFACE', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Dump surface geometry to a text file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surface_filename', type=Type.STRING,
                             doc="Geosurface file"),
                   Parameter('text_filename', type=Type.STRING,
                             doc="Text file")
               ])
    ]
}

