from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('PROJ',
                 doc="Project functions")


gx_defines = [
    Define('COMMAND_ENV',
           doc="Command environments",
           constants=[
               Constant('COMMAND_ENV_NORMAL', value='0', type=Type.INT32_T,
                        doc="Normal"),
               Constant('COMMAND_ENV_IN3DVIEWER', value='1', type=Type.INT32_T,
                        doc="Executing from inside 3D Viewer")
           ]),

    Define('TOOL_TYPE',
           doc="Tool type defines",
           constants=[
               Constant('TOOL_TYPE_DEFAULT', value='0', type=Type.INT32_T,
                        doc="Geosoft created default tools"),
               Constant('TOOL_TYPE_AUXILIARY', value='1', type=Type.INT32_T,
                        doc="Auxiliary tools (including custom XTools)"),
               Constant('TOOL_TYPE_ALL', value='2', type=Type.INT32_T,
                        doc="All tools")
           ]),

    Define('PROJ_DISPLAY',
           doc="How to display an object",
           constants=[
               Constant('PROJ_DISPLAY_NO', value='0', type=Type.INT32_T,
                        doc="Do not display the object"),
               Constant('PROJ_DISPLAY_YES', value='1', type=Type.INT32_T,
                        doc="Display the object unless user set option not to"),
               Constant('PROJ_DISPLAY_ALWAYS', value='2', type=Type.INT32_T,
                        doc="Always display the object")
           ])]


