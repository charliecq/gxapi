from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('TRND',
                 doc="""
                 The :class:`TRND` methods are used to determine trend directions in database data by locating
                 maxima and minima along lines and joining them in a specified direction.
                 The resulting trend lines are appended to the database and used by gridding methods
                 such as Bigrid and Rangrid to enforce features in the specified direction.
                 """)


gx_defines = [
    Define('TRND_NODE',
           doc="Node to find",
           constants=[
               Constant('TRND_MIN', value='0', type=Type.INT32_T),
               Constant('TRND_MAX', value='1', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('GetMaxMin_TRND', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Find the max/min nodes in a line.",
               notes="Trend lines positions consist of X and Y VVs",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_x', type="VV",
                             doc="X Channel"),
                   Parameter('vv_y', type="VV",
                             doc="Y Channel"),
                   Parameter('vv_z', type="VV",
                             doc="Data Channel"),
                   Parameter('vv_xm', type="VV",
                             doc="X MaxMin (returned)"),
                   Parameter('p5', type="VV",
                             doc="Y MaxMin (returned)"),
                   Parameter('p6', type="VV",
                             doc="Data MaxMin (returned)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="MaxMin Window"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`TRND_NODE`")
               ]),

        Method('GetMesh_TRND', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get the lines in a trend mesh.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('chan', type=Type.STRING,
                             doc="Selected channel"),
                   Parameter('window', type=Type.DOUBLE,
                             doc="MaxMin Window"),
                   Parameter('max_length', type=Type.DOUBLE,
                             doc="Maximum join length"),
                   Parameter('mesh_vv', type="VV",
                             doc=":class:`VV` of type GS_D2POINT (returned)"),
                   Parameter('trnd', type=Type.INT32_T,
                             doc=":def:`TRND_NODE`")
               ]),

        Method('TrndDB_TRND', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Uses a selected channel to find data trends in a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('db', type="DB",
                             doc="Database handle"),
                   Parameter('chan', type=Type.STRING,
                             doc="Selected channel"),
                   Parameter('window', type=Type.DOUBLE,
                             doc="MaxMin Window"),
                   Parameter('angle', type=Type.DOUBLE,
                             doc="Preferred angle, degrees CCW from X"),
                   Parameter('deviation', type=Type.DOUBLE,
                             doc="Allowed deviation"),
                   Parameter('max_length', type=Type.DOUBLE,
                             doc="Longest join"),
                   Parameter('deflection', type=Type.DOUBLE,
                             doc="Maximum deflection in join (can be :def_val:`rDUMMY`)"),
                   Parameter('min_length', type=Type.DOUBLE,
                             doc="Minimum length for trend lines (can be :def_val:`rDUMMY`)"),
                   Parameter('resample', type=Type.DOUBLE,
                             doc="Resampling distance (can be :def_val:`rDUMMY`)"),
                   Parameter('br_angle', type=Type.DOUBLE,
                             doc="Breaking angle, degrees CCW from X (can be :def_val:`rDUMMY`)")
               ])
    ]
}

