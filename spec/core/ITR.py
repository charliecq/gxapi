from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('ITR',
                 doc="""
                 The :class:`ITR` class provides access to :class:`ITR` files. An :class:`ITR` file maps
                 ranges of values to specific colors. The :class:`ITR` object is typically
                 used in conjunction with :class:`MVIEW` objects (see :class:`MVIEW` and :class:`MVU`).
                 """,
                 notes="""
                 Histogram ranges and color zone ranges
                 
                 Histogram bins are defined with inclusive minima and exclusive maxima;
                 for instance if Min = 0 and Inc = 1, then the second bin would include
                 all values z such that  0 <= z < 1 (the first bin has all values < 0).
                 
                 Color zones used in displaying grids (:class:`ITR`, ZON etc...) are the
                 opposite, with exclusive minima and inclusive maxima.
                 For instance, if a zone is defined from 0 to 1, then it would
                 contain all values of z such that 0 < z <= 1.
                 
                 These definitions mean that it is impossible to perfectly assign
                 :class:`ITR` colors to individual bars of a histogram. The best work-around
                 when the data values are integers is to define the color zones using
                 0.5 values between the integers. A general work-around is to make the
                 number of histogram bins much larger than the number of color zones.
                 
                 The :const:`ITR_NULL` is used to hold a NULL handle to an :class:`ITR` class.
                 """)


