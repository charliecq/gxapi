from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('EDB',
                 doc="""
                 The :class:`EDB` class provides access to a database as displayed within
                 Oasis montaj, but does not change data within the database itself.
                 It performs functions such as setting the current line.
                 """,
                 notes="""
                 To obtain access to the database itself, it is recommended practice
                 to begin with an :class:`EDB` object, and use the :func:`Lock_EDB` function to
                 lock the underlying map to prevent external changes. The returned
                 :class:`DB` object (see :class:`DB`) may then be safely used to make changes to the map itself.
                 """)


gx_defines = [
    Define('MAX_PROF_WND',
           is_constant=True,
           is_single_constant=True,
           doc="The following value should be kept synchronized with the value defined in src\\geoguilib\\stdafx.h",
           constants=[
               Constant('MAX_PROF_WND', value='5', type=Type.INT32_T)
           ]),

    Define('EDB_PATH',
           doc="Four forms",
           constants=[
               Constant('EDB_PATH_FULL', value='0', type=Type.INT32_T,
                        doc="d:\\directory\\file.gdb"),
               Constant('EDB_PATH_DIR', value='1', type=Type.INT32_T,
                        doc="\\directory\\file.gdb"),
               Constant('EDB_PATH_NAME_EXT', value='2', type=Type.INT32_T,
                        doc="File.gdb"),
               Constant('EDB_PATH_NAME', value='3', type=Type.INT32_T,
                        doc="File")
           ]),

    Define('EDB_PROF',
           doc="Profile data",
           constants=[
               Constant('EDB_PROF_I_CHANNEL', value='0', type=Type.INT32_T,
                        doc="DB_SYMB"),
               Constant('EDB_PROF_I_LINE_STYLE', value='1', type=Type.INT32_T,
                        doc="""
                        0 - no line
                        1 - solid
                        2 - long dash
                        3 - short dash
                        """),
               Constant('EDB_PROF_I_LINE_WEIGHT', value='2', type=Type.INT32_T,
                        doc="""
                        0 - no line
                        1 - normal
                        2 - medium
                        3 - heavy
                        """),
               Constant('EDB_PROF_I_SYMBOL', value='3', type=Type.INT32_T,
                        doc="""
                        0 - no symbol
                        1 - rectangle
                        2 - circle
                        3 - triangle
                        4 - diamond
                        5 - x
                        6 - +
                        """),
               Constant('EDB_PROF_I_SYMBOL_WEIGHT', value='4', type=Type.INT32_T,
                        doc="""
                        0 - normal
                        1 - large
                        """),
               Constant('EDB_PROF_I_COLOR', value='5', type=Type.INT32_T,
                        doc=":class:`MVIEW` Color Value"),
               Constant('EDB_PROF_I_WRAP', value='6', type=Type.INT32_T,
                        doc="0-no, 1-yes"),
               Constant('EDB_PROF_I_BREAK_ON_DUMMY', value='7', type=Type.INT32_T,
                        doc="0-no, 1-yes"),
               Constant('EDB_PROF_I_GRID_LINE', value='8', type=Type.INT32_T,
                        doc="0-no, 1-yes"),
               Constant('EDB_PROF_R_GRID_LINE_INTERVAL', value='9', type=Type.INT32_T,
                        doc="0-no, 1-yes"),
               Constant('EDB_PROF_I_LOG', value='10', type=Type.INT32_T,
                        doc="0-Linear, 1-Log, 2-LogLinear"),
               Constant('EDB_PROF_R_LOG_MINIMUM', value='11', type=Type.INT32_T,
                        doc="Minimum Value"),
               Constant('EDB_PROF_I_SAMESCALE', value='12', type=Type.INT32_T,
                        doc="0-no, 1-yes"),
               Constant('EDB_PROF_I_SOURCELINE', value='13', type=Type.INT32_T,
                        doc="""
                        0 - current line
                        -1 - previous line
                        -2 - next line
                        """),
               Constant('EDB_PROF_I_SCALEOPTION', value='14', type=Type.INT32_T,
                        doc="""
                        0 - scale to fit for each line
                        1 - fix the range
                        2 - fix the scale, center the range
                        """),
               Constant('EDB_PROF_I_SAMERANGE', value='15', type=Type.INT32_T,
                        doc="0-no, 1-yes")
           ]),

    Define('EDB_PROFILE_SCALE',
           doc="Profile Scale Options",
           constants=[
               Constant('EDB_PROFILE_SCALE_LINEAR', value='0', type=Type.INT32_T),
               Constant('EDB_PROFILE_SCALE_LOG', value='1', type=Type.INT32_T),
               Constant('EDB_PROFILE_SCALE_LOGLINEAR', value='2', type=Type.INT32_T)
           ]),

    Define('EDB_REMOVE',
           doc="How to handle pending changes in document",
           constants=[
               Constant('EDB_REMOVE_SAVE', value='0', type=Type.INT32_T),
               Constant('EDB_REMOVE_PROMPT', value='1', type=Type.INT32_T),
               Constant('EDB_REMOVE_DISCARD', value='2', type=Type.INT32_T)
           ]),

    Define('EDB_UNLOAD',
           doc="What type of prompt",
           constants=[
               Constant('EDB_UNLOAD_NO_PROMPT', value='0', type=Type.INT32_T),
               Constant('EDB_UNLOAD_SINGLE_PROMPT', value='1', type=Type.INT32_T),
               Constant('EDB_UNLOAD_MULTI_PROMPT', value='2', type=Type.INT32_T,
                        doc="Obsolete")
           ]),

    Define('EDB_WINDOW_POSITION',
           doc="Window Positioning Options",
           constants=[
               Constant('EDB_WINDOW_POSITION_DOCKED', value='0', type=Type.INT32_T),
               Constant('EDB_WINDOW_POSITION_FLOATING', value='1', type=Type.INT32_T)
           ]),

    Define('EDB_WINDOW_STATE',
           doc="Window State Options",
           constants=[
               Constant('EDB_WINDOW_RESTORE', value='0', type=Type.INT32_T),
               Constant('EDB_WINDOW_MINIMIZE', value='1', type=Type.INT32_T),
               Constant('EDB_WINDOW_MAXIMIZE', value='2', type=Type.INT32_T)
           ]),

    Define('EDB_YAXIS_DIRECTION',
           doc="Window State Options",
           constants=[
               Constant('EDB_YAXIS_NORMAL', value='0', type=Type.INT32_T),
               Constant('EDB_YAXIS_INVERTED', value='1', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('ApplyFormulaInternal_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               Apply a formula to selected cells of the
               current line. (Do not use this wrapper if you
               want to apply a formula across multiple lines)
               
               Notes:
               
               The current selection must be on cell(s) of
               a channel or on the a channel header.
               
               If the selection is on cell(s) of a channel,
               the formula is applied to only these cells.
               
               If the selection is on a channel header, the
               formula is applied to every cell in the channel.
               
               The given formula string must be of the form:
               "<NameOfCurrentChannel>=<SomeExpression>;"
               e.g. "x=y+1;"
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('formula', type=Type.STRING,
                             doc='Formula ("<NameOfCurrentChannel>=<SomeExpression>;")')
               ]),

        Method('Current_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited Database.",
               return_type="EDB",
               return_doc=":class:`EDB` Object"),

        Method('CurrentNoActivate_EDB', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited Database.",
               notes="""
               This function acts just like :func:`Current_EDB` except that the document is not activated (brought to foreground) and no
               guarantee is given about which document is currently active.
               """,
               return_type="EDB",
               return_doc=":class:`EDB` Object"),

        Method('CurrentIfExists_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited Database.",
               return_type="EDB",
               return_doc="""
               :class:`EDB` Object to current edited database. If there is no current database,
               the user is not prompted for a database, and 0 is returned.
               """),

        Method('DelLine0_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Delete Line 0.",
               notes="Deletes an empty line 0 from the database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('Destroy_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Destroy :class:`EDB` handle.",
               notes="This does not unload the database; it simply deletes the gx resource handle",
               return_type=Type.VOID,
               parameters = [
                   Parameter('val', type="EDB",
                             doc=":class:`EDB` to destroy")
               ]),

        Method('DestroyView_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Removes the view from the workspace.",
               notes="""
               Can only be run in interactive mode. After this call the
               :class:`EDB` object will become invalid. If this is the last view on
               the document and the document has been modified the map will be
               unloaded and optionally saved depending on the :def:`EDB_REMOVE`
               parameter.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` object"),
                   Parameter('unload_flag', type=Type.INT32_T,
                             doc=":def:`EDB_REMOVE`")
               ]),

        Method('GetCurChanSymb_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the currently marked channel symbol.",
               return_type="DB_SYMB",
               return_doc="""
               Currently channel symbol.
               :def_val:`NULLSYMB` if the mark is not in a channel.
               """,
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('GetCurLineSymb_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get current line symbol.",
               return_type="DB_SYMB",
               return_doc="""
               Currently displayed line symbol.
               :def_val:`NULLSYMB` if no line displayed.
               """,
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('GetDisplFidRange_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Return the displayed fiducial start index & number of cells",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('start', type=Type.INT32_T, is_ref=True,
                             doc="Fiducial start"),
                   Parameter('num', type=Type.INT32_T, is_ref=True,
                             doc="Number of fiducials")
               ]),

        Method('GetCurPoint_EDB', module='None', version='9.2.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of the currently selected point in the database (first value if range selected)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` object"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="X coordinate (dummy if no selection or if no X channel defined)"),
                   Parameter('y', type=Type.DOUBLE, is_ref=True,
                             doc="Y coordinate (dummy if no selection or if no Y channel defined)"),
                   Parameter('z', type=Type.DOUBLE, is_ref=True,
                             doc="Z coordinate (dummy if no selection or if no Z channel defined)")
               ]),

        Method('GetFidRange_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns currently displayed fid range",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('start', type=Type.DOUBLE, is_ref=True,
                             doc="Fiducial start"),
                   Parameter('incr', type=Type.DOUBLE, is_ref=True,
                             doc="Fiducial increment"),
                   Parameter('num', type=Type.INT32_T, is_ref=True,
                             doc="Number of fiducials")
               ]),

        Method('GetNextLineSymb_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the next line symbol.",
               return_type="DB_SYMB",
               return_doc="""
               The next line symbol of currently displayed line.
               :def_val:`NULLSYMB` if no line displayed.
               """,
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('GetPrevLineSymb_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the previous line symbol.",
               return_type="DB_SYMB",
               return_doc="""
               The previous line symbol of currently displayed line.
               :def_val:`NULLSYMB` if no line displayed.
               """,
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('GetProfileRangeX_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile X range and X channel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum x"),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum x"),
                   Parameter('ph_chan_x', type="DB_SYMB", is_ref=True,
                             doc="X axis channel, :def_val:`NULLSYMB` if none")
               ]),

        Method('GetProfileRangeY_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile Y range and display option",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('window', type=Type.INT32_T,
                             doc="Profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('prof', type=Type.INT32_T,
                             doc="Profile number in window (see :func:`iWindowProfiles_EDB` which returns number of profiles in a window)"),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum y"),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum y"),
                   Parameter('scl', type=Type.INT32_T, is_ref=True,
                             doc=":def:`EDB_PROFILE_SCALE`")
               ]),

        Method('GetProfileSplit_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile split for 3 windows.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('d1', type=Type.DOUBLE, is_ref=True,
                             doc="Split d1 (profile window 0 height / entire profile window height)"),
                   Parameter('d2', type=Type.DOUBLE, is_ref=True,
                             doc="Split d2 (profile window 1 height / entire profile window height)")
               ]),

        Method('GetProfileSplit5_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile split for 5 windows.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('d1', type=Type.DOUBLE, is_ref=True,
                             doc="Split d1 (profile window 0 height / entire profile window height)"),
                   Parameter('d2', type=Type.DOUBLE, is_ref=True,
                             doc="Split d2 (profile window 1 height / entire profile window height)"),
                   Parameter('d3', type=Type.DOUBLE, is_ref=True,
                             doc="Split d3 (profile window 2 height / entire profile window height)"),
                   Parameter('d4', type=Type.DOUBLE, is_ref=True,
                             doc="Split d4 (profile window 3 height / entire profile window height)")
               ]),

        Method('GetProfileSplitVV_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile window splits.",
               notes="""
               The returned :class:`VV` is sized to the maximum number of profiles
               that can be displayed. If a profile is not currently displayed,
               its height fraction is 0.  The sum of all the fractions returned
               is equal to 1.
               
               The profile splits refers to the relative sizes of the individual
               profile windows. To get/set the fraction of the total database window
               devoted to the profiles, use the :func:`SetSplit_EDB` and :func:`rGetSplit_EDB` functions.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('vv', type="VV",
                             doc="Split :class:`VV` (REAL) (profile window heights / entire profile window height)")
               ]),

        Method('GetProfileVerticalGridLines_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile grid vertical line info.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('grid', type=Type.INT32_T, is_ref=True,
                             doc="Vertical grid lines?"),
                   Parameter('interval', type=Type.DOUBLE, is_ref=True,
                             doc="Vertical grid interval")
               ]),

        Method('GetProfileWindow_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile window size",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('window', type=Type.INT32_T,
                             doc="Profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('x', type=Type.INT32_T, is_ref=True,
                             doc="Window x size in pixels"),
                   Parameter('y', type=Type.INT32_T, is_ref=True,
                             doc="Window y size in pixels")
               ]),

        Method('GotoColumn_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Move the channel marker to a specific column.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Channel column number, 0 is first -1 for first column without data")
               ]),

        Method('GotoElem_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Goto an element in the current line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('elem', type=Type.INT32_T,
                             doc="Element number")
               ]),

        Method('GotoLine_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Goto to a line symbol in the editor.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('line_symb', type="DB_SYMB",
                             doc="Line symbol to goto to")
               ]),

        Method('Histogram_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Create histogram stats.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('st', type="ST",
                             doc=":class:`ST` handle to update"),
                   Parameter('min', type=Type.DOUBLE,
                             doc="Histogram minimum"),
                   Parameter('incr', type=Type.DOUBLE,
                             doc="Histogram increment"),
                   Parameter('count', type=Type.INT32_T,
                             doc="Number of increments")
               ]),

        Method('iAllChanList_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get a list of the all channels but in the way they are displayed.",
               notes="""
               The :class:`VV` elements must be INT.
               
               Displayed channel lists are filled in the order the channels
               appear on the display, left to right.
               """,
               see_also=":func:`iDispChanList_EDB`",
               return_type=Type.INT32_T,
               return_doc="""
               Number of symbols in the list.
               Terminates GX if there was an error.
               """,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('vv', type="VV",
                             doc=":class:`VV` (INT) in which to place the list.")
               ]),

        Method('iChannels_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns number of displayed channels",
               return_type=Type.INT32_T,
               return_doc="x - number of displayed channels",
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('iDispChanList_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get a list of the displayed channel symbols.",
               notes="""
               The :class:`VV` elements must be INT.
               
               Displayed channel lists are filled in the order the channels
               appear on the display, left to right.
               """,
               see_also=":func:`iDispChanLST_EDB`",
               return_type=Type.INT32_T,
               return_doc="""
               Number of symbols in the list.
               Terminates GX if there was an error.
               """,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('vv', type="VV",
                             doc=":class:`VV` (INT) in which to place the list.")
               ]),

        Method('iDispChanLST_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get a list of the displayed channel names.",
               notes="""
               Displayed channel lists are filled in the order the channels
               appear on the display, left to right.
               
               The channel names will be placed in the "Name" part of
               the list and the values are set to the symbol handle.
               """,
               see_also=":func:`iDispChanList_EDB`",
               return_type=Type.INT32_T,
               return_doc="""
               Number of channels in the list.
               Terminates GX if there was an error.
               """,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` object")
               ]),

        Method('iDispClassChanLST_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get a list of the displayed channels in a given channel class.",
               notes="""
               Displayed channel lists are filled in the order the channels
               appear on the display, left to right.
               
               The channel names will be placed in the "Name" part of
               the list and the values are set to the symbol handle.
               
               Examples of channel classes in current use are "MASK" and
               "ASSAY". (Searches are case tolerant).
               """,
               see_also=":func:`iDispChanList_EDB`",
               return_type=Type.INT32_T,
               return_doc="""
               Number of channels in the list.
               Terminates GX if there was an error.
               """,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` object"),
                   Parameter('class_name', type=Type.STRING,
                             doc='Class name ("" for all)')
               ]),

        Method('iFindChannelColumn_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Find the column that contains a channel",
               return_type=Type.INT32_T,
               return_doc="""
               Column number that contains a specific channel
               :def_val:`iDUMMY` of channel not loaded
               """,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel")
               ]),

        Method('iFindNearest_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               Find the nearest point on the current line based
               on X,Y and Z and their projection.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               x - Nearest point
               -1 - Not available
               """,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="X - Modified with true point"),
                   Parameter('y', type=Type.DOUBLE, is_ref=True,
                             doc="Y - Modified with true point"),
                   Parameter('z', type=Type.DOUBLE, is_ref=True,
                             doc="Z - Modified with true point"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection of X,Y,Z")
               ]),

        Method('IGetCurChan_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get current channel name.",
               notes='Returns "" if mark not currently in a channel.',
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('str_val', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Where to put the name"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Length of the Buffer")
               ]),

        Method('IGetCurFidString_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               This method returns the currently selected value
               at the current fid (if available).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` object"),
                   Parameter('val', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="String returned here"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Size")
               ]),

        Method('IGetCurLine_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get current line name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('str_val', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Where to put the name"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Length of the Buffer")
               ]),

        Method('iGetCurMark_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the current data mark info.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - if data is marked.
               1 - if data is not currently marked.
               """,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('start', type=Type.DOUBLE, is_ref=True,
                             doc="Start fiducial"),
                   Parameter('end', type=Type.DOUBLE, is_ref=True,
                             doc="End fiducial"),
                   Parameter('inc', type=Type.DOUBLE, is_ref=True,
                             doc="Fiducial increment")
               ]),

        Method('IGetCurrentSelection_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get current selection information.",
               notes="""
               Channel Name    Empty if no channel
               Line Name       "[All]" if all lines are selected
               Fid Range       "[All]" if all values in all lines are selected
               "[None]"  if no values are selected
               "10 to 20"  giving the range of values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('db', type=Type.STRING, is_ref=True, size_of_param='db_size',
                             doc="Database name"),
                   Parameter('db_size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Length of the database name"),
                   Parameter('chan', type=Type.STRING, is_ref=True, size_of_param='chan_size',
                             doc="Name of Selected channel"),
                   Parameter('chan_size', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Length of the channel name"),
                   Parameter('line', type=Type.STRING, is_ref=True, size_of_param='line_size',
                             doc="Selected lines buffer"),
                   Parameter('line_size', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Length of the lines buffer"),
                   Parameter('fid', type=Type.STRING, is_ref=True, size_of_param='fid_size',
                             doc="Fiducial range"),
                   Parameter('fid_size', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Length of the range buffer")
               ]),

        Method('iGetDatabasesLST_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Load the file names of open databases into a :class:`LST`.",
               return_type=Type.INT32_T,
               return_doc="""
               The number of documents loaded into the :class:`LST`.
               The :class:`LST` is cleared first.
               """,
               parameters = [
                   Parameter('lst', type="LST",
                             doc=":class:`LST` to load"),
                   Parameter('path', type=Type.INT32_T,
                             doc=":def:`EDB_PATH`")
               ]),

        Method('iGetMarkChanVV_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get channel data for the current mark.",
               notes="""
               The current "mark" in this case is the start and
               end fiducials and not the selected channel. You
               can use this method to retrieve the selected range
               from any channel, loaded or not.
               
               The :class:`VV` will be resized to the length of the data
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if successful.
               1 if failed, or if entire database is marked.
               """,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('vv', type="VV",
                             doc=":class:`VV` in which to place the data."),
                   Parameter('chan', type="DB_SYMB",
                             doc="Channel symbol to retrieve.")
               ]),

        Method('iGetMarkChanVA_EDB', module='None', version='8.2.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get channel data for the current mark.",
               notes="""
               The current "mark" in this case is the start and
               end fiducials and not the selected channel. You
               can use this method to retrieve the selected range
               from any channel, loaded or not.
               
               The :class:`VA` will be resized to the length of the data
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if successful.
               1 if failed, or if entire database is marked.
               """,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('vv', type="VA",
                             doc=":class:`VA` in which to place the data."),
                   Parameter('chan', type="DB_SYMB",
                             doc="Channel symbol to retrieve.")
               ]),

        Method('IGetName_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the name of the database object of this :class:`EDB`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Name returned"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of the String")
               ]),

        Method('iGetProfileParm_EDB', module='None', version='5.0.0', cpp_post="_int",
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get integer profile parameter",
               return_type=Type.INT32_T,
               return_doc="Data Value (See notes)",
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('window', type=Type.INT32_T,
                             doc="Profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('prof', type=Type.INT32_T,
                             doc="Profile number in window (see :func:`GetProfileRangeY_EDB`)"),
                   Parameter('parm', type=Type.INT32_T,
                             doc=":def:`EDB_PROF`")
               ]),

        Method('iGetWindowState_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Retrieve the current state of the database window",
               return_type=Type.INT32_T,
               return_doc=":def:`EDB_WINDOW_STATE`",
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('iHaveCurrent_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns true if a database is loaded",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`"),

        Method('iIsLocked_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Is this Database locked",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` object")
               ]),

        Method('iLoaded_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns 1 if a database is loaded .",
               return_type=Type.INT32_T,
               return_doc="1 if database is loaded, 0 otherwise.",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Database name")
               ]),

        Method('iProfileOpen_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Return TRUE or FALSE if profile window is open",
               notes="""
               This functions will return FALSE if requested window
               is not supported in current version of Oasis montaj.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               TRUE if window is open
               FALSE if window is closed
               """,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('window', type=Type.INT32_T,
                             doc="Profile window number: 0 is the top window 1 is the middle window 2 is the bottom window")
               ]),

        Method('iReadOnly_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Checks if a database is currently opened in a read-only mode.",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('GetWindowPosition_EDB', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the map window's position and dock state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('left', type=Type.INT32_T, is_ref=True,
                             doc="Window left position"),
                   Parameter('top', type=Type.INT32_T, is_ref=True,
                             doc="Window top position"),
                   Parameter('right', type=Type.INT32_T, is_ref=True,
                             doc="Window right position"),
                   Parameter('bottom', type=Type.INT32_T, is_ref=True,
                             doc="Window bottom position"),
                   Parameter('state', type=Type.INT32_T, is_ref=True,
                             doc="Window state :def:`EDB_WINDOW_STATE`"),
                   Parameter('is_floating', type=Type.INT32_T, is_ref=True,
                             doc="Docked or floating :def:`EDB_WINDOW_POSITION`")
               ]),

        Method('SetWindowPosition_EDB', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the map window's position and dock state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('left', type=Type.INT32_T,
                             doc="Window left position"),
                   Parameter('top', type=Type.INT32_T,
                             doc="Window top position"),
                   Parameter('right', type=Type.INT32_T,
                             doc="Window right position"),
                   Parameter('bottom', type=Type.INT32_T,
                             doc="Window bottom position"),
                   Parameter('state', type=Type.INT32_T,
                             doc="Window state :def:`EDB_WINDOW_STATE`"),
                   Parameter('is_floating', type=Type.INT32_T,
                             doc="Docked or floating :def:`EDB_WINDOW_POSITION`")
               ]),

        Method('iShowProfileName_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Show a profile in the profile window",
               notes="If the symbol is not loaded, it will be loaded.",
               return_type=Type.INT32_T,
               return_doc="Profile ID if loaded, -1 for error",
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('state', type=Type.INT32_T,
                             doc="Profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('chan', type=Type.STRING,
                             doc="Name of the channel")
               ]),

        Method('iGetWindowYAxisDirection_EDB', module='None', version='8.3.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the y-axis direction for a window",
               return_type=Type.INT32_T,
               return_doc=":def:`EDB_YAXIS_DIRECTION`",
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('window', type=Type.INT32_T,
                             doc="Profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)")
               ]),

        Method('iWindowProfiles_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get number of profiles in a window",
               return_type=Type.INT32_T,
               return_doc="Number of profiles in a window",
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('window', type=Type.INT32_T,
                             doc="Profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)")
               ]),

        Method('LaunchHistogram_EDB', module='geochimera', version='5.0.6',
               availability=Availability.PUBLIC, 
               doc="Launch histogram tool on a database.",
               see_also=":func:`LaunchHistogram_CHIMERA` in chimera.gxh",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('chan', type=Type.STRING,
                             doc="First chan name")
               ]),

        Method('LaunchScatter_EDB', module='geochimera', version='5.0.6',
               availability=Availability.PUBLIC, 
               doc="Launch scatter tool on a database.",
               notes="""
               The scatter tool uses the following INI parameters
               
               SCATTER.STM       name of the scatter template,"none" for none
               SCATTER.STM_NAME  name of last template section, "" for none.
               SCATTER.X         name of channel to display in X
               SCATTER.Y         name of channel to display in Y
               SCATTER.MASK      name of channel to use for mask
               """,
               see_also=":func:`LaunchScatter_CHIMERA` in chimera.gxh",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object")
               ]),

        Method('Load_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads a list of databases into the workspace",
               notes="""
               The last listed database will become the current database.
               
               Databases may already be loaded.
               
               Only the first file in the list may have a directory path.
               All other files in the list are assumed to be in the same
               directory as the first file.
               """,
               return_type="EDB",
               return_doc="""
               Handle to current edited database, which will be the last
               database in the list.
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="List of databases (';' or '|' delimited) to load.")
               ]),

        Method('LoadNoActivate_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads documents into the workspace",
               notes="""
               This function acts just like :func:`Load_EDB` except that the document(s) is not activated (brought to foreground) and no
               guarantee is given about which document is currently active.
               """,
               return_type="EDB",
               return_doc="""
               Handle to current edited document, which will be the last
               database in the list if multiple files were provided.
               """,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="List of documents (';' or '|' delimited) to load.")
               ]),

        Method('LoadAllChans_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Load all channels into current database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('LoadChan_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Load a channel into current database",
               notes="""
               If the channel does not exist, or if channel is already
               loaded nothing happens.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel name")
               ]),

        Method('LoadNew_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads a database into the workspace, flags as new.",
               notes="""
               See :func:`Load_EDB`. This is used for brand new databases, to set
               an internal flag such that if on closing the user chooses
               not to save changes, the database is deleted.
               """,
               return_type="EDB",
               return_doc="Handle to the current edited database.",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Database to load.")
               ]),

        Method('LoadPass_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads a database into the editor with login and password.",
               notes="""
               The loaded database will become the current database.
               
               If the database is already loaded, it simply becomes
               the current database.
               """,
               return_type="EDB",
               return_doc="Handle to current edited database.",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of database to load"),
                   Parameter('login', type=Type.STRING,
                             doc="Login Name"),
                   Parameter('password', type=Type.STRING,
                             doc="Password")
               ]),

        Method('LoadWithView_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Load an :class:`EDB` with the view from a current :class:`EDB`.",
               notes="""
               Can only be run in interactive mode. Is used by
               dbsubset to create a new database with the same
               view as previously.
               """,
               return_type="EDB",
               return_doc="New :class:`EDB` handle.",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Source :class:`DB` name"),
                   Parameter('p2', type="EDB",
                             doc=":class:`EDB` to use as the source view")
               ]),

        Method('Lock_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method locks the Edited Database.",
               return_type="DB",
               return_doc="Handle to database associated with edited database.",
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('MakeCurrent_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Makes this :class:`EDB` object the current active object to the user.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` to make active")
               ]),

        Method('RemoveProfile_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Remove a profile from the profile window",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('window', type=Type.INT32_T,
                             doc="Profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('prof', type=Type.INT32_T,
                             doc="Profile number in window (see :func:`GetProfileRangeY_EDB`)")
               ]),

        Method('rGetCurFid_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               This method returns the currently selected fiducial if
               the user is selecting a fiducial. If not, it returns
               a dummy.
               """,
               return_type=Type.DOUBLE,
               return_doc="""
               x     - Fiducial
               DUMMY - No Selected Fiducial
               """,
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('rGetProfileParm_EDB', module='None', version='5.0.0', cpp_post="_double",
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get real profile parameter",
               return_type=Type.DOUBLE,
               return_doc="Real profile parameter",
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('window', type=Type.INT32_T,
                             doc="Profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('prof', type=Type.INT32_T,
                             doc="Profile number in window (see :func:`GetProfileRangeY_EDB`)"),
                   Parameter('parm', type=Type.INT32_T,
                             doc=":def:`EDB_PROF`")
               ]),

        Method('rGetSplit_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get split ratio between spreadsheet and profile sections.",
               return_type=Type.DOUBLE,
               return_doc="""
               d = (spreadsheet window height/
               (spreadsheet window height + entire profile window height))
               """,
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('RunChannelMaker_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Run the maker for a single channel.",
               notes="""
               Skips channels without makers; will not return an
               error if the channel does not exist.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel name")
               ]),

        Method('RunChannelMakers_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Recreate channels with makers.",
               notes="Skips channels without makers.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('SetCurLine_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set the current line name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('line', type=Type.STRING,
                             doc="Line name")
               ]),

        Method('SetCurLineNoMessage_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set Line but do not send a message.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('str_val', type=Type.STRING,
                             doc="Line name")
               ]),

        Method('SetCurMark_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set the current mark.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('start', type=Type.DOUBLE,
                             doc="Start fiducial"),
                   Parameter('end', type=Type.DOUBLE,
                             doc="End fiducial")
               ]),

        Method('SetProfileParmI_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set integer profile parameter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('window', type=Type.INT32_T,
                             doc="Profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('prof', type=Type.INT32_T,
                             doc="Profile number in window (see :func:`GetProfileRangeY_EDB`)"),
                   Parameter('parm', type=Type.INT32_T,
                             doc=":def:`EDB_PROF`"),
                   Parameter('value', type=Type.INT32_T,
                             doc="Setting")
               ]),

        Method('SetProfileParmR_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set real profile parameter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('window', type=Type.INT32_T,
                             doc="Profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('prof', type=Type.INT32_T,
                             doc="Profile number in window (see :func:`GetProfileRangeY_EDB`)"),
                   Parameter('parm', type=Type.INT32_T,
                             doc=":def:`EDB_PROF`"),
                   Parameter('value', type=Type.DOUBLE,
                             doc="Setting")
               ]),

        Method('SetProfileRangeX_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set profile X range and X channel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Minimum x, :def_val:`rDUMMY` for data minimum"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Maximum x, :def_val:`rDUMMY` for data maximum"),
                   Parameter('x_ch', type="DB_SYMB",
                             doc="X axis channel, :def_val:`NULLSYMB` to use fids")
               ]),

        Method('SetProfileRangeY_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set profile Y range and display option",
               notes="""
               If channel is not loaded or displayed, it will
               loaded and/or displayed.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('min_x', type=Type.INT32_T,
                             doc="Profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('max_x', type=Type.INT32_T,
                             doc="Profile number in window (see :func:`GetProfileRangeY_EDB`)"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Minimum y"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Maximum y"),
                   Parameter('scl', type=Type.INT32_T,
                             doc=":def:`EDB_PROFILE_SCALE`")
               ]),

        Method('SetProfileSplit_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set profile split for 3 windows.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('d1', type=Type.DOUBLE,
                             doc="Split d1 (profile window 0 height / entire profile window height)"),
                   Parameter('d2', type=Type.DOUBLE,
                             doc="Split d2 (profile window 1 height / entire profile window height)")
               ]),

        Method('SetProfileSplit5_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set profile split for 5 windows.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('d1', type=Type.DOUBLE,
                             doc="Split d1 (profile window 0 height / entire profile window height)"),
                   Parameter('d2', type=Type.DOUBLE,
                             doc="Split d2 (profile window 1 height / entire profile window height)"),
                   Parameter('d3', type=Type.DOUBLE,
                             doc="Split d3 (profile window 2 height / entire profile window height)"),
                   Parameter('d4', type=Type.DOUBLE,
                             doc="Split d4 (profile window 3 height / entire profile window height)")
               ]),

        Method('SetProfileSplitVV_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set profile splits",
               notes="""
               The input :class:`VV` values are the fractional heights for each
               profile window. Values are summed, and normalized (so you can
               enter "1,1,1", with a :class:`VV` of length 3, if you want 3 equal profile windows).
               
               :class:`VV` values beyond the maximum number of displayable
               profiles (:def_val:`MAX_PROF_WND`) are ignored.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('vv', type="VV",
                             doc="Split :class:`VV` (REAL) (relative sizes of each profile window)")
               ]),

        Method('SetSplit_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set split ratio between spreadsheet and profile sections.",
               notes="""
               d = (spreadsheet window height/
               (spreadsheet window height + entire profile window height))
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('d', type=Type.DOUBLE,
                             doc="Split d (0.0 <= d <= 1.0).")
               ]),

        Method('SetWindowState_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Changes the state of the database window",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('state', type=Type.INT32_T,
                             doc=":def:`EDB_WINDOW_STATE`")
               ]),

        Method('ShowProfile_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Show a profile in the profile window",
               notes="If the symbol is not loaded, it will be loaded.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('window', type=Type.INT32_T,
                             doc="Profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('symb', type="DB_SYMB",
                             doc="Channel symbol")
               ]),

        Method('Statistics_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Add all currently selected data to the :class:`ST`.",
               notes="Use :func:`Histogram_EDB` to get median or histogram.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('st', type="ST",
                             doc=":class:`ST` handle to update")
               ]),

        Method('UnLoad_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads an edited database.",
               notes="""
               If the database is not loaded, nothing happens.
               Same as :func:`UnLoadVerify_EDB` with FALSE to prompt save.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of database to unload")
               ]),

        Method('UnLoadAll_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads all opened databases",
               return_type=Type.VOID),

        Method('UnLoadAllChans_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unload all channels into current database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB")
               ]),

        Method('UnLoadChan_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unload a channel into current database",
               notes="""
               If the channel does not exist, or if channel is already
               loaded nothing happens.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel name")
               ]),

        Method('UnLoadDiscard_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads a database in the workspace, discards changes.",
               notes="If the database is not loaded, nothing happens.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of database to unload")
               ]),

        Method('UnLoadVerify_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads an edited database, optional prompt to save.",
               notes="""
               If the database is not loaded, nothing happens.
               The user can be prompted to save before unloading.
               If :def_val:`EDB_UNLOAD_NO_PROMPT`, data is always saved.
               EDB_UNLOAD_MULTIPROMPT is now obsolete and
               is equivalent to :def_val:`EDB_UNLOAD_SINGLE_PROMPT`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of database to unload"),
                   Parameter('prompt', type=Type.INT32_T,
                             doc=":def:`EDB_UNLOAD`")
               ]),

        Method('UnLock_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method unlocks the Edited Database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB")
               ])
    ],
    'External Window': [

        Method('LoadControl_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="Version of :func:`Load_EDB` that can be used to load a database via subclassing into a Windows control.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('db_file', type=Type.STRING,
                             doc="Database filename"),
                   Parameter('window', type="HWND", is_val=True,
                             doc="Window handle to receive document")
               ]),

        Method('LoadNewControl_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="Version of :func:`LoadNew_EDB` that can be used to load a database via subclassing into a Windows control.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('db_file', type=Type.STRING,
                             doc="Database filename"),
                   Parameter('window', type="HWND", is_val=True,
                             doc="Window handle to receive document")
               ]),

        Method('LoadPassControl_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="Version of :func:`LoadPass_EDB` that can be used to load a database via subclassing into a Windows control.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('db_file', type=Type.STRING,
                             doc="Database filename"),
                   Parameter('user', type=Type.STRING,
                             doc="Login name"),
                   Parameter('password', type=Type.STRING,
                             doc="Password"),
                   Parameter('window', type="HWND", is_val=True,
                             doc="Window handle to receive document")
               ]),

        Method('LoadWithViewControl_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="Version of :func:`LoadWithView_EDB` that can be used to load a database via subclassing into a Windows control.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('db_file', type=Type.STRING,
                             doc="Database filename"),
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` handle to use as the source view"),
                   Parameter('window', type="HWND", is_val=True,
                             doc="Window handle to receive document")
               ])
    ],
    'Obsolete': [

        Method('NoLoad_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Makes a database the Edited Database without loading it.",
               return_type="EDB",
               return_doc="Handle to current edited database",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc='Single databases to "not" load')
               ]),

        Method('ReadDataViewBF_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Retrieve view info from the database via a :class:`BF`.",
               notes="""
               Returns info on loaded channels and profiles for a given line.
               You can use :def_val:`NULLSYMB` to get the line view info from normal lines,
               since the info is the same for all "regular" lines.
               A typical usage would be to call :func:`ReadDataViewBF_EDB` to get view
               info from one database, and then call :func:`WriteDataViewBF_EDB` to
               load this information into another database.
               
               Obsolete
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` object"),
                   Parameter('line_group', type="DB_SYMB",
                             doc="Line or group symbol"),
                   Parameter('bf', type="BF",
                             doc=":class:`BF` (returned)")
               ]),

        Method('WriteDataViewBF_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Write the View info from a :class:`BF` into the database.",
               notes="""
               Set info on loaded channels and profiles for a given line.
               You can use :def_val:`NULLSYMB` to get the line view info from normal lines,
               since the info is the same for all "regular" lines.
               A typical usage would be to call :func:`ReadDataViewBF_EDB` to get view
               info from one database, and then call :func:`WriteDataViewBF_EDB` to
               load this information into another database.
               
               Obsolete
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB",
                             doc=":class:`EDB` object"),
                   Parameter('line_group', type="DB_SYMB",
                             doc="Line or group symbol"),
                   Parameter('bf', type="BF",
                             doc=":class:`BF` (input)")
               ]),

        Method('SetWindowArea_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Set the location of the database window within the frame.",
               notes="""
               The Coordinates are pixels with 0,0 being the bottom
               left corner Oasis montaj frame window.
               
               if the max values are equal or less than the min values
               the window will be mimimized. If any Min values are :def_val:`iMIN`
               or any Max values are :def_val:`iMAX`, the window is maximized.
               
               NOTE: Now Obsolete. Use :func:`SetWindowPosition_EDB`, which includes multi-monitor support.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('x_min', type=Type.INT32_T,
                             doc="X Min"),
                   Parameter('y_min', type=Type.INT32_T,
                             doc="Y Min"),
                   Parameter('x_max', type=Type.INT32_T,
                             doc="X Max"),
                   Parameter('y_max', type=Type.INT32_T,
                             doc="Y Max")
               ]),

        Method('GetWindowArea_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Get the location of the database window within the frame.",
               notes="""
               The Coordinates are pixels with 0,0 being the bottom
               left corner Oasis montaj frame window.
               
               If the window is minimized, the max values will be
               equal to the min values. If the window is maximized
               X Min and Y min will be :def_val:`iMIN` and X max and Y max
               will be :def_val:`iMAX`.
               
               NOTE: Now Obsolete. Use :func:`GetWindowPosition_EDB`, which includes multi-monitor support.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('edb', type="EDB"),
                   Parameter('min_x', type=Type.INT32_T, is_ref=True,
                             doc="X Min returned"),
                   Parameter('min_y', type=Type.INT32_T, is_ref=True,
                             doc="Y Min returned"),
                   Parameter('max_x', type=Type.INT32_T, is_ref=True,
                             doc="X Max returned"),
                   Parameter('max_y', type=Type.INT32_T, is_ref=True,
                             doc="Y Max returned")
               ])
    ]
}

