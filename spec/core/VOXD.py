from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('VOXD',
                 doc=":class:`VOX` Display object.")





gx_methods = {
    'Miscellaneous': [

        Method('Create_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Create a new :class:`VOXD`",
               notes="""
               Fails if the :class:`VOX` object is NOT thematic.
               (See the :func:`CreateThematic_VOXD` function.)
               """,
               return_type="VOXD",
               return_doc=":class:`VOXD` handle, terminates if creation fails",
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` Object"),
                   Parameter('table', type=Type.STRING,
                             doc='Color table name, "" for default'),
                   Parameter('zone', type=Type.INT32_T,
                             doc=":def:`ITR_ZONE`"),
                   Parameter('contour', type=Type.DOUBLE,
                             doc="Color contour interval or :def_val:`rDUMMY`")
               ]),

        Method('CreateITR_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Create a new :class:`VOXD` with our own :class:`ITR`",
               notes="""
               Fails if the :class:`VOX` object is thematic.
               (See the :func:`CreateThematic_VOXD` function.)
               """,
               return_type="VOXD",
               return_doc=":class:`VOXD` handle, terminates if creation fails",
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` Object"),
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` Object")
               ]),

        Method('CreateThematic_VOXD', module='geoengine.map', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a new :class:`VOXD` for a thematic :class:`VOX` object.",
               notes="""
               A thematic voxel is one where the stored integer values
               represent indices into an internally stored :class:`TPAT` object.
               Thematic voxels contain their own color definitions, and
               normal numerical operations, such as applying ITRs for display,
               are not valid.
               
               To determine if a :class:`VOX` object is thematic, use the
               :func:`iIsThematic_VOXD` function.
               
               Fails if the :class:`VOX` object is NOT thematic.
               """,
               return_type="VOXD",
               return_doc=":class:`VOXD` handle, terminates if creation fails",
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` Object")
               ]),

        Method('iIsThematic_VOXD', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Is this a thematic voxel?",
               notes="""
               A thematic voxel is one where the stored integer values
               represent indices into an internally stored :class:`TPAT` object.
               Thematic voxels contain their own color definitions, and
               normal numerical operations, such as applying ITRs for display,
               are not valid.
               """,
               return_type=Type.INT32_T,
               return_doc="1 if :class:`VOX` is thematic",
               parameters = [
                   Parameter('voxd', type="VOXD",
                             doc=":class:`VOXD` object")
               ]),

        Method('GetThematicInfo_VOXD', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Get a copy of a thematic voxel's :class:`TPAT` object and a :class:`VV` containing the current display selections.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxd', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('tpat', type="TPAT",
                             doc=":class:`TPAT` object to get"),
                   Parameter('vv', type="VV",
                             doc=":class:`VV` (int) object to fill with current selections")
               ]),

        Method('SetThematicSelection_VOXD', module='geoengine.map', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Get a copy of a thematic voxel's :class:`TPAT` object and a :class:`VV` containing the current display selections.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxd', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('vv', type="VV",
                             doc=":class:`VV` (int) object to set the current selections to")
               ]),

        Method('Destroy_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`VOXD`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxd', type="VOXD",
                             doc=":class:`VOXD` to destroy.")
               ]),

        Method('GetDrawControls_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the draw controls",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxd', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('box', type=Type.INT32_T, is_ref=True,
                             doc="Draw Bounding Box"),
                   Parameter('trans', type=Type.DOUBLE, is_ref=True,
                             doc="Transparency"),
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="Min X"),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="Min Y"),
                   Parameter('min_z', type=Type.DOUBLE, is_ref=True,
                             doc="Min Z"),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="Max X"),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="Max Y"),
                   Parameter('max_z', type=Type.DOUBLE, is_ref=True,
                             doc="Max Z")
               ]),

        Method('IGetName_VOXD', module='geoengine.map', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Gets the file name of the voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxd', type="VOXD",
                             doc=":class:`VOXD` handle"),
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="File name returned"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_FILE',
                             doc="File name string size")
               ]),

        Method('GetITR_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`ITR` of the :class:`VOXD`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxd', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object")
               ]),

        Method('GetShellControls_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the shell controls",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxd', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('min', type=Type.DOUBLE, is_ref=True,
                             doc="Min Value (:def_val:`rDUMMY` for no limit)"),
                   Parameter('max', type=Type.DOUBLE, is_ref=True,
                             doc="Max Value (:def_val:`rDUMMY` for no limit)")
               ]),

        Method('SetDrawControls_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Set the draw controls",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxd', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('box', type=Type.INT32_T,
                             doc="Draw Bounding Box"),
                   Parameter('trans', type=Type.DOUBLE,
                             doc="Transparency"),
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

        Method('SetITR_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Set the :class:`ITR` of the :class:`VOXD`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxd', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('itr', type="ITR",
                             doc=":class:`ITR` object")
               ]),

        Method('SetShellControls_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Set the shell controls",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxd', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('min', type=Type.DOUBLE,
                             doc="Min Value (:def_val:`rDUMMY` for no limit)"),
                   Parameter('max', type=Type.DOUBLE,
                             doc="Max Value (:def_val:`rDUMMY` for no limit)")
               ])
    ]
}

