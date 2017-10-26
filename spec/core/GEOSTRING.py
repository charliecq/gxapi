from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('GEOSTRING',
                 doc="""
                 The :class:`GEOSTRING` class is used to read information stored in Geostring files 
                 (``*.geosoft_string``). Geosoft geostrings are 3D vector files that store digitized 
                 interpretations drawn on section maps. Both polygon and polyline features can be 
                 stored in the same file. This API currently only provides read access, 
                 but read/write support could be added in the future.
                 """)


gx_defines = [
    Define('GEOSTRING_OPEN',
           doc="Open Modes",
           constants=[
               Constant('GEOSTRING_OPEN_READ', value='0', type=Type.INT32_T),
               Constant('GEOSTRING_OPEN_READWRITE', value='1', type=Type.INT32_T)
           ]),

    Define('SECTION_ORIENTATION',
           doc="Section orientation types",
           constants=[
               Constant('SECTION_ORIENTATION_UNKNOWN', value='0', type=Type.INT32_T),
               Constant('SECTION_ORIENTATION_PLAN', value='1', type=Type.INT32_T),
               Constant('SECTION_ORIENTATION_SECTION', value='2', type=Type.INT32_T),
               Constant('SECTION_ORIENTATION_CROOKED', value='2', type=Type.INT32_T),
               Constant('SECTION_ORIENTATION_GMSYS', value='2', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Open_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Open a Geostring file",
               return_type="GEOSTRING",
               return_doc=":class:`GEOSTRING` Object",
               parameters = [
                   Parameter('geostring_file', type=Type.STRING,
                             doc="Geostring file name"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`GEOSTRING_OPEN`")
               ]),

        Method('Destroy_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`GEOSTRING` Object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('geostring', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object")
               ]),

        Method('GetIPJ_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the coordinate system of the Geostring.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('geostring', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` in which to place the Geostring coordinate system")
               ]),

        Method('GetFeatures_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the features",
               notes="List items are returned with feature GUID in name and feature name in value.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('geostring', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetSections_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the sections",
               notes="List items are returned with section GUID in name and section name in value.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('geostring', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetAllShapes_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the all shapes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('geostring', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetShapesForFeature_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get all shapes linked to a specific feature",
               return_type=Type.VOID,
               parameters = [
                   Parameter('geostring', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('guid', type=Type.STRING,
                             doc="Feature GUID"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetShapesForSection_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get all shapes linked to a specific section",
               return_type=Type.VOID,
               parameters = [
                   Parameter('geostring', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('guid', type=Type.STRING,
                             doc="Section GUID"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetShapesForFeatureAndSection_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get all shapes linked to a specific feature and section",
               return_type=Type.VOID,
               parameters = [
                   Parameter('geostring', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('feature_guid', type=Type.STRING,
                             doc="Feature GUID"),
                   Parameter('section_guid', type=Type.STRING,
                             doc="Section GUID"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetFeatureProperties_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get a feature's properties",
               return_type=Type.VOID,
               parameters = [
                   Parameter('geostring', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('guid', type=Type.STRING,
                             doc="Feature GUID"),
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='name_size',
                             doc="Name"),
                   Parameter('name_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of Name buffer."),
                   Parameter('description', type=Type.STRING, is_ref=True, size_of_param='description_size',
                             doc="Description"),
                   Parameter('description_size', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of Description buffer."),
                   Parameter('polygon', type=Type.INT32_T, is_ref=True,
                             doc=":def:`GEO_BOOL` indicating if feature is decribed by polygons (shapes are polylines if not set)"),
                   Parameter('pat_number', type=Type.INT32_T, is_ref=True,
                             doc="The fill pattern number (see :func:`PatNumber_MVIEW`)"),
                   Parameter('pat_size', type=Type.DOUBLE, is_ref=True,
                             doc="The fill pattern size (see :func:`PatSize_MVIEW`)"),
                   Parameter('pat_thick', type=Type.DOUBLE, is_ref=True,
                             doc="The fill pattern thickness (see :func:`PatThick_MVIEW`)"),
                   Parameter('pat_density', type=Type.DOUBLE, is_ref=True,
                             doc="The fill pattern density (see :func:`PatDensity_MVIEW`)"),
                   Parameter('pat_color', type=Type.INT32_T, is_ref=True,
                             doc="The fill color (an :class:`MVIEW` color)"),
                   Parameter('pat_bg_color', type=Type.INT32_T, is_ref=True,
                             doc="The fill background color (an :class:`MVIEW` color)"),
                   Parameter('line_style', type=Type.INT32_T, is_ref=True,
                             doc="The line style (see :func:`LineStyle_MVIEW`)"),
                   Parameter('line_thickness', type=Type.DOUBLE, is_ref=True,
                             doc="The line thickness (see :func:`LineThick_MVIEW`)"),
                   Parameter('line_pitch', type=Type.DOUBLE, is_ref=True,
                             doc="The dash pattern pitch (see :func:`LineStyle_MVIEW`)"),
                   Parameter('line_color', type=Type.INT32_T, is_ref=True,
                             doc="The line color (an :class:`MVIEW` color)")
               ]),

        Method('GetSectionProperties_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get a section's properties",
               return_type=Type.VOID,
               parameters = [
                   Parameter('geostring', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('guid', type=Type.STRING,
                             doc="Section GUID"),
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='name_size',
                             doc="Name"),
                   Parameter('name_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of Name buffer."),
                   Parameter('container_name', type=Type.STRING, is_ref=True, size_of_param='container_name_size',
                             doc="ContainerName"),
                   Parameter('container_name_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of ContainerName buffer."),
                   Parameter('orientation', type=Type.INT32_T, is_ref=True,
                             doc=":def:`SECTION_ORIENTATION`"),
                   Parameter('easting', type=Type.DOUBLE, is_ref=True,
                             doc="Easting"),
                   Parameter('northing', type=Type.DOUBLE, is_ref=True,
                             doc="Northing"),
                   Parameter('elevation', type=Type.DOUBLE, is_ref=True,
                             doc="Elevation"),
                   Parameter('azimuth', type=Type.DOUBLE, is_ref=True,
                             doc="Azimuth"),
                   Parameter('swing', type=Type.DOUBLE, is_ref=True,
                             doc="Swing"),
                   Parameter('a', type=Type.DOUBLE, is_ref=True,
                             doc="A in the scalar equation of best-fit plane describing the section"),
                   Parameter('b', type=Type.DOUBLE, is_ref=True,
                             doc="B in the scalar equation of best-fit plane describing the section"),
                   Parameter('c', type=Type.DOUBLE, is_ref=True,
                             doc="C in the scalar equation of best-fit plane describing the section"),
                   Parameter('d', type=Type.DOUBLE, is_ref=True,
                             doc="D in the scalar equation of best-fit plane describing the section")
               ]),

        Method('GetShapeProperties_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get a shape's properties",
               return_type=Type.VOID,
               parameters = [
                   Parameter('geostring', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('guid', type=Type.STRING,
                             doc="Shape GUID"),
                   Parameter('feature_guid', type=Type.STRING, is_ref=True, size_of_param='feature_guid_size',
                             doc="Feature GUID"),
                   Parameter('feature_guid_size', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of Feature GUID buffer."),
                   Parameter('section_guid', type=Type.STRING, is_ref=True, size_of_param='section_guid_size',
                             doc="Section GUID"),
                   Parameter('section_guid_size', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of Section GUID buffer."),
                   Parameter('vert_v_vx', type="VV",
                             doc="Vertices X location"),
                   Parameter('vert_v_vy', type="VV",
                             doc="Vertices Y location"),
                   Parameter('vert_v_vz', type="VV",
                             doc="Vertices Z location")
               ])
    ]
}