gx_methods = {
    'Drag-and-drop methods': [

        Method('DropMapClipData_PROJ', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Drop Map clipboard data in the current project (workspace background)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('global', type=Type.INT32_T,
                             doc="Handle to Global Clipboard data")
               ])
    ],
    'Miscellaneous': [

        Method('iAddDocument_PROJ', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Adds (and opens) a document file in the current project.",
               notes="""
               The passed file name must be a valid
               file name complete with an extension and
               qualifiers (if applicable).
               
               The type string can be one of the following:
               
                   Database      
                   Grid          
                   Map           
                   3DView        
                   Voxel         
                   VoxelInversion
                   GMS3D         
                   GMS2D
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Error
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Document name"),
                   Parameter('type', type=Type.STRING,
                             doc="Type of document to add"),
                   Parameter('display', type=Type.INT32_T,
                             doc=":def:`PROJ_DISPLAY`")
               ]),

        Method('iAddDocumentWithoutOpening_PROJ', module='None', version='8.5.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Adds (and opens) a document file in the current project.",
               notes="""
               The passed file name must be a valid
               file name complete with an extension and
               qualifiers (if applicable).
               
               The type string can be one of the following:
               
                   Database      
                   Grid          
                   Map           
                   3DView        
                   Voxel         
                   VoxelInversion
                   GMS3D         
                   GMS2D
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Error
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Document name"),
                   Parameter('type', type=Type.STRING,
                             doc="Type of document to add")
               ]),

        Method('iGetCommandEnvironment_PROJ', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="The current command environment",
               return_type=Type.INT32_T,
               return_doc="""
               :def:`COMMAND_ENV`
               
               Notes									We are moving towards embedded tools and menus and this setting can be
               queried from the project to determine how specific commands should react.
               Only 3D viewer is currently making use of this.
               """),

        Method('iListDocuments_PROJ', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Fills a :class:`VV` with documents of a certain type.",
               notes="""
               The type string can be one of the following:
               Database         List Databases.
               Grid             List Grids.
               Map              List Maps.
               3DView           List 3D Views.
               Voxel            List Voxels.
               VoxelInversion   List VOXI Documents.
               :class:`MXD`              List ArcGIS MXDs.
               GMS3D            List GM-:class:`SYS` 3D Models.
               GMS2D            List GM-:class:`SYS` 2D Models.
               All              Lists all files.
               """,
               return_type=Type.INT32_T,
               return_doc="The number of documents listed in the :class:`VV`.",
               parameters = [
                   Parameter('gvv', type="VV",
                             doc=":class:`VV` of type -:def_val:`STR_FILE`"),
                   Parameter('type', type=Type.STRING,
                             doc="Type of document to obtain")
               ]),

        Method('iListLoadedDocuments_PROJ', module='None', version='9.2',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Fills a :class:`VV` with loaded documents of a certain type.",
               notes="""
               The type string can be one of the following:
               Database         List Databases.
               Grid             List Grids.
               Map              List Maps.
               3DView           List 3D Views.
               Voxel            List Voxels.
               VoxelInversion   List VOXI Documents.
               :class:`MXD`              List ArcGIS MXDs.
               GMS3D            List GM-:class:`SYS` 3D Models.
               GMS2D            List GM-:class:`SYS` 2D Models.
               All              Lists all files.
               """,
               return_type=Type.INT32_T,
               return_doc="The number of loaded documents listed in the :class:`VV`.",
               parameters = [
                   Parameter('gvv', type="VV",
                             doc=":class:`VV` of type -:def_val:`STR_FILE`>"),
                   Parameter('type', type=Type.STRING,
                             doc="Type of document to obtain")
               ]),

        Method('ICurrentDocument_PROJ', module='None', version='9.2.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the name and type of the loaded document with focus.",
               return_type=Type.VOID,
               return_doc="Nothing.",
               parameters = [
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='size_name',
                             doc="Name (empty if none currently loaded)"),
                   Parameter('size_name', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Maximum name length"),
                   Parameter('type', type=Type.STRING, is_ref=True, size_of_param='size_type',
                             doc="Type"),
                   Parameter('size_type', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Maximum type length")
               ]),

        Method('ICurrentDocumentOfType_PROJ', module='None', version='9.2.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the name of a loaded document of a specific type.",
               return_type=Type.VOID,
               return_doc="Nothing.",
               parameters = [
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='size_name',
                             doc="Name (empty if none currently loaded)"),
                   Parameter('size_name', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Maximum name length"),
                   Parameter('type', type=Type.STRING,
                             doc="Type")
               ]),

        Method('iListTools_PROJ', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               Fills an :class:`LST` object with tools of a certain type and
               notes the current visibility setting.
               """,
               notes="""
               GX will terminate if there is an error.
               
               :class:`LST` object will hold the tool name in the name column and
               include whether the tool is currently visible in the value
               column (1=visible, 0-hidden).
               """,
               return_type=Type.INT32_T,
               return_doc="The number of tools found.",
               parameters = [
                   Parameter('lst', type="LST",
                             doc=":class:`LST` object to hold list"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`TOOL_TYPE`")
               ]),

        Method('iRemoveDocument_PROJ', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Removes (and closes if visible) a document from the current project.",
               notes="""
               The passed file name must be a valid
               file name complete with an extension and
               qualifiers (if applicable).
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Document not found in project
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Document name")
               ]),

        Method('iRemoveTool_PROJ', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Removes (and closes if visible) a auxiliary tool from the current project.",
               notes="Nothing",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Tool not found in project
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Tool name")
               ]),

        Method('iSaveCloseDocuments_PROJ', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Saves and closes (if visible) documents contained in the current project.",
               notes="""
               This wrapper brings up the save dialog tool to allow
               the user to save the modified documents for this project.
               Only documents that have actually changed will be listed.
               
               The type string can be one of the following:
                   
                   Database      
                   Grid          
                   Map           
                   3DView        
                   Voxel         
                   VoxelInversion
                   GMS3D         
                   GMS2D
                   All                     
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0  - Ok
               -1 - User hit cancel in save dialog
               1  - Error
               """,
               parameters = [
                   Parameter('type', type=Type.STRING,
                             doc="Type of document to save / close")
               ]),

        Method('IGetName_PROJ', module='None', version='8.4.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Return the name of the project file.",
               notes="Return the name of the project file.",
               return_type=Type.VOID,
               return_doc="Nothing.",
               parameters = [
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='buff',
                             doc="name"),
                   Parameter('buff', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="maximum name length")
               ])
    ]
}

