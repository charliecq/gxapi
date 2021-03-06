from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('SURFACEITEM',
                 doc="""
                 The :class:`SURFACEITEM` allows you to create, read and alter Geosurface files (``*.geosoft_surface``).
                 A Geosurface file can contain one or more surface items (see :class:`SURFACE` class). A surface item can
                 contains one or more triangular polyhedral meshes.
                 """)


gx_defines = [
    Define('SURFACERENDER_MODE',
           doc="Open Modes",
           constants=[
               Constant('SURFACERENDER_SMOOTH', value='0', type=Type.INT32_T),
               Constant('SURFACERENDER_FILL', value='1', type=Type.INT32_T),
               Constant('SURFACERENDER_EDGES', value='2', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`SURFACEITEM`",
               see_also=":func:`SetProperties_SURFACEITEM` and :func:`SetDefaultRenderProperties_SURFACEITEM`",
               return_type="SURFACEITEM",
               return_doc=":class:`SURFACEITEM` Object",
               parameters = [
                   Parameter('type', type=Type.STRING,
                             doc="Type"),
                   Parameter('name', type=Type.STRING,
                             doc="Name")
               ]),

        Method('Destroy_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`SURFACEITEM` Object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object")
               ]),

        Method('GetGUID_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Gets the GUID of the surface item.",
               notes="The value returned by this call will not be valid for newly created items until after a call to :func:`AddSurfaceItem_SURFACE`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('guid', type=Type.STRING, is_ref=True, size_of_param='guid_size',
                             doc="GUID"),
                   Parameter('guid_size', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of GUID buffer.")
               ]),

        Method('SetProperties_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Sets the properties of the surface item.",
               see_also=":func:`GenerateGUID_SYS`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('type', type=Type.STRING,
                             doc="Type"),
                   Parameter('name', type=Type.STRING,
                             doc="Name"),
                   Parameter('source_guid', type=Type.STRING,
                             doc="SourceGuid"),
                   Parameter('source_name', type=Type.STRING,
                             doc="SourceName"),
                   Parameter('source_measure', type=Type.DOUBLE,
                             doc="SourceMeasure"),
                   Parameter('secondary_source_guid', type=Type.STRING,
                             doc="SecondarySourceGuid"),
                   Parameter('secondary_source_name', type=Type.STRING,
                             doc="SecondarySourceName"),
                   Parameter('secondary_source_measure', type=Type.DOUBLE,
                             doc="SecondarySourceMeasure")
               ]),

        Method('SetPropertiesEx_SURFACEITEM', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Sets the properties of the surface item (includes new properties introduced in 8.5).",
               see_also=":func:`GenerateGUID_SYS`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('type', type=Type.STRING,
                             doc="Type"),
                   Parameter('name', type=Type.STRING,
                             doc="Name"),
                   Parameter('source_guid', type=Type.STRING,
                             doc="SourceGuid"),
                   Parameter('source_name', type=Type.STRING,
                             doc="SourceName"),
                   Parameter('source_measure', type=Type.DOUBLE,
                             doc="SourceMeasure"),
                   Parameter('secondary_source_guid', type=Type.STRING,
                             doc="SecondarySourceGuid"),
                   Parameter('secondary_source_name', type=Type.STRING,
                             doc="SecondarySourceName"),
                   Parameter('secondary_source_option', type=Type.INT32_T,
                             doc="SecondarySourceOption"),
                   Parameter('secondary_source_measure', type=Type.DOUBLE,
                             doc="SecondarySourceMeasure"),
                   Parameter('secondary_source_measure2', type=Type.DOUBLE,
                             doc="SecondarySourceMeasure2")
               ]),

        Method('GetProperties_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Gets the properties of the surface item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('type', type=Type.STRING, is_ref=True, size_of_param='type_size',
                             doc="Type"),
                   Parameter('type_size', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of Type buffer."),
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='name_size',
                             doc="Name"),
                   Parameter('name_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of Name buffer."),
                   Parameter('source_guid', type=Type.STRING, is_ref=True, size_of_param='source_guid_size',
                             doc="SourceGuid"),
                   Parameter('source_guid_size', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of SourceGuid buffer."),
                   Parameter('source_name', type=Type.STRING, is_ref=True, size_of_param='source_name_size',
                             doc="SourceName"),
                   Parameter('source_name_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of SourceName buffer."),
                   Parameter('source_measure', type=Type.DOUBLE, is_ref=True,
                             doc="SourceMeasure"),
                   Parameter('secondary_source_guid', type=Type.STRING, is_ref=True, size_of_param='secondary_source_guid_size',
                             doc="SecondarySourceGuid"),
                   Parameter('secondary_source_guid_size', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of SecondarySourceGuid buffer."),
                   Parameter('secondary_source_name', type=Type.STRING, is_ref=True, size_of_param='secondary_source_name_size',
                             doc="SecondarySourceName"),
                   Parameter('secondary_source_name_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of SecondarySourceName buffer."),
                   Parameter('secondary_source_measure', type=Type.DOUBLE, is_ref=True,
                             doc="SecondarySourceMeasure")
               ]),

        Method('GetPropertiesEx_SURFACEITEM', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Gets the properties of the surface item  (includes new properties introduced in 8.5).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('type', type=Type.STRING, is_ref=True, size_of_param='type_size',
                             doc="Type"),
                   Parameter('type_size', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of Type buffer."),
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='name_size',
                             doc="Name"),
                   Parameter('name_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of Name buffer."),
                   Parameter('source_guid', type=Type.STRING, is_ref=True, size_of_param='source_guid_size',
                             doc="SourceGuid"),
                   Parameter('source_guid_size', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of SourceGuid buffer."),
                   Parameter('source_name', type=Type.STRING, is_ref=True, size_of_param='source_name_size',
                             doc="SourceName"),
                   Parameter('source_name_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of SourceName buffer."),
                   Parameter('source_measure', type=Type.DOUBLE, is_ref=True,
                             doc="SourceMeasure"),
                   Parameter('secondary_source_guid', type=Type.STRING, is_ref=True, size_of_param='secondary_source_guid_size',
                             doc="SecondarySourceGuid"),
                   Parameter('secondary_source_guid_size', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of SecondarySourceGuid buffer."),
                   Parameter('secondary_source_name', type=Type.STRING, is_ref=True, size_of_param='secondary_source_name_size',
                             doc="SecondarySourceName"),
                   Parameter('secondary_source_name_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of SecondarySourceName buffer."),
                   Parameter('secondary_source_option', type=Type.INT32_T, is_ref=True,
                             doc="SecondarySourceOption"),
                   Parameter('secondary_source_measure', type=Type.DOUBLE, is_ref=True,
                             doc="SecondarySourceMeasure"),
                   Parameter('secondary_source_measure2', type=Type.DOUBLE, is_ref=True,
                             doc="SecondarySourceMeasure2")
               ]),

        Method('SetDefaultRenderProperties_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Sets default render properties of the surface item.",
               see_also=":func:`iColor_MVIEW`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('color', type=Type.INT32_T,
                             doc="Color"),
                   Parameter('transparency', type=Type.DOUBLE,
                             doc="Transparency"),
                   Parameter('render_mode', type=Type.INT32_T,
                             doc=":def:`SURFACERENDER_MODE`")
               ]),

        Method('GetDefaultRenderProperties_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Gets default render properties of the surface item.",
               see_also=":func:`iColor_MVIEW`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('color', type=Type.INT32_T, is_ref=True,
                             doc="Color"),
                   Parameter('transparency', type=Type.DOUBLE, is_ref=True,
                             doc="Transparency"),
                   Parameter('render_mode', type=Type.INT32_T, is_ref=True,
                             doc=":def:`SURFACERENDER_MODE`")
               ]),

        Method('iNumComponents_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of components in the surface item.",
               return_type=Type.INT32_T,
               return_doc="Number of components in the surface item.",
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object")
               ]),

        Method('iAddMesh_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Adds a triangular polyhedral mesh component to the surface item.",
               return_type=Type.INT32_T,
               return_doc="The index of the component added.",
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('vert_v_vx', type="VV",
                             doc="Vertices X location"),
                   Parameter('vert_v_vy', type="VV",
                             doc="Vertices Y location"),
                   Parameter('vert_v_vz', type="VV",
                             doc="Vertices Z location"),
                   Parameter('tri_vv_pt1', type="VV",
                             doc="Triangles 1st Vertex"),
                   Parameter('tri_vv_pt2', type="VV",
                             doc="Triangles 2nd Vertex"),
                   Parameter('tri_vv_pt3', type="VV",
                             doc="Triangles 3rd Vertex")
               ]),

        Method('GetMesh_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Gets a triangular polyhedral mesh of a component in the surface item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('index', type=Type.INT32_T,
                             doc="Index of the component"),
                   Parameter('vert_v_vx', type="VV",
                             doc="Vertices X"),
                   Parameter('vert_v_vy', type="VV",
                             doc="Vertices Y"),
                   Parameter('vert_v_vz', type="VV",
                             doc="Vertices Z"),
                   Parameter('tri_vv_pt1', type="VV",
                             doc="Triangles 1st Vertex"),
                   Parameter('tri_vv_pt2', type="VV",
                             doc="Triangles 2nd Vertex"),
                   Parameter('tri_vv_pt3', type="VV",
                             doc="Triangles 3rd Vertex")
               ]),

        Method('GetExtents_SURFACEITEM', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the spatial range of the the surface item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` object"),
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

        Method('GetMeshInfo_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Gets information about a triangular polyhedral mesh component in the surface item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('index', type=Type.INT32_T,
                             doc="Index of the component"),
                   Parameter('closed', type=Type.BOOL, is_ref=True,
                             doc="indicating if mesh is closed"),
                   Parameter('n_inner_comps', type=Type.INT32_T, is_ref=True,
                             doc="Number of inner components"),
                   Parameter('area', type=Type.DOUBLE, is_ref=True,
                             doc="Area"),
                   Parameter('volume', type=Type.DOUBLE, is_ref=True,
                             doc="Volume"),
                   Parameter('volume_confidence_interval', type=Type.DOUBLE, is_ref=True,
                             doc="Volume confidence interval")
               ]),

        Method('GetInfo_SURFACEITEM', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Gets information about the surface item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('closed', type=Type.BOOL, is_ref=True,
                             doc="indicating if all meshes in item is closed"),
                   Parameter('area', type=Type.DOUBLE, is_ref=True,
                             doc="Area"),
                   Parameter('volume', type=Type.DOUBLE, is_ref=True,
                             doc="Volume"),
                   Parameter('volume_confidence_interval', type=Type.DOUBLE, is_ref=True,
                             doc="Volume confidence interval")
               ]),

        Method('GetGeometryInfo_SURFACEITEM', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the total number of vertices and triangles of all mesh components in item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('vertices', type=Type.INT32_T, is_ref=True,
                             doc="Total number of vertices"),
                   Parameter('triangles', type=Type.INT32_T, is_ref=True,
                             doc="Total number of triangles")
               ]),

        Method('ComputeExtendedInfo_SURFACEITEM', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Compute more information (including validation) about of all mesh components in the surface item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('surfaceitem', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('components', type=Type.INT32_T, is_ref=True,
                             doc="Number of inner components (recomputed)"),
                   Parameter('vertices', type=Type.INT32_T, is_ref=True,
                             doc="Total number of valid vertices"),
                   Parameter('edges', type=Type.INT32_T, is_ref=True,
                             doc="Total number of valid edges"),
                   Parameter('triangles', type=Type.INT32_T, is_ref=True,
                             doc="Total number of valid triangles"),
                   Parameter('inconsistent', type=Type.INT32_T, is_ref=True,
                             doc="Number of inconsistent triangles"),
                   Parameter('invalid', type=Type.INT32_T, is_ref=True,
                             doc="Number of invalid triangles"),
                   Parameter('intersectiona', type=Type.INT32_T, is_ref=True,
                             doc="Number of self intersections")
               ])
    ]
}

