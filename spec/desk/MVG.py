from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MVG',
                 doc="The :class:`MVG` class provides the ability to create view graphs.")


gx_defines = [
    Define('MVG_DRAW',
           doc=":class:`MVG` draw define",
           constants=[
               Constant('MVG_DRAW_POLYLINE', value='0', type=Type.INT32_T),
               Constant('MVG_DRAW_POLYGON', value='1', type=Type.INT32_T)
           ]),

    Define('MVG_GRID',
           doc=":class:`MVG` grid define",
           constants=[
               Constant('MVG_GRID_DOT', value='0', type=Type.INT32_T),
               Constant('MVG_GRID_LINE', value='1', type=Type.INT32_T),
               Constant('MVG_GRID_CROSS', value='2', type=Type.INT32_T)
           ]),

    Define('MVG_LABEL_BOUND',
           doc=":class:`MVG` label bound define",
           constants=[
               Constant('MVG_LABEL_BOUND_NO', value='0', type=Type.INT32_T),
               Constant('MVG_LABEL_BOUND_YES', value='1', type=Type.INT32_T)
           ]),

    Define('MVG_LABEL_JUST',
           doc=":class:`MVG` label justification define",
           constants=[
               Constant('MVG_LABEL_JUST_TOP', value='0', type=Type.INT32_T),
               Constant('MVG_LABEL_JUST_BOTTOM', value='1', type=Type.INT32_T),
               Constant('MVG_LABEL_JUST_LEFT', value='2', type=Type.INT32_T),
               Constant('MVG_LABEL_JUST_RIGHT', value='3', type=Type.INT32_T)
           ]),

    Define('MVG_LABEL_ORIENT',
           doc=":class:`MVG` label orientation",
           constants=[
               Constant('MVG_LABEL_ORIENT_HORIZONTAL', value='0', type=Type.INT32_T),
               Constant('MVG_LABEL_ORIENT_TOP_RIGHT', value='1', type=Type.INT32_T),
               Constant('MVG_LABEL_ORIENT_TOP_LEFT', value='2', type=Type.INT32_T)
           ]),

    Define('MVG_SCALE',
           doc=":class:`MVG` scale define",
           constants=[
               Constant('MVG_SCALE_LINEAR', value='0', type=Type.INT32_T),
               Constant('MVG_SCALE_LOG', value='1', type=Type.INT32_T),
               Constant('MVG_SCALE_LOGLINEAR', value='2', type=Type.INT32_T)
           ]),

    Define('MVG_WRAP',
           doc=":class:`MVG` wrap define",
           constants=[
               Constant('MVG_WRAP_NO', value='0', type=Type.INT32_T),
               Constant('MVG_WRAP_YES', value='1', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('AxisX_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw an X axis",
               notes="""
               When Log annotation is applied, nice tick intervals will be
               calculated
               
               Obsolete
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mvg', type="MVG"),
                   Parameter('d_y', type=Type.DOUBLE,
                             doc="Y location in plot units (mm)"),
                   Parameter('d_lx', type=Type.DOUBLE,
                             doc="Left  X (rescaling unit)"),
                   Parameter('d_rx', type=Type.DOUBLE,
                             doc="Right X (rescaling unit)"),
                   Parameter('d_maj_int', type=Type.DOUBLE,
                             doc="Major tick interval (rescaling unit). Ticks drawn in decades in LOG or LOGLINEAR scale"),
                   Parameter('d_min_int', type=Type.DOUBLE,
                             doc="Minor tick interval  (rescaling unit). Not used in LOG/LOGLINEAR"),
                   Parameter('d_size', type=Type.DOUBLE,
                             doc="Tick size in view units (mm) (negative for down ticks)")
               ]),

        Method('AxisY_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw a  Y axis",
               notes="""
               When Log annotation is applied, nice tick intervals will be
               calculated
               
               Obsolete
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mvg', type="MVG"),
                   Parameter('d_x', type=Type.DOUBLE,
                             doc="X location in plot units (mm)"),
                   Parameter('d_by', type=Type.DOUBLE,
                             doc="Bottom Y (rescaling unit)"),
                   Parameter('d_ty', type=Type.DOUBLE,
                             doc="Top Y (rescaling unit)"),
                   Parameter('d_maj_int', type=Type.DOUBLE,
                             doc="Major tick interval (rescaling unit). Ticks drawn in decades in LOG or LOGLINEAR scale"),
                   Parameter('d_min_int', type=Type.DOUBLE,
                             doc="Minor tick interval  (rescaling unit). Not used in LOG/LOGLINEAR"),
                   Parameter('d_size', type=Type.DOUBLE,
                             doc="Tick size in plot units (mm)(negative for left ticks)")
               ]),

        Method('Create_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a :class:`MVG` object",
               notes="Obsolete",
               return_type="MVG",
               return_doc=":class:`MVG` handle (NULL if error)",
               parameters = [
                   Parameter('map', type="MAP",
                             doc="H_MAP handle"),
                   Parameter('name', type=Type.STRING,
                             doc="View Name"),
                   Parameter('xmin_m', type=Type.DOUBLE,
                             doc="Minimum X in map unit (mm)"),
                   Parameter('ymin_m', type=Type.DOUBLE,
                             doc="Minimum Y in map unit (mm)"),
                   Parameter('xmax_m', type=Type.DOUBLE,
                             doc="Maximum X in map unit (mm)"),
                   Parameter('ymax_m', type=Type.DOUBLE,
                             doc="Maximum Y in map unit (mm)"),
                   Parameter('xmin_u', type=Type.DOUBLE,
                             doc="Minimum X in view unit (m for example)"),
                   Parameter('ymin_u', type=Type.DOUBLE,
                             doc="Minimum Y in view unit"),
                   Parameter('xmax_u', type=Type.DOUBLE,
                             doc="Maximum X in view unit"),
                   Parameter('ymax_u', type=Type.DOUBLE,
                             doc="Maximum Y in view unit")
               ]),

        Method('Destroy_MVG', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`MVG` handle.",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mvg', type="MVG",
                             doc=":class:`MVG` Handle")
               ]),

        Method('GetMVIEW_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get the :class:`MVIEW` Handle of the Object.",
               notes="Obsolete",
               return_type="MVIEW",
               return_doc=":class:`MVIEW` Handle",
               parameters = [
                   Parameter('mvg', type="MVG",
                             doc=":class:`MVG` object")
               ]),

        Method('Grid_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw a grid in the current :class:`MVG`",
               notes="""
               The grid will be drawn in the current window.
               
               In the LOG and LOGLINEAR rescaling modes, grids will be
               drawn in decades and the X/Y grid increments will be
               ignored.  In addition, grid lines at 0 (zero) and LOGMIN will be drawn.
               
               Obsolete
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mvg', type="MVG"),
                   Parameter('d1st_x', type=Type.DOUBLE,
                             doc="X position of 1st vertical grid line to draw (in rescaling unit)"),
                   Parameter('d1st_y', type=Type.DOUBLE,
                             doc="Y position of 1st horizontal grid line to draw (in rescaling unit)"),
                   Parameter('d_x', type=Type.DOUBLE,
                             doc="X grid increment of rescaled map unit (see above Rescaling functions)"),
                   Parameter('d_y', type=Type.DOUBLE,
                             doc="Y grid increment of rescaled map unit (see above Rescaling functions)"),
                   Parameter('d_dx', type=Type.DOUBLE,
                             doc="X dot increment/cross X size of rescaled map unit"),
                   Parameter('d_dy', type=Type.DOUBLE,
                             doc="Y dot increment/cross Y size of rescaled map unit"),
                   Parameter('l_type', type=Type.INT32_T,
                             doc=":def:`MVG_GRID`")
               ]),

        Method('LabelX_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Label annotations on the X axis",
               notes="""
               Label bounding will justify edge labels to be inside
               the bar limits.
               
               When Log annotation is applied, labels will be drawn in decades.
               
               Obsolete
               """,
               see_also="sAxisX_MVG",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mvg', type="MVG"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y location in plot units (mm)"),
                   Parameter('lx', type=Type.DOUBLE,
                             doc="Left  X (rescaling unit)"),
                   Parameter('rx', type=Type.DOUBLE,
                             doc="Right X (rescaling unit)"),
                   Parameter('maj_int', type=Type.DOUBLE,
                             doc="Major tick interval (ignored if in LOG or LOGLINEAR rescaling)"),
                   Parameter('just', type=Type.INT32_T,
                             doc="Label justification :def:`MVG_LABEL_JUST`"),
                   Parameter('bound', type=Type.INT32_T,
                             doc="Edge label bounding :def:`MVG_LABEL_BOUND`"),
                   Parameter('orient', type=Type.INT32_T,
                             doc="Label orientation   :def:`MVG_LABEL_ORIENT`")
               ]),

        Method('LabelY_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Label annotations on the Y axis",
               notes="""
               Label bounding will justify edge labels to be inside
               the bar limits.
               
               When Log annotation is applied, labels will be drawn in decades.
               
               Obsolete
               """,
               see_also="sAxisY_MVG",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mvg', type="MVG"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X location in plot units (mm)"),
                   Parameter('by', type=Type.DOUBLE,
                             doc="Bottom  Y (rescaling unit)"),
                   Parameter('ty', type=Type.DOUBLE,
                             doc="Top Y (rescaling unit)"),
                   Parameter('maj_int', type=Type.DOUBLE,
                             doc="Label interval (ignored if in LOG or LOGLINEAR rescaling)"),
                   Parameter('just', type=Type.INT32_T,
                             doc="Label justification :def:`MVG_LABEL_JUST`"),
                   Parameter('bound', type=Type.INT32_T,
                             doc="Edge label bounding :def:`MVG_LABEL_BOUND`"),
                   Parameter('orient', type=Type.INT32_T,
                             doc="Label orientation   :def:`MVG_LABEL_ORIENT`")
               ]),

        Method('PolyLineVA_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Creates PolyLines/polygons from :class:`VV` and :class:`VA`.",
               notes="""
               If the :class:`VV` contains dummies, the polylines
               will break at the dummies; the polygons
               will skip the dummies.
               
               If wrapping is applied, POLYGON parameter is ignored and
               only POLYLINES are drawn.
               
               Obsolete
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mvg', type="MVG"),
                   Parameter('draw', type=Type.INT32_T,
                             doc=":def:`MVG_DRAW`"),
                   Parameter('wrap', type=Type.INT32_T,
                             doc=":def:`MVG_WRAP`"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('va', type="VA",
                             doc="Y VAs"),
                   Parameter('vv_array', type="VV",
                             doc=":class:`VV` containing list of :class:`VA` ranges, such as 1,2 40 ... Entire :class:`VA` is drawn if this :class:`VV` is empty.")
               ]),

        Method('PolyLineVV_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Creates PolyLines/polygons from :class:`VV` and :class:`VV`.",
               notes="""
               If the :class:`VV` contains dummies, the polylines
               will break at the dummies; the polygons
               will skip the dummies.
               
               If wrapping is applied, POLYGON parameter is ignored and
               only POLYLINES are drawn.
               
               Obsolete
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mvg', type="MVG"),
                   Parameter('draw', type=Type.INT32_T,
                             doc=":def:`MVG_DRAW`"),
                   Parameter('wrap', type=Type.INT32_T,
                             doc=":def:`MVG_WRAP`"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV`")
               ]),

        Method('RescaleXRange_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Re-scale horizontal axis",
               notes="""
               When RescaleX_MVG is used, only the scaling information
               related to X axis will be considered
               
               Obsolete
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mvg', type="MVG",
                             doc=":class:`MVG` handle"),
                   Parameter('scale', type=Type.INT32_T,
                             doc=":def:`MVG_SCALE`"),
                   Parameter('min', type=Type.DOUBLE,
                             doc="Scale information: new minimum X"),
                   Parameter('max', type=Type.DOUBLE,
                             doc="Scale information: new maximum X"),
                   Parameter('log_min', type=Type.DOUBLE,
                             doc="Scale information: minimum X to apply log10, it is defined only for LOGLINEAR scale")
               ]),

        Method('RescaleYRange_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Re-scale vertical axis",
               notes="""
               When RescaleY_MVG is used, only the scaling information
               related to Y axis will be considered
               
               Obsolete
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mvg', type="MVG",
                             doc=":class:`MVG` handle"),
                   Parameter('scale', type=Type.INT32_T,
                             doc=":def:`MVG_SCALE`"),
                   Parameter('min', type=Type.DOUBLE,
                             doc="Scale information: new minimum Y"),
                   Parameter('max', type=Type.DOUBLE,
                             doc="Scale information: new maximum Y"),
                   Parameter('log_min', type=Type.DOUBLE,
                             doc="Scale information: minimum Y to apply log10, it is defined only for LOGLINEAR scale")
               ])
    ]
}

