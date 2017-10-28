from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MVIEW',
                 doc="""
                 A view (:class:`MVIEW` class) has a 2-D/3-D translation matrix, a map
                 projection and a clip region.  A view contains any number of
                 "groups", and each "group" contains one or more graphics
                 elements (entities).  Different types of groups will contain
                 different types of entities:
                 """,
                 notes="""
                 :class:`CSYMB` groups (color symbols) contain data and rules for
                 presenting the data as color symbols.  See :func:`ColSymbol_MVIEW`
                 and the :class:`CSYMB` class.
                 
                 :class:`AGG` groups (aggregates) contain images.  See :func:`Aggregate_MVIEW`
                 and the :class:`AGG` class.
                 
                 Standard groups contain symbols, lines, polylines, and polygons.
                 See :func:`StartGroup_MVIEW`.
                 """)


gx_defines = [
    Define('MAKER',
           doc="Maker defines",
           constants=[
               Constant('MAKER_GX', value='0', type=Type.INT32_T,
                        doc="GX")
           ]),

    Define('MVIEW_CLIP',
           doc="Boolean clipping defines",
           constants=[
               Constant('CLIP_ON', value='1', type=Type.INT32_T,
                        doc="Turn ON clipping"),
               Constant('CLIP_OFF', value='0', type=Type.INT32_T,
                        doc="Turn OFF clipping")
           ]),

    Define('MVIEW_COLOR',
           doc="""
           24-bit color defines
           The :func:`iColor_MVIEW` function can be used to create a color int from a
           color string description.
           The iColorXXX_MVIEW macros can be used to create colors from component
           intensities.
           """,
           constants=[
               Constant('C_BLACK', value='33554432', type=Type.INT32_T,
                        doc="Black"),
               Constant('C_RED', value='33554687', type=Type.INT32_T,
                        doc="Red"),
               Constant('C_GREEN', value='33619712', type=Type.INT32_T,
                        doc="Green"),
               Constant('C_BLUE', value='50266112', type=Type.INT32_T,
                        doc="Blue"),
               Constant('C_CYAN', value='50331903', type=Type.INT32_T,
                        doc="Cyan"),
               Constant('C_MAGENTA', value='50396928', type=Type.INT32_T,
                        doc="Magenta"),
               Constant('C_YELLOW', value='67043328', type=Type.INT32_T,
                        doc="Yellow"),
               Constant('C_GREY', value='41975936', type=Type.INT32_T,
                        doc="Grey"),
               Constant('C_LT_RED', value='54542336', type=Type.INT32_T,
                        doc="Light Red"),
               Constant('C_LT_GREEN', value='54526016', type=Type.INT32_T,
                        doc="Light Green"),
               Constant('C_LT_BLUE', value='50348096', type=Type.INT32_T,
                        doc="Light Blue"),
               Constant('C_LT_CYAN', value='50331712', type=Type.INT32_T,
                        doc="Light Cyan"),
               Constant('C_LT_MAGENTA', value='50348032', type=Type.INT32_T,
                        doc="Light Magenta"),
               Constant('C_LT_YELLOW', value='54525952', type=Type.INT32_T,
                        doc="Light Yellow"),
               Constant('C_LT_GREY', value='54542400', type=Type.INT32_T,
                        doc="Light Grey"),
               Constant('C_GREY10', value='51910680', type=Type.INT32_T,
                        doc="Grey 10%"),
               Constant('C_GREY25', value='54542400', type=Type.INT32_T,
                        doc="Grey 25%"),
               Constant('C_GREY50', value='41975936', type=Type.INT32_T,
                        doc="Grey 50%"),
               Constant('C_WHITE', value='50331648', type=Type.INT32_T,
                        doc="White"),
               Constant('C_TRANSPARENT', value='0', type=Type.INT32_T,
                        doc="Transparent or no-draw")
           ]),

    Define('MVIEW_CYLINDER3D',
           doc="What parts of the cylinder are closed",
           constants=[
               Constant('MVIEW_CYLINDER3D_OPEN', value='0', type=Type.INT32_T),
               Constant('MVIEW_CYLINDER3D_CLOSESTART', value='1', type=Type.INT32_T),
               Constant('MVIEW_CYLINDER3D_CLOSEEND', value='2', type=Type.INT32_T),
               Constant('MVIEW_CYLINDER3D_CLOSEALL', value='3', type=Type.INT32_T)
           ]),

    Define('MVIEW_DRAW',
           doc="Polygon drawing defines",
           constants=[
               Constant('MVIEW_DRAW_POLYLINE', value='0', type=Type.INT32_T,
                        doc="Draw Polylines"),
               Constant('MVIEW_DRAW_POLYGON', value='1', type=Type.INT32_T,
                        doc="Draw Polygons")
           ]),

    Define('MVIEW_DRAWOBJ3D_ENTITY',
           doc="What types of entities to draw",
           constants=[
               Constant('MVIEW_DRAWOBJ3D_ENTITY_POINTS', value='0', type=Type.INT32_T,
                        doc="Draw 3D Points (no normals) [1 verticies per object]"),
               Constant('MVIEW_DRAWOBJ3D_ENTITY_LINES', value='1', type=Type.INT32_T,
                        doc="Draw 3D Lines (no normals) [2 verticies per object]"),
               Constant('MVIEW_DRAWOBJ3D_ENTITY_LINE_STRIPS', value='2', type=Type.INT32_T,
                        doc="Draw 3D Line strip (no normals) [2+x verticies per object]"),
               Constant('MVIEW_DRAWOBJ3D_ENTITY_LINE_LOOPS', value='3', type=Type.INT32_T,
                        doc="Draw 3D Line loop (no normals, closes loop with first point) [2+x verticies per object]"),
               Constant('MVIEW_DRAWOBJ3D_ENTITY_TRIANGLES', value='4', type=Type.INT32_T,
                        doc="Draw 3D Triangles [3 verticies per object]"),
               Constant('MVIEW_DRAWOBJ3D_ENTITY_TRIANGLE_STRIPS', value='5', type=Type.INT32_T,
                        doc="Draw 3D Triangle strips [3+x verticies per object]"),
               Constant('MVIEW_DRAWOBJ3D_ENTITY_TRIANGLE_FANS', value='6', type=Type.INT32_T,
                        doc="Draw 3D Triangle fans [3+x verticies per object]"),
               Constant('MVIEW_DRAWOBJ3D_ENTITY_QUADS', value='7', type=Type.INT32_T,
                        doc="Draw 3D Quads (Must be in the same plane) [4 verticies per object]"),
               Constant('MVIEW_DRAWOBJ3D_ENTITY_QUADS_STRIPS', value='8', type=Type.INT32_T,
                        doc="Draw 3D Quad Strips (Must be in the same plane) [4+2x verticies per object]"),
               Constant('MVIEW_DRAWOBJ3D_ENTITY_POLYGONS', value='9', type=Type.INT32_T,
                        doc="Draw 3D Quad Polygones (Must be in the same plane, must be convex and cannot intersect itself)")
           ]),

    Define('MVIEW_DRAWOBJ3D_MODE',
           doc="What types of entities to draw",
           constants=[
               Constant('MVIEW_DRAWOBJ3D_MODE_FLAT', value='0', type=Type.INT32_T,
                        doc="Draw flat shaded faces (one normal and color per object)"),
               Constant('MVIEW_DRAWOBJ3D_MODE_SMOOTH', value='1', type=Type.INT32_T,
                        doc="Draw smooth shaded faces (one normal and color per vertex)")
           ]),

    Define('MVIEW_EXTENT',
           doc="Types of extents defines",
           constants=[
               Constant('MVIEW_EXTENT_ALL', value='0', type=Type.INT32_T,
                        doc="All objects"),
               Constant('MVIEW_EXTENT_CLIP', value='1', type=Type.INT32_T,
                        doc="Clipping regions"),
               Constant('MVIEW_EXTENT_MAP', value='2', type=Type.INT32_T,
                        doc="Map extents"),
               Constant('MVIEW_EXTENT_VISIBLE', value='3', type=Type.INT32_T,
                        doc="Visible objects")
           ]),

    Define('MVIEW_FIT',
           doc="Fit area defines",
           constants=[
               Constant('MVIEW_FIT_MAP', value='0', type=Type.INT32_T,
                        doc="Fit it to the map area"),
               Constant('MVIEW_FIT_VIEW', value='1', type=Type.INT32_T,
                        doc="Fit it to the view area")
           ]),

    Define('MVIEW_FONT_WEIGHT',
           doc="Font weight defines",
           constants=[
               Constant('MVIEW_FONT_WEIGHT_NORMAL', value='0', type=Type.INT32_T),
               Constant('MVIEW_FONT_WEIGHT_ULTRALIGHT', value='1', type=Type.INT32_T),
               Constant('MVIEW_FONT_WEIGHT_LIGHT', value='2', type=Type.INT32_T),
               Constant('MVIEW_FONT_WEIGHT_MEDIUM', value='3', type=Type.INT32_T),
               Constant('MVIEW_FONT_WEIGHT_BOLD', value='4', type=Type.INT32_T),
               Constant('MVIEW_FONT_WEIGHT_XBOLD', value='5', type=Type.INT32_T),
               Constant('MVIEW_FONT_WEIGHT_XXBOLD', value='6', type=Type.INT32_T)
           ]),

    Define('MVIEW_GRID',
           doc="Grid Drawing defines",
           constants=[
               Constant('MVIEW_GRID_DOT', value='0', type=Type.INT32_T),
               Constant('MVIEW_GRID_LINE', value='1', type=Type.INT32_T),
               Constant('MVIEW_GRID_CROSS', value='2', type=Type.INT32_T)
           ]),

    Define('MVIEW_GROUP',
           doc="Open Group defines",
           constants=[
               Constant('MVIEW_GROUP_NEW', value='1', type=Type.INT32_T,
                        doc="New Group (destroy any existing group)"),
               Constant('MVIEW_GROUP_APPEND', value='0', type=Type.INT32_T,
                        doc="Append to an existing Group")
           ]),

    Define('MVIEW_GROUP_LIST',
           doc="What groups to list",
           constants=[
               Constant('MVIEW_GROUP_LIST_ALL', value='0', type=Type.INT32_T,
                        doc="All the groups."),
               Constant('MVIEW_GROUP_LIST_MARKED', value='1', type=Type.INT32_T,
                        doc="Those groups marked using the various mark functions."),
               Constant('MVIEW_GROUP_LIST_VISIBLE', value='2', type=Type.INT32_T,
                        doc="Those groups checked as visible in the view/group manager.")
           ]),

    Define('MVIEW_HIDE',
           doc="Boolean hidding defines",
           constants=[
               Constant('HIDE_ON', value='1', type=Type.INT32_T,
                        doc="Turn ON hidding"),
               Constant('HIDE_OFF', value='0', type=Type.INT32_T,
                        doc="Turn OFF hidding")
           ]),

    Define('MVIEW_IS',
           doc="Defines for mview types",
           constants=[
               Constant('MVIEW_IS_AGG', value='0', type=Type.INT32_T),
               Constant('MVIEW_IS_MOVABLE', value='3', type=Type.INT32_T),
               Constant('MVIEW_IS_CSYMB', value='4', type=Type.INT32_T),
               Constant('MVIEW_IS_LINKED', value='5', type=Type.INT32_T),
               Constant('MVIEW_IS_MADE', value='6', type=Type.INT32_T),
               Constant('MVIEW_IS_HIDDEN', value='7', type=Type.INT32_T),
               Constant('MVIEW_IS_CLIPPED', value='8', type=Type.INT32_T),
               Constant('MVIEW_IS_META', value='9', type=Type.INT32_T),
               Constant('MVIEW_IS_VOXD', value='10', type=Type.INT32_T),
               Constant('MVIEW_IS_SHADOW_2D_INTERPRETATION', value='11', type=Type.INT32_T),
               Constant('MVIEW_IS_VECTOR3D', value='12', type=Type.INT32_T)
           ]),

    Define('MVIEW_LABEL_BOUND',
           doc="Label Binding Defines",
           constants=[
               Constant('MVIEW_LABEL_BOUND_NO', value='0', type=Type.INT32_T,
                        doc="Label Not Bound"),
               Constant('MVIEW_LABEL_BOUND_YES', value='1', type=Type.INT32_T,
                        doc="Label Bound")
           ]),

    Define('MVIEW_LABEL_JUST',
           doc="Label Justification Defines",
           constants=[
               Constant('MVIEW_LABEL_JUST_TOP', value='0', type=Type.INT32_T),
               Constant('MVIEW_LABEL_JUST_BOTTOM', value='1', type=Type.INT32_T),
               Constant('MVIEW_LABEL_JUST_LEFT', value='2', type=Type.INT32_T),
               Constant('MVIEW_LABEL_JUST_RIGHT', value='3', type=Type.INT32_T)
           ]),

    Define('MVIEW_LABEL_ORIENT',
           doc="Label Orientation Defines",
           constants=[
               Constant('MVIEW_LABEL_ORIENT_HORIZONTAL', value='0', type=Type.INT32_T),
               Constant('MVIEW_LABEL_ORIENT_TOP_RIGHT', value='1', type=Type.INT32_T),
               Constant('MVIEW_LABEL_ORIENT_TOP_LEFT', value='2', type=Type.INT32_T)
           ]),

    Define('MVIEW_NAME_LENGTH',
           is_constant=True,
           is_single_constant=True,
           doc="Maximum length for view and group names",
           constants=[
               Constant('MVIEW_NAME_LENGTH', value='1040', type=Type.INT32_T,
                        doc="Maximum Length (1040)")
           ]),

    Define('MVIEW_OPEN',
           doc="Open :class:`MVIEW` define",
           constants=[
               Constant('MVIEW_READ', value='0', type=Type.INT32_T,
                        doc="Read Only - No changes"),
               Constant('MVIEW_WRITENEW', value='1', type=Type.INT32_T,
                        doc="Create new :class:`MVIEW` - destroys any existing :class:`MVIEW`"),
               Constant('MVIEW_WRITEOLD', value='2', type=Type.INT32_T,
                        doc="Open existing :class:`MVIEW` for read/write (must exist)")
           ]),

    Define('MVIEW_PJ',
           doc="Projection modes",
           constants=[
               Constant('MVIEW_PJ_OFF', value='0', type=Type.INT32_T,
                        doc="""
                        No reprojection is used and all locations and
                        attributes are assumed to be in the view coordinate
                        system.
                        """),
               Constant('MVIEW_PJ_LOCATION', value='1', type=Type.INT32_T,
                        doc="""
                        Only locations will be transformed to the view
                        coordinate system.
                        """),
               Constant('MVIEW_PJ_ALL', value='2', type=Type.INT32_T,
                        doc="""
                        Locations and attributes (sizes, thicknesses, angles)
                        will be transformed to the view coordinate system.
                        """),
               Constant('MVIEW_PJ_ON', value='3', type=Type.INT32_T,
                        doc="Mode before the last :def_val:`MVIEW_PJ_OFF`.")
           ]),

    Define('MVIEW_RELOCATE',
           doc="Relocation Defines",
           constants=[
               Constant('MVIEW_RELOCATE_FIT', value='0', type=Type.INT32_T,
                        doc="Will fit the image to fill the specified area"),
               Constant('MVIEW_RELOCATE_ASPECT', value='1', type=Type.INT32_T,
                        doc="Will maintain aspect ratio"),
               Constant('MVIEW_RELOCATE_ASPECT_CENTER', value='2', type=Type.INT32_T,
                        doc="Will maintain aspect ratio and center in specified area")
           ]),

    Define('MVIEW_SMOOTH',
           doc="Interpolation method to use for drawing line and polygon edges",
           constants=[
               Constant('MVIEW_SMOOTH_NEAREST', value='0', type=Type.INT32_T,
                        doc="Nearest neighbour"),
               Constant('MVIEW_SMOOTH_CUBIC', value='1', type=Type.INT32_T,
                        doc="Cubic Spline"),
               Constant('MVIEW_SMOOTH_AKIMA', value='2', type=Type.INT32_T,
                        doc="Akima")
           ]),

    Define('MVIEW_TILE',
           doc="Tiling defines",
           constants=[
               Constant('MVIEW_TILE_RECTANGULAR', value='0', type=Type.INT32_T),
               Constant('MVIEW_TILE_DIAGONAL', value='1', type=Type.INT32_T),
               Constant('MVIEW_TILE_TRIANGULAR', value='2', type=Type.INT32_T),
               Constant('MVIEW_TILE_RANDOM', value='3', type=Type.INT32_T)
           ]),

    Define('MVIEW_UNIT',
           doc="Coordinate systems defines",
           constants=[
               Constant('MVIEW_UNIT_VIEW', value='0', type=Type.INT32_T,
                        doc="View coordinates"),
               Constant('MVIEW_UNIT_PLOT', value='1', type=Type.INT32_T,
                        doc="Plot hi-metric (mm*100) on the map."),
               Constant('MVIEW_UNIT_MM', value='2', type=Type.INT32_T,
                        doc="Plot mm on the map."),
               Constant('MVIEW_UNIT_VIEW_UNWARPED', value='3', type=Type.INT32_T,
                        doc="View coordinates without a warp if there is one")
           ]),

    Define('MVIEW_EXTENT_UNIT',
           doc="""
           Types of units for extents (these map to the
           :def:`MVIEW_UNIT` defines directly)
           """,
           constants=[
               Constant('MVIEW_EXTENT_UNIT_VIEW', value='MVIEW_UNIT_VIEW', type=Type.INT32_T,
                        doc=":def_val:`MVIEW_UNIT_VIEW`"),
               Constant('MVIEW_EXTENT_UNIT_PLOT', value='MVIEW_UNIT_PLOT', type=Type.INT32_T,
                        doc=":def_val:`MVIEW_UNIT_PLOT`"),
               Constant('MVIEW_EXTENT_UNIT_MM', value='MVIEW_UNIT_MM', type=Type.INT32_T,
                        doc=":def_val:`MVIEW_UNIT_MM`"),
               Constant('MVIEW_EXTENT_UNIT_VIEW_UNWARPED', value='MVIEW_UNIT_VIEW_UNWARPED', type=Type.INT32_T,
                        doc=":def_val:`MVIEW_UNIT_VIEW_UNWARPED`")
           ]),

    Define('TEXT_REF',
           doc="Text reference locations",
           constants=[
               Constant('TEXT_REF_BOTTOM_LEFT', value='0', type=Type.INT32_T),
               Constant('TEXT_REF_BOTTOM_CENTER', value='1', type=Type.INT32_T),
               Constant('TEXT_REF_BOTTOM_RIGHT', value='2', type=Type.INT32_T),
               Constant('TEXT_REF_MIDDLE_LEFT', value='3', type=Type.INT32_T),
               Constant('TEXT_REF_MIDDLE_CENTER', value='4', type=Type.INT32_T),
               Constant('TEXT_REF_MIDDLE_RIGHT', value='5', type=Type.INT32_T),
               Constant('TEXT_REF_TOP_LEFT', value='6', type=Type.INT32_T),
               Constant('TEXT_REF_TOP_CENTER', value='7', type=Type.INT32_T),
               Constant('TEXT_REF_TOP_RIGHT', value='8', type=Type.INT32_T)
           ]),

    Define('MVIEW_3D_RENDER',
           doc="""
           3D Geometry rendering defines. These flags only affect mixed geometry groups and not the data
           specific groups (e.g. voxels, vector voxels surfaces etc.). Each of those groups 
           has predefined optimum behaviour and any changes to these flags are ignored.
           """,
           constants=[
               Constant('MVIEW_3D_RENDER_BACKFACES', value='1', type=Type.INT32_T,
                        doc="This flag is enabled if the backfaces of geometry should be rendered"),
               Constant('MVIEW_3D_DONT_SCALE_GEOMETRY', value='2', type=Type.INT32_T,
                        doc="""
                        If the exaggeration scales of the 3D view in X, Y and/or Z is set to anything other than 1.0
                        any geometric objects (spheres, cubes etc.) for 3D groups with the following flags 
                        will render untransformed while only the centers of the objects are changed.
                        This ensures the objects appear in the correct place with respect to other data being rendered (and scaled).
                        """)
           ])]


