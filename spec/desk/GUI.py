from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('GUI',
                 doc="""
                 These are graphical functions that typically create a
                 dialog-style window for a specific function. Examples include
                 file import wizards, and the Histogram and Scatter tools.
                 """)


gx_defines = [
    Define('AOI_RETURN_STATE',
           doc="AOI query return state",
           constants=[
               Constant('AOI_RETURN_CANCEL', value='-1', type=Type.INT32_T,
                        doc="User canceled"),
               Constant('AOI_RETURN_NODEFINE', value='0', type=Type.INT32_T,
                        doc="User chose to continue with no AOI defined or available"),
               Constant('AOI_RETURN_DEFINE', value='1', type=Type.INT32_T,
                        doc="User chose to continue and defined valid AOI parameters")
           ]),

    Define('COORDSYS_MODE',
           doc="""
           Coordinate system wizard :class:`IPJ` types allowed on return.
           The wizard present three types of projections for selection
           by the user, Geographic (GCS), Projected (PCS), and Unknown.
           (Unknown requires only that the units be defined.)
           The Editable flag must be Yes for this option to take affect,
           and is overridden internally if the user's license does not
           allow modification of projections (e.g. the OM Viewer).
           """,
           constants=[
               Constant('COORDSYS_MODE_ALL', value='0', type=Type.INT32_T,
                        doc="Allow Geographic (GCS), Projected (PCS), and Unknown"),
               Constant('COORDSYS_MODE_GCS', value='1', type=Type.INT32_T,
                        doc="Allow only Geographic (GCS)"),
               Constant('COORDSYS_MODE_PCS', value='2', type=Type.INT32_T,
                        doc="Allow only Projected (PCS)"),
               Constant('COORDSYS_MODE_GCS_PCS', value='3', type=Type.INT32_T,
                        doc="Allow only Geographic (GCS) and Projected (PCS)"),
               Constant('COORDSYS_MODE_PCS_UNKNOWN', value='4', type=Type.INT32_T,
                        doc="Allow only Projected (PCS), or Unknown")
           ]),

    Define('DAT_TYPE',
           doc="Type of files (grids, images) to support",
           constants=[
               Constant('DAT_TYPE_GRID', value='0', type=Type.INT32_T,
                        doc="Display only grid formats"),
               Constant('DAT_TYPE_IMAGE', value='1', type=Type.INT32_T,
                        doc="Display only image formats"),
               Constant('DAT_TYPE_GRID_AND_IMAGE', value='2', type=Type.INT32_T,
                        doc="Displays both grids and image formats")
           ]),

    Define('FILE_FILTER',
           doc="File filters",
           constants=[
               Constant('FILE_FILTER_ALL', value='1', type=Type.INT32_T,
                        doc="All files              ``*.*``                  ANYWHERE"),
               Constant('FILE_FILTER_GDB', value='2', type=Type.INT32_T,
                        doc="Geosoft Database       ``*.gdb``                LOCAL"),
               Constant('FILE_FILTER_GX', value='3', type=Type.INT32_T,
                        doc="Geosoft Executable     ``*.gx``                 GEOSOFT"),
               Constant('FILE_FILTER_GS', value='4', type=Type.INT32_T,
                        doc="Geosoft Script         ``*.gs``                 BOTH"),
               Constant('FILE_FILTER_INI', value='5', type=Type.INT32_T,
                        doc="Parameter files        ``*.ini``                GEOSOFT"),
               Constant('FILE_FILTER_OMN', value='6', type=Type.INT32_T,
                        doc="Oasis Menu files       ``*.omn``                GEOSOFT"),
               Constant('FILE_FILTER_VU', value='7', type=Type.INT32_T,
                        doc="Oasis View files       ``*.vu``                 LOCAL"),
               Constant('FILE_FILTER_MAP', value='8', type=Type.INT32_T,
                        doc="Oasis Map files        ``*.map``                LOCAL"),
               Constant('FILE_FILTER_PRJ', value='9', type=Type.INT32_T,
                        doc="Projection file        ``*.prj``                LOCAL"),
               Constant('FILE_FILTER_CON', value='10', type=Type.INT32_T,
                        doc="Configuration file     ``*.con``                LOCAL"),
               Constant('FILE_FILTER_MNU', value='11', type=Type.INT32_T,
                        doc="Sushi MNU files        ``*.mnu``                GEOSOFT"),
               Constant('FILE_FILTER_PDF', value='12', type=Type.INT32_T,
                        doc="PDF files              ``*.pdf``                GEOSOFT"),
               Constant('FILE_FILTER_PLT', value='13', type=Type.INT32_T,
                        doc="Geosoft PLT files      ``*.plt``                LOCAL"),
               Constant('FILE_FILTER_GWS', value='14', type=Type.INT32_T,
                        doc="Geosoft workspace      ``*.gws``                LOCAL"),
               Constant('FILE_FILTER_AGG', value='15', type=Type.INT32_T,
                        doc="Aggregate              ``*.agg``                LOCAL"),
               Constant('FILE_FILTER_TBL', value='16', type=Type.INT32_T,
                        doc="Color table            ``*.tbl``                GEOSOFT"),
               Constant('FILE_FILTER_ZON', value='17', type=Type.INT32_T,
                        doc="Zone                   ``*.zon``                LOCAL"),
               Constant('FILE_FILTER_ITR', value='18', type=Type.INT32_T,
                        doc="Image transform        ``*.itr``                LOCAL"),
               Constant('FILE_FILTER_DXF', value='19', type=Type.INT32_T,
                        doc="AutoCAD DXF files      ``*.dxf``                LOCAL"),
               Constant('FILE_FILTER_TIF', value='20', type=Type.INT32_T,
                        doc="TIFF files             ``*.tif``                LOCAL"),
               Constant('FILE_FILTER_EMF', value='21', type=Type.INT32_T,
                        doc="Enhanced Metafies      ``*.emf``                LOCAL"),
               Constant('FILE_FILTER_BMP', value='22', type=Type.INT32_T,
                        doc="Bitmap files           ``*.bmp``                LOCAL"),
               Constant('FILE_FILTER_LUT', value='23', type=Type.INT32_T,
                        doc="ER Mapper LUT          ``*.lut``                GEOSOFT"),
               Constant('FILE_FILTER_PNG', value='24', type=Type.INT32_T,
                        doc="PNG files              ``*.png``                LOCAL"),
               Constant('FILE_FILTER_JPG', value='25', type=Type.INT32_T,
                        doc="JPG files              ``*.jpg``                LOCAL"),
               Constant('FILE_FILTER_PCX', value='26', type=Type.INT32_T,
                        doc="PCX files              ``*.pcx``                LOCAL"),
               Constant('FILE_FILTER_GIF', value='27', type=Type.INT32_T,
                        doc="GIF files              ``*.gif``                LOCAL"),
               Constant('FILE_FILTER_GRD', value='28', type=Type.INT32_T,
                        doc="GRD files              ``*.grd``                LOCAL"),
               Constant('FILE_FILTER_ERS', value='29', type=Type.INT32_T,
                        doc="ERS files              ``*.ers``                LOCAL"),
               Constant('FILE_FILTER_EPS', value='30', type=Type.INT32_T,
                        doc="EPS files              ``*.eps``                LOCAL"),
               Constant('FILE_FILTER_SHP', value='31', type=Type.INT32_T,
                        doc="ArcView Shape files    ``*.shp``                LOCAL"),
               Constant('FILE_FILTER_CGM', value='32', type=Type.INT32_T,
                        doc="CGM files              ``*.cgm``                LOCAL"),
               Constant('FILE_FILTER_TAB', value='33', type=Type.INT32_T,
                        doc="MapInfo Tab files      ``*.tab``                LOCAL"),
               Constant('FILE_FILTER_COMPS', value='34', type=Type.INT32_T,
                        doc="Software Components    Components           LOCAL"),
               Constant('FILE_FILTER_CSV', value='35', type=Type.INT32_T,
                        doc="MapInfo Tab files      ``*.tab``                LOCAL"),
               Constant('FILE_FILTER_GPF', value='36', type=Type.INT32_T,
                        doc="Geosoft Project        ``*.gpf``                LOCAL"),
               Constant('FILE_FILTER_PLY', value='37', type=Type.INT32_T,
                        doc="Geosoft Polygons       ``*.ply``                LOCAL"),
               Constant('FILE_FILTER_STM', value='38', type=Type.INT32_T,
                        doc="Scatter templates      ``*.stm``                LOCAL"),
               Constant('FILE_FILTER_TTM', value='39', type=Type.INT32_T,
                        doc="Triplot templates      ``*.ttm``                LOCAL"),
               Constant('FILE_FILTER_XYZ', value='40', type=Type.INT32_T,
                        doc="Geosoft XYZ files      ``*.xyz``                LOCAL"),
               Constant('FILE_FILTER_BAR', value='41', type=Type.INT32_T,
                        doc="Geosoft Bar file       ``*.geobar``             LOCAL"),
               Constant('FILE_FILTER_GEOSOFT_LICENSE', value='42', type=Type.INT32_T,
                        doc="Geosoft License files   ``*.geosoft_license``   LOCAL"),
               Constant('FILE_FILTER_XML', value='43', type=Type.INT32_T,
                        doc="XML files              ``*.xml``                LOCAL"),
               Constant('FILE_FILTER_GXNET', value='44', type=Type.INT32_T,
                        doc="GX.NET files           ``*.dll``                GEOSOFT"),
               Constant('FILE_FILTER_ECW', value='45', type=Type.INT32_T,
                        doc="ECW files              ``*.ecw``                LOCAL"),
               Constant('FILE_FILTER_J2K', value='46', type=Type.INT32_T,
                        doc="J2K JPEG 2000 files    ``*.j2k``                LOCAL"),
               Constant('FILE_FILTER_JP2', value='47', type=Type.INT32_T,
                        doc="JP2 JPEG 2000 files    ``*.jp2``                LOCAL"),
               Constant('FILE_FILTER_SEL', value='48', type=Type.INT32_T,
                        doc="acQuire parameters     ``*.sel``                LOCAL"),
               Constant('FILE_FILTER_SVG', value='49', type=Type.INT32_T,
                        doc="SVG file               ``*.svg``                LOCAL"),
               Constant('FILE_FILTER_SVZ', value='50', type=Type.INT32_T,
                        doc="SVG Compressed file    ``*.svz``                LOCAL"),
               Constant('FILE_FILTER_WRP', value='51', type=Type.INT32_T,
                        doc="Warp file              ``*.wrp``                LOCAL"),
               Constant('FILE_FILTER_MAPPLOT', value='52', type=Type.INT32_T,
                        doc="MAPPLOT file           ``*.con``                LOCAL"),
               Constant('FILE_FILTER_DTM', value='53', type=Type.INT32_T,
                        doc="Surpac DTM files       ``*.dtm``                LOCAL"),
               Constant('FILE_FILTER_VOXEL', value='54', type=Type.INT32_T,
                        doc="Geosoft Voxel          ``*.geosoft_voxel``      LOCAL"),
               Constant('FILE_FILTER_MAPTEMPLATE', value='55', type=Type.INT32_T,
                        doc="Map Template file      ``*.geosoft_maptemplate``      LOCAL"),
               Constant('FILE_FILTER_ACTION', value='56', type=Type.INT32_T,
                        doc="Action Scripts         ``*.action``             LOCAL"),
               Constant('FILE_FILTER_DM', value='57', type=Type.INT32_T,
                        doc="Datamine files         ``*.dm``                 LOCAL"),
               Constant('FILE_FILTER_KML', value='58', type=Type.INT32_T,
                        doc="Google Earth KML       ``*.kml``                LOCAL"),
               Constant('FILE_FILTER_KMZ', value='59', type=Type.INT32_T,
                        doc="Google Earth Compressed KML  ``*.kmz``          LOCAL"),
               Constant('FILE_FILTER_TARGET_PLAN', value='60', type=Type.INT32_T,
                        doc="Target parameter ini file for plans      ``*.inp``    LOCAL"),
               Constant('FILE_FILTER_TARGET_SECTION', value='61', type=Type.INT32_T,
                        doc="Target parameter ini file for sections   ``*.ins``    LOCAL"),
               Constant('FILE_FILTER_TARGET_STRIPLOG', value='62', type=Type.INT32_T,
                        doc="Target parameter ini file for strip logs ``*.inl``    LOCAL"),
               Constant('FILE_FILTER_TARGET_3D', value='63', type=Type.INT32_T,
                        doc="Target parameter ini file for 3D plots   ``*.in3``    LOCAL"),
               Constant('FILE_FILTER_ARGIS_LYR', value='64', type=Type.INT32_T,
                        doc="ArcGIS Layer files			 ``*.lyr``    LOCAL"),
               Constant('FILE_FILTER_ARGIS_MXD', value='65', type=Type.INT32_T,
                        doc="ArcGIS Map Document files	 ``*.mxd``    LOCAL"),
               Constant('FILE_FILTER_GOCAD_TS', value='66', type=Type.INT32_T,
                        doc="GOCAD TSurf files			 ``*.ts``     LOCAL"),
               Constant('FILE_FILTER_LST', value='67', type=Type.INT32_T,
                        doc="Geosoft list of items: names, values  ``*.lst``     LOCAL"),
               Constant('FILE_FILTER_ECS', value='68', type=Type.INT32_T,
                        doc="GM-SYS external coordinate system     ``*.ecs``     LOCAL"),
               Constant('FILE_FILTER_TARGET_FENCE', value='69', type=Type.INT32_T,
                        doc="Target parameter ini file for fence sections   ``*.ins``    LOCAL"),
               Constant('FILE_FILTER_GMS3D', value='70', type=Type.INT32_T,
                        doc="GM-SYS 3D model   ``*.geosoft_gmsys3d``    LOCAL"),
               Constant('FILE_FILTER_BT2', value='71', type=Type.INT32_T,
                        doc="GEMCOM BT2 ``*.bt2`` LOCAL"),
               Constant('FILE_FILTER_BPR', value='72', type=Type.INT32_T,
                        doc="GEMCOM BPR ``*.bpr`` LOCAL"),
               Constant('FILE_FILTER_BPR2', value='73', type=Type.INT32_T,
                        doc="GEMCOM BPR2 ``*.bpr2`` LOCAL"),
               Constant('FILE_FILTER_XLS', value='74', type=Type.INT32_T,
                        doc="Excel 97-2003 workbook		``*.xls``					LOCAL"),
               Constant('FILE_FILTER_XLSX', value='75', type=Type.INT32_T,
                        doc="Excel 2007 workbook 			``*.xlsx``				LOCAL"),
               Constant('FILE_FILTER_MDB', value='76', type=Type.INT32_T,
                        doc="Access 97-2003  				``*.mdb`` 				LOCAL"),
               Constant('FILE_FILTER_ACCDB', value='77', type=Type.INT32_T,
                        doc="Access 2007 					``*.accdb`` 				LOCAL"),
               Constant('FILE_FILTER_INTERSECTION_TBL', value='78', type=Type.INT32_T,
                        doc="Levelling intersection		``*.tbl``					LOCAL"),
               Constant('FILE_FILTER_UBC_CON', value='79', type=Type.INT32_T,
                        doc="UBC DCIP2D Conductivity model files ``*.con``		LOCAL"),
               Constant('FILE_FILTER_UBC_CHG', value='80', type=Type.INT32_T,
                        doc="UBC DCIP2D Chargeability model files ``*.chg``	LOCAL"),
               Constant('FILE_FILTER_UBC_MSH', value='81', type=Type.INT32_T,
                        doc="UBC DCIP2D Mesh files		``*.msh``					LOCAL"),
               Constant('FILE_FILTER_UBC_MSH_DAT', value='82', type=Type.INT32_T,
                        doc="UBC DCIP2D Mesh files		``*.dat``					LOCAL"),
               Constant('FILE_FILTER_UBC_TOPO_DAT', value='83', type=Type.INT32_T,
                        doc="UBC DCIP2D Topo files		``*.dat``					LOCAL"),
               Constant('FILE_FILTER_UBC_TOPO_XYZ', value='84', type=Type.INT32_T,
                        doc="UBC DCIP2D Topo files		``*.xyz``					LOCAL"),
               Constant('FILE_FILTER_XYZ_TEMPLATE_I0', value='85', type=Type.INT32_T,
                        doc="XYZ Import Templates		      ``*.i0``				LOCAL"),
               Constant('FILE_FILTER_PICO_TEMPLATE_I1', value='86', type=Type.INT32_T,
                        doc="Picodas Import Templates      ``*.i1``				LOCAL"),
               Constant('FILE_FILTER_BB_TEMPLATE_I2', value='87', type=Type.INT32_T,
                        doc="Block Binary Import Templates ``*.i2``				LOCAL"),
               Constant('FILE_FILTER_ASCII_TEMPLATE_I3', value='88', type=Type.INT32_T,
                        doc="ASCII Import Templates		   ``*.i3``				LOCAL"),
               Constant('FILE_FILTER_ODBC_TEMPLATE_I4', value='89', type=Type.INT32_T,
                        doc="ODBC Import Templates		   ``*.i4``				LOCAL"),
               Constant('FILE_FILTER_EXP', value='90', type=Type.INT32_T,
                        doc="Math expression files		   ``*.exp``  			LOCAL"),
               Constant('FILE_FILTER_SEGY', value='91', type=Type.INT32_T,
                        doc="SEG-Y files							``*.sgy``  			LOCAL"),
               Constant('FILE_FILTER_DAARC500', value='92', type=Type.INT32_T,
                        doc="DAARC500 files						xYYMMDD 		   LOCAL"),
               Constant('FILE_FILTER_TXT', value='93', type=Type.INT32_T,
                        doc="Text files							``*.txt``  			LOCAL"),
               Constant('FILE_FILTER_VOXEL_INVERSION', value='94', type=Type.INT32_T,
                        doc="Voxi									``*.geosoft_voxi``	LOCAL"),
               Constant('FILE_FILTER_GMS', value='95', type=Type.INT32_T,
                        doc="GM-SYS Profile model file		``*.gms``	LOCAL"),
               Constant('FILE_FILTER_FLT3D', value='96', type=Type.INT32_T,
                        doc="Geosoft 3D filter files			``*.flt3d``			LOCAL"),
               Constant('FILE_FILTER_RESOURCE_PACK', value='97', type=Type.INT32_T,
                        doc="Geosoft Resource Update Packages ``*.geosoft_resource_pack`` LOCAL"),
               Constant('FILE_FILTER_GEOSTRING', value='98', type=Type.INT32_T,
                        doc="Geostring files ``*.geosoft_string`` LOCAL"),
               Constant('FILE_FILTER_GEOSURFACE', value='99', type=Type.INT32_T,
                        doc="Geosurface files ``*.geosoft_surface`` LOCAL"),
               Constant('FILE_FILTER_GEOSOFT3DV', value='100', type=Type.INT32_T,
                        doc="Geosoft :class:`3DV` ``*.geosoft_3dv`` LOCAL"),
               Constant('FILE_FILTER_VECTORVOXEL', value='101', type=Type.INT32_T,
                        doc="Geosoft Vector Voxel ``*.geosoft_vectorvoxel`` LOCAL"),
               Constant('FILE_FILTER_FLT', value='102', type=Type.INT32_T,
                        doc="Geosoft Filters ``*.flt`` LOCAL"),
               Constant('FILE_FILTER_XYZ_TEMPLATE_O0', value='103', type=Type.INT32_T,
                        doc="XYZ Export Templates ``*.o0`` LOCAL"),
               Constant('FILE_FILTER_GMS2D', value='104', type=Type.INT32_T,
                        doc="GM-SYS Profile model    ``*.geosoft_gmsys2d``   LOCAL"),
               Constant('FILE_FILTER_IP_DATABASE_TEMPLATE', value='105', type=Type.INT32_T,
                        doc=":class:`IP` Database Template ``*.geosoft_ipdatabasetemplate`` LOCAL"),
               Constant('FILE_FILTER_GEOSOFT_RESOURCE_MODULE', value='106', type=Type.INT32_T,
                        doc="Geosoft Resource Module ``*.geosoft_resources``  LOCAL"),
               Constant('FILE_FILTER_VT', value='107', type=Type.INT32_T,
                        doc="Shell VT files     ``*.vt``        LOCAL"),
               Constant('FILE_FILTER_INT', value='108', type=Type.INT32_T,
                        doc="Shell INT files     ``*.int``      LOCAL"),
               Constant('FILE_FILTER_SGT', value='109', type=Type.INT32_T,
                        doc="Shell SGT files     ``*.sgt``      LOCAL"),
               Constant('FILE_FILTER_IMGVIEW', value='110', type=Type.INT32_T,
                        doc="Image Viewer files  ``*.imgview``  LOCAL"),
               Constant('FILE_FILTER_ZIP', value='111', type=Type.INT32_T,
                        doc="Zip files  ``*.zip``  LOCAL"),
               Constant('FILE_FILTER_GPS_TABLE', value='112', type=Type.INT32_T,
                        doc="GPS Table ``*.tbl`` GEOSOFT"),
               Constant('FILE_FILTER_VULCAN_TRIANGULATION', value='113', type=Type.INT32_T,
                        doc="Maptek Vulcan trianguilation file   ``*.tbl``     LOCAL"),
               Constant('FILE_FILTER_VULCAN_BLOCK_MODEL', value='114', type=Type.INT32_T,
                        doc="Maptek Vulcan block model file       ``*.bmf``                        LOCAL"),
               Constant('FILE_FILTER_PRJVIEW', value='115', type=Type.INT32_T,
                        doc="Layout files  ``*.prjview``  LOCAL"),
               Constant('FILE_FILTER_LEAPFROG_MODEL', value='116', type=Type.INT32_T,
                        doc="Leapfrog model files  ``*.lfm``  LOCAL"),
               Constant('FILE_FILTER_IOGAS', value='117', type=Type.INT32_T,
                        doc="Reflex ioGAS files  ``*.gas``  LOCAL"),
               Constant('FILE_FILTER_ASEG_ESF', value='118', type=Type.INT32_T,
                        doc="ASEG ESF file  ``*.esf``  LOCAL"),
               Constant('FILE_FILTER_LACOSTE_DAT', value='119', type=Type.INT32_T,
                        doc="Micro-g LaCoste MGS-6 gravity files  ``*.:class``:`DAT`  LOCAL"),
               Constant('FILE_FILTER_VAR', value='120', type=Type.INT32_T,
                        doc="Geosoft variogram file  ``*.var``  LOCAL"),
               Constant('FILE_FILTER_P190', value='121', type=Type.INT32_T,
                        doc="UKOOA data exchange file  ``*.p190``  LOCAL"),
               Constant('FILE_FILTER_UBC_OBS_DAT', value='122', type=Type.INT32_T,
                        doc="UBC observation files ``*.dat``		LOCAL"),
               Constant('FILE_FILTER_UBC_LOC', value='123', type=Type.INT32_T,
                        doc="UBC location files ``*.loc``		LOCAL"),
               Constant('FILE_FILTER_UBC_MOD', value='124', type=Type.INT32_T,
                        doc="UBC model files ``*.mod``		LOCAL"),
               Constant('FILE_FILTER_UBC_DEN', value='125', type=Type.INT32_T,
                        doc="UBC density model files ``*.den``		LOCAL"),
               Constant('FILE_FILTER_UBC_SUS', value='126', type=Type.INT32_T,
                        doc="UBC susceptibility model files ``*.sus``		LOCAL"),
               Constant('FILE_FILTER_GOCAD_VOXET', value='127', type=Type.INT32_T,
                        doc="GOCAD voxet files ``*.vo``		LOCAL")
           ]),

    Define('FILE_FORM',
           doc="File Form Defines",
           constants=[
               Constant('FILE_FORM_OPEN', value='0', type=Type.INT32_T,
                        doc="Open a file"),
               Constant('FILE_FORM_SAVE', value='1', type=Type.INT32_T,
                        doc="Save a file")
           ]),

    Define('GS_DIRECTORY',
           doc="Geosoft predefined directory",
           constants=[
               Constant('GS_DIRECTORY_NONE', value='0', type=Type.INT32_T),
               Constant('GS_DIRECTORY_GEOSOFT', value='1', type=Type.INT32_T),
               Constant('GS_DIRECTORY_BIN', value='2', type=Type.INT32_T),
               Constant('GS_DIRECTORY_GER', value='3', type=Type.INT32_T),
               Constant('GS_DIRECTORY_OMN', value='4', type=Type.INT32_T),
               Constant('GS_DIRECTORY_TBL', value='5', type=Type.INT32_T),
               Constant('GS_DIRECTORY_FONTS', value='6', type=Type.INT32_T),
               Constant('GS_DIRECTORY_GX', value='7', type=Type.INT32_T),
               Constant('GS_DIRECTORY_GS', value='8', type=Type.INT32_T),
               Constant('GS_DIRECTORY_APPS', value='9', type=Type.INT32_T),
               Constant('GS_DIRECTORY_ETC', value='10', type=Type.INT32_T),
               Constant('GS_DIRECTORY_HLP', value='11', type=Type.INT32_T),
               Constant('GS_DIRECTORY_GXDEV', value='12', type=Type.INT32_T),
               Constant('GS_DIRECTORY_COMPONENT', value='13', type=Type.INT32_T),
               Constant('GS_DIRECTORY_CSV', value='14', type=Type.INT32_T),
               Constant('GS_DIRECTORY_LIC', value='15', type=Type.INT32_T),
               Constant('GS_DIRECTORY_INI', value='16', type=Type.INT32_T),
               Constant('GS_DIRECTORY_TEMP', value='17', type=Type.INT32_T),
               Constant('GS_DIRECTORY_UETC', value='18', type=Type.INT32_T),
               Constant('GS_DIRECTORY_UMAPTEMPLATE', value='19', type=Type.INT32_T),
               Constant('GS_DIRECTORY_COMPONENT_SCRIPTS', value='50', type=Type.INT32_T),
               Constant('GS_DIRECTORY_COMPONENT_HTML', value='51', type=Type.INT32_T),
               Constant('GS_DIRECTORY_IMG', value='52', type=Type.INT32_T),
               Constant('GS_DIRECTORY_BAR', value='53', type=Type.INT32_T),
               Constant('GS_DIRECTORY_GXNET', value='54', type=Type.INT32_T),
               Constant('GS_DIRECTORY_MAPTEMPLATE', value='55', type=Type.INT32_T)
           ]),

    Define('IMPCH_TYPE',
           doc="Import Chem defines",
           constants=[
               Constant('IMPCH_TYPE_DATA', value='0', type=Type.INT32_T),
               Constant('IMPCH_TYPE_ASSAY', value='1', type=Type.INT32_T)
           ]),

    Define('WINDOW_STATE',
           doc="Window State Options",
           constants=[
               Constant('WINDOW_RESTORE', value='0', type=Type.INT32_T),
               Constant('WINDOW_MINIMIZE', value='1', type=Type.INT32_T),
               Constant('WINDOW_MAXIMIZE', value='2', type=Type.INT32_T)
           ]),

    Define('XTOOL_ALIGN',
           doc="XTool docking alignment flags",
           constants=[
               Constant('XTOOL_ALIGN_LEFT', value='1', type=Type.INT32_T),
               Constant('XTOOL_ALIGN_TOP', value='2', type=Type.INT32_T),
               Constant('XTOOL_ALIGN_RIGHT', value='4', type=Type.INT32_T),
               Constant('XTOOL_ALIGN_BOTTOM', value='8', type=Type.INT32_T),
               Constant('XTOOL_ALIGN_ANY', value='15', type=Type.INT32_T)
           ]),

    Define('XTOOL_DOCK',
           doc="XTool default docking state",
           constants=[
               Constant('XTOOL_DOCK_TOP', value='1', type=Type.INT32_T),
               Constant('XTOOL_DOCK_LEFT', value='2', type=Type.INT32_T),
               Constant('XTOOL_DOCK_RIGHT', value='3', type=Type.INT32_T),
               Constant('XTOOL_DOCK_BOTTOM', value='4', type=Type.INT32_T),
               Constant('XTOOL_DOCK_FLOAT', value='5', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('CreateWNDFromHWND_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="Create a standard WND object from an HWND.",
               notes="""
               The object returned must be destroyed by the
               destroy object call.
               """,
               return_type="WND",
               return_doc="x - WND object created",
               parameters = [
                   Parameter('p1', type="HWND", is_val=True,
                             doc="HWND Handle")
               ]),

        Method('Fft2SpecFilter_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Interactive :class:`FFT2` radially averaged power spectrum filter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('spec_file_name', type=Type.STRING,
                             doc="Name of the input spectrum file"),
                   Parameter('con_file_name', type=Type.STRING,
                             doc="Name of the output control file")
               ]),

        Method('GetParentWND_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="Get the current parent window",
               return_type="WND",
               return_doc="Parent window."),

        Method('GetPrinterLST_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Gets a list of all printers.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('lst', type="LST",
                             doc="List to place into")
               ]),

        Method('iGetWindowState_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Retrieve the current state of the Oasis montaj window",
               return_type=Type.INT32_T,
               return_doc=":def:`WINDOW_STATE`"),

        Method('SetWindowState_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Changes the state of the Oasis montaj window",
               return_type=Type.VOID,
               parameters = [
                   Parameter('state', type=Type.INT32_T,
                             doc=":def:`WINDOW_STATE`")
               ]),

        Method('GetWindowPosition_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the Oasis montaj window's position state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('left', type=Type.INT32_T, is_ref=True,
                             doc="Window left position"),
                   Parameter('top', type=Type.INT32_T, is_ref=True,
                             doc="Window top position"),
                   Parameter('right', type=Type.INT32_T, is_ref=True,
                             doc="Window right position"),
                   Parameter('bottom', type=Type.INT32_T, is_ref=True,
                             doc="Window bottom position"),
                   Parameter('state', type=Type.INT32_T, is_ref=True,
                             doc="Window state :def:`WINDOW_STATE`")
               ]),

        Method('SetWindowPosition_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the Oasis montaj window's position and state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('left', type=Type.INT32_T,
                             doc="Window left position"),
                   Parameter('top', type=Type.INT32_T,
                             doc="Window top position"),
                   Parameter('right', type=Type.INT32_T,
                             doc="Window right position"),
                   Parameter('bottom', type=Type.INT32_T,
                             doc="Window bottom position"),
                   Parameter('state', type=Type.INT32_T,
                             doc="Window state :def:`WINDOW_STATE`")
               ]),

        Method('GetWindowArea_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, 
               doc="Get the location of the Oasis montaj window.",
               notes="""
               The Coordinates are pixels with 0,0 being the top
               left corner of the Screen.
               
               if the max values are equal to or less than the min values
               the window will be mimimized. If any Min values are :def_val:`GS_S4MN`
               or any Max values are :def_val:`GS_S4MX`, the window is maximized.
               
               See also :func:`GetClientWindowArea_GUI`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('min_x', type=Type.INT32_T, is_ref=True,
                             doc="X Min returned"),
                   Parameter('min_y', type=Type.INT32_T, is_ref=True,
                             doc="Y Min returned"),
                   Parameter('max_x', type=Type.INT32_T, is_ref=True,
                             doc="X Max returned"),
                   Parameter('max_y', type=Type.INT32_T, is_ref=True,
                             doc="Y Max returned")
               ]),

        Method('GetClientWindowArea_GUI', module='None', version='9.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Get the location of the Oasis montaj client window.",
               notes="""
               Returns the coordinates of the client window area (where MDI document windows are placed).
               The returned coordinates are 0,0 for the minimum X and Y and the window width
               width and height for the maximum X and Y.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('min_x', type=Type.INT32_T, is_ref=True,
                             doc="X Min returned (0)"),
                   Parameter('min_y', type=Type.INT32_T, is_ref=True,
                             doc="Y Min returned (0)"),
                   Parameter('max_x', type=Type.INT32_T, is_ref=True,
                             doc="X Max returned (width)"),
                   Parameter('max_y', type=Type.INT32_T, is_ref=True,
                             doc="Y Max returned (height)")
               ]),

        Method('GridStatHist_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Display Histogram of grid",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid_name', type=Type.STRING,
                             doc="Name of the grid to get stats from")
               ]),

        Method('VoxelStatHist_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Display Histogram of Voxel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox_name', type=Type.STRING,
                             doc="Name of the Voxel to get stats from")
               ]),

        Method('iColorForm_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Select a color.",
               notes="""
               Color value is set on input, and new value returned.
               If the input color type is :def_val:`C_TRANSPARENT`, then the color
               is set to white, if any other type is input the output is
               guaranteed to be of the same type.
               
               If ``no_col`` is 1, then on exit, if white is
               selected, the user is prompted: 'Do you want white (Yes) or
               "None" (No) ?' and the color is converted as requested.
               If this is not the case, the :def_val:`C_TRANSPARENT` is converted
               to white (if "Ok" is selected) and no choice is offered.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('col', type=Type.INT32_T, is_ref=True,
                             doc="Color (modified)"),
                   Parameter('no_col', type=Type.INT32_T,
                             doc="Ask about :def_val:`C_TRANSPARENT` if white is selected (1: yes, 0: no)?")
               ]),

        Method('iColorTransform_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Define an :class:`ITR` of up to 8 zones.",
               notes="""
               The statistics object is required in order to determine
               data ranges, percentiles, etc. Create it using
               :func:`CreateExact_ST`, or be sure to enable histogram statistics.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if OK
               1 if user cancels
               """,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object (modified)"),
                   Parameter('st', type="ST",
                             doc=":class:`ST` object (input)")
               ]),

        Method('iCoordSysWizard_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Launch the coordinate system definition/display :class:`GUI`.",
               notes="""
               Launches the new GX.Net single-dialog coordinate system
               definition dialog. The input :class:`IPJ` is modified on return
               if OK is selected (and the editable parameter is 1).
               The "Data source label" and "Data source" is information displayed
               in the dialog for the user to know where the :class:`IPJ` came from (e.g. "Grid: X.grd")
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('editable', type=Type.INT32_T,
                             doc="Editable :class:`IPJ` (0:No, 1:Yes)"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`COORDSYS_MODE`"),
                   Parameter('source_label', type=Type.STRING,
                             doc="Data source label"),
                   Parameter('source', type=Type.STRING,
                             doc="Data source")
               ]),

        Method('iCoordSysWizardLicensed_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Launch the coordinate system definition/display :class:`GUI`.",
               notes="""
               Same as :func:`iCoordSysWizardLicensed_GUI` but will always be editable. The other
               method is not editable in the viewer while this one is.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('editable', type=Type.INT32_T,
                             doc="Editable :class:`IPJ` (0:No, 1:Yes)"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`COORDSYS_MODE`"),
                   Parameter('source_label', type=Type.STRING,
                             doc="Data source label"),
                   Parameter('source', type=Type.STRING,
                             doc="Data source")
               ]),

        Method('iCoordSysWizardGrid_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch the coordinate system definition/display :class:`GUI`.",
               notes="""
               Same as :func:`iCoordSysWizardLicensed_GUI` but allows the original grid info to be adjusted
               when projections on section or oriented plan grids are modified.
               In the tool, it is the "modified" orientation required to keep the edited projection's grid
               in the same location as it was in the target projection.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('ipj', type="IPJ",
                             doc="Original grid :class:`IPJ` object"),
                   Parameter('target_ipj', type="IPJ",
                             doc="Source (target) grid :class:`IPJ` object. This is supplied so the modified orientation can be calculated and displayed."),
                   Parameter('editable', type=Type.INT32_T,
                             doc="Editable :class:`IPJ` (0:No, 1:Yes)"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`COORDSYS_MODE`"),
                   Parameter('source_label', type=Type.STRING,
                             doc="Data source label"),
                   Parameter('source', type=Type.STRING,
                             doc="Data source"),
                   Parameter('nx', type=Type.INT32_T,
                             doc="Number of cells in X"),
                   Parameter('ny', type=Type.INT32_T,
                             doc="Number of cells in Y"),
                   Parameter('x0', type=Type.DOUBLE, is_ref=True,
                             doc="Grid orgin X (grid's own coordinate system)"),
                   Parameter('y0', type=Type.DOUBLE, is_ref=True,
                             doc="Grid orgin Y (grid's own coordinate system)"),
                   Parameter('dx', type=Type.DOUBLE, is_ref=True,
                             doc="Grid cell size X"),
                   Parameter('dy', type=Type.DOUBLE, is_ref=True,
                             doc="Grid cell size Y"),
                   Parameter('rot', type=Type.DOUBLE, is_ref=True,
                             doc="Grid rotation angle (degrees CCW)")
               ]),

        Method('iDatabaseType_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Returns the type string of an external DAO database.",
               notes="""
               If the file extension is "mdb", then an MSJET (Microsoft Access)
               database is assumed. If the file name is "ODBC", then "ODBC" is
               returned as the type. Otherwise, a dialog appears listing the
               other valid DAO database types.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               terminates on error
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="File Name"),
                   Parameter('type', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Database type (returned)"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of type string")
               ]),

        Method('iDatamineType_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Returns the type of a Datamine file.",
               notes="""
               Often, a Datamine file can be opened a number of different ways
               (e.g. as a string file or a as wireframe (point) file.
               The following function checks to see if there is a choice to be made
               between types supported by Geosoft for import. If not, it just returns
               the original type "hint" from Datamine. If there is a choice, it puts up
               a dialog with the choices for the user to pick from.
               Do a bit-wise AND with the returned type to determine the file type
               (or the type selected).
               
               Currently supported overlapping types/choices:
               
               dmString
               dmWireframePoint
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="File Name (for display purposes only)"),
                   Parameter('type', type=Type.INT32_T, is_ref=True)
               ]),

        Method('iExportXYZTemplateEditor_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="""
               Allows the user to edit XYZ export template
               using a complex dialog. The Template name
               may change during editing.
               """,
               notes="""
               Only uses the current :class:`DB`. This function does
               not exactly work as supposed to. Instead of using
               the :class:`EDB` handle passed to it, it only will use
               the current :class:`DB`. Please see ExportXYXTemplateEditorEx_GUI
               for an updated function.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('template', type=Type.STRING,
                             doc="Name of the Template (can change)"),
                   Parameter('size', type=Type.INT32_T,
                             doc="Size of the Template")
               ]),

        Method('iExportXYZTemplateEditorEx_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="""
               Allows the user to edit an XYZ export template
               using a complex dialog. The template name
               may change during editing.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` object"),
                   Parameter('template', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Template name"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of name")
               ]),

        Method('iFileFilterIndex_GUI', module='geoguilib', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Return the FILE_FILTER_XXX value for a file filter string.",
               notes="""
               For example, if "Database (``*.gdb``)" is input,
               then the :def_val:`FILE_FILTER_GDB` value is returned.
               """,
               return_type=Type.INT32_T,
               return_doc=":def:`FILE_FILTER`, -1 if not found",
               parameters = [
                   Parameter('filter', type=Type.STRING,
                             doc="Input filter string")
               ]),

        Method('iGCSDatumWarningSHP_GUI', module='geoguilib', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Launch the GCS Datum Warning dialog for :class:`SHP` files.",
               notes="Runs the GCS Warning dialog with one data source",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('data_source', type=Type.STRING,
                             doc="Data source"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` object")
               ]),

        Method('iGCSDatumWarningSHPDBEx_GUI', module='geoguilib', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Launch the GCS Datum Warning dialog for :class:`SHP` files (Database).",
               notes="Runs the GCS Warning dialog with multiple data sources (Database)",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('source_lst', type="LST",
                             doc="Data source names"),
                   Parameter('datum_from_lst', type="LST",
                             doc="Corresponding datum names"),
                   Parameter('ldtlst', type="LST",
                             doc="Returned corresponding LDT names"),
                   Parameter('db', type="DB")
               ]),

        Method('iGCSDatumWarningSHPEx_GUI', module='geoguilib', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Launch the GCS Datum Warning dialog for :class:`SHP` files.",
               notes="Runs the GCS Warning dialog with multiple data sources",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('source_lst', type="LST",
                             doc="Data source names"),
                   Parameter('datum_from_lst', type="LST",
                             doc="Corresponding datum names"),
                   Parameter('ldtlst', type="LST",
                             doc="Returned corresponding LDT names"),
                   Parameter('mview', type="MVIEW")
               ]),

        Method('iGetAreaOfInterest_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Get the current area of interest from the application.",
               notes="""
               Depending on what is currently visible on screen and
               the defined coordinate system the user may be prompted
               by a warning and optionaly cancel the process.
               """,
               return_type=Type.INT32_T,
               return_doc=":def:`AOI_RETURN_STATE`",
               parameters = [
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Min X"),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Min Y"),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Max X"),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Max y"),
                   Parameter('ply', type="PLY",
                             doc="AOI Bounding :class:`PLY` (Filled if available, otherwise empty)"),
                   Parameter('ipj', type="IPJ",
                             doc="AOI Bounding :class:`IPJ`")
               ]),

        Method('iGetAreaOfInterest3D_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Get the current area of interest from the application in 3D.",
               notes="""
               Depending on what is currently visible on screen and
               the defined coordinate system the user may be prompted
               by a warning and optionaly cancel the process.
               """,
               return_type=Type.INT32_T,
               return_doc=":def:`AOI_RETURN_STATE`",
               parameters = [
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Min X"),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Min Y"),
                   Parameter('min_z', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Min Z"),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Max X"),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Max y"),
                   Parameter('max_z', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Max Z"),
                   Parameter('ply', type="PLY",
                             doc="AOI Bounding :class:`PLY` (Filled if available, otherwise empty)"),
                   Parameter('ipj', type="IPJ",
                             doc="AOI Bounding :class:`IPJ`")
               ]),

        Method('IGetDATDefaults_GUI', module='geoguilib', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Return the user default extension and qualifier for grids/images.",
               notes="""
               The default grid/image filters are normally stored in
               "MONTAJ.DEFAULT_XGD_IN" and "MONTAJ.DEFAULT_XGD_OUT"
               
               If no filter is defined, or the filter is not found
               then "grd" and "GRD" are returned as the default extension
               and qualifier.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('flags', type=Type.INT32_T,
                             doc=":def:`DAT_TYPE`"),
                   Parameter('open', type=Type.INT32_T,
                             doc=":def:`FILE_FORM`"),
                   Parameter('ext', type=Type.STRING, is_ref=True, size_of_param='ext_size',
                             doc='Returned default extension (e.g. "grd")'),
                   Parameter('ext_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size for extension"),
                   Parameter('qual', type=Type.STRING, is_ref=True, size_of_param='qual_size',
                             doc='Returned default qualifier (e.g. "GRD")'),
                   Parameter('qual_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size for the qualifier")
               ]),

        Method('IGetFileFilter_GUI', module='geoguilib', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Return the defined filter, mask, extension and directory for an input filter.",
               notes="""
               Returns the four parts of the file filter;
               e.g. for :def_val:`FILE_FILTER_GDB` it returns:
               
               Filter:    "Database (``*.gdb``)"
               Mask:      "``*.gdb``"
               Extension: "gdb"
               Directory: ":def_val:`GS_DIRECTORY_NONE`"
               
               This function is useful for constuction open/save dialog
               file filters, especially in GX.Net functions.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('file_filter', type=Type.INT32_T,
                             doc=":def:`FILE_FILTER`"),
                   Parameter('filter', type=Type.STRING, is_ref=True, size_of_param='filter_size',
                             doc="Returned file filter string"),
                   Parameter('filter_size', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of the file filter buffer"),
                   Parameter('mask', type=Type.STRING, is_ref=True, size_of_param='m',
                             doc="Returned file mask string"),
                   Parameter('m', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of the file mask buffer"),
                   Parameter('ext', type=Type.STRING, is_ref=True, size_of_param='e',
                             doc="Returned file extension"),
                   Parameter('e', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of the file extension buffer"),
                   Parameter('path', type=Type.INT32_T, is_ref=True,
                             doc=":def:`GS_DIRECTORY` Returned directory.")
               ]),

        Method('IGetGSDirectory_GUI', module='geoguilib', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Return the directory path for value of :def:`GS_DIRECTORY`.",
               notes="""
               Works along with the :func:`IGetFileFilter_GUI` function. Note that
               most values of FILE_FILTER_XXX will return :def_val:`GS_DIRECTORY_NONE`,
               and give the current workspace directory.
               
               This function is useful for constuction open/save dialog
               file filters, especially in GX.Net functions.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('path', type=Type.INT32_T,
                             doc=":def:`GS_DIRECTORY` Returned directory."),
                   Parameter('dir', type=Type.STRING, is_ref=True, size_of_param='dir_size',
                             doc="Returned directory path"),
                   Parameter('dir_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of the directory path buffer")
               ]),

        Method('iGetHWNDFromWND_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, no_gxh=True, 
               doc="Get the HWND object from WND object.",
               return_type=Type.INT32_T,
               return_doc="x - HWND object",
               parameters = [
                   Parameter('wnd', type="WND",
                             doc="WND Handle")
               ]),

        Method('IiBrowseDir_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Browses for a specific directory.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('title', type=Type.STRING,
                             doc="Title of the Form"),
                   Parameter('default', type=Type.STRING,
                             doc='Default path (Can be "")'),
                   Parameter('dir_path', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Result Path Buffer (default on input)"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Path Buffer Size")
               ]),

        Method('IiColorTransformEx_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Define an :class:`ITR` of up to 12 zones, with file load/save buttons.",
               notes="""
               The statistics object is required in order to determine
               data ranges, percentiles, etc. Create it using
               :func:`CreateExact_ST`, or be sure to enable histogram statistics.
               The color transform file name is used as the default when the save
               button is pushed, and is updated both after the load and save buttons
               are pushed by the value input or selected by the user.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if OK
               1 if user cancels
               """,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object (modified)"),
                   Parameter('st', type="ST",
                             doc=":class:`ST` object (input)"),
                   Parameter('zones', type=Type.INT32_T,
                             doc="Max number of zones (8 or 12)"),
                   Parameter('load_save', type=Type.INT32_T,
                             doc="Show file load/save buttons (TRUE or FALSE)?"),
                   Parameter('file', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Default color transform file name"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size for the file name")
               ]),

        Method('IiCumulativePercent_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Define a percent-based :class:`ITR` of up to 12 zones.",
               notes="""
               The :class:`ITR` values are interpreted as cumulative percent values, using
               the "PERCENT=1" value in the :class:`ITR`'s :class:`REG`.
               
               Note that processes using ITRs do not automatically know to convert between
               percent values and "actual" data values. The :class:`REG` "PERCENT" value is simply
               a flag to indicate to a user that the values are intended to be in the range
               from 0 < x < 100. The :class:`ITR` should not, therefore, be applied directly to data
               unless that data is already given in percent.
               
               If the file name is defined on input, the initial :class:`ITR` will be loaded from it.
               If it is left blank, a default 5-color transform with
               The color transform file name is used as the default when the save
               button is pushed, and is updated both after the load and save buttons
               are pushed by the value input or selected by the user.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if OK
               1 if user cancels
               """,
               parameters = [
                   Parameter('file', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Default color transform file name"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size for the file name"),
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object (returned)")
               ]),

        Method('IiDatFileForm_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Grid and Image file Open/Save Form for Multiple/Single file selections",
               notes="""
               Remember to make the string size big enough for multiple file
               selections. In the case of multiple selections the names will be separated
               by a semicolon and only the first file will contain the full path.
               
               When using the multiple flag on any of these functions please be aware that
               the string returned will be in the format:
               drive:\\path1\\path2\\name.grid|name2.grid|name3.grid(QUALIFIERS)
               All grids are required to be of the same type.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('title', type=Type.STRING,
                             doc="Title of the Form"),
                   Parameter('default', type=Type.STRING,
                             doc="Default value"),
                   Parameter('psz_file_path', type=Type.STRING, is_ref=True, size_of_param='file_size',
                             doc="Where the file name(s) is returned"),
                   Parameter('file_size', type=Type.INT32_T, default_length='STR_MULTI_FILE',
                             doc="Size of the File Name Buffer"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`DAT_TYPE`"),
                   Parameter('validation_type', type=Type.INT32_T,
                             doc=":def:`FILE_FORM`"),
                   Parameter('multi', type=Type.INT32_T,
                             doc="Allow Multiple file selections = TRUE Single   file selections = FALSE")
               ]),

        Method('IiGenFileForm_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="General file Open/Save Form for Multiple/Single file selections and multiple filter capability",
               notes="""
               Remember to make the string size big enough for multiple file
               selections. In the case of multiple selections the names will be separated
               by a semicolon and only the first file will contain the full path.
               
               Defined Functions     The following four functions are handy defines and simply pass the appropriate
               parameter.
               
               iFileOpen_GUI
               iFileSave_GUI
               iMultiFileOpen_GUI
               iMultiFileSave_GUI
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('title', type=Type.STRING,
                             doc="Title of the Form"),
                   Parameter('filt_vv', type="VV",
                             doc="INT :class:`VV` of file filters to use :def:`FILE_FILTER` The first one is default, can pass (:class:`VV`) 0 for to use next parameter."),
                   Parameter('filter', type=Type.INT32_T,
                             doc=":def:`FILE_FILTER` (ignored if parameter above is not zero)"),
                   Parameter('default', type=Type.STRING,
                             doc="Default value"),
                   Parameter('file_path', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Where the file name(s) is returned"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_MULTI_FILE',
                             doc="Size of the File Name Buffer"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`FILE_FORM`"),
                   Parameter('multi', type=Type.INT32_T,
                             doc="Allow Multiple file selections = TRUE Single   file selections = FALSE")
               ]),

        Method('IiCustomFileForm_GUI', module='None', version='9.3.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="General file Open/Save Form for Multiple/Single file selections and custom filter capability",
               notes="""
               Remember to make the string size big enough for multiple file
               selections. In the case of multiple selections the names will be separated
               by a semicolon and only the first file will contain the full path.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('title', type=Type.STRING,
                             doc="Title of the Form"),
                   Parameter('filter', type=Type.STRING,
                             doc="Custom filter."),
                   Parameter('default', type=Type.STRING,
                             doc="Default value"),
                   Parameter('file_path', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Where the file name(s) is returned"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_MULTI_FILE',
                             doc="Size of the File Name Buffer"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`FILE_FORM`"),
                   Parameter('multi', type=Type.INT32_T,
                             doc="Allow Multiple file selections = TRUE Single   file selections = FALSE")
               ]),

        Method('IiImportDrillDatabaseADO2_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Same as :func:`iImportDrillDatabaseADO_GUI`, but template name is returned.",
               notes="""
               If it is not defined on input, the template name is set
               to be the Wholeplot table name; e.g.
               "HOLESURVEY.i4" for "Project_HOLESURVEY"
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('connect', type=Type.STRING,
                             doc="External database connection string (Blank for OLEDB Wizard)"),
                   Parameter('temp', type=Type.STRING, is_ref=True, size_of_param='temp_size',
                             doc="Template to make (if left blank, the created template name is returned)"),
                   Parameter('temp_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of the template name string"),
                   Parameter('table', type=Type.STRING, is_ref=True, size_of_param='table_size',
                             doc="Name of table"),
                   Parameter('table_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('type', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned :def:`DH_DATA`"),
                   Parameter('reg', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('IiImportDrillDatabaseESRI_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Same as iImportDrillDatabaseADO2_GUI, but from an ArcGIS Geodatabase",
               notes="""
               If it is not defined on input, the template name is set
               to be the Wholeplot table name; e.g.
               "HOLESURVEY.i4" for "Project_HOLESURVEY"
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('connect', type=Type.STRING,
                             doc='External database connection string  (e.g. "d:\\Personal\\test.mdb|Table" or "d:\\File\\test.gdb|TableX|FeatureClassY)"'),
                   Parameter('temp', type=Type.STRING, is_ref=True, size_of_param='temp_size',
                             doc="Template to make (if left blank, the created template name is returned)"),
                   Parameter('temp_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of the template name string"),
                   Parameter('table', type=Type.STRING, is_ref=True, size_of_param='table_size',
                             doc="Name of table"),
                   Parameter('table_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('type', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned :def:`DH_DATA`"),
                   Parameter('geochem', type=Type.BOOL,
                             doc="Geosoft Geochemistry Database?"),
                   Parameter('reg', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('IiImportDrillDatabaseODBC_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="""
               Generate a template file for importing drill holes
               from ODBC database data.
               """,
               notes="""
               If the input connection string is empty (""), then the ODBC connection dialogs
               will appear (e.g. to connect to a machine database) before the import wizard
               is run. The connect string used for this connection is then returned.
               This string can then be used on input to skip the ODBC connection dialogs and
               go straight to the Wholeplot import wizard.
               Because the name of the database is not necessarily known, the template name is created
               from the name of the table opened - e.g. "HOLELOCATION.i4".
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('connect', type=Type.STRING, is_ref=True, size_of_param='connect_size',
                             doc="Connection string"),
                   Parameter('connect_size', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of connection string returned"),
                   Parameter('temp', type=Type.STRING, is_ref=True, size_of_param='temp_size',
                             doc="Template to make"),
                   Parameter('temp_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of template string returned"),
                   Parameter('table', type=Type.STRING, is_ref=True, size_of_param='table_size',
                             doc="Name of table"),
                   Parameter('table_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('type', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned :def:`DH_DATA`"),
                   Parameter('reg', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('IiImportDrillDatabaseODBCMaxwell_GUI', module='None', version='8.3.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Same as :func:`IiImportDrillDatabaseODBC_GUI` but customized for Maxwell.",
               notes="Same as :func:`IiImportDrillDatabaseODBC_GUI` but customized for Maxwell.",
               return_type=Type.INT32_T,
               return_doc="0-OK 1-Cancel",
               parameters = [
                   Parameter('connect', type=Type.STRING, is_ref=True, size_of_param='connect_size',
                             doc="Connection string"),
                   Parameter('connect_size', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of connection string returned"),
                   Parameter('temp', type=Type.STRING, is_ref=True, size_of_param='temp_size',
                             doc="Template to make"),
                   Parameter('temp_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of template string returned"),
                   Parameter('table', type=Type.STRING, is_ref=True, size_of_param='table_size',
                             doc="Name of table"),
                   Parameter('table_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('type', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned :def:`DH_DATA`"),
                   Parameter('reg', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('iImportAsciiWizard_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Generate a template file from a gui.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Cancel
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Data file name"),
                   Parameter('temp', type=Type.STRING,
                             doc="Template to make")
               ]),

        Method('iImportChemDatabase_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Generate a template file for importing Geochems Database.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Data file name"),
                   Parameter('temp', type=Type.STRING,
                             doc="Template to make"),
                   Parameter('table', type=Type.STRING, is_ref=True, size_of_param='table_size',
                             doc="Name of table"),
                   Parameter('table_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`IMPCH_TYPE`")
               ]),

        Method('iImportChemDatabaseADO_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Improved template creation for importing geochem database (ADO).",
               notes="""
               This is an improved version of ImportChemDatabase_GUI using the
               new ADO technology, as opposed to DAO. Use in conjuction with
               :func:`ImportADO_DU`. See also ImportDatabaseADO_GUI.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('connect', type=Type.STRING,
                             doc="External database connection string (Blank for OLEDB Wizard)"),
                   Parameter('temp', type=Type.STRING,
                             doc="Template to make"),
                   Parameter('table', type=Type.STRING, is_ref=True, size_of_param='table_size',
                             doc="Name of table"),
                   Parameter('table_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`IMPCH_TYPE`")
               ]),

        Method('iImportDatabase_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Create template to import an external database table.",
               notes="""
               This is used to select a single database table, and
               selected fields from that table. If the database is not
               Microsoft Access (type .mdb), an introductory dialog
               requests the file type.
               This function DOES NOT import the table itself, but
               creates an import template which may be used to import
               the table (see :func:`ImportDAO_DU`).
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="External database file name"),
                   Parameter('temp', type=Type.STRING,
                             doc="Template to make"),
                   Parameter('table', type=Type.STRING, is_ref=True, size_of_param='table_size',
                             doc="Name of table imported (returned)"),
                   Parameter('table_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table string")
               ]),

        Method('iImportDatabaseADO_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Create template to import an external database table (ADO Version).",
               notes="""
               1. This is used to select a single database table, and
                  selected fields from that table.
               
               2. This function DOES NOT import the table itself, but
                  creates an import template which may be used to import
                  the table (see :func:`ImportADO_DU`).
               
               3. If connection string is of type "FILENAME=..." the connection will attempt to resolve
                  it as a file database. (see also ODBCFileConnect_GUI)
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('connect', type=Type.STRING,
                             doc="External database connection string (Blank for OLEDB Wizard)"),
                   Parameter('temp', type=Type.STRING,
                             doc="Template to make"),
                   Parameter('table', type=Type.STRING, is_ref=True, size_of_param='table_size',
                             doc="Name of table imported (returned)"),
                   Parameter('table_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table string")
               ]),

        Method('iImportDatabaseSQL_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="""
               Create template to import an external database table,
               created using SQL.
               """,
               notes="""
               1. This is used to build an Oasis montaj group (line) from
                  one or more database tables and fields, by selecting from
                  one or more SQL selection queries. The list of queries
                  is read from a text file with the following syntax:
               
                  Query_Name_1
                  Query...
                  Query... (continued)
                  ...
                  ...
                  END_QUERY
                  Query_Name_2
                  etc.
               
               2. Each query has a title line, the query itself, then the
                  "END_QUERY" line to finish.  The title of a subsequent query
                  is on the line after an "END_QUERY" line.
               
               3. If the text file parameter is left blank (""), then
                  selection queries in the database itself are listed.
                  In addition to the pre-defined queries, there is a
                  "User Defined" query which may be filled in by the user.
               
               4. This function DOES NOT import the table itself, but
                  creates an import template which may be used to import
                  the data (see :func:`ImportDAO_DU`).
               
               5. If connection string is of type "FILENAME=..." the connection will attempt to resolve
                  it as a file database. (see also ODBCFileConnect_GUI)
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="External database file name"),
                   Parameter('sql', type=Type.STRING,
                             doc='Text file with SQL queries to use, ("" - get from database)'),
                   Parameter('temp', type=Type.STRING,
                             doc="Import template to make"),
                   Parameter('line', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Name of table imported (returned)"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table string")
               ]),

        Method('iImportDatabaseSQLADO_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="""
               Create template to import an external database table,
               created using SQL (New ADO Version).
               """,
               notes="""
               This is used to build an Oasis montaj group (line) from
               one or more database tables and fields, by selecting from
               one or more SQL selection queries. The list of queries
               is read from a text file with the following syntax:
               
               Query_Name_1
               Query...
               Query... (continued)
               ...
               ...
               END_QUERY
               Query_Name_2
               etc.
               
               Each query has a title line, the query itself, then the
               "END_QUERY" line to finish.  The title of a subsequent query
               is on the line after an "END_QUERY" line.
               
               If the text file parameter is left blank (""), then
               selection queries in the database itself are listed.
               In addition to the pre-defined queries, there is a
               "User Defined" query which may be filled in by the user.
               
               This function DOES NOT import the table itself, but
               creates an import template which may be used to import
               the data (see :func:`ImportDAO_DU`).
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 Cancel
               """,
               parameters = [
                   Parameter('connect', type=Type.STRING,
                             doc="External database connection string (Blank for OLEDB Wizard)"),
                   Parameter('sql', type=Type.STRING,
                             doc='Text file with SQL queries to use, ("" - get from database)'),
                   Parameter('temp', type=Type.STRING,
                             doc="Import template to make"),
                   Parameter('line', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Name of table imported (returned)"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table string")
               ]),

        Method('iImportDrillDatabaseADO_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Generate a template file for importing drill holes.",
               notes="""
               This is an improved version of ImportDrillDatabase_GUI using the
               new ADO technology, as opposed to DAO. Use in conjunction with
               :func:`ImportADO_DU`. See also ImportDatabaseADO_GUI.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('connect', type=Type.STRING,
                             doc="External database connection string (Blank for OLEDB Wizard)"),
                   Parameter('temp', type=Type.STRING,
                             doc="Template to make"),
                   Parameter('table', type=Type.STRING, is_ref=True, size_of_param='table_size',
                             doc="Name of table"),
                   Parameter('table_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('type', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned :def:`DH_DATA`"),
                   Parameter('reg', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('iImportTemplateSQL_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Create template to import an external database table; provide query.",
               notes="""
               This is similar to :func:`iImportDatabaseSQL_GUI`, but dispenses with
               the dialog offering a selection of queries. Instead, the
               user supplies the query as a string.
               
               This function DOES NOT import the table itself, but
               creates an import template which may be used to import
               the data (see :func:`ImportDAO_DU`).
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 Cancel
               terminates on error
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="External database file name"),
                   Parameter('temp', type=Type.STRING,
                             doc="Import template to make"),
                   Parameter('sql', type=Type.STRING,
                             doc="SQL selection query to run on database"),
                   Parameter('line', type=Type.STRING,
                             doc="Name of Oasis table to create")
               ]),

        Method('iImportTemplateSQLADO_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Create template to import an external database table; provide query.",
               notes="""
               This is similar to :func:`iImportDatabaseSQL_GUI`, but dispenses with
               the dialog offering a selection of queries. Instead, the
               user supplies the query as a string.
               
               This function DOES NOT import the table itself, but
               creates an import template which may be used to import
               the data (see :func:`ImportADO_DU`).
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               terminates on error
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="External database connection string (Blank for OLEDB Wizard)"),
                   Parameter('temp', type=Type.STRING,
                             doc="Import template to make"),
                   Parameter('sql', type=Type.STRING,
                             doc="SQL selection query to run on database"),
                   Parameter('line', type=Type.STRING,
                             doc="Name of Oasis table to create")
               ]),

        Method('iImportXYZTemplateEditor_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="""
               Allows the user to edit XYZ import templates
               using a complex dialog. The Template name
               may change during editing.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('template', type=Type.STRING,
                             doc="Name of the Template (can change)"),
                   Parameter('size', type=Type.INT32_T,
                             doc="Size of the Template"),
                   Parameter('file', type=Type.STRING,
                             doc="Name of the XYZ file to base it on")
               ]),

        Method('IiODBCFileConnect_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Get the connection string for a file database as well as optional table name and FileUsage attribute",
               notes="""
               If the file extension is "mdb" or "xls" then a Microsoft Access
               or Excel database is assumed. Otherwise, a dialog appears listing
               the installed ODBC file database drivers. If the driver takes a
               directory as a database (FileUsage==1) the table name is also
               returned. This is needed because the table name may or may not include
               the file extension.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               terminates on error
               """,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="File Name"),
                   Parameter('connect', type=Type.STRING, is_ref=True, size_of_param='c_size',
                             doc="Connection string (returned)"),
                   Parameter('c_size', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of connection string"),
                   Parameter('usage', type=Type.INT32_T,
                             doc="File Usage (0 - ODBC drivers not queried, 1 - Directory containing tables, 2 - File containing tables)"),
                   Parameter('table', type=Type.STRING, is_ref=True, size_of_param='t_size',
                             doc="Table name of file (returned if plUsage==1)"),
                   Parameter('t_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name")
               ]),

        Method('IiSymbolForm_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="- Select a symbol.",
               notes="Symbols are set on input, and new values returned.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('symb_font', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Symbol font file name"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size for symbol font face name"),
                   Parameter('geo_font', type=Type.BOOL, is_ref=True,
                             doc="Geosoft font?"),
                   Parameter('weight', type=Type.INT32_T, is_ref=True,
                             doc="Weight :def:`MVIEW_FONT_WEIGHT`"),
                   Parameter('symb_num', type=Type.INT32_T, is_ref=True,
                             doc="Symbol number"),
                   Parameter('symb_size', type=Type.DOUBLE, is_ref=True,
                             doc="Symbol size"),
                   Parameter('symb_ang', type=Type.DOUBLE, is_ref=True,
                             doc="Symbol angle"),
                   Parameter('edge_col', type=Type.INT32_T, is_ref=True,
                             doc="Edge color"),
                   Parameter('fill_col', type=Type.INT32_T, is_ref=True,
                             doc="Fill color")
               ]),

        Method('iMetaDataTool_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Edit a :class:`META` object",
               return_type=Type.INT32_T,
               return_doc="""
               0         - OK
               non-zero  - Cancel
               """,
               parameters = [
                   Parameter('meta', type="META",
                             doc="Meta object"),
                   Parameter('root_token', type="META_TOKEN",
                             doc="Root Token, :def_val:`H_META_INVALID_TOKEN` for root"),
                   Parameter('schema', type=Type.INT32_T,
                             doc="Display schema information ?")
               ]),

        Method('ImportChemWizard_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Generate a template file for importing geochems.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Data file name"),
                   Parameter('temp', type=Type.STRING,
                             doc="Template to make"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`IMPCH_TYPE`")
               ]),

        Method('ImportDrillWizard_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Generate a template file for importing drill holes.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Data file name"),
                   Parameter('temp', type=Type.STRING,
                             doc="Template to make"),
                   Parameter('table', type=Type.STRING, is_ref=True, size_of_param='table_size',
                             doc="Name of table"),
                   Parameter('table_size', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of table name string"),
                   Parameter('type', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned :def:`DH_DATA`"),
                   Parameter('reg', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('InternetTrust_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Change the Internet Trust Relationships",
               return_type=Type.VOID),

        Method('iPatternForm_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="- Select a pattern.",
               notes="""
               Pattern values set on input, and new values returned.
               Solid fill is indicated by Pattern number 0.
               
               Returned Values (not set on input)
               
               Size
                    pattern tile size in mm.

               Thick
                    pattern line thickness in percent of the tile size.
                    valid range is 0-100.

               Density
                    Tile spacing. A value of 1 means tiles are laid with no overlap.
                    A value of 2 means they overlap each other.
               
               The pattern Angle and Style parameters are not user-definable.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('pat', type=Type.INT32_T, is_ref=True,
                             doc="Current Pattern"),
                   Parameter('size', type=Type.DOUBLE, is_ref=True,
                             doc="Current Size,           // returned"),
                   Parameter('thick', type=Type.INT32_T, is_ref=True,
                             doc="Current Thick (0-100)   // returned"),
                   Parameter('dense', type=Type.DOUBLE, is_ref=True,
                             doc="Current Density,        // returned"),
                   Parameter('col', type=Type.INT32_T, is_ref=True,
                             doc="Current Pattern Color   // passed in and returned"),
                   Parameter('back_col', type=Type.INT32_T, is_ref=True,
                             doc="Current Background Color  // passed in and returned; can be :def_val:`C_TRANSPARENT`")
               ]),

        Method('iLinePatternForm_GUI', module='None', version='8.1.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Select a line pattern.",
               notes="Same as :func:`iPatternForm_GUI` but for line patterns.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('pattern', type=Type.INT32_T, is_ref=True,
                             doc="Current Pattern"),
                   Parameter('thickness', type=Type.DOUBLE, is_ref=True,
                             doc="Current Thickness"),
                   Parameter('pitch', type=Type.DOUBLE, is_ref=True,
                             doc="Current Pitch"),
                   Parameter('colour', type=Type.INT32_T, is_ref=True,
                             doc="Current Pattern Color")
               ]),

        Method('iTwoPanelSelection_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="General purpose two-panel selection.",
               notes="""
               Takes as input two LSTs, one contains all available items,
               the second currently selected items. These are processed,
               and in the left panel are displayed all items in the first
               :class:`LST` not in the selection :class:`LST`, and on the right all items
               in the first :class:`LST` which are in the selection :class:`LST`. (Items in
               the selection :class:`LST` NOT in the first :class:`LST` are ignored).
               Once the user has finalized the selections, the final selections
               are returned in the selection :class:`LST`.
               
               Selections and display are based on the :def_val:`LST_ITEM_NAME` part of the
               :class:`LST` item, but on export both the :def_val:`LST_ITEM_NAME` and :def_val:`LST_ITEM_VALUE`
               elements of the selected items from the first :class:`LST` are transferred
               to the second list for output.
               
               The sConvertToCSV_LST and sConvertFromCSV_LST functions in lst.h
               can be used to convert the selection LSTs to forms that can be
               stored and retrieved from GX parameters (or :class:`REG` or INI, etc.).
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('ls_tf', type="LST",
                             doc="All available items for selection."),
                   Parameter('ls_ts', type="LST",
                             doc="Selections (altered on output)"),
                   Parameter('title', type=Type.STRING,
                             doc="Title for dialog")
               ]),

        Method('iTwoPanelSelection2_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Two-panel selection, items not sorted alphabetically.",
               notes="""
               Same as :func:`iTwoPanelSelection_GUI`, but the items in the
               two lists are not sorted alphabetically, but are ordered
               exactly as input, and when an item is selected it is
               added at the end of the lists.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('ls_tf', type="LST",
                             doc="All available items for selection."),
                   Parameter('ls_ts', type="LST",
                             doc="Selections (altered on output)"),
                   Parameter('title', type=Type.STRING,
                             doc="Title for dialog")
               ]),

        Method('iTwoPanelSelectionEx_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Two-panel selection; options for sort and ability to select no items.",
               notes="""
               Same as :func:`iTwoPanelSelection_GUI`, but the items in the
               two lists are not sorted alphabetically, but are ordered
               exactly as input, and when an item is selected it is
               added at the end of the lists.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('ls_tf', type="LST",
                             doc="All available items for selection."),
                   Parameter('ls_ts', type="LST",
                             doc="Selections (altered on output)"),
                   Parameter('sorted', type=Type.INT32_T,
                             doc="Sort items alphabetically (0:No, 1:Yes)"),
                   Parameter('allow_no_select', type=Type.INT32_T,
                             doc="Allow no items selected (0:No, 1:Yes)"),
                   Parameter('title', type=Type.STRING,
                             doc="Title for dialog")
               ]),

        Method('iTwoPanelSelectionEx2_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Two-panel selection; extended options including a help link.",
               notes="""
               Same as :func:`iTwoPanelSelectionEx_GUI`, but user can specify a help
               link.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('ls_tf', type="LST",
                             doc="All available items for selection."),
                   Parameter('ls_ts', type="LST",
                             doc="Selections (altered on output)"),
                   Parameter('sorted', type=Type.INT32_T,
                             doc="Sort items alphabetically (0:No, 1:Yes)"),
                   Parameter('allow_no_select', type=Type.INT32_T,
                             doc="Allow no items selected (0:No, 1:Yes)"),
                   Parameter('title', type=Type.STRING,
                             doc="Title for dialog"),
                   Parameter('help', type=Type.STRING,
                             doc="Help link")
               ]),

        Method('LaunchSingleGeoDOTNETXTool_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch a user created .Net GEOXTOOL ensuring a single instance.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dll', type=Type.STRING,
                             doc="Assembly name"),
                   Parameter('func', type=Type.STRING,
                             doc="Control Class Name"),
                   Parameter('meta', type="META",
                             doc=":class:`META` Handle (holding tool configuration data)")
               ]),

        Method('LaunchGeoDOTNETXTool_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch a user created .Net GEOXTOOL.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dll', type=Type.STRING,
                             doc="Assembly name"),
                   Parameter('func', type=Type.STRING,
                             doc="Control Class Name"),
                   Parameter('meta', type="META",
                             doc=":class:`META` Handle (holding tool configuration data)")
               ]),

        Method('LaunchGeoXTool_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch a user created GEOXTOOL.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dll', type=Type.STRING,
                             doc="DLL name"),
                   Parameter('func', type=Type.STRING,
                             doc="Function Name"),
                   Parameter('meta', type="META",
                             doc=":class:`META` Handle (holding tool configuration data)")
               ]),

        Method('LaunchSingleGeoDOTNETXToolEx_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch a user created .Net GEOXTOOL ensuring a single instance.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dll', type=Type.STRING,
                             doc="Assembly name"),
                   Parameter('func', type=Type.STRING,
                             doc="Control Class Name"),
                   Parameter('meta', type="META",
                             doc=":class:`META` Handle (holding tool configuration data)"),
                   Parameter('align', type=Type.INT32_T,
                             doc=":def:`XTOOL_ALIGN` (can specify one or more or :def_val:`XTOOL_ALIGN_ANY`)"),
                   Parameter('dock', type=Type.INT32_T,
                             doc=":def:`XTOOL_DOCK`"),
                   Parameter('width', type=Type.INT32_T,
                             doc="Default width"),
                   Parameter('height', type=Type.INT32_T,
                             doc="Default height")
               ]),

        Method('LaunchGeoDOTNETXToolEx_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch a user created .Net GEOXTOOL.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dll', type=Type.STRING,
                             doc="Assembly name"),
                   Parameter('func', type=Type.STRING,
                             doc="Control Class Name"),
                   Parameter('meta', type="META",
                             doc=":class:`META` Handle (holding tool configuration data)"),
                   Parameter('align', type=Type.INT32_T,
                             doc=":def:`XTOOL_ALIGN` (can specify one or more or :def_val:`XTOOL_ALIGN_ANY`)"),
                   Parameter('dock', type=Type.INT32_T,
                             doc=":def:`XTOOL_DOCK`"),
                   Parameter('width', type=Type.INT32_T,
                             doc="Default width"),
                   Parameter('height', type=Type.INT32_T,
                             doc="Default height")
               ]),

        Method('LaunchGeoXToolEx_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch a user created GEOXTOOL.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dll', type=Type.STRING,
                             doc="DLL name"),
                   Parameter('func', type=Type.STRING,
                             doc="Function Name"),
                   Parameter('meta', type="META",
                             doc=":class:`META` Handle (holding tool configuration data)"),
                   Parameter('align', type=Type.INT32_T,
                             doc=":def:`XTOOL_ALIGN` (can specify one or more or :def_val:`XTOOL_ALIGN_ANY`)"),
                   Parameter('dock', type=Type.INT32_T,
                             doc=":def:`XTOOL_DOCK`"),
                   Parameter('width', type=Type.INT32_T,
                             doc="Default width"),
                   Parameter('height', type=Type.INT32_T,
                             doc="Default height")
               ]),

        Method('MetaDataViewer_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="View a :class:`META` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('meta', type="META",
                             doc="Meta object"),
                   Parameter('root_token', type="META_TOKEN",
                             doc="Root token, :def_val:`H_META_INVALID_TOKEN` for root"),
                   Parameter('schema', type=Type.INT32_T,
                             doc="Display schema information ?")
               ]),

        Method('PrintFile_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Prints a file to current printer",
               return_type=Type.VOID,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="Filename string")
               ]),

        Method('RenderPattern_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="- Render a pattern.",
               notes="Renders a Geosoft pattern to a Windows DC.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('hdc', type="HDC", is_val=True,
                             doc="DC handle"),
                   Parameter('left', type=Type.INT32_T,
                             doc="Left value of the render rect in Windows coordinates (bottom>top)"),
                   Parameter('bottom', type=Type.INT32_T,
                             doc="Bottom value"),
                   Parameter('right', type=Type.INT32_T,
                             doc="Right value"),
                   Parameter('top', type=Type.INT32_T,
                             doc="Top value"),
                   Parameter('pat', type=Type.INT32_T,
                             doc="Pattern number"),
                   Parameter('size', type=Type.DOUBLE,
                             doc="Pattern size,           // input :def_val:`GS_R8DM` to use default"),
                   Parameter('thick', type=Type.INT32_T,
                             doc="Pattern thick (0-100)   // input :def_val:`GS_S4DM` to use default"),
                   Parameter('dense', type=Type.DOUBLE,
                             doc="Pattern density,        // input :def_val:`GS_R8DM` to use default"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Pattern color	  // input :def_val:`GS_S4DM` to use default"),
                   Parameter('back_col', type=Type.INT32_T,
                             doc="Pattern background color // input :def_val:`GS_S4DM` to use default; can be :def_val:`C_TRANSPARENT`"),
                   Parameter('is_enabled', type=Type.INT32_T,
                             doc="Is this window enabled?"),
                   Parameter('is_button', type=Type.INT32_T,
                             doc="Is this a button?"),
                   Parameter('is_selected', type=Type.INT32_T,
                             doc="Is this window selected?")
               ]),

        Method('RenderLinePattern_GUI', module='None', version='8.1.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="Render a line pattern.",
               notes="Same as :func:`RenderPattern_GUI` but for line patterns.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('hdc', type="HDC", is_val=True,
                             doc="DC Handle"),
                   Parameter('left', type=Type.INT32_T,
                             doc="Left value of the render rect in Windows coordinates (bottom>top)"),
                   Parameter('bottom', type=Type.INT32_T,
                             doc="Bottom value"),
                   Parameter('right', type=Type.INT32_T,
                             doc="Right value"),
                   Parameter('top', type=Type.INT32_T,
                             doc="Top value"),
                   Parameter('pattern', type=Type.INT32_T,
                             doc="Pattern number"),
                   Parameter('thickness', type=Type.DOUBLE,
                             doc="Pattern thickness"),
                   Parameter('pitch', type=Type.DOUBLE,
                             doc="Pattern pitch"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Pattern color"),
                   Parameter('is_enabled', type=Type.INT32_T,
                             doc="Is this window enabled?"),
                   Parameter('is_button', type=Type.INT32_T,
                             doc="Is this a button?"),
                   Parameter('is_selected', type=Type.INT32_T,
                             doc="Is this window selected?")
               ]),

        Method('SetParentWND_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="Set the current parent WND",
               notes="""
               The parent WND is used by all modal dialogs as a
               parent to ensure the dialog is correctly modal.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('wnd', type="WND",
                             doc="New Parent Window")
               ]),

        Method('SetPrinter_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Sets the Printer.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('printer', type=Type.STRING,
                             doc="Printer Name")
               ]),

        Method('SetProgAlwaysOn_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               Ability to set the progress bar to stay visible even
               if main application is processing messages
               """,
               notes="""
               In montaj the progress bar is hidden when the main window
               start processing messages. This is not always desirable
               in some 3rd party apps, hence this function.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('on', type=Type.BOOL,
                             doc="Should progress bar remain visible")
               ]),

        Method('SetWindowArea_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, 
               doc="Set the location of the Oasis montaj window.",
               notes="""
               The Coordinates are pixels with 0,0 being the top
               left corner of the Screen.
               
               If the window is minimized, the max values will be
               equal to the min values. If the window is maximized
               X Min and Y min will be :def_val:`GS_S4MN` and X max and Y max
               will be :def_val:`GS_S4MX`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('min_x', type=Type.INT32_T,
                             doc="X Min"),
                   Parameter('min_y', type=Type.INT32_T,
                             doc="Y Min"),
                   Parameter('max_x', type=Type.INT32_T,
                             doc="X Max"),
                   Parameter('max_y', type=Type.INT32_T,
                             doc="Y Max")
               ]),

        Method('ShowDirectHist_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Display histogram of data directly",
               return_type=Type.VOID,
               parameters = [
                   Parameter('min', type=Type.DOUBLE,
                             doc="Min    Value to display"),
                   Parameter('max', type=Type.DOUBLE,
                             doc="Max    Value to display"),
                   Parameter('mean', type=Type.DOUBLE,
                             doc="Mean   Value to display"),
                   Parameter('std_dev', type=Type.DOUBLE,
                             doc="StdDev Value to display"),
                   Parameter('median', type=Type.DOUBLE,
                             doc="Median Value to display"),
                   Parameter('items', type=Type.INT32_T,
                             doc="Items  Number of items this comprises"),
                   Parameter('vv', type="VV",
                             doc=":class:`VV` holding hist counts")
               ]),

        Method('ShowHist_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Display Histogram of data from :class:`ST`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('st', type="ST",
                             doc="Statistics obj")
               ]),

        Method('SimpleMapDialog_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="General purpose map display :class:`GUI` with no interaction.",
               notes="""
               This function displays a map in a simple resizable dialog that fits the map into it.
               It is generally useful to display temporary maps as graphs (e.g. variograms).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('map', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('title', type=Type.STRING,
                             doc="Title"),
                   Parameter('help_id', type=Type.STRING,
                             doc="HelpID")
               ]),

        Method('ThematicVoxelInfo_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Display GX.Net thematic voxel info :class:`GUI`.",
               notes="""
               Displays the thematic voxel codes, colors, total volume for
               each code, and number of valid items (cubes) for each code.
               This is a replacement for the numeric stats done on normal
               numerical voxel grids.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object")
               ]),

        Method('Show3DViewerDialog_GUI', module='None', version='9.3.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Display a standalone 3D viewer",
               notes="Any changes made to the 3D View will be persisted.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('title', type=Type.STRING,
                             doc="Title"),
                   Parameter('o3dv', type=Type.STRING,
                             doc="3D View name (.geosoft_3dv)")
               ])
    ],
    'Obsolete': [

        Method('DefineDrillITR_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, 
               doc="Define color zones for gridded data.",
               notes="""
               The :class:`ITR` for Wholeplot gridded data is now defined inside the tabbed
               dialog for the Plan or Section maps. Calls to this function now bring
               up an error message.
               
               Obsolete
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('dh', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to grid"),
                   Parameter('file', type=Type.STRING,
                             doc="Name of :class:`ITR` file")
               ]),

        Method('ExportXYZTemplateEditor_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, is_gui=True, 
               doc="""
               Allows the user to edit XYZ export template
               using a complex dialog. The Template name
               may change during editing.
               """,
               notes="Obsolete, use :func:`iExportXYZTemplateEditor_GUI`",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('template', type=Type.STRING,
                             doc="Name of the Template (can change)"),
                   Parameter('size', type=Type.INT32_T,
                             doc="Size of the Template")
               ]),

        Method('ExportXYZTemplateEditorEx_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, is_gui=True, 
               doc="""
               Allows the user to edit XYZ export template
               using a complex dialog. The Template name
               may change during editing.
               """,
               notes="Obsolete, use :func:`iExportXYZTemplateEditorEx_GUI`",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` object"),
                   Parameter('template', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Template name"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of name")
               ]),

        Method('GetDapData_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, is_gui=True, 
               doc="Allow the user find DAP data.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ipj', type="IPJ",
                             doc="Projection of area of interest"),
                   Parameter('ply', type="PLY",
                             doc="If exact clipping is needed, supply the :class:`PLY`. If the server is able, it will do exact clipping on this region. Can be NULL (0)."),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Min X"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Min Y"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Max Y"),
                   Parameter('client', type=Type.INT32_T,
                             doc="DAP_CLIENT")
               ]),

        Method('IiBrowseDirEdit_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, is_gui=True, 
               doc="Browses for a specific directory, user editable.",
               notes="""
               Allows the user to edit the directory name in an edit window,
               as well as browse for an existing directory, so it is possible
               to specify a new directory name. It remains up to the caller to
               test to see if the directory exists, and if not, to create it.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('title', type=Type.STRING,
                             doc="Title of the Form"),
                   Parameter('default', type=Type.STRING,
                             doc='Default path (Can be "")'),
                   Parameter('dir_path', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Result Path Buffer (default on input)"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Path Buffer Size")
               ]),

        Method('iImportDrillDatabase_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, 
               doc="Generate a template file for importing drill holes.",
               notes="Obsolete, use ImportDrillDatabaseADO_GUI",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Data file name"),
                   Parameter('temp', type=Type.STRING,
                             doc="Template to make"),
                   Parameter('table', type=Type.STRING, is_ref=True, size_of_param='table_size',
                             doc="Name of table"),
                   Parameter('table_size', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of table name string"),
                   Parameter('type', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned (See DH_DATA_? in dh.gxh)"),
                   Parameter('reg', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('ImportAsciiWizard_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, is_gui=True, 
               doc="Generate a template file from a gui.",
               notes="Obsolete, use :func:`ImportAsciiWizard_GUI`",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Cancel
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Data file name"),
                   Parameter('temp', type=Type.STRING,
                             doc="Template to make")
               ]),

        Method('ImportXYZTemplateEditor_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, is_gui=True, 
               doc="""
               Allows the user to edit XYZ import templates
               using a complex dialog. The Template name
               may change during editing.
               """,
               notes="Obsolete, use :func:`iImportXYZTemplateEditor_GUI`",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('template', type=Type.STRING,
                             doc="Name of the Template (can change)"),
                   Parameter('size', type=Type.INT32_T,
                             doc="Size of the Template"),
                   Parameter('file', type=Type.STRING,
                             doc="Name of the XYZ file to base it on")
               ]),

        Method('IODBCFileConnect_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, 
               doc="""
               Get the connection string for a file database as well as
               optional table name and FileUsage attribute
               """,
               notes="Obsolete, use :func:`IODBCFileConnect_GUI`",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="File Name"),
                   Parameter('connect', type=Type.STRING, is_ref=True, size_of_param='c_size',
                             doc="Connection string (returned)"),
                   Parameter('c_size', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of connection string"),
                   Parameter('usage', type=Type.INT32_T,
                             doc="File Usage (0 - ODBC drivers not queried, 1 - Directory containing tables, 2 - File containing tables)"),
                   Parameter('table', type=Type.STRING, is_ref=True, size_of_param='t_size',
                             doc="Table name of file (returned if plUsage==1)"),
                   Parameter('t_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name")
               ]),

        Method('QueryIPJ_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, is_gui=True, 
               doc="Display the :class:`IPJ` wizard.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ipj', type="IPJ",
                             doc="Current :class:`IPJ`")
               ]),

        Method('IIPQC_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, 
               doc="""
               Quality Control on an :class:`IP` database. Replaced by the modal
               dialog and lLaunchIPQCTool_IPGUI.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` obj"),
                   Parameter('p3', type=Type.STRING,
                             doc="Current line"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="Selected channel (returned)"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Size of channel buffer")
               ])
    ]
}

