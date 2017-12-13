from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DXFI',
                 doc="The :class:`DXFI` class is used for importing AutoCAD® dxf files into Geosoft maps.")





gx_methods = {
    'Miscellaneous': [

        Method('Create_DXFI', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create :class:`DXFI`.",
               return_type="DXFI",
               return_doc=":class:`DXFI` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="DXF file name")
               ]),

        Method('Destroy_DXFI', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`DXFI` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dxfi', type="DXFI",
                             doc=":class:`DXFI` Handle")
               ]),

        Method('DXF2PLY_DXFI', module='geogxx', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Convert a DXF file to a :class:`PLY` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ply', type="PLY",
                             doc=":class:`PLY` handle"),
                   Parameter('dxfi', type="DXFI",
                             doc=":class:`DXFI` handle")
               ]),

        Method('DXF2ViewEx_DXFI', module='geogxx', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Draw entities in a DXF file to a view in a map",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dxfi', type="DXFI"),
                   Parameter('view', type="MVIEW"),
                   Parameter('max_pen', type=Type.INT32_T,
                             doc="User defined number of pens to use (can be :const:`iDUMMY`)"),
                   Parameter('pb_group', type=Type.INT32_T,
                             doc="TRUE to place entire DXF in one group"),
                   Parameter('group', type=Type.STRING,
                             doc='Group name for one group (can be "" if above is FALSE)'),
                   Parameter('pb_one_color', type=Type.INT32_T,
                             doc="TRUE to force one color"),
                   Parameter('color', type=Type.INT32_T,
                             doc=":def:`MVIEW_COLOR` (ignored if above is FALSE)")
               ]),

        Method('GetRange_DXFI', module='geogxx', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get DXF data range",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dxfi', type="DXFI",
                             doc=":class:`DXFI` handle"),
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="X min"),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="X max"),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="Y min"),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="Y max"),
                   Parameter('min_z', type=Type.DOUBLE, is_ref=True,
                             doc="Z min"),
                   Parameter('max_z', type=Type.DOUBLE, is_ref=True,
                             doc="Z max")
               ])
    ],
    'Obsolete': [

        Method('DXF2Map_DXFI', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Draw entities in a DXF file in a map",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('map', type="MAP",
                             doc="Map handle"),
                   Parameter('dxfi', type="DXFI",
                             doc=":class:`DXFI` handle"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="User defined map scale"),
                   Parameter('u_fac', type=Type.DOUBLE,
                             doc="Unit conversion factor"),
                   Parameter('x0', type=Type.DOUBLE,
                             doc="X origin of the map"),
                   Parameter('y0', type=Type.DOUBLE,
                             doc="Y origin of the map"),
                   Parameter('max_pen', type=Type.INT32_T,
                             doc="User defined number of pens to use"),
                   Parameter('pb_black', type=Type.INT32_T,
                             doc="Force black color if 1")
               ]),

        Method('DXF2MapEx_DXFI', module='geogxx', version='5.0.6',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Draw entities in a DXF file in a map",
               notes="""
               The DXF will be drawin in the "*Data" view.  If a "*Data" view
               does not exist, it will be created.
               
               Obsolete
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('dxfi', type="DXFI",
                             doc=":class:`DXFI` handle"),
                   Parameter('map', type="MAP",
                             doc="Map handle"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="User defined map scale"),
                   Parameter('u_fac', type=Type.DOUBLE,
                             doc="Unit conversion factor"),
                   Parameter('x0', type=Type.DOUBLE,
                             doc="X origin of the map"),
                   Parameter('y0', type=Type.DOUBLE,
                             doc="Y origin of the map"),
                   Parameter('max_pen', type=Type.INT32_T,
                             doc="User defined number of pens to use"),
                   Parameter('pb_group', type=Type.INT32_T,
                             doc="TRUE to place entire DXF in one group"),
                   Parameter('group', type=Type.STRING,
                             doc="Group name for one group"),
                   Parameter('pb_one_color', type=Type.INT32_T,
                             doc="TRUE to force one color"),
                   Parameter('p_color', type=Type.INT32_T,
                             doc=":def:`MVIEW_COLOR`")
               ]),

        Method('DXF2View_DXFI', module='geogxx', version='5.0.6',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Draw entities in a DXF file to a view in a map",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dxfi', type="DXFI"),
                   Parameter('view', type="MVIEW"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="User defined map scale"),
                   Parameter('u_fac', type=Type.DOUBLE,
                             doc="Unit conversion factor"),
                   Parameter('x0', type=Type.DOUBLE,
                             doc="X origin of the map"),
                   Parameter('y0', type=Type.DOUBLE,
                             doc="Y origin of the map"),
                   Parameter('max_pen', type=Type.INT32_T,
                             doc="User defined number of pens to use"),
                   Parameter('pb_group', type=Type.INT32_T,
                             doc="TRUE to place entire DXF in one group"),
                   Parameter('group', type=Type.STRING,
                             doc="Group name for one group"),
                   Parameter('pb_one_color', type=Type.INT32_T,
                             doc="TRUE to force one color"),
                   Parameter('p_color', type=Type.INT32_T,
                             doc=":def:`MVIEW_COLOR`")
               ]),

        Method('MapExtents_DXFI', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Get map extent",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dxfi', type="DXFI",
                             doc=":class:`DXFI` handle"),
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="Min X - returned"),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="Min Y - returned"),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="Max X - returned"),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="Max Y - returned")
               ]),

        Method('SetIPJ_DXFI', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Set the projection of the DXF.",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dxfi', type="DXFI",
                             doc="View"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` to place in the view")
               ])
    ]
}

