from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('VAU',
                 doc="""
                 This is not a class. These are methods that work on
                 data stored in :class:`VA` objects
                 """)


gx_defines = [
    Define('VAU_PRUNE',
           doc="Prune Options",
           constants=[
               Constant('VAU_PRUNE_DUMMY', value='0', type=Type.INT32_T),
               Constant('VAU_PRUNE_VALID', value='1', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('CondDepthTEM_VAU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Calculate TEM apparent conductivity and depth",
               return_type=Type.VOID,
               parameters = [
                   Parameter('resp_va', type="VA",
                             doc="Response channel (microvolts)"),
                   Parameter('time_va', type="VA",
                             doc="Time channel (milliseconds)"),
                   Parameter('cond_va', type="VA",
                             doc="Conductivity channel (siemen/m)"),
                   Parameter('depth_va', type="VA",
                             doc="Depth (m)"),
                   Parameter('current', type=Type.DOUBLE,
                             doc="Transmitter current"),
                   Parameter('flag', type=Type.INT32_T,
                             doc="Flag  Transmitter defined by moment (0) or by 4 VVs (1) below"),
                   Parameter('min_xvv', type="VV",
                             doc="Minimum X to define transmitter loop layout (moment)"),
                   Parameter('min_yvv', type="VV",
                             doc="Minimum Y to define transmitter loop layout (moment)"),
                   Parameter('max_xvv', type="VV",
                             doc="Maximum X to define transmitter loop layout (moment)"),
                   Parameter('max_yvv', type="VV",
                             doc="Maximum Y to define transmitter loop layout (moment)"),
                   Parameter('t_moment', type=Type.DOUBLE,
                             doc="Transmitter moment (square meters), dummy if the above flag is 1"),
                   Parameter('r_moment', type=Type.DOUBLE,
                             doc="Receiver moment (square meters)"),
                   Parameter('array', type=Type.INT32_T,
                             doc=":def:`TEM_ARRAY`")
               ]),

        Method('Prune_VAU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Prune values from a :class:`VA` based on reference :class:`VA`",
               notes="""
               Pruning will shorten the :class:`VA` by removing values
               that are either dummy or non-dummy in the reference
               :class:`VA`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('v_ap', type="VA",
                             doc=":class:`VA` to prune"),
                   Parameter('vv_r', type="VV",
                             doc="Reference :class:`VV`"),
                   Parameter('o', type=Type.INT32_T,
                             doc=":def:`VAU_PRUNE`")
               ]),

        Method('SectionCondTEM_VAU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Derive TEM apparent conductivity section at given depth",
               return_type=Type.VOID,
               parameters = [
                   Parameter('cond_va', type="VA",
                             doc="Conductivity :class:`VA`,:def_val:`GS_DOUBLE`"),
                   Parameter('depth_va', type="VA",
                             doc="Depth :class:`VA`,:def_val:`GS_DOUBLE`"),
                   Parameter('section', type=Type.DOUBLE,
                             doc="Depth derive TEM section (same unit as Depth :class:`VA`)"),
                   Parameter('out_vv', type="VV",
                             doc="Returned conductivity at given depth,:def_val:`GS_DOUBLE`")
               ]),

        Method('TotalVector_VAU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate total vector for X,Y and Z components",
               return_type=Type.VOID,
               parameters = [
                   Parameter('xva', type="VA",
                             doc="X Component object"),
                   Parameter('yva', type="VA",
                             doc="Y Component object"),
                   Parameter('zva', type="VA",
                             doc="Z Component object"),
                   Parameter('tva', type="VA",
                             doc="Returned total vector :class:`VA` object")
               ])
    ]
}