gx_methods = {
    '3D Entity': [

        Method('Box3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D box",
               notes="The Fill color is used to color the box.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Min X"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Min Y"),
                   Parameter('min_z', type=Type.DOUBLE,
                             doc="Min Z"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Max Y"),
                   Parameter('max_z', type=Type.DOUBLE,
                             doc="Max Z")
               ]),

        Method('CRCView_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Generate an XML CRC of a View",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MAP` object"),
                   Parameter('crc', type=Type.INT32_T, is_ref=True,
                             doc="CRC returned"),
                   Parameter('file', type=Type.STRING,
                             doc="Name of xml to generate (.zip added)")
               ]),

        Method('CRCViewGroup_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Generate an XML CRC of a Group",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MAP` object"),
                   Parameter('group', type=Type.STRING,
                             doc="Name of Group"),
                   Parameter('crc', type=Type.INT32_T, is_ref=True,
                             doc="CRC returned"),
                   Parameter('file', type=Type.STRING,
                             doc="Name of xml to generate (.zip added)")
               ]),

        Method('Cylinder3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D cylinder",
               notes="""
               The Fill color is used to color the cylinder.
               The flags determine if the cylinder is open and what
               end are closed. Note that you can create cones by
               specifying a 0 radius for one of the ends.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('start_x', type=Type.DOUBLE,
                             doc="Start X"),
                   Parameter('start_y', type=Type.DOUBLE,
                             doc="Start Y"),
                   Parameter('start_z', type=Type.DOUBLE,
                             doc="Start Z"),
                   Parameter('end_x', type=Type.DOUBLE,
                             doc="End X"),
                   Parameter('end_y', type=Type.DOUBLE,
                             doc="End Y"),
                   Parameter('end_z', type=Type.DOUBLE,
                             doc="End Z"),
                   Parameter('start_radius', type=Type.DOUBLE,
                             doc="Start Radius (can be zero)"),
                   Parameter('end_radius', type=Type.DOUBLE,
                             doc="End Radius (can be zero)"),
                   Parameter('flags', type=Type.INT32_T,
                             doc=":def:`MVIEW_CYLINDER3D`")
               ]),

        Method('DrawObject3D_MVIEW', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D object optimized for rendering",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`MVIEW_DRAWOBJ3D_ENTITY`"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`MVIEW_DRAWOBJ3D_MODE`"),
                   Parameter('objects', type=Type.INT32_T,
                             doc="Number of Objects"),
                   Parameter('default_count', type=Type.INT32_T,
                             doc="Default Count (if variable and not specified)"),
                   Parameter('vert_v_vx', type="VV",
                             doc="Verticies X"),
                   Parameter('vert_v_vy', type="VV",
                             doc="Verticies Y"),
                   Parameter('vert_v_vz', type="VV",
                             doc="Verticies Z"),
                   Parameter('norm_v_vx', type="VV",
                             doc="Normals X (can be NULL)"),
                   Parameter('norm_v_vy', type="VV",
                             doc="Normals Y (can be NULL)"),
                   Parameter('norm_v_vz', type="VV",
                             doc="Normals Z (can be NULL)"),
                   Parameter('color_vv', type="VV",
                             doc="Colors :class:`VV` (can be NULL)"),
                   Parameter('index_vv', type="VV",
                             doc="Index  :class:`VV` (can be NULL)"),
                   Parameter('count_vv', type="VV",
                             doc="Count  :class:`VV` (can be NULL)")
               ]),

        Method('DrawSurface3DEx_MVIEW', module='geoengine.map', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D object built from triangles",
               notes="""
               Provide one normal per vertex.
               Triangles are defined by indices into the set of vertices.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('group_name', type=Type.STRING,
                             doc="Group name"),
                   Parameter('vert_v_vx', type="VV",
                             doc="Vertices X (:def_val:`GS_REAL`)"),
                   Parameter('vert_v_vy', type="VV",
                             doc="Vertices Y (:def_val:`GS_REAL`)"),
                   Parameter('vert_v_vz', type="VV",
                             doc="Vertices Z (:def_val:`GS_REAL`)"),
                   Parameter('norm_v_vx', type="VV",
                             doc="Normals X (:def_val:`GS_REAL`)"),
                   Parameter('norm_v_vy', type="VV",
                             doc="Normals Y (:def_val:`GS_REAL`)"),
                   Parameter('norm_v_vz', type="VV",
                             doc="Normals Z (:def_val:`GS_REAL`)"),
                   Parameter('color_vv', type="VV",
                             doc="Colors :class:`VV` (:def_val:`GS_INT`) [can be NULL]"),
                   Parameter('color', type=Type.INT32_T,
                             doc="Color used if above :class:`VV` is NULL [0 for :class:`MVIEW`'s fill color]"),
                   Parameter('tri_vv_pt1', type="VV",
                             doc="Triangles Point 1 (:def_val:`GS_INT`)"),
                   Parameter('tri_vv_pt2', type="VV",
                             doc="Triangles Point 2 (:def_val:`GS_INT`)"),
                   Parameter('tri_vv_pt3', type="VV",
                             doc="Triangles Point 3 (:def_val:`GS_INT`)"),
                   Parameter('ipj', type="IPJ",
                             doc="Native :class:`IPJ` of 3D object")
               ]),

        Method('DrawSurface3DFromFile_MVIEW', module='geoengine.map', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D object from a surface file",
               notes="",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('group_name', type=Type.STRING,
                             doc="Group name"),
                   Parameter('surface_file', type=Type.STRING,
                             doc="Surface file")
               ]),

        Method('FontWeightLST_MVIEW', module='geoengine.map', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Fill a :class:`LST` with the different font weights.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('lst', type="LST",
                             doc=":class:`LST` object")
               ]),

        Method('GetAGGFileNames_MVIEW', module='geoengine.map', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Get the names of grid files stored in an :class:`AGG`.",
               notes="""
               The group must be an :class:`AGG` group. Check this using
               :func:`iIsGroup_MVIEW` and :def_val:`MVIEW_IS_AGG`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.STRING,
                             doc="Group name"),
                   Parameter('vv', type="VV",
                             doc="Returned string :class:`VV` of type -:def_val:`STR_FILE`")
               ]),

        Method('IGetMeta_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Retrieves Metadata from a group",
               return_type="META",
               return_doc=":class:`META` Object",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('group', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('meta', type=Type.STRING, is_ref=True, size_of_param='length',
                             doc="Meta name"),
                   Parameter('length', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Length of Meta name variable")
               ]),

        Method('MeasureText_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Compute the bounding rectangle in view units of the text using the current attributes.",
               notes="""
               Area will be 0 if error occurred (does not fail).
               This will return the bounding rectangle as if the text was placed at 0,0 and adjusted according to
               the current text alignment and angle set for the view. Also see notes for :func:`TextSize_MVIEW`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('text', type=Type.STRING,
                             doc="Text string"),
                   Parameter('x_min', type=Type.DOUBLE, is_ref=True,
                             doc="X minimum"),
                   Parameter('y_min', type=Type.DOUBLE, is_ref=True,
                             doc="Y minimum"),
                   Parameter('x_max', type=Type.DOUBLE, is_ref=True,
                             doc="X maximum"),
                   Parameter('y_max', type=Type.DOUBLE, is_ref=True,
                             doc="Y maximum")
               ]),

        Method('Point3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D point.",
               notes="The Line color and line thickness will affect rendering.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y"),
                   Parameter('z', type=Type.DOUBLE,
                             doc="Z")
               ]),

        Method('PolyLine3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D polyline.",
               notes="""
               Dummies are not allowed in the line.
               Line Color, Thickness is supported on rendering
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('vv_x', type="VV",
                             doc="X coordinates."),
                   Parameter('vv_y', type="VV",
                             doc="Y coordinates."),
                   Parameter('vv_z', type="VV",
                             doc="Z coordinates.")
               ]),

        Method('RelocateGroup_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Re-locate a group in a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.STRING,
                             doc="Group name"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Area X minimum"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Area Y minimum"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Area X maximum"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Area Y maximum"),
                   Parameter('asp', type=Type.INT32_T,
                             doc=":def:`MVIEW_RELOCATE`")
               ]),

        Method('SetMeta_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Update the :class:`META` in this group with the new meta object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('group', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('meta', type="META",
                             doc=":class:`META` object"),
                   Parameter('name', type=Type.STRING,
                             doc="Meta name of Object")
               ]),

        Method('Sphere3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D sphere",
               notes="The Fill color is used to color the sphere.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="Center X"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Center Y"),
                   Parameter('z', type=Type.DOUBLE,
                             doc="Center Z"),
                   Parameter('radius', type=Type.DOUBLE,
                             doc="Radius")
               ]),

        Method('UpdateMETAfromGroup_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Fill the :class:`META` with group dataset information",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('group', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('meta', type="META",
                             doc=":class:`META` object to fill")
               ])
    ],
    '3D Plane': [

        Method('DeletePlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Delete a plane in a view",
               notes="""
               If the groups on the plane are not deleted, they will remain in the
               3D view as "New" groups but will be unassigned to a plane.  The
               SetAllNewGroupsToPlane  function can be used to assign these groups
               to a different plane.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.INT32_T,
                             doc="Plane number to delete"),
                   Parameter('del_grp', type=Type.INT32_T,
                             doc="TRUE to delete all groups on the plane")
               ]),

        Method('GetPlaneClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Plane Clip Region",
               notes="By default it is the View's Clip Region",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('pply', type="PLY",
                             doc="Clip Region")
               ]),

        Method('GetPlaneEquation_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Get the equation of a plane",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('pitch', type=Type.DOUBLE, is_ref=True,
                             doc="Rotation about X (Y toward Z +ve, between -360 and 360)"),
                   Parameter('yaw', type=Type.DOUBLE, is_ref=True,
                             doc="Rotation about Y (Z toward X +ve, between -360 and 360)"),
                   Parameter('roll', type=Type.DOUBLE, is_ref=True,
                             doc="Rotation about Z (Y toward X +ve, between -360 and 360)"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="X offset of plane"),
                   Parameter('y', type=Type.DOUBLE, is_ref=True,
                             doc="Y offset of plane"),
                   Parameter('z', type=Type.DOUBLE, is_ref=True,
                             doc="Z offset of plane"),
                   Parameter('sx', type=Type.DOUBLE, is_ref=True,
                             doc="X scale"),
                   Parameter('sy', type=Type.DOUBLE, is_ref=True,
                             doc="Y scale"),
                   Parameter('str_val', type=Type.DOUBLE, is_ref=True,
                             doc="Z scale")
               ]),

        Method('GetViewPlaneEquation_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Get the View's Plane Equation",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('pitch', type=Type.DOUBLE, is_ref=True,
                             doc="Angle in X"),
                   Parameter('yaw', type=Type.DOUBLE, is_ref=True,
                             doc="Angle in Y"),
                   Parameter('roll', type=Type.DOUBLE, is_ref=True,
                             doc="Angle in Z"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="Offset in X"),
                   Parameter('y', type=Type.DOUBLE, is_ref=True,
                             doc="Offset in Y"),
                   Parameter('z', type=Type.DOUBLE, is_ref=True,
                             doc="Offset in Z"),
                   Parameter('sx', type=Type.DOUBLE, is_ref=True,
                             doc="Scale in X"),
                   Parameter('sy', type=Type.DOUBLE, is_ref=True,
                             doc="Scale in Y"),
                   Parameter('str_val', type=Type.DOUBLE, is_ref=True,
                             doc="Scale in Z")
               ]),

        Method('iCreatePlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Create a 3D Plane for 2D Groups",
               return_type=Type.INT32_T,
               return_doc="x - Index of plane",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.STRING,
                             doc="Name of Plane")
               ]),

        Method('iFindPlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Find a plane in a view",
               return_type=Type.INT32_T,
               return_doc="Plane number, -1 if not found",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.STRING,
                             doc="Name of the plane")
               ]),

        Method('IGetDefPlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Get the default drawing plane.",
               notes="""
               2D drawing to a 3D View will always be placed on the
               default drawing plane.  If no default drawing plane
               has been set, the first valid plane in the view is
               used as the default drawing plane.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='length',
                             doc="Name"),
                   Parameter('length', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Maximum name length")
               ]),

        Method('iIsView3D_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Is the view 3D?",
               return_type=Type.INT32_T,
               return_doc="TRUE if view is 3D",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object")
               ]),

        Method('iIsSection_MVIEW', module='geoengine.map', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Is the view a section view?",
               notes="""
               Section views are recognized because their projection contains one of the following orientations:
               
               :def_val:`IPJ_ORIENT_SECTION` - Target-type sections with Z projection horizontally
               :def_val:`IPJ_ORIENT_SECTION_NORMAL` - Like :def_val:`IPJ_ORIENT_SECTION`, but Z projects
               perpendicular to the secton plane.
               :def_val:`IPJ_ORIENT_SECTION_CROOKED` - Crooked sections
               :def_val:`IPJ_ORIENT_3D` - Some Sections extracted from a voxel - e.g. VoxelToGrids,
               as the voxel can have any orientation in 3D.
               """,
               return_type=Type.INT32_T,
               return_doc="TRUE if view is a section view.",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object")
               ]),

        Method('ListPlaneGroups_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="List all groups in a specific plane of a 3D view",
               notes="""
               The group names are placed in the list names, group
               numbers are placed in the list values.
               
               Groups are added to the end of the :class:`LST`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.INT32_T,
                             doc="Plane number"),
                   Parameter('lst', type="LST",
                             doc="List of plane names and numbers")
               ]),

        Method('ListPlanes_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="List all planes in a 3D view",
               notes="""
               The plane names are placed in the list names, plane
               numbers are placed in the list values.
               
               Planes are added to the end of the :class:`LST`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('lst', type="LST",
                             doc="List of plane names and numbers")
               ]),

        Method('SetAllGroupsToPlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set all groups to be within one plane",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.INT32_T,
                             doc="Plane Index to set all groups to")
               ]),

        Method('SetAllNewGroupsToPlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set all groups that are not in any plane to this plane",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.INT32_T,
                             doc="Plane Index to set all groups to")
               ]),

        Method('SetDefPlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the default drawing plane.",
               notes="""
               2D drawing to a 3D View will always be placed on the
               default drawing plane.  If no default drawing plane
               has been set, the first valid plane in the view is
               used as the default drawing plane.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('name', type=Type.STRING,
                             doc="Name")
               ]),

        Method('SetGroupToPlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set a group to a plane",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.INT32_T,
                             doc="Plane Index to set all groups to"),
                   Parameter('group', type=Type.STRING,
                             doc="Name of group to set")
               ]),

        Method('SetH3DN_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the :class:`3DN` object for this view",
               notes="To make the view a 2D view, set a :class:`3DN` of NULL.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` to set (NULL for 2D view)")
               ]),

        Method('Get3DPointOfView_MVIEW', module='geoengine.map', version='9.2.0',
               availability=Availability.PUBLIC, 
               doc="Get 3D point of view (values are will be :def_val:`rDUMMY` if view for 2D views)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` Handle"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="X center"),
                   Parameter('y', type=Type.DOUBLE, is_ref=True,
                             doc="Y center"),
                   Parameter('z', type=Type.DOUBLE, is_ref=True,
                             doc="Z center"),
                   Parameter('distance', type=Type.DOUBLE, is_ref=True,
                             doc="Distance from center"),
                   Parameter('declination', type=Type.DOUBLE, is_ref=True,
                             doc="Declination, 0 to 360 CW from Y"),
                   Parameter('inclination', type=Type.DOUBLE, is_ref=True,
                             doc="Inclination, -90 to +90")
               ]),

        Method('Set3DPointOfView_MVIEW', module='geoengine.map', version='9.2.0',
               availability=Availability.PUBLIC, 
               doc="Set 3D point of view (no effect on 2D views)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` Handle"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X center"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y center"),
                   Parameter('z', type=Type.DOUBLE,
                             doc="Z center"),
                   Parameter('distance', type=Type.DOUBLE,
                             doc="Distance from center"),
                   Parameter('declination', type=Type.DOUBLE,
                             doc="Declination, 0 to 360 CW from Y"),
                   Parameter('inclination', type=Type.DOUBLE,
                             doc="Inclination, -90 to +90")
               ]),

        Method('SetPlaneClipPLY_MVIEW', module='geoengine.map', version='5.1.4',
               availability=Availability.PUBLIC, 
               doc="Set the Plane Clip Region",
               notes="By default it is the View's Clip Region",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('pply', type="PLY",
                             doc="Clip Region")
               ]),

        Method('SetPlaneEquation_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the equation of a plane",
               notes="""
               For a grid with the "Y" axis giving elevation:
               use rotations = (-90, 0, 0) for a section with azimuth 90 (E-W)
               use rotations = (-90, 0, -90) for a section with azimuth 0 (N-S)
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('pitch', type=Type.DOUBLE,
                             doc="Rotation about X (Z toward Y +ve, between -360 and 360)"),
                   Parameter('yaw', type=Type.DOUBLE,
                             doc="Rotation about Y (Z toward X +ve, between -360 and 360)"),
                   Parameter('roll', type=Type.DOUBLE,
                             doc="Rotation about Z (Y toward X +ve, between -360 and 360)"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X offset of plane"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y offset of plane"),
                   Parameter('z', type=Type.DOUBLE,
                             doc="Z offset of plane"),
                   Parameter('sx', type=Type.DOUBLE,
                             doc="X scale"),
                   Parameter('sy', type=Type.DOUBLE,
                             doc="Y scale"),
                   Parameter('str_val', type=Type.DOUBLE,
                             doc="Z scale")
               ]),

        Method('SetPlaneSurface_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the surface image of a plane",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('surface', type=Type.STRING,
                             doc="Optional surface image/grid name, can be NULL")
               ]),

        Method('SetPlaneSurfInfo_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the surface information",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('sample', type=Type.INT32_T,
                             doc="Sample rate (>=1)"),
                   Parameter('base', type=Type.DOUBLE,
                             doc="Base"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="Scale"),
                   Parameter('min', type=Type.DOUBLE,
                             doc="Min"),
                   Parameter('max', type=Type.DOUBLE,
                             doc="Max")
               ])
    ],
    '3D Rendering 2D': [

        Method('DefinePlane3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Define a 2D drawing plane based on point and normal",
               notes="""
               2D rendering commands are translated to 3D commands
               based on the plane.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('center_x', type=Type.DOUBLE,
                             doc="Center point X"),
                   Parameter('center_y', type=Type.DOUBLE,
                             doc="Center point Y"),
                   Parameter('center_z', type=Type.DOUBLE,
                             doc="Center point Z"),
                   Parameter('x_vector_x', type=Type.DOUBLE,
                             doc="X Vector X"),
                   Parameter('x_vector_y', type=Type.DOUBLE,
                             doc="X Vector Y"),
                   Parameter('x_vector_z', type=Type.DOUBLE,
                             doc="X Vector Z"),
                   Parameter('y_vector_x', type=Type.DOUBLE,
                             doc="Y Vector X"),
                   Parameter('y_vector_y', type=Type.DOUBLE,
                             doc="Y Vector Y"),
                   Parameter('y_vector_z', type=Type.DOUBLE,
                             doc="Y Vector Z")
               ]),

        Method('DefineViewerAxis3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="""
               Define a 2D drawing plane based on the user's view that
               oriented around the vector.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('center_x', type=Type.DOUBLE,
                             doc="Center point X"),
                   Parameter('center_y', type=Type.DOUBLE,
                             doc="Center point Y"),
                   Parameter('center_z', type=Type.DOUBLE,
                             doc="Center point Z"),
                   Parameter('dir_point_x', type=Type.DOUBLE,
                             doc="Directional Point X"),
                   Parameter('dir_point_y', type=Type.DOUBLE,
                             doc="Directional Point Y"),
                   Parameter('dir_point_z', type=Type.DOUBLE,
                             doc="Directional Point Z")
               ]),

        Method('DefineViewerPlane3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Define a 2D drawing plane based on the user's view.",
               notes="""
               The plane is always facing the viewer. Otherwise the
               this is identical to the previous
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('center_x', type=Type.DOUBLE,
                             doc="Center point X"),
                   Parameter('center_y', type=Type.DOUBLE,
                             doc="Center point Y"),
                   Parameter('center_z', type=Type.DOUBLE,
                             doc="Center point Z")
               ])
    ],
    'Clipping': [

        Method('_ClipPolyEx_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a polygon to the clip region.",
               notes="""
               The polygon will be added to the current clip region.
               The :class:`VV`'s cannot have any dummy elements.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('unit', type=Type.INT32_T,
                             doc=":def:`MVIEW_UNIT`"),
                   Parameter('exclude', type=Type.INT32_T,
                             doc="Exclude")
               ]),

        Method('_ClipRectEx_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a rectangle to the clip region.",
               notes="The rectangle will be added to the current clip region.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="X minimum"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Y minimum"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="X maximum"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Y maximum"),
                   Parameter('unit', type=Type.INT32_T,
                             doc=":def:`MVIEW_UNIT`"),
                   Parameter('exclude', type=Type.INT32_T,
                             doc="Exclude")
               ]),

        Method('ClipClear_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Remove/clear the view clip region.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle")
               ]),

        Method('ClipGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Clipping mode on/off for all groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`MVIEW_CLIP`")
               ]),

        Method('ClipMarkedGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Clipping mode on/off for marked groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`MVIEW_CLIP`")
               ]),

        Method('ClipPoly_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a polygon to the clip region.",
               notes="""
               The polygon will be added to the current clip region.
               The :class:`VV`'s cannot have any dummy elements.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('unit', type=Type.INT32_T,
                             doc=":def:`MVIEW_UNIT`")
               ]),

        Method('ClipRect_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a rectangle to the clip region.",
               notes="The rectangle will be added to the current clip region.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="X minimum"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Y minimum"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="X maximum"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Y maximum"),
                   Parameter('unit', type=Type.INT32_T,
                             doc=":def:`MVIEW_UNIT`")
               ]),

        Method('DeleteExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Deletes an extended clip :class:`PLY` object used by this view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('ext_ply', type=Type.INT32_T,
                             doc="Extended ClipPLY number")
               ]),

        Method('ExtClipPLYList_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the names of existing extended clip :class:`PLY` objects in this view as list.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('lst', type="LST")
               ]),

        Method('GetClipPLY_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get clipping polygons, in the user projection",
               notes="""
               The returned :class:`PLY` is recast into the User projection.
               For oriented views (especially sections), use
               :func:`GetPLY_MVIEW`, which returns the Clip :class:`PLY` in the view's native
               projection (e.g. the one set using :func:`SetIPJ_MVIEW`).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('poly', type="PLY",
                             doc="Poly")
               ]),

        Method('GetExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get an extended clip :class:`PLY` object used by this view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('ext_ply', type=Type.INT32_T,
                             doc="Extended ClipPLY number"),
                   Parameter('ply', type="PLY",
                             doc=":class:`PLY` object to get")
               ]),

        Method('GetGroupExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets extended clip information for group in view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('group', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('ext_ply', type=Type.INT32_T, is_ref=True,
                             doc="Extended :class:`PLY` number (returned, -1 if not set)")
               ]),

        Method('GetPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get clipping polygons, in the base projection",
               notes="""
               This should be used to get the clipping polygon for
               oriented views (especially sections).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('poly', type="PLY",
                             doc="Poly")
               ]),

        Method('GroupClipMode_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Clipping mode on or off for new groups.",
               notes="All new groups will be clipped.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`MVIEW_CLIP`")
               ]),

        Method('IGetNameExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the name of the extended clip :class:`PLY` object in this view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('ext_ply', type=Type.INT32_T,
                             doc="Extended ClipPLY number"),
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='length',
                             doc="Name"),
                   Parameter('length', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Length of Name variable")
               ]),

        Method('iNumExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of extended clip :class:`PLY` objects in this view.",
               return_type=Type.INT32_T,
               return_doc="Number of PLYs",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object")
               ]),

        Method('iSetExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Set an extended clip :class:`PLY` object used by this view.",
               return_type=Type.INT32_T,
               return_doc="Index of new or changed :class:`PLY`, -1 on error",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('ext_ply', type=Type.INT32_T,
                             doc="Extended ClipPLY number, If greater or equal to the return value of :func:`iNumExtClipPLY_MVIEW` it will be added to the end of the current list"),
                   Parameter('name', type=Type.STRING,
                             doc="Name (Has to be unique, otherwise error will be returned)"),
                   Parameter('ply', type="PLY",
                             doc=":class:`PLY` object to set, use a null :class:`PLY` to rename an existing object")
               ]),

        Method('SetClipPLY_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set clipping region to a :class:`PLY`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('poly', type="PLY",
                             doc="Poly")
               ]),

        Method('SetGroupExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets extended clip information for group in view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('group', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('ext_ply', type=Type.INT32_T,
                             doc="Extended :class:`PLY` number (-1 to clear)")
               ])
    ],
    'Color': [

        Method('Color2RGB_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Convert to RGB values.",
               notes="Color component intensities will be in the range 0-255.",
               see_also=":func:`iColor_MVIEW`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('color', type=Type.INT32_T,
                             doc="Color value"),
                   Parameter('r', type=Type.INT32_T, is_ref=True,
                             doc="Red"),
                   Parameter('g', type=Type.INT32_T, is_ref=True,
                             doc="Green"),
                   Parameter('b', type=Type.INT32_T, is_ref=True,
                             doc="Blue")
               ]),

        Method('ColorDescr_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a color to a color string label",
               notes="See :func:`iColor_MVIEW`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('color', type=Type.INT32_T,
                             doc="COL_ANY variable"),
                   Parameter('color_descr', type=Type.STRING, is_ref=True, size_of_param='length',
                             doc="Color descriptor returned"),
                   Parameter('length', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Length of the string")
               ]),

        Method('iColor_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a color from a color string label",
               notes="""
               Color strings may be "R","G","B","C","M","Y",
               "H","S","V", or "K" or a combination of these
               characters, each followed by up to three digits
               specifying a number between 0 and 255.
               An empty string produce C_ANY_NONE.
               
               You must stay in the same color model, RGB, CMY,
               HSV or K.
               
               For example "R", "R127G22", "H255S127V32"
               
               Characters are not case sensitive.
               """,
               see_also="iColorXXX_MVIEW macros",
               return_type=Type.INT32_T,
               return_doc="Color int",
               parameters = [
                   Parameter('color', type=Type.STRING,
                             doc="Color name string")
               ]),

        Method('iColorCMY_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return CMY color.",
               notes="Color component intensities must be in the range 0-255.",
               see_also=":func:`iColor_MVIEW`",
               return_type=Type.INT32_T,
               return_doc="Color int based on color model.",
               parameters = [
                   Parameter('c', type=Type.INT32_T,
                             doc="Cyan"),
                   Parameter('m', type=Type.INT32_T,
                             doc="Magenta"),
                   Parameter('y', type=Type.INT32_T,
                             doc="Yellow")
               ]),

        Method('iColorHSV_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return HSV color.",
               notes="Color component intensities must be in the range 0-255.",
               see_also=":func:`iColor_MVIEW`",
               return_type=Type.INT32_T,
               return_doc="Color int based on color model.",
               parameters = [
                   Parameter('h', type=Type.INT32_T,
                             doc="Hue"),
                   Parameter('s', type=Type.INT32_T,
                             doc="Saturation"),
                   Parameter('v', type=Type.INT32_T,
                             doc="Color")
               ]),

        Method('iColorRGB_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return RGB color.",
               notes="Color component intensities must be in the range 0-255.",
               see_also=":func:`iColor_MVIEW`",
               return_type=Type.INT32_T,
               return_doc="Color int based on color model.",
               parameters = [
                   Parameter('r', type=Type.INT32_T,
                             doc="Red"),
                   Parameter('g', type=Type.INT32_T,
                             doc="Green"),
                   Parameter('b', type=Type.INT32_T,
                             doc="Blue")
               ])
    ],
    'Drawing Attribute': [

        Method('ClipMode_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the view clipping mode on or off.",
               notes="""
               Entitles that follow in this group will be clipped
               or not clipped depending on this mode.
               
               The montaj editor cannot change the clip mode of
               embedded clipped/unclipped enties that are controlled
               by this call.  Use the Group clipping functions
               instead.
               
               It is highly recommended that you use the :func:`GroupClipMode_MVIEW`
               function to control clipping on a group-by-group basis, instead
               of using :func:`ClipMode_MVIEW` when inside a group, as it is impossible
               to determine the  true visible extents of a group. In such cases, the
               "zoom to full map extents" command may give incorrect results.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`MVIEW_CLIP`")
               ]),

        Method('FillColor_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the fill color.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('color', type=Type.INT32_T,
                             doc="Color")
               ]),

        Method('LineColor_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the line color.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('color', type=Type.INT32_T,
                             doc="Color")
               ]),

        Method('LineSmooth_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set the line edge smoothing.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('smooth', type=Type.INT32_T,
                             doc=":def:`MVIEW_SMOOTH`")
               ]),

        Method('LineStyle_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the style of a line.",
               notes="""
               Line styles are selected by ordinal value (line style #)
               from those defined in default.lpt.  If default.lpt does
               not have a the style specified, the file user.lpt is
               searched.  If this file does not contain the line style
               solid is assumed.
               
               Note that line styles from default.lpt and user.lpt are
               read into the map at the time the map is created, not
               at display time.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('style', type=Type.INT32_T,
                             doc="Line Style #, see default.lpt"),
                   Parameter('pitch', type=Type.DOUBLE,
                             doc="Pitch in view units")
               ]),

        Method('LineThick_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the line thickness.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('thick', type=Type.DOUBLE,
                             doc="Line thickness in view space units")
               ]),

        Method('PatAngle_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the pattern angle",
               notes="""
               Allows the user to apply a rotation to the basic
               pattern. Care should be taken to ensure that the
               tiling remains continuous; i.e. if the pattern
               consists of horizontal lines, only angles of
               -90, 0, 90, 180 (etc.) would give seamless tiling.
               However, simple, closed figure, such as a star,
               could be given any angle.
               Rotations about the center point (0.5, 0.5) of the
               unit cell are performed prior to applying PatSize.
               The default value is 0.0.
               Setting an angle of -999 inititates the random angle
               feature, and each pattern tile is rotated to a different
               angle. Using this along with PatStyle(View, :def_val:`MVIEW_TILE_RANDOM`)
               can give a "hand-drawn" effect to geological fills.
               
               See the IMPORTANT note for sPatNumber_MVIEW().
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('angle', type=Type.DOUBLE,
                             doc="Angle")
               ]),

        Method('PatDensity_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the tiling density.",
               notes="""
               This number is the ratio between the plotted unit cell size and the
               distance between the plotted tile centers. The default value is 1.
               A value larger than 1 increases the density of the pattern, while
               values less than 1 make the pattern more "spread out".
               This can be used along with sPatStyleMethod to create more complicated
               fills from simple patterns.
               
               See the IMPORTANT note for sPatNumber_MVIEW().
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('density', type=Type.DOUBLE,
                             doc="Relative density (default = 1).")
               ]),

        Method('PatNumber_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the pattern number",
               notes="""
               Pattern 0 is solid fill.(default)
               Set the pattern color using :func:`FillColor_MVIEW`.
               
               Patterns are selected by ordinal value (pattern number)
               from those defined in default.pat.  If default.pat does
               not have a the pattern specified, the file user.pat is
               searched.  If this file does not contain the pattern
               solid is assumed.
               
               Note that patterns from default.pat and user.pat are
               read into the map at the time the map is created, not
               at display time.
               
               IMPORTANT: A call to this function resets all the various
               pattern attributes to those defined for the selected pattern.
               If you want to modify any attributes, call that function (e.g.
               sPatSize_MVIEW(), AFTER you call sPatNumber_MVIEW().
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('number', type=Type.INT32_T,
                             doc="Pattern number")
               ]),

        Method('PatSize_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the pattern unit cell size (X)",
               notes="See the IMPORTANT note for sPatNumber_MVIEW().",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('size', type=Type.DOUBLE,
                             doc="Pattern size in view units")
               ]),

        Method('PatStyle_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the tiling method (i.e. rectangle, triangle)",
               notes="""
               Normally, the unit cell is duplicated across the fill area
               like floor tiles (:def_val:`MVIEW_TILE_RECTANGULAR`).
               DIAGONAL tiling rotates the tiling positions (but not the tiles)
               by 45 degrees.
               TRIANGULAR tiling
               Offsets each succeeding row by half the unit cell size, and
               lessens the vertical offset, so that the unit cell centers
               form a triangular grid pattern.
               RANDOM tiling adds small random offsets in both directions to give
               the diffuse effect seen on many geological maps.
               
               NOTE: Some patterns are designed to be interlocking and may only
               work "correctly" with one tiling method.
               
               See the IMPORTANT note for sPatNumber_MVIEW().
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('style', type=Type.INT32_T,
                             doc=":def:`MVIEW_TILE`")
               ]),

        Method('PatThick_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the pattern line thickness",
               notes="See the IMPORTANT note for sPatNumber_MVIEW().",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('thick', type=Type.DOUBLE,
                             doc="Line thickness as fraction of pattern size (ie. 0.05)")
               ]),

        Method('SymbAngle_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Symb angle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('angle', type=Type.DOUBLE,
                             doc="Angle in degrees CCW from +X")
               ]),

        Method('SymbColor_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Symbol color.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('color', type=Type.INT32_T,
                             doc="Color")
               ]),

        Method('SymbFillColor_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Symbol color fill.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('color', type=Type.INT32_T,
                             doc="Color")
               ]),

        Method('SymbFont_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the symbol font and style.",
               notes="""
               If the font cannot be found, the DEFAULT_SYMBOL_FONT
               specified in the [MONTAJ] section of GEOSOFT.INI
               will be used.
               
               See :func:`TextFont_MVIEW` for the font name syntax.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('face', type=Type.STRING,
                             doc="Face name"),
                   Parameter('geofont', type=Type.INT32_T,
                             doc="Geosoft font? :def:`GEO_BOOL`"),
                   Parameter('weight', type=Type.INT32_T,
                             doc=":def:`MVIEW_FONT_WEIGHT`"),
                   Parameter('italic', type=Type.INT32_T,
                             doc="Italic font? :def:`GEO_BOOL`")
               ]),

        Method('SymbNumber_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Symbol number.",
               notes="""
               The lower 16 bits of the number is interpreted as UTF-16 with a valid Unicode character
               code point. GFN fonts wil produce valid symbols depending on the font for 0x01-0x7f and the degree,
               plus-minus and diameter symbol(latin small letter o with stroke) for 0xB0, 0xB1 and 0xF8 respectively.
               
               It is possible to check if a character is valid using :func:`iIsValidUTF16Char_UNC`. The high 16-bits are reserved
               for future use. Also see: :func:`iValidSymbol_UNC` and :func:`ValidateSymbols_UNC`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('number', type=Type.INT32_T,
                             doc="Symbol number")
               ]),

        Method('SymbSize_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Symb size.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('size', type=Type.DOUBLE,
                             doc="Size in view units")
               ]),

        Method('TextAngle_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the text angle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('angle', type=Type.DOUBLE,
                             doc="Angle in degrees CCW from +X")
               ]),

        Method('TextColor_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Text color.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('color', type=Type.INT32_T,
                             doc="Color")
               ]),

        Method('TextFont_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the text font.",
               notes="""
               Font characteristics can be defined using the function parameters,
               or may be defined as decorations in the font name.  A decorated font
               name has the following format:
               
               font_name(type,weight,italics,charset)
               
               where
               type     - "TT" or "GFN"
               weight   - last word from MVIEW_FONT_WEIGHT_ (ie. "LIGHT")
               italics  - "ITALICS" for for italics
               charset  - Before version 6.2. this decoration was honoured and it affected the display
               of characters above ASCII 127. 6.2. introduced Unicode in the core
               montaj engine that eliminated the need for such a setting. All strings
               on the GX API level are encoded in :def:`UTF8` during runtime which makes it possible
               to represent all possible characters without using character sets. This decoration
               will now be ignored.
               
               Qualifiers take precidence over passed parameters.
               The order of qualifiers is not relevant.
               
               examples:
               
               "sr(GFN,ITALICS)"  - geosoft GFN font, normal weight, italics
               "Arial(TT,XBOLD)"  - TrueType font, bold
               "Times(TT,ITALICS,_EastEurope)"
               - TrueType font, italics, Eastern Europe charcters
               
               Decorated name qualifiers take precedence over passed parameters.
               
               If the font cannot be found, or if "Default" is used, the DEFAULT_MAP_FONT
               specified in the [MONTAJ] section of GEOSOFT.INI
               will be used.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('face', type=Type.STRING,
                             doc="Font face name"),
                   Parameter('geo_font', type=Type.INT32_T,
                             doc="Geosoft font? (TRUE or FALSE)"),
                   Parameter('weight', type=Type.INT32_T,
                             doc=":def:`MVIEW_FONT_WEIGHT`"),
                   Parameter('italic', type=Type.INT32_T,
                             doc="Italic font? (TRUE or FALSE)")
               ]),

        Method('TextRef_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the text plot reference point.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('ref', type=Type.INT32_T,
                             doc=":def:`TEXT_REF`")
               ]),

        Method('TextSize_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the text size.",
               notes="""
               Because views may have differing X and Y scales this size can only make sense in one of these directions
               otherwise text would appear warped on these kinds of views. The X direction was chosen to represent the
               font size. For instance if the X scale is 1 unit/mm and my Y scale is 2 units/mm a font size of 3.0 view
               units will result in un-rotated text that appears 6 view units or 3mm high in the Y direction.
               
               Another important thing to keep in mind that this size represents what is known as the "ascent" height
               of the font. The full height of the text may be higher if characters with accents or lower extension
               (e.g. the lowercase y) appear in the text. For TrueType fonts the mapping system will do a best effort
               positioning and sizing of the text using the alignment set and information about the font that it queries
               from the operating system. For instance; if Arial text "Blog" is placed at (0,0) and the alignment
               setting is Left-Bottom the left side of the B should be aligned at 0 in the X direction and the
               bottom of all the letters except y will be at 0 in the Y direction. The lower part of the y will extend
               below 0 in the Y (this is known as the "descent" height of the font at this size). The letters B and l
               should be very close to the size set here (this may differ slightly for different fonts).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('size', type=Type.DOUBLE,
                             doc="Size in view units")
               ]),

        Method('Transparency_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the transparency for new objects.",
               notes="""
               1.0 Renders completely opaque objects while 0.0 will be transparent.
               Objects written after this will have a combined transparency value with the
               group transparency if it is set (e.g. 0.5 for group and 0.8 stream will result in 0.4).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('trans', type=Type.DOUBLE,
                             doc="Transparency (1.0 - Opaque, 0.0 - Transparent)")
               ]),

        Method('ZValue_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets Z-value info.",
               notes="""
               This number is stored in map mainly for exports to other vector formats (e.g ShapeFiles)
               A contour map that's exported to a shape file will use this value as a Z-value attributes for its shapes.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('val', type=Type.DOUBLE,
                             doc="Z-Value")
               ])
    ],
    'Drawing Entity': [

        Method('Arc_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw an arc.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="Center x"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Center y"),
                   Parameter('radius', type=Type.DOUBLE,
                             doc="Radius"),
                   Parameter('ratio', type=Type.DOUBLE,
                             doc="Ratio x/y"),
                   Parameter('angle', type=Type.DOUBLE,
                             doc="Angle"),
                   Parameter('start', type=Type.DOUBLE,
                             doc="Start angle"),
                   Parameter('end', type=Type.DOUBLE,
                             doc="End angle")
               ]),

        Method('Chord_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a filled arc.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="Center x"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Center y"),
                   Parameter('radius', type=Type.DOUBLE,
                             doc="Radius"),
                   Parameter('ratio', type=Type.DOUBLE,
                             doc="Ratio x/y"),
                   Parameter('angle', type=Type.DOUBLE,
                             doc="Angle"),
                   Parameter('start', type=Type.DOUBLE,
                             doc="Start angle"),
                   Parameter('end', type=Type.DOUBLE,
                             doc="End angle")
               ]),

        Method('ClassifiedSymbols_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Plot classified symbols",
               notes="""
               For example, to plot three levels <95, 95-100 and
               100-120, three string arguments would be:
               
               "95,100,120"      maximums of each class
               "2.0,2.5,3.0"     sizes in mm
               "y,g,r"           fill colors
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('vv_z', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('scal_mm', type=Type.DOUBLE,
                             doc="Scale factor to convert mm to view units"),
                   Parameter('zmin', type=Type.DOUBLE,
                             doc="Classified minimum Z to plot"),
                   Parameter('zval', type=Type.STRING,
                             doc="Comma delimited list of Z maximums"),
                   Parameter('size', type=Type.STRING,
                             doc="Comma delimited list of sizes in mm"),
                   Parameter('fcol', type=Type.STRING,
                             doc="Comma delimited list of color strings")
               ]),

        Method('ComplexPolygon_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a polygon with holes in it.",
               notes="You pass a :class:`VV` with polygon sizes and 2 point vvs.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('vv_i', type="VV",
                             doc=":class:`VV` of type int holding the number of points for each polygon"),
                   Parameter('vv_x', type="VV",
                             doc="X coordinates."),
                   Parameter('vv_y', type="VV",
                             doc="Y coordinates.")
               ]),

        Method('Ellipse_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw an ellipse",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="Center x"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Center y"),
                   Parameter('radius', type=Type.DOUBLE,
                             doc="Radius"),
                   Parameter('ratio', type=Type.DOUBLE,
                             doc="Ratio x/y"),
                   Parameter('angle', type=Type.DOUBLE,
                             doc="Angle")
               ]),

        Method('Line_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('x0', type=Type.DOUBLE,
                             doc="X0"),
                   Parameter('y0', type=Type.DOUBLE,
                             doc="Y0"),
                   Parameter('x1', type=Type.DOUBLE,
                             doc="X1"),
                   Parameter('y1', type=Type.DOUBLE,
                             doc="Y1")
               ]),

        Method('LineVV_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw line segments stored in a GS_D2LINE :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('gvv', type="VV",
                             doc=":class:`VV` for GS_D2LINE")
               ]),

        Method('PolygonDm_MVIEW', module='geoengine.map', version='5.0.6',
               availability=Availability.PUBLIC, 
               doc="Like PolyLineDm, but draw polygons.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('vv_x', type="VV",
                             doc="X coordinates."),
                   Parameter('vv_y', type="VV",
                             doc="Y coordinates.")
               ]),

        Method('PolygonPLY_MVIEW', module='geoengine.map', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Draw a complex polygon from :class:`PLY`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('ply', type="PLY")
               ]),

        Method('PolyLine_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a polyline or polygon (dummies deleted).",
               notes="""
               Dummies in X and/or Y :class:`VV` are deleted and it results
               in 'solid' line. Using :func:`PolyLineDm_MVIEW` (below) function
               if gaps from dummies are to be kept.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`MVIEW_DRAW`"),
                   Parameter('vv_x', type="VV",
                             doc="X coordinates."),
                   Parameter('vv_y', type="VV",
                             doc="Y coordinates.")
               ]),

        Method('PolyLineDm_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a polyline with gaps defined by dummies in X/Y VVs",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('vv_x', type="VV",
                             doc="X coordinates."),
                   Parameter('vv_y', type="VV",
                             doc="Y coordinates.")
               ]),

        Method('PolyWrap_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw wrapped polylines from X and Y :class:`VV`'s.",
               notes="""
               Convert a given VVy into a wrapped VVy using
               the current view window as the wrap region.
               Then draw polylines from it.
               """,
               see_also=":func:`PolyLine_MVIEW`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('vv_x', type="VV",
                             doc="X coordinates."),
                   Parameter('vv_y', type="VV",
                             doc="Y coordinates.")
               ]),

        Method('Rectangle_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a rectangle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('x0', type=Type.DOUBLE,
                             doc="X0"),
                   Parameter('y0', type=Type.DOUBLE,
                             doc="Y0"),
                   Parameter('x1', type=Type.DOUBLE,
                             doc="X1"),
                   Parameter('y1', type=Type.DOUBLE,
                             doc="Y1")
               ]),

        Method('Segment_MVIEW', module='geoengine.map', version='5.0.7',
               availability=Availability.PUBLIC, 
               doc="Draw a filled segment of an ellipse.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="Center x"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Center y"),
                   Parameter('radius', type=Type.DOUBLE,
                             doc="Radius"),
                   Parameter('ratio', type=Type.DOUBLE,
                             doc="Ratio x/y"),
                   Parameter('angle', type=Type.DOUBLE,
                             doc="Angle"),
                   Parameter('start', type=Type.DOUBLE,
                             doc="Start angle"),
                   Parameter('end', type=Type.DOUBLE,
                             doc="End angle")
               ]),

        Method('SizeSymbols_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Plot sized symbols",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X"),
                   Parameter('vv_y', type="VV",
                             doc="Y"),
                   Parameter('vv_z', type="VV",
                             doc="Symbol sizes (in view units)")
               ]),

        Method('Symbol_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Plot a symbol",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y")
               ]),

        Method('Symbols_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Plot symbols",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X"),
                   Parameter('vv_y', type="VV",
                             doc="Y")
               ]),

        Method('SymbolsITR_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Plot symbols using an :class:`ITR`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('itr', type=Type.STRING,
                             doc=":class:`ITR` file name (ZON or :class:`ITR`)"),
                   Parameter('vv_x', type="VV",
                             doc="X"),
                   Parameter('vv_y', type="VV",
                             doc="Y"),
                   Parameter('vv_z', type="VV",
                             doc="Z")
               ]),

        Method('Text_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw text.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('text', type=Type.STRING,
                             doc="Text to plot"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X location of text"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y location of text")
               ])
    ],
    'Drawing Object': [

        Method('Aggregate_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add an aggregate to a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('agg', type="AGG",
                             doc="Aggregate"),
                   Parameter('name', type=Type.STRING,
                             doc="Aggregate name Maximum length is :def_val:`MVIEW_NAME_LENGTH`")
               ]),

        Method('GetAggregate_MVIEW', module='geoengine.map', version='9.2.0',
               availability=Availability.PUBLIC, 
               doc="Get an existing Aggregate object from the view.",
               notes="This method returns a cached object owned by the :class:`MVIEW` and will be destroyed automatically when the :class:`MVIEW` is disposed",
               return_type="AGG",
               return_doc=":class:`AGG` object",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number")
               ]),

        Method('ChangeLineMessage_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Change the specified line in a view.",
               notes="""
               The line name can be created by calling LineLabel_DB using
               :def_val:`DB_LINE_LABEL_FORMAT_LINK`. This insures that the label is
               created is the same way as used in the database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('line', type=Type.STRING,
                             doc="Change to this line")
               ]),

        Method('ColSymbol_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a colored symbol object to a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('name', type=Type.STRING,
                             doc="Name of the color symbol group"),
                   Parameter('csymb', type="CSYMB",
                             doc=":class:`CSYMB` object")
               ]),

        Method('GetColSymbol_MVIEW', module='geoengine.map', version='9.2.0',
               availability=Availability.PUBLIC, 
               doc="Get an existing colored symbol object from the view.",
               notes="This method returns a cached object owned by the :class:`MVIEW` and will be destroyed automatically when the :class:`MVIEW` is disposed",
               return_type="CSYMB",
               return_doc=":class:`CSYMB` object",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number")
               ]),

        Method('DATALINKD_MVIEW', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Add a Data Link Display (:class:`DATALINKD`) object to the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('datalinkd', type="DATALINKD"),
                   Parameter('name', type=Type.STRING,
                             doc="Name Maximum length is :def_val:`MVIEW_NAME_LENGTH`")
               ]),

        Method('GetDATALINKD_MVIEW', module='geoengine.map', version='9.2.0',
               availability=Availability.PUBLIC, 
               doc="Get an existing Data Link Display (:class:`DATALINKD`) object from the view.",
               notes="This method returns a cached object owned by the :class:`MVIEW` and will be destroyed automatically when the :class:`MVIEW` is disposed",
               return_type="DATALINKD",
               return_doc=":class:`DATALINKD` object",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number")
               ]),

        Method('EasyMaker_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Used for GX makers which use both maps and databases.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('name', type=Type.STRING,
                             doc="Maker name, used in menu prompt"),
                   Parameter('groups', type=Type.STRING,
                             doc='INI groups (terminate each with a ";")')
               ]),

        Method('EMFObject_MVIEW', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Add an EMF file data object to the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Min X"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Min Y"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Max Y"),
                   Parameter('file', type=Type.STRING,
                             doc="EMF File holding data")
               ]),

        Method('ExternalStringObject_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add an external string data object to the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Min X"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Min Y"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Max Y"),
                   Parameter('name', type=Type.STRING,
                             doc="Name of external object"),
                   Parameter('cl', type=Type.STRING,
                             doc="Class of external object"),
                   Parameter('data', type=Type.STRING,
                             doc="String data of external object")
               ]),

        Method('Link_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Make a link to a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('db', type="DB",
                             doc="Database handle"),
                   Parameter('name', type=Type.STRING,
                             doc="Link name")
               ]),

        Method('Maker_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Generates a Maker for the database and/or map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('db', type=Type.INT32_T,
                             doc="Database required? (0 = No, 1 = Yes)"),
                   Parameter('map', type=Type.INT32_T,
                             doc="Map required?      (0 = No, 1 = Yes)"),
                   Parameter('prog', type=Type.STRING,
                             doc="Program name"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`MAKER`"),
                   Parameter('name', type=Type.STRING,
                             doc="Maker name, used in menu prompt"),
                   Parameter('groups', type=Type.STRING,
                             doc='INI groups (terminate each with a ";")')
               ]),

        Method('Meta_MVIEW', module='geoengine.map', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Store Metadata in a group",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('meta', type="META",
                             doc=":class:`META` object"),
                   Parameter('name', type=Type.STRING,
                             doc="Menu name of Object")
               ]),

        Method('VOXD_MVIEW', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Add a Voxel Display (:class:`VOXD`) object to the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('voxd', type="VOXD"),
                   Parameter('name', type=Type.STRING,
                             doc="Name Maximum length is :def_val:`MVIEW_NAME_LENGTH`")
               ]),

        Method('GetVOXD_MVIEW', module='geoengine.map', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Get an existing :class:`VOXD` object from the view.",
               notes="This method returns a cached object owned by the :class:`MVIEW` and will be destroyed automatically when the :class:`MVIEW` is disposed",
               return_type="VOXD",
               return_doc=":class:`VOXD` object",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number")
               ]),

        Method('DrawVectorVoxelVectors_MVIEW', module='geoengine.map', version='7.6.0',
               availability=Availability.PUBLIC, 
               doc="Display vectors from a vector voxel in the view.",
               notes="This will result in a :class:`VECTOR3D` group object within the view",
               return_type=Type.VOID,
               return_doc="Each data value in a vector voxel contains X, Y and Z components of a vector. The amplitudes do NOT necessarily correspond to the spatial size of the voxel.",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vox', type="VOX"),
                   Parameter('group', type=Type.STRING,
                             doc="View group name Maximum length is :def_val:`MVIEW_NAME_LENGTH`"),
                   Parameter('itr', type="ITR",
                             doc="Image transform - must contain zones"),
                   Parameter('scale_factor', type=Type.DOUBLE,
                             doc="Vector length scale factor - w.r.t. the voxel minimum horizontal cell size (default 1)"),
                   Parameter('height_base_ratio', type=Type.DOUBLE,
                             doc="Ratio of the vector cone height to its base (default 4)"),
                   Parameter('max_base_size_ratio', type=Type.DOUBLE,
                             doc="Ratio of maximum base size to minimum horizontal cell size (default 0.25)"),
                   Parameter('cutoff_value', type=Type.DOUBLE,
                             doc="Cutoff value - do not plot vectors with amplitudes less than this value (:def_val:`rDUMMY` or 0 to plot all)"),
                   Parameter('max_vectors', type=Type.INT32_T,
                             doc="Maximum number of vectors - decimate as required to reduce (:def_val:`iDUMMY` to plot all)")
               ]),

        Method('GetVECTOR3D_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Get an existing :class:`VECTOR3D` object from the view.",
               notes="This method returns a cached object owned by the :class:`MVIEW` and will be destroyed automatically when the :class:`MVIEW` is disposed",
               return_type="VECTOR3D",
               return_doc=":class:`VECTOR3D` object",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number")
               ]),

        Method('DrawVectors3D_MVIEW', module='geoengine.map', version='8.0.1',
               availability=Availability.PUBLIC, 
               doc="Display vectors in the view.",
               return_type=Type.VOID,
               return_doc="Plot vectors as cones scaled in area to the maximum amplitude",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.STRING,
                             doc="View group name Maximum length is :def_val:`MVIEW_NAME_LENGTH`"),
                   Parameter('vv_x', type="VV",
                             doc="X locations"),
                   Parameter('vv_y', type="VV",
                             doc="Y locations"),
                   Parameter('vv_z', type="VV",
                             doc="Z locations"),
                   Parameter('vv_vx', type="VV",
                             doc="Vector X component"),
                   Parameter('vv_vy', type="VV",
                             doc="Vector Y component"),
                   Parameter('vv_vz', type="VV",
                             doc="Vector Z component"),
                   Parameter('itr', type="ITR",
                             doc="Image transform - must contain zones"),
                   Parameter('scale_for_max_vector', type=Type.DOUBLE,
                             doc="""
                             Scale factor for the longest vector in map units / vector units. Vector lengths for the rest of the vectors scale by the square root of the vector amplitudes.
                             This results in the apparent (viewed) area of the vector being proportional to the amplitude.
                             """),
                   Parameter('height_base_ratio', type=Type.DOUBLE,
                             doc="Ratio of the vector cone height to its base (default 4)"),
                   Parameter('max_base_size_ratio', type=Type.DOUBLE,
                             doc="Maximum base size in view units. Leave blank (dummy) for no limit. If applied this can make larger vectors skinnier, but does not reduce the length, so they don't obscure other vectors as much.")
               ])
    ],
    'Group Methods': [

        Method('SetGroupITR_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Set group :class:`ITR`",
               notes="""
               A group :class:`ITR` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
               Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
               to refresh the objects.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number"),
                   Parameter('itr', type="ITR")
               ]),

        Method('GetGroupITR_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Get group :class:`ITR`",
               notes="""
               A group :class:`ITR` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
               Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
               to refresh the objects.
               """,
               return_type="ITR",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number")
               ]),

        Method('iGroupITRExists_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Determine if group :class:`ITR` exists.",
               notes="""
               A group :class:`ITR` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
               Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
               to refresh the objects.
               """,
               return_type=Type.INT32_T,
               return_doc="1 - :class:`ITR` exists, 0 - :class:`ITR` does not exist",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number")
               ]),

        Method('DeleteGroupITR_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Deletes existing :class:`ITR` associated with a group.",
               notes="""
               A group :class:`ITR` associate a color distribution with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
               Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
               to refresh the objects.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number")
               ]),

        Method('SetGroupTPAT_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Set group :class:`TPAT`",
               notes="""
               A group :class:`TPAT` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
               Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
               to refresh the objects.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number"),
                   Parameter('tpat', type="TPAT")
               ]),

        Method('GetGroupTPAT_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Get group :class:`TPAT`",
               notes="""
               A group :class:`TPAT` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
               Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
               to refresh the objects.
               """,
               return_type="TPAT",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number")
               ]),

        Method('iGroupTPATExists_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Determine if group :class:`TPAT` exists.",
               notes="""
               A group :class:`TPAT` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
               Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
               to refresh the objects.
               """,
               return_type=Type.INT32_T,
               return_doc="1 - :class:`TPAT` exists, 0 - :class:`TPAT` does not exist",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number")
               ]),

        Method('DeleteGroupTPAT_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Deletes existing :class:`TPAT` associated with a group.",
               notes="""
               A group :class:`TPAT` associate a thematic color map with mixed vector groups (e.g. Drillhole Lithology tubes) groups. Used by legend UI support in 3D.
               Note that modifying this information does not currently change the group contents and a group needs to be regenerated (e.g. with maker) 
               to refresh the objects.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number")
               ]),

        Method('iGroupStorageExists_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Determine if generic storage associated with a group exists.",
               notes='External API users should not use storage names starting with "Geosoft"',
               return_type=Type.INT32_T,
               return_doc="1 - storage exists, 0 - storage does not exist",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number"),
                   Parameter('storage_name', type=Type.STRING,
                             doc="Storage name")
               ]),

        Method('ReadGroupStorage_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Reads existing generic storage associated with a group into an in-memory :class:`BF`.",
               notes='External API users should not use storage names starting with "Geosoft"',
               return_type="BF",
               return_doc=":class:`BF` Object",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number"),
                   Parameter('storage_name', type=Type.STRING,
                             doc="Storage name")
               ]),

        Method('DeleteGroupStorage_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Deletes existing generic storage associated with a group.",
               notes='External API users should not use storage names starting with "Geosoft"',
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number"),
                   Parameter('storage_name', type=Type.STRING,
                             doc="Storage name")
               ]),

        Method('WriteGroupStorage_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Open generic existing storage associated with a group for reading.",
               notes='External API users should not use storage names starting with "Geosoft"',
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number"),
                   Parameter('storage_name', type=Type.STRING,
                             doc="Storage name"),
                   Parameter('bf', type="BF",
                             doc=":class:`BF` to read from")
               ]),

        Method('CopyMarkedGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copies all marked groups from one view into another view",
               notes="""
               Projections in source and destination views are used to copy the
               entities. Entities are clipped by the destination view's clipping
               region.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mvie_ws', type="MVIEW",
                             doc="Source :class:`MVIEW`"),
                   Parameter('mvie_wd', type="MVIEW",
                             doc="Destination :class:`MVIEW`")
               ]),

        Method('CopyRawMarkedGroups_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Copies all marked groups raw from one view into another",
               notes="The projections, and clipping is completly ignored.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mvie_ws', type="MVIEW",
                             doc="Source :class:`MVIEW`"),
                   Parameter('mvie_wd', type="MVIEW",
                             doc="Destination :class:`MVIEW`")
               ]),

        Method('CRCGroup_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Compute CRC for a group.",
               return_type="CRC",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('name', type=Type.STRING,
                             doc="Group name"),
                   Parameter('crc', type="CRC",
                             doc="CRC to start (use :def_val:`CRC_INIT_VALUE`)")
               ]),

        Method('DeleteGroup_MVIEW', module='geoengine.map', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Delete a group.",
               notes="Does nothing if the group does not already exist.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('group', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('DelMarkedGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Delete marked groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle")
               ]),

        Method('GetGroupExtent_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get extent of a group in a view",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('group_name', type=Type.STRING,
                             doc="Group name"),
                   Parameter('xmin', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum X, returned"),
                   Parameter('ymin', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum Y, returned"),
                   Parameter('xmax', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum X, returned"),
                   Parameter('ymax', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum Y, returned"),
                   Parameter('unit', type=Type.INT32_T,
                             doc=":def:`MVIEW_UNIT`")
               ]),

        Method('GetGroupTransparency_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the transparency value of group",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('group_name', type=Type.STRING,
                             doc="Group name"),
                   Parameter('trans', type=Type.DOUBLE, is_ref=True,
                             doc="Transparency (1.0 - Opaque, 0.0 - Transparent)")
               ]),

        Method('GroupToPLY_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Save all polygons in group into :class:`PLY` obj.",
               notes="""
               The coordinates will be in the working coordinate system
               of the view.  The SetWorkingIPJ_MVIEW method can be used
               to change the working coordinate system. This function will
               return an empty :class:`PLY` if the group is hidden.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('name', type=Type.STRING,
                             doc="Group name"),
                   Parameter('pply', type="PLY",
                             doc=":class:`PLY` to add to")
               ]),

        Method('HideMarkedGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Hide/Show marked groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`MVIEW_HIDE`")
               ]),

        Method('HideShadow2DInterpretations_MVIEW', module='geoengine.map', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Hide/Show 2d shadow interpretations.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`MVIEW_HIDE`")
               ]),

        Method('iExistGroup_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Checks to see if a group exists.",
               return_type=Type.INT32_T,
               return_doc="""
               0  - group does not exist.
               1  - group exists.
               """,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('name', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('IGenNewGroupName_MVIEW', module='geoengine.map', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="""
               Generate the name of a group from a base name that
               is new. (always unique and won't overwrite existing
               objects).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('group', type=Type.STRING,
                             doc="Base Name of group"),
                   Parameter('new_name', type=Type.STRING, is_ref=True, size_of_param='length',
                             doc="New Name of group"),
                   Parameter('length', type=Type.INT32_T, default_length='STR_GROUP',
                             doc="Size of buffer.")
               ]),

        Method('iIsGroup_MVIEW', module='geoengine.map', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Query a status or characteristic of a group",
               return_type=Type.INT32_T,
               return_doc="TRUE or FALSE (1 or 0)",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('group', type=Type.STRING,
                             doc="Group name"),
                   Parameter('what', type=Type.INT32_T,
                             doc=":def:`MVIEW_IS`")
               ]),

        Method('iIsGroupEmpty_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Is the group empty?",
               return_type=Type.INT32_T,
               return_doc="TRUE or FALSE (1 or 0)",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('group', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('iIsMovable_MVIEW', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Is this view movable?",
               notes="""
               Views are always physically movable in the API, this
               flag is for preventing accidental moving in the :class:`GUI`.
               By default views are not movable.
               """,
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('mview', type="MVIEW")
               ]),

        Method('iIsVisible_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Is this view visible?",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('mview', type="MVIEW")
               ]),

        Method('iListGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a list of the groups in a view.",
               return_type=Type.INT32_T,
               return_doc="Number of groups in the list",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('lst', type="LST",
                             doc="List"),
                   Parameter('flag', type=Type.INT32_T,
                             doc=":def:`MVIEW_GROUP_LIST`")
               ]),

        Method('iRenderOrder_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Query the view render order",
               notes="Views with lower numbers should render first, :def_val:`iDUMMY` is undefined",
               return_type=Type.INT32_T,
               return_doc="Render order",
               parameters = [
                   Parameter('mview', type="MVIEW")
               ]),

        Method('MarkAllGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Mark or unmark all groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('mark', type=Type.INT32_T,
                             doc="0 - unmark, 1 - mark")
               ]),

        Method('MarkEmptyGroups_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Mark/unmark all empty groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('mark', type=Type.INT32_T,
                             doc="0 - unmark, 1 - mark")
               ]),

        Method('MarkGroup_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Mark or unmark a specific group",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('name', type=Type.STRING,
                             doc="Group name"),
                   Parameter('mark', type=Type.INT32_T,
                             doc="0 - unmark, 1 - mark")
               ]),

        Method('MoveGroupBackward_MVIEW', module='geoengine.map', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Move the group backward one position (render sooner).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('MoveGroupForward_MVIEW', module='geoengine.map', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Move the group forward one position (render later).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('MoveGroupToBack_MVIEW', module='geoengine.map', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Move the group to the back (render first).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('MoveGroupToFront_MVIEW', module='geoengine.map', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Move the group to the front (render last).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('RenameGroup_MVIEW', module='geoengine.map', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Rename a group.",
               notes="Does nothing if the group does not already exist.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('old', type=Type.STRING,
                             doc="Old group name"),
                   Parameter('new', type=Type.STRING,
                             doc="New group name")
               ]),

        Method('SetGroupMoveable_MVIEW', module='geoengine.map', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Set the movable attribute of a group.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('group', type=Type.STRING,
                             doc="Group name"),
                   Parameter('move', type=Type.INT32_T,
                             doc="0 - not movable, 1 - movable")
               ]),

        Method('SetGroupTransparency_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the transparency value of group",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('group_name', type=Type.STRING,
                             doc="Group name"),
                   Parameter('trans', type=Type.DOUBLE,
                             doc="Transparency  (1.0 - Opaque, 0.0 - Transparent)")
               ]),

        Method('SetMarkMoveable_MVIEW', module='geoengine.map', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Set the movable attribute of marked groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('move', type=Type.INT32_T,
                             doc="0 - not movable, 1 - movable")
               ]),

        Method('SetMovability_MVIEW', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Set the view movability",
               notes="""
               Views are always physically movable in the API, this
               flag is for preventing accidental moving in the :class:`GUI`.
               By default views are not movable.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('flag', type=Type.INT32_T,
                             doc=":def:`GEO_BOOL`")
               ]),

        Method('SetRenderOrder_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set the view render order",
               notes="Views with lower numbers should render first, :def_val:`iDUMMY` is undefined",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('order', type=Type.INT32_T,
                             doc="Render order")
               ]),

        Method('SetVisibility_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set the view visibility",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('flag', type=Type.INT32_T,
                             doc=":def:`GEO_BOOL`")
               ]),

        Method('StartGroup_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Start a group.",
               notes="""
               Line and fill colors and thickness must be set
               before drawing to a group.
               
               If the group name is NULL, output will be sent to
               the primary group stream and the :def:`MVIEW_GROUP` is
               ignored.
               
               Group names must be different from view names.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('name', type=Type.STRING,
                             doc="Group name, can be NULL, Maximum length is :def_val:`MVIEW_NAME_LENGTH`"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`MVIEW_GROUP`")
               ]),

        Method('GetGroupGUID_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Gets a GUID of a group in the :class:`MVIEW`.",
               notes="If a GUID was never queried a new one will be assigned and the map will be modified. Only if the map is saved will this value then persist.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` Object"),
                   Parameter('group', type=Type.INT32_T,
                             doc="Group number"),
                   Parameter('guid', type=Type.STRING, is_ref=True, size_of_param='guid_size',
                             doc="GUID"),
                   Parameter('guid_size', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of GUID buffer.")
               ]),

        Method('iFindGroupByGUID_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Find a Group by name.",
               return_type=Type.INT32_T,
               return_doc="Group Number.",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('guid', type=Type.STRING,
                             doc="GUID")
               ])
    ],
    'Projection': [

        Method('_SetWorkingIPJ_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the working projection of the view.",
               notes="""
               The working projection is the coordinate system of coordinates drawn to
               the view.  The working coordinate system can be different than the view
               coordinate system, in which case the coordinates are re-projected to the
               view coordinate system before they are placed in the view.
               """,
               see_also=":func:`ModePJ_MVIEW` to control use of the working projection.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('ipj', type="IPJ",
                             doc="The input projection")
               ]),

        Method('ClearESRILDTs_MVIEW', module='geoengine.map', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Clear ESRI local datum transformations currently in use.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View")
               ]),

        Method('iIsProjectionEmpty_MVIEW', module='geoengine.map', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns 1 if the view projection and view user projection are both empty (undefined).",
               notes="""
               Use, for instance, to see if the map view contains projection information. The first time you add data that
               has projection information you should set up an empty view projection so that subsequent data added with a different
               projection is properly displayed in relation to the initial data.
               """,
               return_type=Type.INT32_T,
               return_doc="1 if the view projection and view user projection are both empty.",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object")
               ]),

        Method('GetIPJ_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the projection of the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` in which to place the view :class:`IPJ`")
               ]),

        Method('GetUserIPJ_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the user projection of the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` in which to place the view :class:`IPJ`")
               ]),

        Method('ModePJ_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the working projection mode",
               notes="""
               This controls how your coordinates and attributes will be interpreted.
               A working projection must be set useing SetWorkingIPJ_MVIEW for this
               method to have any effect.
               """,
               see_also="SetWorkingIPJ",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`MVIEW_PJ`")
               ]),

        Method('rNorth_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns North direction at center of view.",
               notes="""
               North is calculated from the :class:`IPJ` North direction.
               It will be :def_val:`rDUMMY` if :class:`IPJ` is unknown.
               """,
               return_type=Type.DOUBLE,
               return_doc="North direction id deg. azimuth relative to view Y.",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object")
               ]),

        Method('SetIPJ_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the projection of the view.",
               notes="""
               This function also sets the User :class:`IPJ`,
               and automatically clears the WARP before doing so.
               This would be equivalent to calling :func:`_ClearWarp_IPJ'
               followed by :func:`SetUserIPJ_MVIEW` on the view.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` to place in the view")
               ]),

        Method('SetUserIPJ_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the user projection of the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` to place in the view")
               ])
    ],
    'Render': [

        Method('iGet3DGroupFlags_MVIEW', module='geoengine.map', version='9.1.0',
               availability=Availability.PUBLIC, 
               doc="Get a 3D geometry group's 3D rendering flags.",
               return_type=Type.INT32_T,
               return_doc="Combination of :def:`MVIEW_3D_RENDER` flags or 0",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group_num', type=Type.INT32_T,
                             doc="Group number")
               ]),

        Method('Set3DGroupFlags_MVIEW', module='geoengine.map', version='9.1.0',
               availability=Availability.PUBLIC, 
               doc="Set a 3D geometry group's 3D rendering flags.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group_num', type=Type.INT32_T,
                             doc="Group number"),
                   Parameter('flags', type=Type.INT32_T,
                             doc="Combination of :def:`MVIEW_3D_RENDER` flags or 0")
               ]),

        Method('_GetGroupFreezeScale_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get a scale freezing value for the group (:def_val:`rDUMMY` for disabled).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group_num', type=Type.INT32_T,
                             doc="Group number"),
                   Parameter('scale', type=Type.DOUBLE, is_ref=True,
                             doc="Variable to fill with freeze scale")
               ]),

        Method('_SetFreezeScale_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Set a scale freezing value into stream (:def_val:`rDUMMY` for disabled).",
               notes="Objects written after this will override any scale freezing set for the group",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="Freeze Scale value")
               ]),

        Method('_SetGroupFreezeScale_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Set a scale freezing value for the group (:def_val:`rDUMMY` for disabled).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group_num', type=Type.INT32_T,
                             doc="Group number"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="Variable to fill with freeze scale")
               ]),

        Method('iFindGroup_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Find a Group by name.",
               return_type=Type.INT32_T,
               return_doc="Group Number.",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group_name', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('IGroupName_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get a group name",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('group_num', type=Type.INT32_T,
                             doc="Group number, error if not valid"),
                   Parameter('group_name', type=Type.STRING, is_ref=True, size_of_param='length',
                             doc="Group Name"),
                   Parameter('length', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Maximum name length")
               ]),

        Method('Render_MVIEW', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, no_gxh=True, 
               doc="Render a specified area of view onto a Windows DC handle",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` Handle"),
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
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Area X minimum"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Area Y minimum"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Area X maximum"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Area Y maximum")
               ])
    ],
    'Utility Drawing': [

        Method('_SetUFac_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the unit conversion of a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View to set UFac to"),
                   Parameter('hdc', type=Type.DOUBLE,
                             doc="New UFac value")
               ]),

        Method('AxisX_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw an X axis",
               notes="All coordinates are in view units.",
               see_also="rOptimumTick_MVIEW",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('y_loc', type=Type.DOUBLE,
                             doc="Y location in view units"),
                   Parameter('left', type=Type.DOUBLE,
                             doc="Left  X"),
                   Parameter('right', type=Type.DOUBLE,
                             doc="Right X"),
                   Parameter('major_tick', type=Type.DOUBLE,
                             doc="Major tick interval"),
                   Parameter('minor_tick', type=Type.DOUBLE,
                             doc="Minor tick interval (half size of major)"),
                   Parameter('tick_size', type=Type.DOUBLE,
                             doc="Tick size in view units (negative for down ticks)")
               ]),

        Method('AxisY_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a  Y axis",
               notes="All coordinates are in view units.",
               see_also="rOptimumTick_MVIEW",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('x_loc', type=Type.DOUBLE,
                             doc="X location in view units"),
                   Parameter('bottom', type=Type.DOUBLE,
                             doc="Bottom Y"),
                   Parameter('top', type=Type.DOUBLE,
                             doc="Top    Y"),
                   Parameter('major_tick', type=Type.DOUBLE,
                             doc="Major tick interval"),
                   Parameter('minor_tick', type=Type.DOUBLE,
                             doc="Minor tick interval (half size of major)"),
                   Parameter('tick_size', type=Type.DOUBLE,
                             doc="Tick size in view units (negative for left ticks)")
               ]),

        Method('Grid_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a grid in the current window",
               notes="""
               The grid will be drawn in the current window specified
               by the last SetWindow call.
               """,
               see_also=":func:`AxisX_MVIEW`, :func:`AxisY_MVIEW`, :func:`OptimumTick_MVIEW`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('x_inc', type=Type.DOUBLE,
                             doc="X grid increment"),
                   Parameter('y_inc', type=Type.DOUBLE,
                             doc="Y grid increment"),
                   Parameter('dx', type=Type.DOUBLE,
                             doc="dX dot increment/cross X size"),
                   Parameter('dy', type=Type.DOUBLE,
                             doc="dY dot increment/cross Y size"),
                   Parameter('grid_type', type=Type.INT32_T,
                             doc=":def:`MVIEW_GRID`")
               ]),

        Method('LabelFid_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Label fiducials on a profile",
               notes="""
               A 1mm long vertical tick is drawn at the place
               where a label is present. The label is drawn
               below the tick.
               
               The incoming X :class:`VV` is used to define the place for
               label.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('fid_start', type=Type.DOUBLE,
                             doc="Fiducial start"),
                   Parameter('fid_incr', type=Type.DOUBLE,
                             doc="Fiducial increment"),
                   Parameter('interval', type=Type.DOUBLE,
                             doc="Fiducial label interval, default 100.0"),
                   Parameter('y_loc', type=Type.DOUBLE,
                             doc="Y location in view unit"),
                   Parameter('y_scale', type=Type.DOUBLE,
                             doc="Y scale")
               ]),

        Method('LabelX_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Label annotations on the X axis",
               notes="""
               Label bounding will justify edge labels to be inside
               the bar limits. But bounding does not apply if
               labels are drawn vertically (top right or top left)
               """,
               see_also=":func:`AxisX_MVIEW`, :func:`AxisY_MVIEW`, :func:`OptimumTick_MVIEW`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('l_loc', type=Type.DOUBLE,
                             doc="Y location in view units"),
                   Parameter('left', type=Type.DOUBLE,
                             doc="Left  X"),
                   Parameter('right', type=Type.DOUBLE,
                             doc="Right X"),
                   Parameter('lable_int', type=Type.DOUBLE,
                             doc="Label interval"),
                   Parameter('just', type=Type.INT32_T,
                             doc=":def:`MVIEW_LABEL_JUST`"),
                   Parameter('bound', type=Type.INT32_T,
                             doc=":def:`MVIEW_LABEL_BOUND`"),
                   Parameter('orient', type=Type.INT32_T,
                             doc=":def:`MVIEW_LABEL_ORIENT`")
               ]),

        Method('LabelY_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Label annotations on the Y axis",
               notes="""
               Label bounding will justify edge labels to be inside
               the bar limits. But bounding does not apply if
               labels are drawn vertically (top right or top left)
               """,
               see_also=":func:`AxisX_MVIEW`, :func:`AxisY_MVIEW`, :func:`OptimumTick_MVIEW`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X location in view units"),
                   Parameter('bottom', type=Type.DOUBLE,
                             doc="Bottom Y"),
                   Parameter('top', type=Type.DOUBLE,
                             doc="Top    Y"),
                   Parameter('lable_int', type=Type.DOUBLE,
                             doc="Label interval"),
                   Parameter('just', type=Type.INT32_T,
                             doc=":def:`MVIEW_LABEL_JUST`"),
                   Parameter('bound', type=Type.INT32_T,
                             doc=":def:`MVIEW_LABEL_BOUND`"),
                   Parameter('orient', type=Type.INT32_T,
                             doc=":def:`MVIEW_LABEL_ORIENT`")
               ]),

        Method('OptimumTick_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return a default optimum tick interval",
               return_type=Type.VOID,
               parameters = [
                   Parameter('min', type=Type.DOUBLE,
                             doc="Minimum of range"),
                   Parameter('max', type=Type.DOUBLE,
                             doc="Maximum"),
                   Parameter('sep', type=Type.DOUBLE, is_ref=True,
                             doc="Optimum interval")
               ])
    ],
    'View': [

        Method('Create_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create :class:`MVIEW`.",
               notes="""
               View scaling is set to mm on the map and the view
               origin is set to the map origin.
               """,
               return_type="MVIEW",
               return_doc=":class:`MVIEW`, aborts if creation fails",
               parameters = [
                   Parameter('map', type="MAP",
                             doc=":class:`MAP` on which to place the view"),
                   Parameter('name', type=Type.STRING,
                             doc="View name (maximum :def_val:`MVIEW_NAME_LENGTH`)"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`MVIEW_OPEN`")
               ]),

        Method('CreateCrookedSection_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Creates a new crooked section view.",
               notes="""
               A crooked section is a section running vertically beneath
               a path of (X, Y) locations, like a river. This view supports
               linking to other plan, section, or 3D views.
               The data view coordinates are set up so that vertical coordinate
               corresponds to elevation, and the X coordinate is the distance along
               the crooked feature, beginning at zero on the left, but the
               status bar will show the true (X, Y, Z) location.
               
               If the scale is set to :def_val:`rDUMMY`, then it will be calculated so that
               the points will all fit horizontally.
               """,
               return_type="MVIEW",
               return_doc=":class:`MVIEW`, aborts if creation fails",
               parameters = [
                   Parameter('map', type="MAP",
                             doc=":class:`MAP` Object"),
                   Parameter('ipj', type="IPJ",
                             doc="Geographic projection of input X, Y locations below (without orientation)"),
                   Parameter('name', type=Type.STRING,
                             doc="View Name"),
                   Parameter('x0', type=Type.DOUBLE,
                             doc="Base view bottom left corner X (mm)"),
                   Parameter('y0', type=Type.DOUBLE,
                             doc="Base view bottom left corner Y (mm)"),
                   Parameter('xs', type=Type.DOUBLE,
                             doc="Base view size in X (mm)"),
                   Parameter('ys', type=Type.DOUBLE,
                             doc="Base view size in Y (mm)"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="Map horizontal scale (X-axis)"),
                   Parameter('v_ex', type=Type.DOUBLE,
                             doc="Vertical exaggeration (1.0 is normal, must be >0.0)"),
                   Parameter('dist0', type=Type.DOUBLE,
                             doc="Starting distance at the left side of the view."),
                   Parameter('elev', type=Type.DOUBLE,
                             doc="Elevation at TOP of the view"),
                   Parameter('v_vxs', type="VV",
                             doc="Cumulative distances along the secton"),
                   Parameter('v_vx', type="VV",
                             doc="True X locations along the section"),
                   Parameter('v_vy', type="VV",
                             doc="True Y locations along the section")
               ]),

        Method('CreateCrookedSectionDataProfile_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Creates a new crooked section data profile view.",
               notes="""
               This is the same as :func:`CreateCrookedSection_MVIEW`, except that the
               vertical axis plots a data value, not elevation, and allows for
               logarithmic scaling.
               
               See Also: :func:`CreateCrookedSection_MVIEW`.
               """,
               return_type="MVIEW",
               return_doc=":class:`MVIEW`, aborts if creation fails",
               parameters = [
                   Parameter('map', type="MAP",
                             doc=":class:`MAP` Object"),
                   Parameter('ipj', type="IPJ",
                             doc="Geographic projection of input X, Y locations below (without orientation)"),
                   Parameter('name', type=Type.STRING,
                             doc="View Name"),
                   Parameter('x0', type=Type.DOUBLE,
                             doc="Base view bottom left corner X (mm)"),
                   Parameter('y0', type=Type.DOUBLE,
                             doc="Base view bottom left corner Y (mm)"),
                   Parameter('xs', type=Type.DOUBLE,
                             doc="Base view size in X (mm)"),
                   Parameter('ys', type=Type.DOUBLE,
                             doc="Base view size in Y (mm)"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="Map horizontal scale (X-axis)"),
                   Parameter('dist0', type=Type.DOUBLE,
                             doc="Starting distance at the left side of the view."),
                   Parameter('min_z', type=Type.DOUBLE,
                             doc="Data value at bottom of the view"),
                   Parameter('max_z', type=Type.DOUBLE,
                             doc="Data value at top of the view"),
                   Parameter('log_z', type=Type.INT32_T,
                             doc="Make logarithmic Y-axis (0:No, 1:Yes)?"),
                   Parameter('v_vxs', type="VV",
                             doc="Cumulative distances along the secton"),
                   Parameter('v_vx', type="VV",
                             doc="True X locations along the section"),
                   Parameter('v_vy', type="VV",
                             doc="True Y locations along the section")
               ]),

        Method('Destroy_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`MVIEW` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` Handle")
               ]),

        Method('Extent_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the view extents",
               notes="""
               The CLIP region is the current view window or the limits
               of the current clip polygon.
               
               If :def_val:`MVIEW_EXTENT_ALL` is requested and the view has no groups, the
               clip extents are returned.
               
               If clip extents are requested and there are no clip extents, an
               area 0.0,0.0 1.0,1.0 is returned.
               
               The :def_val:`MVIEW_EXTENT_VISIBLE` flag will return the union of the :def_val:`MVIEW_EXTENT_CLIP` area and the
               extents of all non-masked visible groups in the view.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('what', type=Type.INT32_T,
                             doc=":def:`MVIEW_EXTENT`"),
                   Parameter('unit', type=Type.INT32_T,
                             doc=":def:`MVIEW_EXTENT_UNIT`"),
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="X minimum"),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="Y minimum"),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="X maximum"),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="Y maximum")
               ]),

        Method('GetMAP_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`MAP` of the view.",
               return_type="MAP",
               return_doc="The :class:`MAP` of the View.",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View handle")
               ]),

        Method('GetREG_MVIEW', module='geoengine.map', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`REG` of the view.",
               return_type="REG",
               return_doc="The :class:`REG` of the View.",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View handle")
               ]),

        Method('IGetName_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the name of a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View handle"),
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='length',
                             doc="View name returned"),
                   Parameter('length', type=Type.INT32_T, default_length='STR_VIEW',
                             doc="View name string size")
               ]),

        Method('GetGUID_MVIEW', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Gets the GUID of the :class:`MVIEW`.",
               notes="If a GUID was never queried a new one will be assigned and the map will be modified. Only if the map is saved will this value then persist.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` Object"),
                   Parameter('guid', type=Type.STRING, is_ref=True, size_of_param='guid_size',
                             doc="GUID"),
                   Parameter('guid_size', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of GUID buffer.")
               ])
    ],
    'View Control': [

        Method('_PlotToView_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a plot coordinate in mm to a VIEW coordinate.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="X in plot mm, returned in View coordinates"),
                   Parameter('y', type=Type.DOUBLE, is_ref=True,
                             doc="Y in plot mm, returned in View coordinates")
               ]),

        Method('_SetThinRes_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set polyline/polygon thinning resolution",
               notes="""
               The thinning resolution controls the removal of
               redundant points from polylines and polygons.  Points
               that deviate from a straight line by less than the
               thinning resolution are removed.  This can significantly
               reduce the size of a :class:`MAP` file.
               We recommend that you set the thinning resolution to
               0.02 mm.
               
               By default, the thinning resolution is set to 0.05mm.
               
               Set resolution to 0.0 to remove colinear points only.
               
               To turn off thinning after turning it on, call
               SetThinRes_MVIEW with a resolution of -1.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('thin', type=Type.DOUBLE,
                             doc="Thinning resolution in mm, -1.0 to turn off.")
               ]),

        Method('_ViewToPlot_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a VIEW coordinate to a plot coordinate in mm.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="X in View, returned in mm from plot origin"),
                   Parameter('y', type=Type.DOUBLE, is_ref=True,
                             doc="Y in View, returned in mm from plot origin")
               ]),

        Method('BestFitWindow_MVIEW', module='geoengine.map', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="""
               Fit an area in ground coordinates centered to an area in mm on map or vise versa
               keeping X and Y scales the same.
               """,
               notes="""
               X and Y scales will be redefined and units will remain unchanged.
               The final X and Y ranges (if changed) are returned.
               """,
               see_also=":func:`FitWindow_MVIEW`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('m_min_x', type=Type.DOUBLE, is_ref=True,
                             doc="X minimum (mm) of the area in map relative to map origin"),
                   Parameter('m_min_y', type=Type.DOUBLE, is_ref=True,
                             doc="Y minimum  .."),
                   Parameter('m_max_x', type=Type.DOUBLE, is_ref=True,
                             doc="X maximum  .."),
                   Parameter('m_max_y', type=Type.DOUBLE, is_ref=True,
                             doc="Y maximum  .."),
                   Parameter('v_min_x', type=Type.DOUBLE, is_ref=True,
                             doc="Min X in ground coordinate to fit to the area defined above"),
                   Parameter('v_min_y', type=Type.DOUBLE, is_ref=True,
                             doc="Min Y in ground coordinate .."),
                   Parameter('v_max_x', type=Type.DOUBLE, is_ref=True,
                             doc="Max X in ground coordinate .."),
                   Parameter('v_max_y', type=Type.DOUBLE, is_ref=True,
                             doc="Max Y in ground coordinate .."),
                   Parameter('fit_view', type=Type.INT32_T,
                             doc=":def:`MVIEW_FIT`")
               ]),

        Method('FitMapWindow3D_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the 2D view window for a 3D view.",
               notes="""
               3D views are placed in 2D maps within a 2D mapping window
               that is analgous to a 2D View.  This allows all 2D functions
               (such as changing a view location and size) to treat a 3D
               view just like a 2D view.
               
               The :func:`FitMapWindow3D_MVIEW` function allows you to
               locate and set the "apparent" 2D mapping of a 3D view on
               the map. An intial map window is established
               as specified on the map, and the view scaling is
               established to fit the specified area within that
               map area.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View (3D)"),
                   Parameter('m_min_x', type=Type.DOUBLE,
                             doc="X minimum (mm) of the area in map relative to map origin"),
                   Parameter('m_min_y', type=Type.DOUBLE,
                             doc="Y minimum  .."),
                   Parameter('m_max_x', type=Type.DOUBLE,
                             doc="X maximum  .."),
                   Parameter('m_max_y', type=Type.DOUBLE,
                             doc="Y maximum  .."),
                   Parameter('v_min_x', type=Type.DOUBLE,
                             doc="Min X in ground coordinate to fit to the area defined above"),
                   Parameter('v_min_y', type=Type.DOUBLE,
                             doc="Min Y in ground coordinate .."),
                   Parameter('v_max_x', type=Type.DOUBLE,
                             doc="Max X in ground coordinate .."),
                   Parameter('v_max_y', type=Type.DOUBLE,
                             doc="Max Y in ground coordinate ..")
               ]),

        Method('FitWindow_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Fit an area in ground coordinates to an area in mm on map.",
               notes="""
               X and Y scales will be redefined and the units will be set to <unknown>.
               Coordinate ranges must be greater than 0.0.
               """,
               see_also=":func:`SetWindow_MVIEW`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('m_min_x', type=Type.DOUBLE,
                             doc="X minimum (mm) of the area in map relative to map origin"),
                   Parameter('m_min_y', type=Type.DOUBLE,
                             doc="Y minimum  .."),
                   Parameter('m_max_x', type=Type.DOUBLE,
                             doc="X maximum  .."),
                   Parameter('m_max_y', type=Type.DOUBLE,
                             doc="Y maximum  .."),
                   Parameter('v_min_x', type=Type.DOUBLE,
                             doc="Min X in ground coordinate to fit to the area defined above"),
                   Parameter('v_min_y', type=Type.DOUBLE,
                             doc="Min Y in ground coordinate .."),
                   Parameter('v_max_x', type=Type.DOUBLE,
                             doc="Max X in ground coordinate .."),
                   Parameter('v_max_y', type=Type.DOUBLE,
                             doc="Max Y in ground coordinate ..")
               ]),

        Method('IGetClassName_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Get a class name.",
               notes="""
               :class:`MVIEW` class names are intended to be used to record the
               names of certain classes in the view, such as "Plane"
               for the default drawing plane.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('cl', type=Type.STRING,
                             doc="Class"),
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='length',
                             doc="Name"),
                   Parameter('length', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Maximum name length")
               ]),

        Method('MapOrigin_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the map origin from a view",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('x_origin', type=Type.DOUBLE, is_ref=True,
                             doc="Returned map origin - X"),
                   Parameter('y_origin', type=Type.DOUBLE, is_ref=True,
                             doc="Returned map origin - Y")
               ]),

        Method('ReScale_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Change the scale of a view.",
               notes="""
               The view size is multiplied by the scale factor.
               The view location will move relative to the map origin
               by the scale factor.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="Scale factor (> 0.0)")
               ]),

        Method('rGetMapScale_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the current map scale of the view",
               return_type=Type.DOUBLE,
               return_doc="The current map scale to 6 significant digits",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` Handle")
               ]),

        Method('rScaleMM_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the horizontal scale in view X units/mm",
               notes="""
               The scale factor is intended to be used by methods
               that would like to specify sizes in mm.  Examples
               would be text sizes, line thicknesses and line
               pitch.
               """,
               return_type=Type.DOUBLE,
               return_doc="Returns horizontal scale in view X units/mm",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` Handle")
               ]),

        Method('rScalePjMM_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get horizontal scale in projected user units/mm",
               notes="""
               The scale factor is intended to be used by methods
               that would like to specify sizes in mm.  Examples
               would be text sizes, line thicknesses and line
               pitch.
               Same as rScaleMM if working projection not defined
               """,
               return_type=Type.DOUBLE,
               return_doc="Returns horizontal scale in projected user units/mm",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` Handle")
               ]),

        Method('rScaleYMM_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the vertical scale in Y units/mm",
               notes="""
               The scale factor is intended to be used by methods
               that would like to specify sizes in mm.  Examples
               would be text sizes, line thicknesses and line
               pitch.
               """,
               return_type=Type.DOUBLE,
               return_doc="Returns vertical scale in view Y units/mm",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` Handle")
               ]),

        Method('ScaleAllGroup_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Scale all groups (except for GRID) in a view",
               notes="""
               X (and Y) scale is the ratio of the new dimension over
               the old dimension of a reference object. For example, if a horizontal
               straight line of 10m long becomes 20m, X scale should be 2.
               
               The view is then scaled back so that the view occupies the same
               area size as before.  The view's clip area is updated as well.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('xs', type=Type.DOUBLE,
                             doc="X scale"),
                   Parameter('ys', type=Type.DOUBLE,
                             doc="Y scale")
               ]),

        Method('ScaleWindow_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Assign view coordinates to define a window.",
               notes="""
               The provided coordinates are converted to map mm
               using the current view translation and scaling.
               SetWindow is effectively called.
               """,
               see_also=":func:`SetWindow_MVIEW`, :func:`ScaleWindow_MVIEW`, :func:`TranScale_MVIEW`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="X minimum in view coordinates"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Y minimum"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="X maximum"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Y maximum"),
                   Parameter('bot_x', type=Type.DOUBLE,
                             doc="X minimum in plot coordinates"),
                   Parameter('bot_y', type=Type.DOUBLE,
                             doc="Y minimum"),
                   Parameter('x_scal', type=Type.DOUBLE,
                             doc="Horizontal scale (view unit/plot unit in mm)"),
                   Parameter('y_scal', type=Type.DOUBLE,
                             doc="Vertical scale")
               ]),

        Method('SetClassName_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set a class name.",
               notes="""
               :class:`MVIEW` class names are intended to be used to record the
               names of certain classes in the view, such as "Plane"
               for the default drawing plane.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('cl', type=Type.STRING,
                             doc="Class"),
                   Parameter('name', type=Type.STRING,
                             doc="Name")
               ]),

        Method('SetWindow_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the view window",
               notes="""
               The current clip region will be set to the clip
               window.
               """,
               see_also=":func:`FitWindow_MVIEW`, :func:`ScaleWindow_MVIEW`, :func:`Extent_MVIEW`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="X minimum"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Y minimum"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="X maximum"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Y maximum"),
                   Parameter('unit', type=Type.INT32_T,
                             doc=":def:`MVIEW_UNIT`")
               ]),

        Method('TranScale_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the view translation and scaling",
               notes="""
               Warning. For reasons unknown (and maybe a bug), this
               function resets the view :class:`IPJ` units. It is a good idea
               to call the SetUnits_IPJ function after calling this
               function in order to restore them. This will be addressed
               in v6.4.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X origin (user X to be placed at map 0)"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y origin (user Y to be placed at map 0)"),
                   Parameter('xs', type=Type.DOUBLE,
                             doc="X mm/user unit"),
                   Parameter('ys', type=Type.DOUBLE,
                             doc="Y mm/user unit")
               ]),

        Method('UserToView_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a USERplot in mm to a VIEW coordinate",
               see_also="""
               :func:`SetUserIPJ_MVIEW`
               :func:`GetUserIPJ_MVIEW`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="X in USER, returned in View coordinates"),
                   Parameter('y', type=Type.DOUBLE, is_ref=True,
                             doc="Y in USER, returned in View coordinates")
               ]),

        Method('ViewToUser_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a VIEW coordinate to a USER coordinate.",
               see_also="""
               :func:`SetUserIPJ_MVIEW`
               :func:`GetUserIPJ_MVIEW`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="X in View, returned in user coordinates"),
                   Parameter('y', type=Type.DOUBLE, is_ref=True,
                             doc="Y in View, returned in user coordinates")
               ])
    ],
    'Miscellaneous': [

    ],
    'Obsolete': [

        Method('Draw3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Draw a 3D object built from triangles",
               notes="""
               This is a general 3D entity support command. You specify
               all the verticies and the normals at the verticies and
               possibly colors (optional). If the colors are not specified
               the default fill color will be used. The triangles are then
               composed using indexes into the vertices specified.
               As of v6.4, this method creates a single group with the name
               "surface". You should use the new Surface3D_MVIEW function,
               which allows direct specification of a single color, and the
               group name.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('vert_v_vx', type="VV",
                             doc="Verticies X"),
                   Parameter('vert_v_vy', type="VV",
                             doc="Verticies Y"),
                   Parameter('vert_v_vz', type="VV",
                             doc="Verticies Z"),
                   Parameter('norm_v_vx', type="VV",
                             doc="Normals X"),
                   Parameter('norm_v_vy', type="VV",
                             doc="Normals Y"),
                   Parameter('norm_v_vz', type="VV",
                             doc="Normals Z"),
                   Parameter('color_vv', type="VV",
                             doc="Colors :class:`VV` or COL_ANY (can be NULL)"),
                   Parameter('index_vv', type="VV",
                             doc="Long :class:`VV` of triangle indexes,3 per triangle")
               ]),

        Method('GetPlaneIPJ_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Get the Plane Projection",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection object returning Plane Projection")
               ]),

        Method('GetStatusXYZ_MVIEW', module='geoengine.map', version='5.1.5',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Get current XYZ status display parameters.",
               notes="See above :func:`SetStatusXYZ_MVIEW`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('flag', type=Type.INT32_T, is_ref=True,
                             doc="Enable XYZ in for status bar display"),
                   Parameter('z', type=Type.DOUBLE, is_ref=True,
                             doc="Z value in viewed section coordinates (dummy if not defined).")
               ]),

        Method('PolyAggregate_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Add a PolyAggregate to a view.",
               notes="This creates an animation on the map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('pagg', type="PAGG",
                             doc="PolyAggregate"),
                   Parameter('name', type=Type.STRING,
                             doc="PolyAggregate name (Maximum length is :def_val:`MVIEW_NAME_LENGTH`)")
               ]),

        Method('SetPlaneIPJ_MVIEW', module='geoengine.map', version='5.1.4',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Set the Plane Projection",
               notes="By default it is the View's Clip Projection",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('plane', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection")
               ]),

        Method('SetStatusXYZ_MVIEW', module='geoengine.map', version='5.1.5',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Set parameters to enable XYZ status display.",
               notes="""
               The view coordinates are displayed in X and Y, and normally
               OE performs a :func:`ConvertXY_PJ` on the (X, Y) value in the view
               using the UserIPJ to display the current (X, Y) in the
               status bar. In some views, however, (for instance sections
               in Wholeplot), A 3D conversion is required. In a Wholeplot
               section, the "Z" axis is perpendicular to the screen, and
               the section center has a Z value of 0.0. The User :class:`IPJ`
               uses the current X,Y, and the Z supplied in this function to
               do a proper 3D conversion and display the X,Y and Z value at
               the specific location in the view.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('flag', type=Type.INT32_T,
                             doc="Enable XYZ in for status bar display"),
                   Parameter('z', type=Type.DOUBLE,
                             doc="Z value in viewed section coordinates")
               ]),

        Method('Surface_MVIEW', module='geoengine.map', version='5.0.5',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Add an 3d Surface to a view.",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('sur', type="SUR",
                             doc="Surface"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Min X of location on map"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Min Y of location on map"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Max X of location on map"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Max Y of location on map"),
                   Parameter('name', type=Type.STRING,
                             doc="Surface name (Maximum length is :def_val:`MVIEW_NAME_LENGTH`)")
               ]),

        Method('DrawSurface3D_MVIEW', module='geoengine.map', version='7.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Draw a 3D object built from triangles",
               notes="""
               Provide one normal per vertex.
               Triangles are defined by indices into the set of vertices.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW"),
                   Parameter('group_name', type=Type.STRING,
                             doc="Group name"),
                   Parameter('vert_v_vx', type="VV",
                             doc="Vertices X (:def_val:`GS_REAL`)"),
                   Parameter('vert_v_vy', type="VV",
                             doc="Vertices Y (:def_val:`GS_REAL`)"),
                   Parameter('vert_v_vz', type="VV",
                             doc="Vertices Z (:def_val:`GS_REAL`)"),
                   Parameter('norm_v_vx', type="VV",
                             doc="Normals X (:def_val:`GS_REAL`)"),
                   Parameter('norm_v_vy', type="VV",
                             doc="Normals Y (:def_val:`GS_REAL`)"),
                   Parameter('norm_v_vz', type="VV",
                             doc="Normals Z (:def_val:`GS_REAL`)"),
                   Parameter('color_vv', type="VV",
                             doc="Colors :class:`VV` (:def_val:`GS_INT`) [can be NULL]"),
                   Parameter('color', type=Type.INT32_T,
                             doc="Color used if above :class:`VV` is NULL [0 for :class:`MVIEW`'s fill color]"),
                   Parameter('tri_vv_pt1', type="VV",
                             doc="Triangles Point 1 (:def_val:`GS_INT`)"),
                   Parameter('tri_vv_pt2', type="VV",
                             doc="Triangles Point 2 (:def_val:`GS_INT`)"),
                   Parameter('tri_vv_pt3', type="VV",
                             doc="Triangles Point 3 (:def_val:`GS_INT`)")
               ])
    ]
}

