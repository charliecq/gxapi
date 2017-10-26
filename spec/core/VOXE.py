from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('VOXE',
                 doc="""
                 :class:`VOX` evaluator class. Used to sample values from
                 the voxel.
                 """)


gx_defines = [
    Define('VOXE_EVAL',
           doc="Voxel Evaluation modes",
           constants=[
               Constant('VOXE_EVAL_NEAR', value='0', type=Type.INT32_T,
                        doc="Nearest value"),
               Constant('VOXE_EVAL_INTERP', value='1', type=Type.INT32_T,
                        doc="Linear Interpolation"),
               Constant('VOXE_EVAL_BEST', value='2', type=Type.INT32_T,
                        doc="Best Interpolation")
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_VOXE', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Create a handle to an :class:`VOXE` object",
               return_type="VOXE",
               return_doc=":class:`VOXE` handle, terminates if creation fails",
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` Object")
               ]),

        Method('Destroy_VOXE', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`VOXE`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxe', type="VOXE",
                             doc=":class:`VOXE` to destroy.")
               ]),

        Method('Profile_VOXE', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Extract a profile of data along points provided.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxe', type="VOXE",
                             doc=":class:`VOXE` object"),
                   Parameter('v_vx', type="VV",
                             doc="X :class:`VV` (must be double)"),
                   Parameter('v_vy', type="VV",
                             doc="Y :class:`VV` (must be double)"),
                   Parameter('v_vz', type="VV",
                             doc="Z :class:`VV` (must be double)"),
                   Parameter('v_vd', type="VV",
                             doc="D :class:`VV` (must be double)"),
                   Parameter('interp', type=Type.INT32_T,
                             doc=":def:`VOXE_EVAL`")
               ]),

        Method('rValue_VOXE', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get a value at a specific point",
               return_type=Type.DOUBLE,
               return_doc="Value at the point or DUMMY if not valid",
               parameters = [
                   Parameter('voxe', type="VOXE",
                             doc=":class:`VOXE` object"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X Location"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y Location"),
                   Parameter('z', type=Type.DOUBLE,
                             doc="Z Location"),
                   Parameter('interp', type=Type.INT32_T,
                             doc=":def:`VOXE_EVAL`")
               ]),

        Method('Vector_VOXE', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Extract a profile of data along a vector",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxe', type="VOXE",
                             doc=":class:`VOXE` object"),
                   Parameter('ox', type=Type.DOUBLE,
                             doc="X Origin"),
                   Parameter('oy', type=Type.DOUBLE,
                             doc="Y Origin"),
                   Parameter('oz', type=Type.DOUBLE,
                             doc="Z Origin"),
                   Parameter('vx', type=Type.DOUBLE,
                             doc="X Delta"),
                   Parameter('vy', type=Type.DOUBLE,
                             doc="Y Delta"),
                   Parameter('vz', type=Type.DOUBLE,
                             doc="Z Delta"),
                   Parameter('vv', type="VV",
                             doc="Data :class:`VV` (must be double)"),
                   Parameter('interp', type=Type.INT32_T,
                             doc=":def:`VOXE_EVAL`")
               ])
    ]
}

