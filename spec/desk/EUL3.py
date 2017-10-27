from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('EUL3',
                 doc="""
                 This is a specialized class which performs 3D Euler deconvolution
                 for potential field interpretation.
                 """)


gx_defines = [
    Define('EUL3_RESULT',
           doc="Euler result types",
           constants=[
               Constant('EUL3_RESULT_X', value='1', type=Type.INT32_T),
               Constant('EUL3_RESULT_Y', value='2', type=Type.INT32_T),
               Constant('EUL3_RESULT_DEPTH', value='3', type=Type.INT32_T),
               Constant('EUL3_RESULT_BACKGROUND', value='4', type=Type.INT32_T),
               Constant('EUL3_RESULT_DEPTHERROR', value='5', type=Type.INT32_T),
               Constant('EUL3_RESULT_LOCATIONERROR', value='6', type=Type.INT32_T),
               Constant('EUL3_RESULT_WINDOWX', value='7', type=Type.INT32_T),
               Constant('EUL3_RESULT_WINDOWY', value='8', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('_Destr_EUL3', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Destroys a :class:`EUL3` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('eul3', type="EUL3",
                             doc=":class:`EUL3` object")
               ]),

        Method('Creat_EUL3', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Creates an :class:`EUL3` object.",
               return_type="EUL3",
               return_doc=":class:`EUL3` Object",
               parameters = [
                   Parameter('imgt', type="IMG",
                             doc="Image of grid T"),
                   Parameter('imgtx', type="IMG",
                             doc="Image of grid Tx"),
                   Parameter('imgty', type="IMG",
                             doc="Image of grid Ty"),
                   Parameter('imgtz', type="IMG",
                             doc="Image of grid Tz"),
                   Parameter('wnd_siz', type=Type.INT32_T,
                             doc="Window size (maximum 20)"),
                   Parameter('gi', type=Type.DOUBLE,
                             doc="Geometric index, from 0.0 to 3.0"),
                   Parameter('tolrnc', type=Type.DOUBLE,
                             doc="Max tolerance to allow (percentage)"),
                   Parameter('max_dis', type=Type.DOUBLE,
                             doc="Max dist. acceptable (0 for infinite)"),
                   Parameter('obs_flg', type=Type.INT32_T,
                             doc="ObsFlg  Height (0) or Elevation (1)"),
                   Parameter('obs_hght', type=Type.DOUBLE,
                             doc="Height of observation plane"),
                   Parameter('obs_elev', type=Type.DOUBLE,
                             doc="Elevation of observation plane")
               ]),

        Method('GetResult_EUL3', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Get a result field :class:`VV` from :class:`EUL3` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('eul3', type="EUL3",
                             doc=":class:`EUL3` object"),
                   Parameter('vv_r', type="VV",
                             doc=":class:`VV` to store the result"),
                   Parameter('pi_res_field', type=Type.INT32_T,
                             doc=":def:`EUL3_RESULT`")
               ]),

        Method('Write_EUL3', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Write the results of :class:`EUL3` object to output file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('eul3', type="EUL3",
                             doc=":class:`EUL3` object"),
                   Parameter('out_fil', type=Type.STRING,
                             doc="Output File Name")
               ]),

        Method('ExEulerDerive_EUL3', module='geogxx', version='9.0.0',
               availability=Availability.EXTENSION, 
               doc="Calculates gradients",
               return_type=Type.INT32_T,
               return_doc="0 for OK, -1 for Error",
               parameters = [
                   Parameter('vv_dist', type="VV",
                             doc="Input distance"),
                   Parameter('pr_dx', type=Type.DOUBLE,
                             doc="Sample Interval"),
                   Parameter('vv_mag', type="VV",
                             doc="Input mag"),
                   Parameter('length', type=Type.INT32_T,
                             doc="SampleCount"),
                   Parameter('vv_gx', type="VV",
                             doc="Horizontal Gradient out"),
                   Parameter('vv_gz', type="VV",
                             doc="Vertical Gradient out"),
                   Parameter('max_sol', type=Type.INT32_T,
                             doc="Output array size limit")
               ]),

        Method('ExEulerCalc_EUL3', module='geogxx', version='9.0.0',
               availability=Availability.EXTENSION, 
               doc="Does the exeuler depth calculations",
               return_type=Type.INT32_T,
               return_doc=">0 for OK, -1 for Error",
               parameters = [
                   Parameter('typ', type=Type.INT32_T,
                             doc="Solution type flag (0 for contacts, 1 for dykes)"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Structural index value (used only when generating dykes)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Window length"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Field strength in nT"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Inclination"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Declination"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Profile azimuth wrt north"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Minimum depth for returned solutions"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Maximum depth for returned solutions"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Percentage error allowed before rejection"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="Number of points in profile"),
                   Parameter('p12', type="VV",
                             doc="Array of point distances along profile"),
                   Parameter('p13', type="VV",
                             doc="Array of observed values"),
                   Parameter('p14', type="VV",
                             doc="Array of horizontal derivative values. Can be NULL for calculated"),
                   Parameter('p15', type="VV",
                             doc="Array of vertical derivative values. Can be NULL for calculated"),
                   Parameter('p16', type=Type.INT32_T,
                             doc="Length of solutions arrays passed in"),
                   Parameter('p17', type="VV",
                             doc="The profile distance for each solution"),
                   Parameter('p18', type="VV",
                             doc="The depth for each solution"),
                   Parameter('p19', type="VV",
                             doc="The dip for each solution"),
                   Parameter('p20', type="VV",
                             doc="The susceptibility for each solution")
               ])
    ]
}

