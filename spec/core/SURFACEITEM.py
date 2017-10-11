from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('SURFACEITEM',
                 doc="""
                 The :class:`SURFACEITEM` allows you to create, read and alter Geosurface files (*.geosoft_surface).
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
                   Parameter('p1', type=Type.STRING,
                             doc="Type"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name")
               ]),

        Method('Destroy_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`SURFACEITEM` Object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object")
               ]),

        Method('GetGUID_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Gets the GUID of the surface item.",
               notes="The value returned by this call will not be valid for newly created items until after a call to :func:`AddSurfaceItem_SURFACE`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="GUID"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of GUID buffer.")
               ]),

        Method('SetProperties_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Sets the properties of the surface item.",
               see_also=":func:`GenerateGUID_SYS`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Type"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name"),
                   Parameter('p4', type=Type.STRING,
                             doc="SourceGuid"),
                   Parameter('p5', type=Type.STRING,
                             doc="SourceName"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="SourceMeasure"),
                   Parameter('p7', type=Type.STRING,
                             doc="SecondarySourceGuid"),
                   Parameter('p8', type=Type.STRING,
                             doc="SecondarySourceName"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="SecondarySourceMeasure")
               ]),

        Method('SetPropertiesEx_SURFACEITEM', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Sets the properties of the surface item (includes new properties introduced in 8.5).",
               see_also=":func:`GenerateGUID_SYS`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Type"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name"),
                   Parameter('p4', type=Type.STRING,
                             doc="SourceGuid"),
                   Parameter('p5', type=Type.STRING,
                             doc="SourceName"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="SourceMeasure"),
                   Parameter('p7', type=Type.STRING,
                             doc="SecondarySourceGuid"),
                   Parameter('p8', type=Type.STRING,
                             doc="SecondarySourceName"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="SecondarySourceOption"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="SecondarySourceMeasure"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="SecondarySourceMeasure2")
               ]),

        Method('GetProperties_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Gets the properties of the surface item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Type"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of Type buffer."),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="Name"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of Name buffer."),
                   Parameter('p6', type=Type.STRING, is_ref=True, size_of_param='p7',
                             doc="SourceGuid"),
                   Parameter('p7', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of SourceGuid buffer."),
                   Parameter('p8', type=Type.STRING, is_ref=True, size_of_param='p9',
                             doc="SourceName"),
                   Parameter('p9', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of SourceName buffer."),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="SourceMeasure"),
                   Parameter('p11', type=Type.STRING, is_ref=True, size_of_param='p12',
                             doc="SecondarySourceGuid"),
                   Parameter('p12', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of SecondarySourceGuid buffer."),
                   Parameter('p13', type=Type.STRING, is_ref=True, size_of_param='p14',
                             doc="SecondarySourceName"),
                   Parameter('p14', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of SecondarySourceName buffer."),
                   Parameter('p15', type=Type.DOUBLE, is_ref=True,
                             doc="SecondarySourceMeasure")
               ]),

        Method('GetPropertiesEx_SURFACEITEM', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Gets the properties of the surface item  (includes new properties introduced in 8.5).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Type"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of Type buffer."),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="Name"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of Name buffer."),
                   Parameter('p6', type=Type.STRING, is_ref=True, size_of_param='p7',
                             doc="SourceGuid"),
                   Parameter('p7', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of SourceGuid buffer."),
                   Parameter('p8', type=Type.STRING, is_ref=True, size_of_param='p9',
                             doc="SourceName"),
                   Parameter('p9', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of SourceName buffer."),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="SourceMeasure"),
                   Parameter('p11', type=Type.STRING, is_ref=True, size_of_param='p12',
                             doc="SecondarySourceGuid"),
                   Parameter('p12', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of SecondarySourceGuid buffer."),
                   Parameter('p13', type=Type.STRING, is_ref=True, size_of_param='p14',
                             doc="SecondarySourceName"),
                   Parameter('p14', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of SecondarySourceName buffer."),
                   Parameter('p15', type=Type.INT32_T, is_ref=True,
                             doc="SecondarySourceOption"),
                   Parameter('p16', type=Type.DOUBLE, is_ref=True,
                             doc="SecondarySourceMeasure"),
                   Parameter('p17', type=Type.DOUBLE, is_ref=True,
                             doc="SecondarySourceMeasure2")
               ]),

        Method('SetDefaultRenderProperties_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Sets default render properties of the surface item.",
               see_also=":func:`iColor_MVIEW`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Color"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Transparency"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`SURFACERENDER_MODE`")
               ]),

        Method('GetDefaultRenderProperties_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Gets default render properties of the surface item.",
               see_also=":func:`iColor_MVIEW`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Color"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Transparency"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc=":def:`SURFACERENDER_MODE`")
               ]),

        Method('iNumComponents_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of components in the surface item.",
               return_type=Type.INT32_T,
               return_doc="Number of components in the surface item.",
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object")
               ]),

        Method('iAddMesh_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Adds a triangular polyhedral mesh component to the surface item.",
               return_type=Type.INT32_T,
               return_doc="The index of the component added.",
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('p2', type="VV",
                             doc="Vertices X location"),
                   Parameter('p3', type="VV",
                             doc="Vertices Y location"),
                   Parameter('p4', type="VV",
                             doc="Vertices Z location"),
                   Parameter('p5', type="VV",
                             doc="Triangles 1st Vertex"),
                   Parameter('p6', type="VV",
                             doc="Triangles 2nd Vertex"),
                   Parameter('p7', type="VV",
                             doc="Triangles 3rd Vertex")
               ]),

        Method('GetMesh_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Gets a triangular polyhedral mesh of a component in the surface item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Index of the component"),
                   Parameter('p3', type="VV",
                             doc="Vertices X"),
                   Parameter('p4', type="VV",
                             doc="Vertices Y"),
                   Parameter('p5', type="VV",
                             doc="Vertices Z"),
                   Parameter('p6', type="VV",
                             doc="Triangles 1st Vertex"),
                   Parameter('p7', type="VV",
                             doc="Triangles 2nd Vertex"),
                   Parameter('p8', type="VV",
                             doc="Triangles 3rd Vertex")
               ]),

        Method('GetExtents_SURFACEITEM', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the spatial range of the the surface item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum valid data in X."),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum valid data in Y."),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum valid data in Z."),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum valid data in X."),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum valid data in Y."),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum valid data in Z.")
               ]),

        Method('GetMeshInfo_SURFACEITEM', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Gets information about a triangular polyhedral mesh component in the surface item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Index of the component"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc=":def:`GEO_BOOL` indicating if mesh is closed"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="number of inner components"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Area"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Volume"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Volume confidence interval")
               ]),

        Method('GetInfo_SURFACEITEM', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Gets information about the surface item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc=":def:`GEO_BOOL` indicating if all meshes in item is closed"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Area"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Volume"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Volume confidence interval")
               ]),

        Method('GetGeometryInfo_SURFACEITEM', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the total number of vertices and triangles of all mesh components in item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Total number of vertices"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Total number of triangles")
               ]),

        Method('ComputeExtendedInfo_SURFACEITEM', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Compute more information (including validation) about of all mesh components in the surface item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` Object"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Number of inner components (recomputed)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Total number of valid vertices"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Total number of valid edges"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Total number of valid triangles"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="Number of inconsistent triangles"),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc="Number of invalid triangles"),
                   Parameter('p8', type=Type.INT32_T, is_ref=True,
                             doc="Number of self intersections")
               ])
    ]
}

