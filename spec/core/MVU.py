from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MVU',
                 doc="""
                 A catchall library for methods using the :class:`MAP` and :class:`MVIEW` classes.
                 These include drawing flight paths, legends, postings, and
                 special objects such as histograms and bar charts.
                 """)


gx_defines = [
    Define('EMLAY_GEOMETRY',
           doc="Type of Geometry",
           constants=[
               Constant('EMLAY_V_COPLANAR', value='0', type=Type.INT32_T,
                        doc="0"),
               Constant('EMLAY_H_COPLANAR', value='1', type=Type.INT32_T,
                        doc="1"),
               Constant('EMLAY_V_COAXIAL', value='2', type=Type.INT32_T,
                        doc="2")
           ]),

    Define('ARROW_ALIGNMENT',
           doc="Direction of alignment",
           constants=[
               Constant('ARROW_ALIGNMENT_HORIZONTAL', value='0', type=Type.INT32_T),
               Constant('ARROW_ALIGNMENT_VERTICAL', value='1', type=Type.INT32_T)
           ]),

    Define('BARCHART_LABEL',
           doc="Place to draw bar labels",
           constants=[
               Constant('BARCHART_LABEL_NO', value='0', type=Type.INT32_T,
                        doc="No label"),
               Constant('BARCHART_LABEL_BELOWX', value='1', type=Type.INT32_T,
                        doc="Label below X axis"),
               Constant('BARCHART_LABEL_ABOVEX', value='2', type=Type.INT32_T,
                        doc="Label above X axis"),
               Constant('BARCHART_LABEL_PEND', value='3', type=Type.INT32_T,
                        doc="Label at positive end of bar"),
               Constant('BARCHART_LABEL_NEND', value='4', type=Type.INT32_T,
                        doc="Label at negative end of bar"),
               Constant('BARCHART_LABEL_ALTERNAT1', value='5', type=Type.INT32_T,
                        doc="Label at alternative ends,1st label at positive end"),
               Constant('BARCHART_LABEL_ALTERNAT2', value='6', type=Type.INT32_T,
                        doc="Label at alternative ends,1st label at negative end")
           ]),

    Define('COLORBAR_LABEL',
           doc="Label text orientation",
           constants=[
               Constant('COLORBAR_LABEL_HORIZONTAL', value='0', type=Type.INT32_T,
                        doc="(default)"),
               Constant('COLORBAR_LABEL_VERTICAL', value='1', type=Type.INT32_T,
                        doc="Gives text an orientation of -90 degrees")
           ]),

    Define('COLORBAR_STYLE',
           doc="Label text orientation",
           constants=[
               Constant('COLORBAR_STYLE_NONE', value='0', type=Type.INT32_T,
                        doc="Don't draw"),
               Constant('COLORBAR_STYLE_MAXMIN', value='1', type=Type.INT32_T,
                        doc="Post max/min values")
           ]),

    Define('MVU_ORIENTATION',
           doc="Orientation (of whatever)",
           constants=[
               Constant('MVU_ORIENTATION_VERTICAL', value='0', type=Type.INT32_T,
                        doc="Vertical"),
               Constant('MVU_ORIENTATION_HORIZONTAL', value='1', type=Type.INT32_T,
                        doc="Horizontal")
           ]),

    Define('MVU_DIVISION_STYLE',
           doc="Orientation (of whatever)",
           constants=[
               Constant('MVU_DIVISION_STYLE_NONE', value='0', type=Type.INT32_T,
                        doc="No division marks"),
               Constant('MVU_DIVISION_STYLE_LINES', value='1', type=Type.INT32_T,
                        doc="Division line"),
               Constant('MVU_DIVISION_STYLE_TICS', value='2', type=Type.INT32_T,
                        doc="Inside tics, both sides")
           ]),

    Define('MVU_ARROW',
           doc="""
           Type Arrow. These definitions are used as binary flags, and can be
           used together by passing sums.
           """,
           constants=[
               Constant('MVU_ARROW_SOLID', value='1', type=Type.INT32_T,
                        doc="""
                        Plot the head as a solid triangle, otherwise plot a "stick arrow"
                        with three lines for the tail and two barbs.
                        """),
               Constant('MVU_ARROW_FIXED', value='2', type=Type.INT32_T,
                        doc="""
                        If used, input the actual length of the barbs on the arrow, in
                        view X-axis units, as measured along the tail. If not used, enter the ratio
                        between the length of the barbs and full length of the arrow (e.g. 0.4).
                        In the latter case, the longer the arrow, the bigger the arrow head.
                        """)
           ]),

    Define('MVU_FLIGHT_COMPASS',
           doc="Compass direction",
           constants=[
               Constant('MVU_FLIGHT_COMPASS_NONE', value='-1', type=Type.INT32_T),
               Constant('MVU_FLIGHT_COMPASS_EAST', value='0', type=Type.INT32_T),
               Constant('MVU_FLIGHT_COMPASS_NORTH', value='1', type=Type.INT32_T),
               Constant('MVU_FLIGHT_COMPASS_WEST', value='2', type=Type.INT32_T),
               Constant('MVU_FLIGHT_COMPASS_SOUTH', value='3', type=Type.INT32_T)
           ]),

    Define('MVU_FLIGHT_DUMMIES',
           doc="Show Dummies",
           constants=[
               Constant('MVU_FLIGHT_DUMMIES_NOTINCLUDED', value='0', type=Type.INT32_T),
               Constant('MVU_FLIGHT_DUMMIES_INCLUDED', value='1', type=Type.INT32_T)
           ]),

    Define('MVU_FLIGHT_LOCATE',
           doc="Line label locations",
           constants=[
               Constant('MVU_FLIGHT_LOCATE_NONE', value='0', type=Type.INT32_T,
                        doc="No label"),
               Constant('MVU_FLIGHT_LOCATE_END', value='1', type=Type.INT32_T,
                        doc="""
                        L100.2 -------------------------- L100.2
                        
                        dOffA controls distance from label to line.
                        dOffB controls vertical offset from center.
                        """),
               Constant('MVU_FLIGHT_LOCATE_ABOVE', value='2', type=Type.INT32_T,
                        doc="""
                        L100.2                            L100.2
                        ----------------------------------------
                        
                        dOffA controls label distance above the line.
                        dOffB controls offset in from line end.
                        """),
               Constant('MVU_FLIGHT_LOCATE_BELOW', value='3', type=Type.INT32_T,
                        doc="""
                        ----------------------------------------
                        L100.2                            L100.2
                        
                        dOffA controls label distance below the line.
                        dOffB controls offset in from line end.
                        """),
               Constant('MVU_FLIGHT_DIRECTION', value='8', type=Type.INT32_T,
                        doc="""
                        To add '>' to label to indicate direction, for example:
                        :def_val:`MVU_FLIGHT_LOCATE_END`+:def_val:`MVU_FLIGHT_DIRECTION`
                        """)
           ]),

    Define('MVU_VOX_SURFACE_METHOD',
           doc="TODO",
           constants=[
               Constant('MVU_VOX_SURFACE_METHOD_MARCHING_CUBES', value='0', type=Type.INT32_T)
           ]),

    Define('MVU_VOX_SURFACE_OPTION',
           doc="TODO",
           constants=[
               Constant('MVU_VOX_SURFACE_OPTION_OPEN', value='0', type=Type.INT32_T),
               Constant('MVU_VOX_SURFACE_OPTION_CLOSED', value='1', type=Type.INT32_T)
           ]),

    Define('MVU_TEXTBOX',
           doc="Type of Box",
           constants=[
               Constant('MVU_TEXTBOX_LEFT', value='0', type=Type.INT32_T),
               Constant('MVU_TEXTBOX_CENTER', value='1', type=Type.INT32_T),
               Constant('MVU_TEXTBOX_RIGHT', value='2', type=Type.INT32_T)
           ]),

    Define('MVU_VPOINT',
           doc="Head Acuteness",
           constants=[
               Constant('MVU_VPOINT_SHARP', value='0', type=Type.INT32_T),
               Constant('MVU_VPOINT_MEDIUM', value='1', type=Type.INT32_T),
               Constant('MVU_VPOINT_BLUNT', value='2', type=Type.INT32_T)
           ]),

    Define('MVU_VPOS',
           doc="Head Position",
           constants=[
               Constant('MVU_VPOS_HEAD', value='0', type=Type.INT32_T),
               Constant('MVU_VPOS_MIDDLE', value='1', type=Type.INT32_T),
               Constant('MVU_VPOS_TAIL', value='2', type=Type.INT32_T)
           ]),

    Define('MVU_VSIZE',
           doc="Head Size",
           constants=[
               Constant('MVU_VSIZE_NOHEAD', value='0', type=Type.INT32_T),
               Constant('MVU_VSIZE_SMALLHEAD', value='1', type=Type.INT32_T),
               Constant('MVU_VSIZE_MEDIUMHEAD', value='2', type=Type.INT32_T),
               Constant('MVU_VSIZE_LARGEHEAD', value='3', type=Type.INT32_T),
               Constant('MVU_VSIZE_NOTAIL', value='4', type=Type.INT32_T)
           ]),

    Define('MVU_VSTYLE',
           doc="Head Style",
           constants=[
               Constant('MVU_VSTYLE_LINES', value='0', type=Type.INT32_T),
               Constant('MVU_VSTYLE_BARB', value='1', type=Type.INT32_T),
               Constant('MVU_VSTYLE_TRIANGLE', value='2', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Arrow_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw an arrow.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('hx', type=Type.DOUBLE,
                             doc="Head X location"),
                   Parameter('hy', type=Type.DOUBLE,
                             doc="Head Y location"),
                   Parameter('tx', type=Type.DOUBLE,
                             doc="Tail X location"),
                   Parameter('ty', type=Type.DOUBLE,
                             doc="Tail Y location"),
                   Parameter('ratio', type=Type.DOUBLE,
                             doc="See :def:`MVU_ARROW` definitions for explanation"),
                   Parameter('angle', type=Type.DOUBLE,
                             doc="Angle of barbs with respect to the tail in degrees."),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`MVU_ARROW`")
               ]),

        Method('ArrowVectorVV_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw arrow vectors based on input VVs.",
               notes="""
               The locations are given in two VVs, and the directions
               in the two others. A wide range of sizes are available.
               If the scaling is set to :def_val:`rDUMMY`, then arrows are automatically
               scaled so the largest is 1cm in length.
               If the line thickness is set to :def_val:`rDUMMY`, the line thickness scales
               with the arrow size, and is 1/20 of the vector length.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X locations"),
                   Parameter('vv_y', type="VV",
                             doc="Y locations"),
                   Parameter('vv_dx', type="VV",
                             doc="X Vector value (can be negative)"),
                   Parameter('vv_dy', type="VV",
                             doc="Y Vector value (can be negative)"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="Scaling (units/mm)"),
                   Parameter('pos', type=Type.INT32_T,
                             doc=":def:`MVU_VPOS`"),
                   Parameter('size', type=Type.INT32_T,
                             doc=":def:`MVU_VSIZE`"),
                   Parameter('style', type=Type.INT32_T,
                             doc=":def:`MVU_VSTYLE`"),
                   Parameter('point', type=Type.INT32_T,
                             doc=":def:`MVU_VPOINT`"),
                   Parameter('thickness', type=Type.DOUBLE,
                             doc="Line thickness (can be Dummy)")
               ]),

        Method('BarChart_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Plot bar chart on a map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group_name', type=Type.STRING,
                             doc="Group name"),
                   Parameter('data', type="DB",
                             doc="Database handle"),
                   Parameter('line', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('x_chan', type=Type.STRING,
                             doc="Horizontal (X) axis' channel name"),
                   Parameter('list', type=Type.STRING,
                             doc="List of channel names (comma separated)"),
                   Parameter('x_title', type=Type.STRING,
                             doc="X axis title"),
                   Parameter('x_txt_size', type=Type.DOUBLE,
                             doc="Text size for X axis"),
                   Parameter('y_title', type=Type.STRING,
                             doc="Y axis title"),
                   Parameter('y_txt_size', type=Type.DOUBLE,
                             doc="Text size for Y axis"),
                   Parameter('bar_title', type=Type.STRING,
                             doc="Overall chart title"),
                   Parameter('bar_txt_size', type=Type.DOUBLE,
                             doc="Text size for overall title"),
                   Parameter('bar_width', type=Type.DOUBLE,
                             doc="Bar width in mm"),
                   Parameter('dist_fid', type=Type.INT32_T,
                             doc="Distance based (1) or fiducial based (0)"),
                   Parameter('label', type=Type.INT32_T,
                             doc=":def:`BARCHART_LABEL`"),
                   Parameter('tick', type=Type.INT32_T,
                             doc="Draw ticks along X axis (1) or not (0)"),
                   Parameter('right_axis', type=Type.INT32_T,
                             doc="Draw right vertical axis (1) or not"),
                   Parameter('top_axis', type=Type.INT32_T,
                             doc="Draw top horizontal axis (1)"),
                   Parameter('bottom_axis', type=Type.INT32_T,
                             doc="Draw bottom horizontal axis (1) or not"),
                   Parameter('surround', type=Type.INT32_T,
                             doc="Draw surronding box (1) or not (0) The following 4 parameters are required if drawing the surronding box"),
                   Parameter('left', type=Type.DOUBLE,
                             doc="Width in mm between left Y axis of bar chart with left surronding line"),
                   Parameter('bottom', type=Type.DOUBLE,
                             doc="Width in mm between bottom X axis of bar chart with bottom surronding line"),
                   Parameter('right', type=Type.DOUBLE,
                             doc="Width in mm between right Y axis of bar chart with right surronding line"),
                   Parameter('top', type=Type.DOUBLE,
                             doc="Width in mm between top X axis of bar chart with top surronding line"),
                   Parameter('xm', type=Type.DOUBLE,
                             doc="X in mm (bottom left corner of bar chart)"),
                   Parameter('ym', type=Type.DOUBLE,
                             doc="Y in mm (bottom left corner of bar chart)"),
                   Parameter('widthm', type=Type.DOUBLE,
                             doc="Width of the bar chart in mm"),
                   Parameter('heightm', type=Type.DOUBLE,
                             doc="Height of the bar chart in mm")
               ]),

        Method('CDIPixelPlot_MVU', module='geoengine.map', version='7.2.0',
               availability=Availability.LICENSED, 
               doc="Create a color pixel-style plot of CDI data.",
               notes="""
               Draws a single colored rectangle for each data point in
               Conductivity-Depth data (for example). It is similar to the
               result you get if you plot a grid with Pixel=1, but in this
               data the row and column widths are not necessarily constant,
               and the data can move up and down with topography. The pixels
               are sized so that the boundaries are half-way between adjacent
               data, both vertically and horizontally.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.STRING,
                             doc="Name of the group to create"),
                   Parameter('data_va', type="VA",
                             doc="Data [lNR x lNC]"),
                   Parameter('elev_va', type="VA",
                             doc="Elevations (Y) [lNR x lNC]"),
                   Parameter('xvv', type="VV",
                             doc="Position (X) [lNC]"),
                   Parameter('itr', type="ITR",
                             doc="Data color transform")
               ]),

        Method('CDIPixelPlot3D_MVU', module='geoengine.map', version='7.2.0',
               availability=Availability.LICENSED, 
               doc="Create a color pixel-style plot of CDI data in a 3D view.",
               notes="""
               Similar to :func:`CDIPixelPlot_MVU`, but plotted onto a series of
               plotting planes which hang from the XY path in 3D. Each vertical plane azimuth
               is defined by two adjacent points on the path. The color "pixel" for each
               data point is plotted in two halves, with each half on adjacent plotting planes,
               with the bend at the data point.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('group', type=Type.STRING,
                             doc="Name of the group to create"),
                   Parameter('data_va', type="VA",
                             doc="Data [lNR x lNC]"),
                   Parameter('elev_va', type="VA",
                             doc="Elevations (Z) [lNR x lNC]"),
                   Parameter('xvv', type="VV",
                             doc="Position (X) [lNC]"),
                   Parameter('yvv', type="VV",
                             doc="Position (Y) [lNC]"),
                   Parameter('itr', type="ITR",
                             doc="Data color transform")
               ]),

        Method('ColorBar_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a Color Bar in view",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('itr', type="ITR",
                             doc="Itr"),
                   Parameter('decimal', type=Type.INT32_T,
                             doc="Decimals"),
                   Parameter('ann', type=Type.DOUBLE,
                             doc="Annotation offset from box in mm."),
                   Parameter('height', type=Type.DOUBLE,
                             doc="Box height"),
                   Parameter('width', type=Type.DOUBLE,
                             doc="Box width"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X location (bottom left corner of color boxes)"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y location")
               ]),

        Method('ColorBar2_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a Color Bar from two :class:`ITR`",
               notes="""
               The secondary :class:`ITR` is used to blend horizontally with the
               primary :class:`ITR` in each box.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('itr', type="ITR"),
                   Parameter('itr2', type="ITR",
                             doc="Secondary :class:`ITR`"),
                   Parameter('decimal', type=Type.INT32_T,
                             doc="Decimals"),
                   Parameter('ann', type=Type.DOUBLE,
                             doc="Annotation size"),
                   Parameter('height', type=Type.DOUBLE,
                             doc="Box height"),
                   Parameter('width', type=Type.DOUBLE,
                             doc="Box width"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X location (bottom left corner of color boxes)"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y location")
               ]),

        Method('ColorBar2Style_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a Color Bar from two ITRs with style options",
               notes="""
               The secondary :class:`ITR` is used to blend horizontally with the
               primary :class:`ITR` in each box.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('itr', type="ITR"),
                   Parameter('itr2', type="ITR",
                             doc="Secondary :class:`ITR`"),
                   Parameter('decimal', type=Type.INT32_T,
                             doc="Decimals"),
                   Parameter('ann', type=Type.DOUBLE,
                             doc="Annotation size"),
                   Parameter('height', type=Type.DOUBLE,
                             doc="Box height"),
                   Parameter('width', type=Type.DOUBLE,
                             doc="Box width"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X location (bottom left corner of color boxes)"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('style', type=Type.INT32_T,
                             doc=":def:`COLORBAR_STYLE`")
               ]),

        Method('ColorBarHor_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a horizontal color bar in view",
               notes="""
               The sign of the annotation offset determines whether labels are
               plotted above or below the colorbar. Labels above are text-justified
               to the bottom of the text, and labels below are text-justified to
               the top of the text.
               """,
               see_also=":func:`ColorBar_MVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('itr', type="ITR",
                             doc="Itr"),
                   Parameter('decimal', type=Type.INT32_T,
                             doc="Decimals"),
                   Parameter('ann', type=Type.DOUBLE,
                             doc="Annotation offset from box in mm (negative for labels below)."),
                   Parameter('width', type=Type.DOUBLE,
                             doc="Box width in mm"),
                   Parameter('height', type=Type.DOUBLE,
                             doc="Box height in mm"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X location (bottom left corner of color boxes) in mm"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y location in mm"),
                   Parameter('label_orient', type=Type.INT32_T,
                             doc=":def:`COLORBAR_LABEL`")
               ]),

        Method('ColorBarHor2_MVU', module='geoengine.map', version='5.1.0',
               availability=Availability.LICENSED, 
               doc="Create a Horizontal Color Bar from two ITRs",
               notes="""
               The secondary :class:`ITR` is used to blend horizontally with the
               primary :class:`ITR` in each box.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('itr', type="ITR"),
                   Parameter('itr2', type="ITR",
                             doc="Secondary :class:`ITR`"),
                   Parameter('decimal', type=Type.INT32_T,
                             doc="Decimals"),
                   Parameter('ann', type=Type.DOUBLE,
                             doc="Annotation size"),
                   Parameter('height', type=Type.DOUBLE,
                             doc="Box height"),
                   Parameter('width', type=Type.DOUBLE,
                             doc="Box width"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X location (bottom left corner of color boxes)"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('label_orient', type=Type.INT32_T,
                             doc=":def:`COLORBAR_LABEL`")
               ]),

        Method('ColorBarHor2Style_MVU', module='geoengine.map', version='5.1.0',
               availability=Availability.LICENSED, 
               doc="Create a Horizontal Color Bar from two ITRs with style options",
               notes="""
               The secondary :class:`ITR` is used to blend horizontally with the
               primary :class:`ITR` in each box.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('itr', type="ITR"),
                   Parameter('itr2', type="ITR",
                             doc="Secondary :class:`ITR`"),
                   Parameter('decimal', type=Type.INT32_T,
                             doc="Decimals"),
                   Parameter('ann', type=Type.DOUBLE,
                             doc="Annotation size"),
                   Parameter('height', type=Type.DOUBLE,
                             doc="Box height"),
                   Parameter('width', type=Type.DOUBLE,
                             doc="Box width"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X location (bottom left corner of color boxes)"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('style', type=Type.INT32_T,
                             doc=":def:`COLORBAR_STYLE`"),
                   Parameter('label_orient', type=Type.INT32_T,
                             doc=":def:`COLORBAR_LABEL`")
               ]),

        Method('ColorBarHorStyle_MVU', module='geoengine.map', version='5.1.0',
               availability=Availability.LICENSED, 
               doc="Create a Horizontal Color Bar in view with style options",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('itr', type="ITR",
                             doc="Itr"),
                   Parameter('decimal', type=Type.INT32_T,
                             doc="Decimals"),
                   Parameter('ann', type=Type.DOUBLE,
                             doc="Annotation size"),
                   Parameter('height', type=Type.DOUBLE,
                             doc="Box height"),
                   Parameter('width', type=Type.DOUBLE,
                             doc="Box width"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X location (bottom left corner of color boxes)"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('style', type=Type.INT32_T,
                             doc=":def:`COLORBAR_STYLE`"),
                   Parameter('label_orient', type=Type.INT32_T,
                             doc=":def:`COLORBAR_LABEL`")
               ]),

        Method('ColorBarStyle_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a Color Bar in view with style options",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('itr', type="ITR",
                             doc="Itr"),
                   Parameter('decimal', type=Type.INT32_T,
                             doc="Decimals"),
                   Parameter('ann', type=Type.DOUBLE,
                             doc="Annotation size"),
                   Parameter('height', type=Type.DOUBLE,
                             doc="Box height"),
                   Parameter('width', type=Type.DOUBLE,
                             doc="Box width"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X location (bottom left corner of color boxes)"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('style', type=Type.INT32_T,
                             doc=":def:`COLORBAR_STYLE`")
               ]),

        Method('ColorBarREG_MVU', module='geoengine.map', version='8.2',
               availability=Availability.LICENSED, 
               doc="Create a Color Bar in view",
               notes="""
               To allow for expansion, all parameters are passed inside the :class:`REG` object.
               
               BAR_ORIENTATION        one of MVU_ORIENTATION_XXX (DEFAULT = :def_val:`MVU_ORIENTATION_VERTICAL`)
               DECIMALS					decimals in plotted values (see sFormatStr_GS for rules) (DEFAULT = 1)
               ANNOFF						annotation offset from bar (+/- determines side of the bar left/right and below/above)
               BOX_SIZE               box height (mm) (width for horizontal color bar) (DEFAULT = 4)
               BAR_WIDTH              width (mm) (short dimension) of the color bar (DEFAULT = 8)
               MINIMUM_GAP            Minimum space between annotations, otherwise drop annotations (DEFAULT = 0 mm)
               The actual height is over-estimated, so even with zero gap there will normally always be some space between labels.
               FIXED_INTERVAL         Preset interval for annotations scale (DEFAULT = DUMMY, use color zones)
               FIXED_MINOR_INTERVAL   Preset minor interval for annotations scale (DEFAULT = DUMMY, if defined must be 1/10, 1/5, 1/4 or 1/2 of FIXED_INTERVAL)
               X								X location	(REQUIRED)
               Y								Y location	(REQUIRED)
               POST_MAXMIN            Post limit values at ends of the bar (0 or 1)? (DEFAULT = 0)
               DIVISION_STYLE         One of MVU_DIVISION_STYLE_XXX (DEFAULT = :def_val:`MVU_DIVISION_STYLE_LINES`)
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('itr', type="ITR",
                             doc="Itr"),
                   Parameter('itr2', type="ITR",
                             doc="Optional 2nd Itr (can be null)"),
                   Parameter('reg', type="REG",
                             doc="Parameters")
               ]),

        Method('Contour_MVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Creates a contour map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('con', type=Type.STRING,
                             doc="Control file name"),
                   Parameter('grid', type=Type.STRING,
                             doc="Grid file name")
               ]),

        Method('ContourPLY_MVU', module='geogxx', version='5.1.6',
               availability=Availability.LICENSED, 
               doc="Creates a contour map with clipped areas.",
               notes="""
               The clipping :class:`PLY` can include a surrounding inclusive polygon
               and zero, one or more interior exclusive polygons. Construct
               a :class:`PLY` object using the :func:`AddPolygonEx_PLY` function, to add both
               inclusive (as the first :class:`PLY`) and exclusive interior regions.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('ply', type="PLY",
                             doc="Clipping :class:`PLY`"),
                   Parameter('con', type=Type.STRING,
                             doc="Control file name"),
                   Parameter('grid', type=Type.STRING,
                             doc="Grid file name")
               ]),

        Method('CSymbLegend_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Plot a legend for the classified color symbols.",
               notes="""
               If the symbol size, color, font etc are specified in
               the :class:`ITR`'s :class:`REG`, then the Symbol scale factor is used
               allow the user to adjust the symbol sizes. They will be
               plotted at a size equal to the size in the :class:`REG` times
               the scale factor.
               If no symbol size info can be found in the :class:`REG`, then
               the symbol size is set equal to the Label Font Size.
               If no symbol font or number info is included in the
               :class:`REG`, it is the programmer's responsibility to select
               the correct font and symbol before CSymbLegend is
               called. The same is true of the edge color.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('x1', type=Type.DOUBLE,
                             doc="Plot origin X"),
                   Parameter('y1', type=Type.DOUBLE,
                             doc="Plot origin Y"),
                   Parameter('font_size', type=Type.DOUBLE,
                             doc="Label Font size (mm)"),
                   Parameter('symb_scale', type=Type.DOUBLE,
                             doc="Symbol scale factor"),
                   Parameter('file', type=Type.STRING,
                             doc=":class:`AGG`, :class:`ITR` or ZON file name"),
                   Parameter('title', type=Type.STRING,
                             doc="Plot title"),
                   Parameter('sub_title', type=Type.STRING,
                             doc="Plot subtitle")
               ]),

        Method('DecayCurve_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Plot decay curves at survey locations",
               notes="""
               Box width and height are used to draw horizontal and vertical
               bars. Curves outside the box are not clipped.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X coordinate :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y coordinate :class:`VV`"),
                   Parameter('v_ay', type="VA",
                             doc=":class:`VA` channel to plot"),
                   Parameter('v_ax', type="VA",
                             doc=":class:`VA` channel as horizontal axis (normally time channel)"),
                   Parameter('log', type=Type.INT32_T,
                             doc="Log option: 0 linear (default), 1 logarithm, 2 log/linear"),
                   Parameter('log_min', type=Type.DOUBLE,
                             doc="Min value to apply log (must be > 0.0)"),
                   Parameter('angle', type=Type.DOUBLE,
                             doc="Angle in degrees measured CCW from East of the map"),
                   Parameter('x_bar', type=Type.INT32_T,
                             doc="Draw horizontal bar: 0 none, 1 bottom, 2 top, 3 both"),
                   Parameter('y_bar', type=Type.INT32_T,
                             doc="Draw vertical bar:   0 none, 1 bottom, 2 top, 3 both"),
                   Parameter('x_off_set', type=Type.DOUBLE,
                             doc="X offset in mm: Horizontal distance between survey location and origin of the box inside which decay curvey is drawn"),
                   Parameter('y_off_set', type=Type.DOUBLE,
                             doc="Y offset in mm"),
                   Parameter('width', type=Type.DOUBLE,
                             doc="Box width in mm:Decay curve at each survey location is drawn within this box"),
                   Parameter('height', type=Type.DOUBLE,
                             doc="Box height in mm"),
                   Parameter('x_min', type=Type.DOUBLE,
                             doc="Minimum value for X (horizontal axis)"),
                   Parameter('y_min', type=Type.DOUBLE,
                             doc="Minimum value for Y (vertical axis)"),
                   Parameter('x_scale', type=Type.DOUBLE,
                             doc="X scale"),
                   Parameter('y_scale', type=Type.DOUBLE,
                             doc="Y scale"),
                   Parameter('line_pitch', type=Type.DOUBLE,
                             doc="Line pitch, default is 5.0mm"),
                   Parameter('line_style', type=Type.INT32_T,
                             doc="Line style"),
                   Parameter('line_color', type=Type.STRING,
                             doc="Line color")
               ]),

        Method('DirectionPlot_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Plot an arrow to indicate the direction of a flight line",
               notes="""
               An arrow will be drawn in the direction from the first valid
               to the last points in the X and Y VVs.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('size', type=Type.DOUBLE,
                             doc="Arrow size in mm"),
                   Parameter('loc', type=Type.DOUBLE,
                             doc="Location to draw in mm - can be X or Y depending on next parameter"),
                   Parameter('align', type=Type.INT32_T,
                             doc=":def:`ARROW_ALIGNMENT`")
               ]),

        Method('EMForward_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Plot an EM forward model against inverted data.",
               notes="""
               This function is designed to display an inverted result beside
               the forward model curves. This is useful for trouble-shooting
               or understanding why a certain inversion result was obtained.
               The earth model is a simple halfspace.

               The forward model is plotted either as a function of
               resistivity at a single height, or as a function of height at
               a single resistivity. In either case, the relevant VVs must be
               completely filled (even if one is all the same value).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('xo', type=Type.DOUBLE,
                             doc="Plot X origin"),
                   Parameter('yo', type=Type.DOUBLE,
                             doc="Plot Y origin"),
                   Parameter('size_x', type=Type.DOUBLE,
                             doc="Plot X size"),
                   Parameter('size_y', type=Type.DOUBLE,
                             doc="Plot Y size"),
                   Parameter('coil_sep', type=Type.DOUBLE,
                             doc="Coil Separation (m)"),
                   Parameter('coil_frequency', type=Type.DOUBLE,
                             doc="Coil Frequency (Hz)"),
                   Parameter('coil_configuration', type=Type.INT32_T,
                             doc=":def:`EMLAY_GEOMETRY`"),
                   Parameter('r', type=Type.DOUBLE,
                             doc="Inverted or current resistivity"),
                   Parameter('h', type=Type.DOUBLE,
                             doc="Inverted or current height"),
                   Parameter('i', type=Type.DOUBLE,
                             doc="In-phase datum"),
                   Parameter('q', type=Type.DOUBLE,
                             doc="Quadrature datum"),
                   Parameter('rvv', type="VV",
                             doc="Forward model resistivities"),
                   Parameter('hvv', type="VV",
                             doc="Forward model heights"),
                   Parameter('ivv', type="VV",
                             doc="Forward model In-phase (ppm)"),
                   Parameter('qvv', type="VV",
                             doc="Forward model Quadrature (ppm)"),
                   Parameter('lin_log', type=Type.INT32_T,
                             doc="Plot resistivity as linear (0) or log (1)"),
                   Parameter('var', type=Type.INT32_T,
                             doc="Plot as function of resistivity (0) or height (1)")
               ]),

        Method('ExportDatamineString_MVU', module='geoengine.interoperability', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Export selected map groups in a map view to a Datamine coordinate string file.",
               notes="""
               The lines, rectangles and polygons in the specified groups
               will be exported to a Datamine coordinate string (``*.dm``) file.
               The function attempts to duplicate the colors, etc. used.
               Complex polygon objects will be exported as independent
               single polygons.
               """,
               see_also=":class:`LST` class",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` with group names in the name part of the :class:`LST`."),
                   Parameter('file', type=Type.STRING,
                             doc="Datamine string file (``*.dm``) to export to")
               ]),

        Method('ExportDXF3D_MVU', module='geoengine.interoperability', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Export selected map groups in a map view to an AutoCAD 3D DXF file.",
               notes="Supported objects exported include lines, polygons, text.",
               see_also=":class:`LST` class",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` with group names in the name part of the :class:`LST`."),
                   Parameter('wa', type="WA",
                             doc="DXF file to export")
               ]),

        Method('ExportSurpacSTR_MVU', module='geoengine.interoperability', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Export selected map groups in a map view to a Surpac :class:`STR` file.",
               notes="""
               The lines, rectangles and polygons in the specified groups
               will be exported to a Surpac :class:`STR` file. An accompanying styles
               file will be created which will attempt to duplicate the
               colors, etc. used.
               Complex polygon objects will be exported as independent
               single polygons.
               """,
               see_also=":class:`LST` class",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` with group names in the name part of the :class:`LST`."),
                   Parameter('str_wa', type="WA",
                             doc=":class:`STR` file to export to"),
                   Parameter('styles_wa', type="WA",
                             doc="Styles file to export to")
               ]),

        Method('FlightPlot_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw a flight line",
               notes="""
               Current line color, thickness and style are used to
               draw the line.
               
               Current font, font color and font style are used to
               annotate the line labels.
               
               If current clipping is ON in the VIEW, lines will be
               clipped to the window before plotting.  In this case,
               labels should be located ABOVE or BELOW the line
               traces to prevent labels being clipped.
               
               The offsets dOffA and dOffB control the vertical and
               horizontal label offsets with respect to the ends of
               the line trace and depending on the label location.
               
               The vertical line reference angle dVerAng is used
               to determine if lines are considered vertical or
               horizontal.  Vertical lines use the sUp parameter
               to determine the label up direction.  Normally, use an
               angle of 60 degrees unless there are lines that run in
               this direction.
               """,
               see_also=":func:`PathPlot_MVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X"),
                   Parameter('vv_y', type="VV",
                             doc="Y"),
                   Parameter('line', type=Type.STRING,
                             doc="Line label"),
                   Parameter('locate', type=Type.INT32_T,
                             doc=":def:`MVU_FLIGHT_LOCATE`"),
                   Parameter('vangle', type=Type.DOUBLE,
                             doc="Lines steeper than this angle are considered vertical and the up label direction is used."),
                   Parameter('up', type=Type.INT32_T,
                             doc="Up label direction:   1 up is right, -1 up is left"),
                   Parameter('loff', type=Type.DOUBLE,
                             doc="Along line label offset in mm."),
                   Parameter('voff', type=Type.DOUBLE,
                             doc="Perpendicular label offset mm.")
               ]),

        Method('GenAreas_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Generate areas from an line group.",
               notes="""
               The specified line group will be used to create a new group that
               is composed of all the resolved polygonal areas in the line group.
               Each polygonal area is assigned a color/pattern as specified in the
               color and pattern :class:`VV`'s.  Color/patterns are assigned in rotating
               sequence.
               """,
               see_also=":func:`ReGenAreas_MVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('lines', type=Type.STRING,
                             doc="Group with lines"),
                   Parameter('col_vv', type="VV",
                             doc="Colors  (color int)"),
                   Parameter('pat_vv', type="VV",
                             doc="Patterns (int), must be same length at colors"),
                   Parameter('pitch', type=Type.DOUBLE,
                             doc="Pattern size")
               ]),

        Method('GetRangeGOCADSurface_MVU', module='geoengine.map', version='6.4.0',
               availability=Availability.LICENSED, 
               doc="Get the XYZ range of a GOCAD surface.",
               notes="""
               Required to set up a map view before doing the actual
               surface import.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="GOCAD file name"),
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="Min X value"),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="Min Y value"),
                   Parameter('min_z', type=Type.DOUBLE, is_ref=True,
                             doc="Min Z value"),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="Max X value"),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="Max Y value"),
                   Parameter('max_z', type=Type.DOUBLE, is_ref=True,
                             doc="Max Z value")
               ]),

        Method('Histogram_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Plot the histogram on a map.",
               notes="""
               This function just calls :func:`Histogram2_MVU` with decimals set
               to -7 (7 significant figures).
               """,
               see_also=":func:`Histogram2_MVU`, :func:`Histogram3_MVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('st_data', type="ST",
                             doc=":class:`ST` with summary stats of original data"),
                   Parameter('st_hist', type="ST",
                             doc=":class:`ST` with histogram info of original or log10 data"),
                   Parameter('title', type=Type.STRING,
                             doc="Title"),
                   Parameter('unit', type=Type.STRING,
                             doc="Unit"),
                   Parameter('xm', type=Type.DOUBLE,
                             doc="X in mm (bottom left corner of histogram box)"),
                   Parameter('ym', type=Type.DOUBLE,
                             doc="Y in mm (bottom left corner of histogram box)"),
                   Parameter('widthm', type=Type.DOUBLE,
                             doc="Box width in mm"),
                   Parameter('heightm', type=Type.DOUBLE,
                             doc="Box height in mm"),
                   Parameter('xd', type=Type.DOUBLE,
                             doc="Minimum X in data unit (bottom left corner of histogram boxes)"),
                   Parameter('yd', type=Type.DOUBLE,
                             doc="Minimum Y in data unit"),
                   Parameter('widthd', type=Type.DOUBLE,
                             doc="Box width in data unit"),
                   Parameter('heightd', type=Type.DOUBLE,
                             doc="Box height in data unit"),
                   Parameter('sum_width', type=Type.DOUBLE,
                             doc="Width (mm) of the additional box for summary stats"),
                   Parameter('log', type=Type.INT32_T,
                             doc="Log horizontal axis: 0 - Normal, 1 - Log"),
                   Parameter('summ', type=Type.INT32_T,
                             doc="Summary stats: 0 - do not draw, 1 - draw"),
                   Parameter('fill_color', type=Type.INT32_T,
                             doc="Fill color"),
                   Parameter('st_box', type="ST",
                             doc=":class:`ST` with histogram for box-whisker plot (-1 for no plot)")
               ]),

        Method('Histogram2_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Plot the histogram on a map.",
               notes="""
               A vertical line through from bottom to top horizontal axis is drawn
               Also a label 'Threshold value' is plotted against this line. However,
               None of them will be plotted if threshold value is dummy or outside
               the X data range.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('st_data', type="ST",
                             doc=":class:`ST` with summary stats of original data"),
                   Parameter('st_hist', type="ST",
                             doc=":class:`ST` with histogram info of original or log10 data"),
                   Parameter('x_title', type=Type.STRING,
                             doc="X axis title"),
                   Parameter('y_title', type=Type.STRING,
                             doc="Y axis title"),
                   Parameter('xy_txt_size', type=Type.DOUBLE,
                             doc="Text size in mm for X/Y axis' titles. Accept dummy"),
                   Parameter('title', type=Type.STRING,
                             doc="Overall title. Plotted below X axis if X axis title is not given"),
                   Parameter('plot_txt_size', type=Type.DOUBLE,
                             doc="Text size in mm for plot overall title. Accept dummy"),
                   Parameter('unit', type=Type.STRING,
                             doc="Unit"),
                   Parameter('xm', type=Type.DOUBLE,
                             doc="X in mm (bottom left corner of histogram box)"),
                   Parameter('ym', type=Type.DOUBLE,
                             doc="Y in mm (bottom left corner of histogram box)"),
                   Parameter('widthm', type=Type.DOUBLE,
                             doc="Box width in mm"),
                   Parameter('heightm', type=Type.DOUBLE,
                             doc="Box height in mm"),
                   Parameter('xd', type=Type.DOUBLE,
                             doc="Minimum X in data unit (bottom left corner of histogram boxes)"),
                   Parameter('yd', type=Type.DOUBLE,
                             doc="Minimum Y in data unit"),
                   Parameter('widthd', type=Type.DOUBLE,
                             doc="Box width in data unit"),
                   Parameter('heightd', type=Type.DOUBLE,
                             doc="Box height in data unit"),
                   Parameter('sum_width', type=Type.DOUBLE,
                             doc="Width (mm) of the additional box for summary stats"),
                   Parameter('log', type=Type.INT32_T,
                             doc="Log horizontal axis: 0 - Normal, 1 - Log"),
                   Parameter('summ', type=Type.INT32_T,
                             doc="Summary stats: 0 - do not draw, 1 - draw"),
                   Parameter('fill_color', type=Type.INT32_T,
                             doc="Fill color"),
                   Parameter('st_box', type="ST",
                             doc=":class:`ST` with histogram for box-wisker plot (-1 for no plot)"),
                   Parameter('x_marker', type=Type.DOUBLE,
                             doc="X value (threshold value) to draw a vertical line (see notes)")
               ]),

        Method('Histogram3_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Plot the histogram on a map, specify decimals.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('st_data', type="ST",
                             doc=":class:`ST` with summary stats of original data"),
                   Parameter('st_hist', type="ST",
                             doc=":class:`ST` with histogram info of original or log10 data"),
                   Parameter('title', type=Type.STRING,
                             doc="Title"),
                   Parameter('unit', type=Type.STRING,
                             doc="Unit"),
                   Parameter('xm', type=Type.DOUBLE,
                             doc="X in mm (bottom left corner of histogram box)"),
                   Parameter('ym', type=Type.DOUBLE,
                             doc="Y in mm (bottom left corner of histogram box)"),
                   Parameter('widthm', type=Type.DOUBLE,
                             doc="Box width in mm"),
                   Parameter('heightm', type=Type.DOUBLE,
                             doc="Box height in mm"),
                   Parameter('xd', type=Type.DOUBLE,
                             doc="Minimum X in data unit (bottom left corner of histogram boxes)"),
                   Parameter('yd', type=Type.DOUBLE,
                             doc="Minimum Y in data unit"),
                   Parameter('widthd', type=Type.DOUBLE,
                             doc="Box width in data unit"),
                   Parameter('heightd', type=Type.DOUBLE,
                             doc="Box height in data unit"),
                   Parameter('sum_width', type=Type.DOUBLE,
                             doc="Width (mm) of the additional box for summary stats"),
                   Parameter('log', type=Type.INT32_T,
                             doc="Log horizontal axis: 0 - Normal, 1 - Log"),
                   Parameter('summ', type=Type.INT32_T,
                             doc="Summary stats: 0 - do not draw, 1 - draw"),
                   Parameter('fill_color', type=Type.INT32_T,
                             doc="Fill color"),
                   Parameter('data_decimal', type=Type.INT32_T,
                             doc="Decimals for data, negative for sig. fig."),
                   Parameter('stat_decimal', type=Type.INT32_T,
                             doc="Decimals for stats, negative for sig. fig."),
                   Parameter('st_box', type="ST",
                             doc=":class:`ST` with histogram for box-whisker plot (-1 for no plot)")
               ]),

        Method('Histogram4_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="As :func:`Histogram3_MVU`, but allow probability scaling of percents.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('st_data', type="ST",
                             doc=":class:`ST` with summary stats of original data"),
                   Parameter('st_hist', type="ST",
                             doc=":class:`ST` with histogram info of original or log10 data"),
                   Parameter('title', type=Type.STRING,
                             doc="Title"),
                   Parameter('unit', type=Type.STRING,
                             doc="Unit"),
                   Parameter('xm', type=Type.DOUBLE,
                             doc="X in mm (bottom left corner of histogram box)"),
                   Parameter('ym', type=Type.DOUBLE,
                             doc="Y in mm (bottom left corner of histogram box)"),
                   Parameter('widthm', type=Type.DOUBLE,
                             doc="Box width in mm"),
                   Parameter('heightm', type=Type.DOUBLE,
                             doc="Box height in mm"),
                   Parameter('xd', type=Type.DOUBLE,
                             doc="Minimum X in data unit (bottom left corner of histogram boxes)"),
                   Parameter('yd', type=Type.DOUBLE,
                             doc="Minimum Y in data unit"),
                   Parameter('widthd', type=Type.DOUBLE,
                             doc="Box width in data unit"),
                   Parameter('heightd', type=Type.DOUBLE,
                             doc="Box height in data unit"),
                   Parameter('sum_width', type=Type.DOUBLE,
                             doc="Width (mm) of the additional box for summary stats"),
                   Parameter('log', type=Type.INT32_T,
                             doc="Log horizontal axis: 0 - Normal, 1 - Log"),
                   Parameter('summ', type=Type.INT32_T,
                             doc="Summary stats: 0 - do not draw, 1 - draw"),
                   Parameter('prob', type=Type.INT32_T,
                             doc="Probability scaling: 0 - linear scale, 1 - scale as normal distribution"),
                   Parameter('fill_color', type=Type.INT32_T,
                             doc="Fill color"),
                   Parameter('data_decimal', type=Type.INT32_T,
                             doc="Decimals for data, negative for sig. fig."),
                   Parameter('stat_decimal', type=Type.INT32_T,
                             doc="Decimals for stats, negative for sig. fig."),
                   Parameter('st_box', type="ST",
                             doc=":class:`ST` with histogram for box-whisker plot (-1 for no plot)")
               ]),

        Method('Histogram5_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="As :func:`Histogram4_MVU`, but allow :class:`ITR` to color bars.",
               notes="The :class:`ITR` can be empty (but must still be a valid :class:`ITR` object).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('st_data', type="ST",
                             doc=":class:`ST` with summary stats of original data"),
                   Parameter('st_hist', type="ST",
                             doc=":class:`ST` with histogram info of original or log10 data"),
                   Parameter('title', type=Type.STRING,
                             doc="Title"),
                   Parameter('unit', type=Type.STRING,
                             doc="Unit"),
                   Parameter('lmd', type=Type.DOUBLE,
                             doc="[i] Lambda Value"),
                   Parameter('xm', type=Type.DOUBLE,
                             doc="X in mm (bottom left corner of histogram box)"),
                   Parameter('ym', type=Type.DOUBLE,
                             doc="Y in mm (bottom left corner of histogram box)"),
                   Parameter('widthm', type=Type.DOUBLE,
                             doc="Box width in mm"),
                   Parameter('heightm', type=Type.DOUBLE,
                             doc="Box height in mm"),
                   Parameter('xd', type=Type.DOUBLE,
                             doc="Minimum X in data unit (bottom left corner of histogram boxes)"),
                   Parameter('yd', type=Type.DOUBLE,
                             doc="Minimum Y in data unit"),
                   Parameter('widthd', type=Type.DOUBLE,
                             doc="Box width in data unit"),
                   Parameter('heightd', type=Type.DOUBLE,
                             doc="Box height in data unit"),
                   Parameter('sum_width', type=Type.DOUBLE,
                             doc="Width (mm) of the additional box for summary stats"),
                   Parameter('log', type=Type.INT32_T,
                             doc="Log horizontal axis: 0 - Normal, 1 - Log, 2 - Lambda"),
                   Parameter('summ', type=Type.INT32_T,
                             doc="Summary stats: 0 - do not draw, 1 - draw"),
                   Parameter('prob', type=Type.INT32_T,
                             doc="Probability scaling: 0 - linear scale, 1 - scale as normal distribution"),
                   Parameter('fill_color', type=Type.INT32_T,
                             doc="Fill color"),
                   Parameter('data_decimal', type=Type.INT32_T,
                             doc="Decimals for data, negative for sig. fig."),
                   Parameter('stat_decimal', type=Type.INT32_T,
                             doc="Decimals for stats, negative for sig. fig."),
                   Parameter('st_box', type="ST",
                             doc=":class:`ST` with histogram for box-whisker plot (-1 for no plot)"),
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` to color bars.")
               ]),

        Method('iExportableDXF3DGroupsLST_MVU', module='geoengine.interoperability', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="Return a :class:`LST` of groups you can export using sExportDXF3D_MVU.",
               notes="""
               Returns a list of visible groups that the DXF 3D export can
               export. Removes things like :class:`VOXD`, :class:`AGG`, and target
               groups starting with "Dh", which are typically plotted in 3D
               views on a reference plan oriented toward the user, and thus
               not exportable.
               """,
               return_type=Type.INT32_T,
               return_doc="The number of groups in the :class:`LST`.",
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` with group names in the name part of the :class:`LST`.")
               ]),

        Method('iMapsetTest_MVU', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Test function to ensure parameters to :func:`Mapset_MVU` is sane",
               notes="""
               Use :func:`ShowError_SYS` to display errors that may have been encountered. This function can also be used
               to calculate the default scale without creating a map.
               """,
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL` TRUE if the parameters are good.",
               parameters = [
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Minimum X of data area (data units)"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Maximum X of data area (data units)"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Minimum Y of data area (data units)"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Maximum Y of data area (data units)"),
                   Parameter('size', type=Type.STRING,
                             doc="Media size as a string 'x_cm,y_cm', or a standard paper size (e.g. 'A4', 'E')"),
                   Parameter('port', type=Type.INT32_T,
                             doc="0 - landscape; 1 - portrait"),
                   Parameter('exact', type=Type.INT32_T,
                             doc="1 - map size fixed to media; 0 - map size adjusted to data and margins."),
                   Parameter('scale', type=Type.DOUBLE, is_ref=True,
                             doc="Map scale (rDummy for default)"),
                   Parameter('conv', type=Type.DOUBLE,
                             doc="Conversion factor (to units/meter) (rDummy for default)"),
                   Parameter('marg_xmin', type=Type.DOUBLE,
                             doc="Left margin (cm)"),
                   Parameter('marg_xmax', type=Type.DOUBLE,
                             doc="Right margin (cm)"),
                   Parameter('marg_ymin', type=Type.DOUBLE,
                             doc="Bottom margin (cm)"),
                   Parameter('marg_ymax', type=Type.DOUBLE,
                             doc="Top margin (cm)"),
                   Parameter('inside', type=Type.DOUBLE,
                             doc="Inside data margin (cm)")
               ]),

        Method('iMapset2Test_MVU', module='geoengine.map', version='8.3.0',
               availability=Availability.LICENSED, 
               doc="Test function to ensure parameters to :func:`Mapset_MVU` is sane",
               notes="Same as :func:`iMapsetTest_MVU`, with vertical exaggeration.",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL` TRUE if the parameters are good.",
               parameters = [
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Minimum X of data area (data units)"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Maximum X of data area (data units)"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Minimum Y of data area (data units)"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Maximum Y of data area (data units)"),
                   Parameter('size', type=Type.STRING,
                             doc="Media size as a string 'x_cm,y_cm', or a standard paper size (e.g. 'A4', 'E')"),
                   Parameter('port', type=Type.INT32_T,
                             doc="0 - landscape; 1 - portrait"),
                   Parameter('exact', type=Type.INT32_T,
                             doc="1 - map size fixed to media; 0 - map size adjusted to data and margins."),
                   Parameter('scale', type=Type.DOUBLE, is_ref=True,
                             doc="Map scale (rDummy for default)"),
                   Parameter('vert_exag', type=Type.DOUBLE,
                             doc="Vertical exaggeration (Normally 1.0)"),
                   Parameter('conv', type=Type.DOUBLE,
                             doc="Conversion factor (to units/meter) (rDummy for default)"),
                   Parameter('marg_xmin', type=Type.DOUBLE,
                             doc="Left margin (cm)"),
                   Parameter('marg_xmax', type=Type.DOUBLE,
                             doc="Right margin (cm)"),
                   Parameter('marg_ymin', type=Type.DOUBLE,
                             doc="Bottom margin (cm)"),
                   Parameter('marg_ymax', type=Type.DOUBLE,
                             doc="Top margin (cm)"),
                   Parameter('inside', type=Type.DOUBLE,
                             doc="Inside data margin (cm)")
               ]),

        Method('ImportGOCADSurface_MVU', module='geoengine.map', version='6.4.0',
               availability=Availability.LICENSED, 
               doc="Import and plot a GOCAD surface model.",
               notes="""
               The vertex normals are not included in the
               GOCAD import, but are calculated using
               the normal of each defined triangle, and taking the
               average when vertex is shared among more than one triangle.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('file', type=Type.STRING,
                             doc="GOCAD file name"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Color to plot (:def_val:`C_TRANSPARENT` to use file-defined color).")
               ]),

        Method('LoadPlot_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Load a Geosoft PLT file into a :class:`MAP`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('map', type="MAP",
                             doc="Map handle"),
                   Parameter('name', type=Type.STRING,
                             doc="Plot file name")
               ]),

        Method('MapFromPLT_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates a new map from a PLT file.",
               notes="""
               This only creates a map, it does not read the PLT into
               the map.  The base view and data view will be the same
               size.
               """,
               see_also=":func:`LoadPlot_MVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('map', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('base', type=Type.STRING,
                             doc="Name to use for the base map view"),
                   Parameter('data', type=Type.STRING,
                             doc="Name to use for the data view"),
                   Parameter('plt', type=Type.STRING,
                             doc="Plot file name"),
                   Parameter('mpx', type=Type.DOUBLE,
                             doc="Map paper size in X direction (cm)"),
                   Parameter('mpy', type=Type.DOUBLE,
                             doc="Map paper size in Y direction (cm)")
               ]),

        Method('MapMDF_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates an MDF from a Map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('map', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('mdf', type=Type.STRING,
                             doc="MDF file name"),
                   Parameter('data', type=Type.STRING,
                             doc="Data view name")
               ]),

        Method('Mapset_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates a new map directly from parameters.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('map', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('base', type=Type.STRING,
                             doc="Name to use for the base map view"),
                   Parameter('data', type=Type.STRING,
                             doc="Name to use for the data view"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Minimum X of data area (data units)"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Maximum X of data area (data units)"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Minimum Y of data area (data units)"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Maximum Y of data area (data units)"),
                   Parameter('size', type=Type.STRING,
                             doc="Media size as a string 'x_cm,y_cm', or a standard paper size (e.g. 'A4', 'E')"),
                   Parameter('port', type=Type.INT32_T,
                             doc="0 - landscape; 1 - portrait"),
                   Parameter('exact', type=Type.INT32_T,
                             doc="1 - map size fixed to media; 0 - map size adjusted to data and margins."),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="Map scale (rDummy for default)"),
                   Parameter('conv', type=Type.DOUBLE,
                             doc="Conversion factor (to units/meter) (rDummy for default)"),
                   Parameter('marg_xmin', type=Type.DOUBLE,
                             doc="Left margin (cm)"),
                   Parameter('marg_xmax', type=Type.DOUBLE,
                             doc="Right margin (cm)"),
                   Parameter('marg_ymin', type=Type.DOUBLE,
                             doc="Bottom margin (cm)"),
                   Parameter('marg_ymax', type=Type.DOUBLE,
                             doc="Top margin (cm)"),
                   Parameter('inside', type=Type.DOUBLE,
                             doc="Inside data margin (cm)")
               ]),

        Method('Mapset2_MVU', module='geoengine.map', version='8.3.0',
               availability=Availability.PUBLIC, 
               doc="Same as :func:`Mapset_MVU`, with vertical exaggeration.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('map', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('base', type=Type.STRING,
                             doc="Name to use for the base map view"),
                   Parameter('data', type=Type.STRING,
                             doc="Name to use for the data view"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Minimum X of data area (data units)"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Maximum X of data area (data units)"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Minimum Y of data area (data units)"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Maximum Y of data area (data units)"),
                   Parameter('size', type=Type.STRING,
                             doc="Media size as a string 'x_cm,y_cm', or a standard paper size (e.g. 'A4', 'E')"),
                   Parameter('port', type=Type.INT32_T,
                             doc="0 - landscape; 1 - portrait"),
                   Parameter('exact', type=Type.INT32_T,
                             doc="1 - map size fixed to media; 0 - map size adjusted to data and margins."),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="Map scale (rDummy for default)"),
                   Parameter('vert_exag', type=Type.DOUBLE,
                             doc="Vertical Exaggeration (1.0 for none)"),
                   Parameter('conv', type=Type.DOUBLE,
                             doc="Conversion factor (to units/meter) (rDummy for default)"),
                   Parameter('marg_xmin', type=Type.DOUBLE,
                             doc="Left margin (cm)"),
                   Parameter('marg_xmax', type=Type.DOUBLE,
                             doc="Right margin (cm)"),
                   Parameter('marg_ymin', type=Type.DOUBLE,
                             doc="Bottom margin (cm)"),
                   Parameter('marg_ymax', type=Type.DOUBLE,
                             doc="Top margin (cm)"),
                   Parameter('inside', type=Type.DOUBLE,
                             doc="Inside data margin (cm)")
               ]),

        Method('MDF_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates a new map from an MDF file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('map', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('mdf', type=Type.STRING,
                             doc="MDF file name"),
                   Parameter('base', type=Type.STRING,
                             doc="Name to use for the base map view"),
                   Parameter('data', type=Type.STRING,
                             doc="Name to use for the data view")
               ]),

        Method('PathPlot_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw a flight line",
               notes="""
               See :func:`FlightPlot_MVU`.  This is the same except for the
               additional line gap parameter.
               """,
               see_also="FlighPlot_MVU",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X"),
                   Parameter('vv_y', type="VV",
                             doc="Y"),
                   Parameter('line', type=Type.STRING,
                             doc="Line label"),
                   Parameter('locate', type=Type.INT32_T,
                             doc=":def:`MVU_FLIGHT_LOCATE`"),
                   Parameter('vangle', type=Type.DOUBLE,
                             doc="Lines steeper than this angle are considered vertical and the up label direction is used."),
                   Parameter('up', type=Type.INT32_T,
                             doc="Up label direction:   1 up is right -1 up is left"),
                   Parameter('loff', type=Type.DOUBLE,
                             doc="Along line label offset in mm."),
                   Parameter('voff', type=Type.DOUBLE,
                             doc="Perpendicular label offset mm."),
                   Parameter('gap', type=Type.DOUBLE,
                             doc="Maximum gap before breaking line, 0.0 for no breaks.")
               ]),

        Method('PathPlotEx_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw a flight line",
               notes="This is the same except for the additional line compass parameter.",
               see_also=":func:`PathPlot_MVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X"),
                   Parameter('vv_y', type="VV",
                             doc="Y"),
                   Parameter('line', type=Type.STRING,
                             doc="Line label"),
                   Parameter('locate', type=Type.INT32_T,
                             doc=":def:`MVU_FLIGHT_LOCATE`"),
                   Parameter('compass', type=Type.INT32_T,
                             doc=":def:`MVU_FLIGHT_COMPASS`"),
                   Parameter('vangle', type=Type.DOUBLE,
                             doc="Lines steeper than this angle are considered vertical and the up label direction is used."),
                   Parameter('up', type=Type.INT32_T,
                             doc="Up label direction:   1 up is right -1 up is left"),
                   Parameter('loff', type=Type.DOUBLE,
                             doc="Along line label offset in mm."),
                   Parameter('voff', type=Type.DOUBLE,
                             doc="Perpendicular label offset mm."),
                   Parameter('gap', type=Type.DOUBLE,
                             doc="Maximum gap before breaking line, 0.0 for no breaks.")
               ]),

        Method('PathPlotEx2_MVU', module='geoengine.map', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Draw a flight line",
               notes="This is the same except for the additional line dummies parameter.",
               see_also=":func:`PathPlotEx_MVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X"),
                   Parameter('vv_y', type="VV",
                             doc="Y"),
                   Parameter('line', type=Type.STRING,
                             doc="Line label"),
                   Parameter('locate', type=Type.INT32_T,
                             doc=":def:`MVU_FLIGHT_LOCATE`"),
                   Parameter('compass', type=Type.INT32_T,
                             doc=":def:`MVU_FLIGHT_COMPASS`"),
                   Parameter('vangle', type=Type.DOUBLE,
                             doc="Lines steeper than this angle are considered vertical and the up label direction is used."),
                   Parameter('up', type=Type.INT32_T,
                             doc="Up label direction:   1 up is right -1 up is left"),
                   Parameter('loff', type=Type.DOUBLE,
                             doc="Along line label offset in mm."),
                   Parameter('voff', type=Type.DOUBLE,
                             doc="Perpendicular label offset mm."),
                   Parameter('gap', type=Type.DOUBLE,
                             doc="Maximum gap before breaking line, 0.0 for no breaks."),
                   Parameter('dummies', type=Type.INT32_T,
                             doc=":def:`MVU_FLIGHT_DUMMIES`")
               ]),

        Method('PlotVoxelSurface_MVU', module='geoengine.map', version='6.4.0',
               availability=Availability.LICENSED, 
               doc="Extract an iso-surface from a voxel and plot it to a 2D or 3D view.",
               notes="""
               The Marching Cubes method of Lorensen and Cline, Computer Graphics, V21,
               Number 4, July 1987, is used to calculate a given iso-surface in a voxel
               model. The resulting surface is plotted to a 2D or 3D view. If the view
               is 2-D, then only the intersection of the surface with the 2D surface is
               plotted, using lines.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vox', type="VOX",
                             doc="Voxel model"),
                   Parameter('value', type=Type.DOUBLE,
                             doc="Iso-surface value"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Drawing color"),
                   Parameter('line_thick', type=Type.DOUBLE,
                             doc="Line thickness for line drawing, and 2D views.")
               ]),

        Method('PlotVoxelSurface2_MVU', module='geoengine.map', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Extract an iso-surface from a voxel and plot it to a 2D or 3D view.",
               notes="""
               The Marching Cubes method of Lorensen and Cline, Computer Graphics, V21,
               Number 4, July 1987, is used to calculate a given iso-surface in a voxel
               model. The resulting surface is plotted to a 2D or 3D view. If the view
               is 2-D, then only the intersection of the surface with the 2D surface is
               plotted, using lines.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vox', type="VOX",
                             doc="Voxel model"),
                   Parameter('value', type=Type.DOUBLE,
                             doc="Iso-surface value"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Drawing color"),
                   Parameter('line_thick', type=Type.DOUBLE,
                             doc="Line thickness for line drawing, and 2D views."),
                   Parameter('transparency', type=Type.DOUBLE,
                             doc="Transparency (0 - transparent, 1 - opaque)."),
                   Parameter('surface_name', type=Type.STRING,
                             doc="Iso-surface name")
               ]),

        Method('GenerateSurfaceFromVoxel_MVU', module='geoengine.map', version='8.5.0',
               availability=Availability.LICENSED, 
               doc="TODO...",
               notes="TODO... Move to :class:`VOX` method for surface generation only and use GeosurfaceD to display.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vox', type="VOX",
                             doc="Voxel model"),
                   Parameter('method', type=Type.INT32_T,
                             doc=":def:`MVU_VOX_SURFACE_METHOD`"),
                   Parameter('option', type=Type.INT32_T,
                             doc=":def:`MVU_VOX_SURFACE_OPTION`"),
                   Parameter('min_value', type=Type.DOUBLE,
                             doc="TODO"),
                   Parameter('max_value', type=Type.DOUBLE,
                             doc="TODO"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Drawing color"),
                   Parameter('line_thick', type=Type.DOUBLE,
                             doc="Line thickness for line drawing, and 2D views."),
                   Parameter('transparency', type=Type.DOUBLE,
                             doc="Transparency (0 - transparent, 1 - opaque)."),
                   Parameter('surface_name', type=Type.STRING,
                             doc="Geosurface file")
               ]),

        Method('Post_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Post values on a map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X locations"),
                   Parameter('vv_y', type="VV",
                             doc="Y locations"),
                   Parameter('vv_z', type="VV",
                             doc="Values to post"),
                   Parameter('dummy', type=Type.INT32_T,
                             doc="Do not plot dummy values? :def:`GEO_BOOL`"),
                   Parameter('size', type=Type.INT32_T,
                             doc="Numb Size"),
                   Parameter('format', type=Type.INT32_T,
                             doc="Format"),
                   Parameter('decimals', type=Type.INT32_T,
                             doc="Decimals"),
                   Parameter('ref', type=Type.INT32_T,
                             doc="Reference point number"),
                   Parameter('angle', type=Type.DOUBLE,
                             doc="Text angle")
               ]),

        Method('PostEx_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Post values on a map with more paramters.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X locations"),
                   Parameter('vv_y', type="VV",
                             doc="Y locations"),
                   Parameter('vv_z', type="VV",
                             doc="Values to post"),
                   Parameter('vv_s', type="VV",
                             doc="Station"),
                   Parameter('dummy', type=Type.INT32_T,
                             doc="Do not plot dummy values? :def:`GEO_BOOL`"),
                   Parameter('base', type=Type.DOUBLE,
                             doc="Base to remove, default is 0.0"),
                   Parameter('min_detect', type=Type.DOUBLE,
                             doc="Detection limit, can be :def_val:`GS_R8DM`"),
                   Parameter('size', type=Type.INT32_T,
                             doc="Numb Size"),
                   Parameter('format', type=Type.INT32_T,
                             doc="Format"),
                   Parameter('decimals', type=Type.INT32_T,
                             doc="Decimals"),
                   Parameter('offset_l', type=Type.DOUBLE,
                             doc="Offset along line (right and above are positive)"),
                   Parameter('offset_p', type=Type.DOUBLE,
                             doc="Offset perpendicular to line"),
                   Parameter('alternate', type=Type.INT32_T,
                             doc="TRUE - Positive above, Negative below FALSE - All above."),
                   Parameter('mod', type=Type.DOUBLE,
                             doc="Modulas on station vv"),
                   Parameter('ref', type=Type.INT32_T,
                             doc="Reference point number"),
                   Parameter('angle', type=Type.DOUBLE,
                             doc="Text angle (degree, CCW from down-line)"),
                   Parameter('fixed', type=Type.INT32_T,
                             doc="Fixed angle ?"),
                   Parameter('ref_ang', type=Type.DOUBLE,
                             doc="Vertical reference angle"),
                   Parameter('up', type=Type.INT32_T,
                             doc="1 up is right, -1 up is left")
               ]),

        Method('Probability_MVU', module='geoengine.map', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Plot a probability plot on a map.",
               notes="The :class:`ITR` can be empty (but must still be a valid :class:`ITR` object).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('st_data', type="ST",
                             doc=":class:`ST` with summary stats of original data"),
                   Parameter('st_hist', type="ST",
                             doc=":class:`ST` with histogram info of original or log10 data"),
                   Parameter('title', type=Type.STRING,
                             doc="Title"),
                   Parameter('unit', type=Type.STRING,
                             doc="Unit"),
                   Parameter('transform', type=Type.INT32_T,
                             doc="Transform type (0: Raw, 1: Log, 2: Lambda)"),
                   Parameter('lmd', type=Type.DOUBLE,
                             doc="Lambda Value for lambda transform"),
                   Parameter('xm', type=Type.DOUBLE,
                             doc="X in mm (bottom left corner of histogram box)"),
                   Parameter('ym', type=Type.DOUBLE,
                             doc="Y in mm (bottom left corner of histogram box)"),
                   Parameter('widthm', type=Type.DOUBLE,
                             doc="Box width in mm"),
                   Parameter('heightm', type=Type.DOUBLE,
                             doc="Box height in mm"),
                   Parameter('symb_size', type=Type.DOUBLE,
                             doc="Symbol size in mm"),
                   Parameter('sigma', type=Type.DOUBLE,
                             doc="Sigma (X range is -sigma to sigma)"),
                   Parameter('sum_width', type=Type.DOUBLE,
                             doc="Width (mm) of the additional box for summary stats"),
                   Parameter('summ', type=Type.INT32_T,
                             doc="Summary stats: 0 - do not draw, 1 - draw"),
                   Parameter('data_decimal', type=Type.INT32_T,
                             doc="Decimals for data, negative for sig. fig."),
                   Parameter('stat_decimal', type=Type.INT32_T,
                             doc="Decimals for stats, negative for sig. fig."),
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` to color symbols.")
               ]),

        Method('ProfilePlot_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw a profile along line trace",
               notes="Profiles will be drawn in the current line style.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X"),
                   Parameter('vv_y', type="VV",
                             doc="Y"),
                   Parameter('vv_z', type="VV",
                             doc="Z"),
                   Parameter('vangle', type=Type.DOUBLE,
                             doc="Lines steeper than this angle are considered vertical and the up label direction is used."),
                   Parameter('up', type=Type.INT32_T,
                             doc="Up label direction:   1 up is right -1 up is left"),
                   Parameter('gap', type=Type.DOUBLE,
                             doc="Maximum gap in data to span (view units)"),
                   Parameter('base', type=Type.DOUBLE,
                             doc="Z profile base, :def_val:`rDUMMY` to use data minimum"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="Z scale in view units/Z unit"),
                   Parameter('join', type=Type.INT32_T,
                             doc="1 to join profile to line ends.")
               ]),

        Method('ProfilePlotEx_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw a profile along line trace with more parameters",
               notes="Profiles will be drawn in the current line style.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X"),
                   Parameter('vv_y', type="VV",
                             doc="Y"),
                   Parameter('vv_z', type="VV",
                             doc="Z"),
                   Parameter('vangle', type=Type.DOUBLE,
                             doc="Lines steeper than this angle are considered vertical and the up label direction is used."),
                   Parameter('up', type=Type.INT32_T,
                             doc="Up label direction:   1 up is right -1 up is left"),
                   Parameter('gap', type=Type.DOUBLE,
                             doc="Maximum gap in data to span (view units)"),
                   Parameter('base', type=Type.DOUBLE,
                             doc="Z profile base, :def_val:`rDUMMY` to use data minimum"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="Z scale in view units/Z unit"),
                   Parameter('join', type=Type.INT32_T,
                             doc="1 to join profile to line ends."),
                   Parameter('log', type=Type.INT32_T,
                             doc="Log option: 0 linear (default), 1 logarithm, 2 log/linear"),
                   Parameter('log_base', type=Type.DOUBLE,
                             doc="Log base"),
                   Parameter('smooth', type=Type.INT32_T,
                             doc="Smooth curve option: 0 no (default), 1 yes"),
                   Parameter('pos_f_color', type=Type.STRING,
                             doc="Positive fill color"),
                   Parameter('neg_f_color', type=Type.STRING,
                             doc="Negative fill color")
               ]),

        Method('PropSymbLegend_MVU', module='geoengine.map', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Draw a legend for proportional symbols.",
               notes="""
               All symbol attributes, except for the size, are assumed
               to be defined (or defaults are used).
               Spacing is based on the maximum of the largest plotted symbol
               and the font size.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('x1', type=Type.DOUBLE,
                             doc="Plot origin X"),
                   Parameter('y1', type=Type.DOUBLE,
                             doc="Plot origin Y"),
                   Parameter('font_size', type=Type.DOUBLE,
                             doc="Label Font size (mm)"),
                   Parameter('symb_scale', type=Type.DOUBLE,
                             doc="Symbol scale factor (data value/mm)"),
                   Parameter('base', type=Type.DOUBLE,
                             doc="Base value to remove before scaling"),
                   Parameter('n_symb', type=Type.INT32_T,
                             doc="Number of symbols"),
                   Parameter('start', type=Type.DOUBLE,
                             doc="Starting symbol data value (>= Base value)"),
                   Parameter('increment', type=Type.DOUBLE,
                             doc="Data value increment (>0.0)"),
                   Parameter('title', type=Type.STRING,
                             doc="Plot title"),
                   Parameter('sub_title', type=Type.STRING,
                             doc="Plot subtitle")
               ]),

        Method('ReGenAreas_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Re-Generate from a line group and existing area group",
               notes="""
               The area group must exist and will be modified to match the current
               line group.
               
               All non-polygon entities in the current area group will remain in the
               new area group.  All existing polygon groups will be used to determine
               the most likely attributes for the new polygon groups.
               
               There must be existing polygon groups in the area group.
               """,
               see_also=":func:`GenAreas_MVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('lines', type=Type.STRING,
                             doc="Group with lines")
               ]),

        Method('SymbOff_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draws symbols with an offset and against a flag channel",
               notes="""
               Symbols are not plotted for positions where the flag :class:`VV`
               value is 0 or :def_val:`iDUMMY`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X, must be type of REAL"),
                   Parameter('vv_y', type="VV",
                             doc="Y, must be type of REAL"),
                   Parameter('vv_f', type="VV",
                             doc="Flag :class:`VV`, must be type of INT"),
                   Parameter('x_off', type=Type.DOUBLE,
                             doc="X Offset"),
                   Parameter('y_off', type=Type.DOUBLE,
                             doc="Y Offset")
               ]),

        Method('TextBox_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw a wrapped text box",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('xmin', type=Type.DOUBLE,
                             doc="Min X"),
                   Parameter('ymin', type=Type.DOUBLE,
                             doc="Min Y"),
                   Parameter('xmax', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('ymax', type=Type.DOUBLE,
                             doc="Max Y"),
                   Parameter('text', type=Type.STRING,
                             doc="Text"),
                   Parameter('space', type=Type.DOUBLE,
                             doc="Line spacing (1.2 good)"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`MVU_TEXTBOX`")
               ]),

        Method('Tick_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw line ticks on a map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X locations"),
                   Parameter('vv_y', type="VV",
                             doc="Y locations"),
                   Parameter('vv_s', type="VV",
                             doc="Station"),
                   Parameter('size', type=Type.DOUBLE,
                             doc="Tick size"),
                   Parameter('mod', type=Type.DOUBLE,
                             doc="Tick modulus on station vv"),
                   Parameter('mt_size', type=Type.DOUBLE,
                             doc="Major tick size"),
                   Parameter('mt_mod', type=Type.DOUBLE,
                             doc="Major tick modulus on station vv")
               ]),

        Method('TickEx_MVU', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Same as :func:`Tick_MVU`, with gap allowance.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X locations"),
                   Parameter('vv_y', type="VV",
                             doc="Y locations"),
                   Parameter('vv_s', type="VV",
                             doc="Station"),
                   Parameter('size', type=Type.DOUBLE,
                             doc="Tick size"),
                   Parameter('mod', type=Type.DOUBLE,
                             doc="Tick modulus on station vv"),
                   Parameter('mt_size', type=Type.DOUBLE,
                             doc="Major tick size"),
                   Parameter('mt_mod', type=Type.DOUBLE,
                             doc="Major tick modulus on station vv"),
                   Parameter('gap', type=Type.DOUBLE,
                             doc="Maximum gap to span; set to 0 or :def_val:`rDUMMY` to ignore all gaps.")
               ]),

        Method('TrndPath_MVU', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Plot min and max trend lines.",
               notes="""
               Trend lines positions consist of X and Y VVs
               interspersed with dummies, which separate the
               individual trend sections.
               Set the minimum number of sections to > 0 to
               plot only the longer trend lines.
               (The number of sections in one trend section is
               equal to the number of points between dummies minus one.)
               Set the minimum distance to > 0 to
               plot only the longer trend lines.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv_x', type="VV",
                             doc="X"),
                   Parameter('vv_y', type="VV",
                             doc="Y"),
                   Parameter('min_sect', type=Type.INT32_T,
                             doc="Minimum number of sections"),
                   Parameter('min_dist', type=Type.DOUBLE,
                             doc="Minimum length of sections")
               ])
    ],
    'Obsolete': [

        Method('PlotVoxelSurface3_MVU', module='geoengine.map', version='8.3.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Extract an iso-surface from a voxel and plot it to a 2D or 3D view.",
               notes="Same as :func:`PlotVoxelSurface2_MVU` but with a couple more options.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vox', type="VOX",
                             doc="Voxel model"),
                   Parameter('value', type=Type.DOUBLE,
                             doc="Iso-surface value"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Drawing color"),
                   Parameter('line_thick', type=Type.DOUBLE,
                             doc="Line thickness for line drawing, and 2D views."),
                   Parameter('transparency', type=Type.DOUBLE,
                             doc="Transparency (0 - transparent, 1 - opaque)."),
                   Parameter('surface_name', type=Type.STRING,
                             doc="Iso-surface name"),
                   Parameter('create_closed_geosurface_around_voxel', type=Type.INT32_T,
                             doc="Create closed geosurface around voxel? :def:`GEO_BOOL`"),
                   Parameter('enclose_cells_less_than_surface_value', type=Type.INT32_T,
                             doc="Closed geosurface should enclose cells LESS than surface value? :def:`GEO_BOOL`"),
                   Parameter('exclude_objects_with_volume_less_than_this_value', type=Type.DOUBLE,
                             doc="Exclude objects with volume less than this value")
               ]),

        Method('DuplicateChem_MVU', module='geochimera', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Plot an ASSAY Duplicate result in a graph window.",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv', type="VV",
                             doc="Duplicate data"),
                   Parameter('log', type=Type.INT32_T,
                             doc="Log-transform: 0 - linear, 1 - log"),
                   Parameter('det_lim', type=Type.DOUBLE,
                             doc="Detect Limit"),
                   Parameter('old', type=Type.INT32_T,
                             doc="Number of old samples in the :class:`VV`"),
                   Parameter('tol', type=Type.DOUBLE,
                             doc="Tolerance as a function of std dev"),
                   Parameter('title', type=Type.STRING,
                             doc="Title"),
                   Parameter('unit', type=Type.STRING,
                             doc="Unit"),
                   Parameter('x0', type=Type.DOUBLE,
                             doc="X location (bottom left corner of graph)"),
                   Parameter('y0', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('xs', type=Type.DOUBLE,
                             doc="Graph width"),
                   Parameter('ys', type=Type.DOUBLE,
                             doc="Graph height")
               ]),

        Method('Scatter_MVU', module='geochimera', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Plot the scatter plot on a map.",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('view', type="MVIEW",
                             doc="View"),
                   Parameter('title', type=Type.STRING,
                             doc="Title"),
                   Parameter('x_loc', type=Type.DOUBLE,
                             doc="X location (bottom left corner of color boxes)"),
                   Parameter('y_loc', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('box_width', type=Type.DOUBLE,
                             doc="Box width"),
                   Parameter('box_height', type=Type.DOUBLE,
                             doc="Box height"),
                   Parameter('horiz_chan_vv', type="VV",
                             doc="Horizontal channel"),
                   Parameter('vert_chan_vv', type="VV",
                             doc="Vertical channel"),
                   Parameter('mask_chan', type="VV",
                             doc="Mask channel"),
                   Parameter('horiz_chan_name', type=Type.STRING,
                             doc="Horizontal channel name"),
                   Parameter('vert_chan_name', type=Type.STRING,
                             doc="Vertical channel name"),
                   Parameter('mask_chan_name', type=Type.STRING,
                             doc="Mask channel name"),
                   Parameter('horiz_chan_units', type=Type.STRING,
                             doc="Horizontal channel units"),
                   Parameter('vert_chan_units', type=Type.STRING,
                             doc="Vertical channel units"),
                   Parameter('min_horiz_val', type=Type.DOUBLE,
                             doc="Min. Horizontal value"),
                   Parameter('max_horiz_val', type=Type.DOUBLE,
                             doc="Max. Horizontal value"),
                   Parameter('min_vert_val', type=Type.DOUBLE,
                             doc="Min. Vertical value"),
                   Parameter('max_vert_val', type=Type.DOUBLE,
                             doc="Max. Vertical value"),
                   Parameter('min_horiz_range', type=Type.DOUBLE,
                             doc="Min. Horizontal range value"),
                   Parameter('max_horiz_range', type=Type.DOUBLE,
                             doc="Max. Horizontal range value"),
                   Parameter('min_vert_range', type=Type.DOUBLE,
                             doc="Min. Vertical range value"),
                   Parameter('max_vert_range', type=Type.DOUBLE,
                             doc="Max. Vertical range value"),
                   Parameter('use_min_horiz_sel', type=Type.INT32_T,
                             doc="Use Min Horz. Range selection?"),
                   Parameter('use_max_horiz_sel', type=Type.INT32_T,
                             doc="Use Max Horz. Range selection?"),
                   Parameter('use_min_vert_sel', type=Type.INT32_T,
                             doc="Use Min Vert. Range selection?"),
                   Parameter('use_max_vert_sel', type=Type.INT32_T,
                             doc="Use Max Vert. Range selection?"),
                   Parameter('use_linear_horiz_axis_scaling', type=Type.INT32_T,
                             doc="Use linear horizontal axis scaling?"),
                   Parameter('use_linear_vert_axis_scaling', type=Type.INT32_T,
                             doc="Use linear vertical axis scaling?"),
                   Parameter('symbol_size', type=Type.INT32_T,
                             doc="Symbol size (0: small, 1: medium, 2: large)")
               ]),

        Method('Scatter2_MVU', module='geochimera', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Plot the scatter plot on a map using symbol number, size and color VVs.",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location (bottom left corner of box)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Box width"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Box height"),
                   Parameter('p7', type="VV",
                             doc="Horizontal channel"),
                   Parameter('p8', type="VV",
                             doc="Vertical channel"),
                   Parameter('p9', type=Type.STRING,
                             doc='Decorated font name, "" for default symbol font (normally symbols.gfn)'),
                   Parameter('p10', type="VV",
                             doc="Symbol numbers"),
                   Parameter('p11', type="VV",
                             doc="Symbol sizes"),
                   Parameter('p12', type="VV",
                             doc="Colors  if symbol number or color == 0, do not plot"),
                   Parameter('p13', type=Type.INT32_T,
                             doc="Annotation style 0 - outside, 1 - inside"),
                   Parameter('p14', type=Type.STRING,
                             doc="Horizontal channel name"),
                   Parameter('p15', type=Type.STRING,
                             doc="Vertical channel name"),
                   Parameter('p16', type=Type.STRING,
                             doc="Horizontal channel units"),
                   Parameter('p17', type=Type.STRING,
                             doc="Vertical channel units"),
                   Parameter('p18', type=Type.DOUBLE,
                             doc="Min. Horizontal value, :def_val:`rDUMMY` for default"),
                   Parameter('p19', type=Type.DOUBLE,
                             doc="Max. Horizontal value"),
                   Parameter('p20', type=Type.DOUBLE,
                             doc="Min. Vertical value"),
                   Parameter('p21', type=Type.DOUBLE,
                             doc="Max. Vertical value"),
                   Parameter('p22', type=Type.DOUBLE,
                             doc="Min. Horizontal range value"),
                   Parameter('p23', type=Type.DOUBLE,
                             doc="Max. Horizontal range value"),
                   Parameter('p24', type=Type.DOUBLE,
                             doc="Min. Vertical range value"),
                   Parameter('p25', type=Type.DOUBLE,
                             doc="Max. Vertical range value"),
                   Parameter('p26', type=Type.INT32_T,
                             doc="Use Min Horz. Range selection?"),
                   Parameter('p27', type=Type.INT32_T,
                             doc="Use Max Horz. Range selection?"),
                   Parameter('p28', type=Type.INT32_T,
                             doc="Use Min Vert. Range selection?"),
                   Parameter('p29', type=Type.INT32_T,
                             doc="Use Max Vert. Range selection?"),
                   Parameter('p30', type=Type.INT32_T,
                             doc="Horizontal axis scaling: 0 - linear, 1 - log"),
                   Parameter('p31', type=Type.INT32_T,
                             doc="Vertical axis scaling")
               ]),

        Method('Standard_MVU', module='geochimera', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Plot an ASSAY standard result in a graph window.",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc="View"),
                   Parameter('vv', type="VV",
                             doc="Standard data"),
                   Parameter('old', type=Type.INT32_T,
                             doc="Number of old samples in the :class:`VV`"),
                   Parameter('tol', type=Type.DOUBLE,
                             doc="Tolerance as a function of std dev (default=2)"),
                   Parameter('title', type=Type.STRING,
                             doc="Title"),
                   Parameter('unit', type=Type.STRING,
                             doc="Unit"),
                   Parameter('x0', type=Type.DOUBLE,
                             doc="X location (bottom left corner of graph)"),
                   Parameter('y0', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('width', type=Type.DOUBLE,
                             doc="Graph width"),
                   Parameter('height', type=Type.DOUBLE,
                             doc="Graph height")
               ])
    ]
}