gx_defines = [
    Define('ITR_COLOR_MODEL',
           doc=":class:`ITR` Color Model defines",
           constants=[
               Constant('ITR_COLOR_MODEL_HSV', value='1', type=Type.INT32_T),
               Constant('ITR_COLOR_MODEL_RGB', value='2', type=Type.INT32_T),
               Constant('ITR_COLOR_MODEL_CMY', value='3', type=Type.INT32_T)
           ]),

    Define('ITR_NULL',
           is_null_handle=True,
           doc="Null :class:`ITR` object"),

    Define('ITR_POWER',
           doc="Power Zoning defines",
           constants=[
               Constant('ITR_POWER_10', value='0', type=Type.INT32_T,
                        doc="Power of 10"),
               Constant('ITR_POWER_EXP', value='1', type=Type.INT32_T,
                        doc="Exponential")
           ]),

    Define('ITR_ZONE',
           doc="Zoning Methods",
           constants=[
               Constant('ITR_ZONE_DEFAULT', value='0', type=Type.INT32_T),
               Constant('ITR_ZONE_LINEAR', value='1', type=Type.INT32_T),
               Constant('ITR_ZONE_NORMAL', value='2', type=Type.INT32_T),
               Constant('ITR_ZONE_EQUALAREA', value='3', type=Type.INT32_T),
               Constant('ITR_ZONE_SHADE', value='4', type=Type.INT32_T),
               Constant('ITR_ZONE_LOGLINEAR', value='5', type=Type.INT32_T)
           ]),

    Define('ITR_ZONE_MODEL',
           doc=":class:`ITR` Zone Model defines",
           constants=[
               Constant('ITR_ZONE_MODEL_NOZONE', value='-1', type=Type.INT32_T,
                        doc="The :class:`ITR` has no numeric zones defined (e.g. from a TBL file)"),
               Constant('ITR_ZONE_MODEL_NONE', value='0', type=Type.INT32_T,
                        doc="There is no specific zone model defined."),
               Constant('ITR_ZONE_MODEL_LINEAR', value='1', type=Type.INT32_T,
                        doc="The :class:`ITR` is set up with a linear transform."),
               Constant('ITR_ZONE_MODEL_NORMAL', value='2', type=Type.INT32_T,
                        doc="The :class:`ITR` is set up with a normal distribution transform."),
               Constant('ITR_ZONE_MODEL_EQUAL', value='3', type=Type.INT32_T,
                        doc="The :class:`ITR` is set up with an equal area transform."),
               Constant('ITR_MODEL_LOGLIN', value='4', type=Type.INT32_T,
                        doc="The :class:`ITR` is set up with a log-linear transform.")
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('ChangeBrightness_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Change the brightness.",
               notes="""
               0.0 brightness does nothing.
               -1.0 to 0.0 makes colors darker, -1.0 is black
               0.0 to 1.0 makes colors lighter, 1.0 is white
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('brt', type=Type.DOUBLE,
                             doc="-1.0 - black; 0.0 no change; 1.0 white")
               ]),

        Method('ColorVV_ITR', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Get color transform of a :class:`VV`.",
               notes="""
               If the input value is a dummy, then the output color
               is 0 (no color).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR"),
                   Parameter('vv_d', type="VV",
                             doc="Input :class:`VV` of values (none-string)"),
                   Parameter('vv_c', type="VV",
                             doc="Output :class:`VV` of colors (type INT)")
               ]),

        Method('Copy_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copies ITRs",
               return_type=Type.VOID,
               parameters = [
                   Parameter('it_rd', type="ITR",
                             doc=":class:`ITR` Destination"),
                   Parameter('it_rs', type="ITR",
                             doc=":class:`ITR` Source")
               ]),

        Method('Create_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create an :class:`ITR` object",
               return_type="ITR",
               return_doc=":class:`ITR` object"),

        Method('CreateFile_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create an :class:`ITR` object from an itr, tbl, zon, lut file.",
               return_type="ITR",
               return_doc=":class:`ITR` object",
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="File name, type determined from extension")
               ]),

        Method('CreateIMG_ITR', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Create an :class:`ITR` for an image.",
               notes="""
               The :const:`ITR_ZONE_DEFAULT` model will ask the :class:`IMG` to provide
               a model if it can.
               
               If a shaded relief model is selected, a shaded image
               will be created and a shaded image file will be created with
               the same name as the original grid but with the suffux "_s"
               added to the name part of the grid.
               """,
               return_type="ITR",
               return_doc=":class:`ITR` object",
               parameters = [
                   Parameter('img', type="IMG"),
                   Parameter('tbl', type=Type.STRING,
                             doc="Color table name, NULL for default"),
                   Parameter('zone', type=Type.INT32_T,
                             doc=":def:`ITR_ZONE`"),
                   Parameter('contour', type=Type.DOUBLE,
                             doc="Color contour interval or :const:`rDUMMY`")
               ]),

        Method('CreateMap_ITR', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create :class:`ITR` from Map with :class:`AGG` Group name.",
               return_type="ITR",
               return_doc=":class:`ITR` object",
               parameters = [
                   Parameter('map', type="MAP",
                             doc=":class:`MAP` on which to place the view"),
                   Parameter('name', type=Type.STRING,
                             doc=":class:`AGG` Group name")
               ]),

        Method('CreateS_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create an :class:`ITR` object from a :class:`BF`",
               return_type="ITR",
               return_doc=":class:`ITR` object",
               parameters = [
                   Parameter('bf', type="BF",
                             doc=":class:`BF` to serialize from")
               ]),

        Method('Destroy_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`ITR` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` Handle")
               ]),

        Method('EqualArea_ITR', module='geoengine.core', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Calculate an equal area transform.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('st', type="ST",
                             doc="Stat object with a histogram"),
                   Parameter('contour', type=Type.DOUBLE,
                             doc="Color contour interval or dummy for none")
               ]),

        Method('GetDataLimits_ITR', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get :class:`ITR` max/min data limits.",
               notes="""
               In some ITRs, especially those defined and
               embedded inside grid (:class:`IMG`) objects, the
               actual data minimum and maximum values are
               stored. This function retrieves those values.
               This is NOT true of all :class:`ITR` objects, and in
               those cases dummy values will be returned.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR"),
                   Parameter('min', type=Type.DOUBLE, is_ref=True,
                             doc="Data minimum value (or :const:`rDUMMY` if not set)"),
                   Parameter('max', type=Type.DOUBLE, is_ref=True,
                             doc="Data maximum value (or :const:`rDUMMY` if not set)")
               ]),

        Method('GetREG_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`ITR`'s :class:`REG`",
               return_type="REG",
               return_doc=":class:`REG` object",
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object")
               ]),

        Method('GetZoneColor_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the color in a zone of the :class:`ITR`",
               notes="Valid indices are 0 to N-1, where N is the size of the :class:`ITR`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('zone', type=Type.INT32_T,
                             doc="Number of the zone to set."),
                   Parameter('color', type=Type.INT32_T, is_ref=True,
                             doc=":def:`MVIEW_COLOR`")
               ]),

        Method('iColorValue_ITR', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Transform single data value to color",
               return_type=Type.INT32_T,
               return_doc=":def:`MVIEW_COLOR`",
               parameters = [
                   Parameter('itr', type="ITR"),
                   Parameter('val', type=Type.DOUBLE,
                             doc="Data value")
               ]),

        Method('iGetSize_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of zones in an :class:`ITR`",
               return_type=Type.INT32_T,
               return_doc="The number of zones.",
               parameters = [
                   Parameter('itr', type="ITR",
                             doc="The :class:`ITR` object")
               ]),

        Method('iGetZoneModelType_ITR', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`ITR` zone model (e.g. Linear, LogLin, Equal Area).",
               notes="""
               This function may be used to determine if a color
               transform is included in an :class:`ITR`.
               """,
               return_type=Type.INT32_T,
               return_doc=":def:`ITR_ZONE_MODEL`",
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object")
               ]),

        Method('Linear_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Calculate a linear transform.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('min', type=Type.DOUBLE,
                             doc="Minimum"),
                   Parameter('max', type=Type.DOUBLE,
                             doc="Maximum"),
                   Parameter('contour', type=Type.DOUBLE,
                             doc="Color contour interval or dummy for none")
               ]),

        Method('LoadA_ITR', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Load to an ASCII file, ZON, TBL or ER-Mapper LUT",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR"),
                   Parameter('file', type=Type.STRING,
                             doc="File name")
               ]),

        Method('LogLinear_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Calculate a log transform.",
               notes="The function name is a misnomer. This is a pure log transform.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('min', type=Type.DOUBLE,
                             doc="Minimum ( > 0)"),
                   Parameter('max', type=Type.DOUBLE,
                             doc="Maximum ( > minimum)"),
                   Parameter('contour', type=Type.DOUBLE,
                             doc="Color contour interval or dummy for none")
               ]),

        Method('Normal_ITR', module='geoengine.core', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Calculate a normal distribution transform.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('std_dev', type=Type.DOUBLE,
                             doc="Standard deviation"),
                   Parameter('mean', type=Type.DOUBLE,
                             doc="Mean"),
                   Parameter('exp', type=Type.DOUBLE,
                             doc="Expansion, normally 1.0"),
                   Parameter('contour', type=Type.DOUBLE,
                             doc="Color contour interval or dummy for none")
               ]),

        Method('PowerZone_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Modified :class:`ITR` zone values to 10 (or e) raized to the power of the values",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('pow', type=Type.INT32_T,
                             doc=":def:`ITR_POWER`")
               ]),

        Method('rGetBrightness_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the brightness setting of the :class:`ITR`",
               notes="""
               Brightness can range from -1.0 (black) to 1.0 (white).
               This brightness control is relative to the normal color
               when the :class:`ITR` is created.
               """,
               see_also=":func:`ChangeBrightness_ITR`, :func:`rGetBrightness_AGG`, :func:`ChangeBrightness_AGG`",
               return_type=Type.DOUBLE,
               return_doc="The brightness setting of the :class:`ITR`",
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object")
               ]),

        Method('rGetZoneValue_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the value in a zone of the :class:`ITR`",
               notes="Valid indices are 0 to N-2, where N is the size of the :class:`ITR`.",
               return_type=Type.DOUBLE,
               return_doc="The value of the specified zone.",
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('zone', type=Type.INT32_T,
                             doc="Number of the zone to set.")
               ]),

        Method('SaveA_ITR', module='geoengine.core', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Save to an ASCII file, ZON, TBL or ER-Mapper LUT",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR"),
                   Parameter('file', type=Type.STRING,
                             doc="File name")
               ]),

        Method('SaveFile_ITR', module='geoengine.core', version='8.2',
               availability=Availability.PUBLIC, 
               doc="Save to any type (based on the extension of the input file name).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR"),
                   Parameter('file', type=Type.STRING,
                             doc="File name")
               ]),

        Method('Serial_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Serialize an :class:`ITR` to a :class:`BF`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object to serialize"),
                   Parameter('bf', type="BF",
                             doc=":class:`BF` to serialize to")
               ]),

        Method('SetAggMap_ITR', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set :class:`ITR` to an :class:`AGG` in map",
               notes="See the :func:`CreateMap_ITR` function",
               return_type=Type.VOID,
               parameters = [
                   Parameter('map', type="MAP",
                             doc=":class:`MAP` on which to place the view"),
                   Parameter('name', type=Type.STRING,
                             doc=":class:`AGG` group name"),
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object to set")
               ]),

        Method('SetBrightContrast_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the brightness of the :class:`ITR` colors",
               notes="""
               Brightness settings:
               0.0   - black
               0.5   - normal (no change)
               1.0   - white
               
               Contrast
               0.0   - flat
               1.0   - full contrast (normal)
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('brt', type=Type.DOUBLE,
                             doc="0.0 - black; 0.5 normal; 1.0 white"),
                   Parameter('con', type=Type.DOUBLE,
                             doc="0.0 - flat; 1.0 normal")
               ]),

        Method('SetColorModel_ITR', module='geoengine.core', version='5.0.2',
               availability=Availability.PUBLIC, 
               doc="Set the color model of an :class:`ITR`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('model', type=Type.INT32_T,
                             doc=":def:`ITR_COLOR_MODEL`")
               ]),

        Method('iDefaultColorMethod_ITR', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Return the user-defined global default color method.",
               return_type=Type.INT32_T,
               return_doc="One of :const:`ITR_ZONE_EQUALAREA`, :const:`ITR_ZONE_LINEAR`, :const:`ITR_ZONE_NORMAL` or :const:`ITR_ZONE_LOGLINEAR`"
               ),

        Method('SetDataLimits_ITR', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set :class:`ITR` max/min data limits.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR"),
                   Parameter('min', type=Type.DOUBLE,
                             doc="Data minimum value"),
                   Parameter('max', type=Type.DOUBLE,
                             doc="Data maximum value")
               ]),

        Method('SetSize_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the number of zones in an :class:`ITR`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('zones', type=Type.INT32_T,
                             doc="Number of zones to set :class:`ITR` to.")
               ]),

        Method('SetZoneColor_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the color in a zone of the :class:`ITR`",
               notes="Valid indices are 0 to N-1, where N is the size of the :class:`ITR`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('zone', type=Type.INT32_T,
                             doc="Number of the zone to set."),
                   Parameter('color', type=Type.INT32_T,
                             doc=":def:`MVIEW_COLOR`")
               ]),

        Method('SetZoneValue_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the value in a zone of the :class:`ITR`",
               notes="Valid indices are 0 to N-2, where N is the size of the :class:`ITR`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('zone', type=Type.INT32_T,
                             doc="Number of the zone to set."),
                   Parameter('value', type=Type.DOUBLE,
                             doc="The value to set")
               ])
    ]
}

