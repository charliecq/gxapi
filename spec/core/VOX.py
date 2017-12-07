from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('VOX',
                 doc="""
                 High Performance 3D Grid. Designed for accessing
                 3D grids quickly using slices. It designed arround
                 non-uniform multi-resolution  compressed storage.
                 To sample a voxel at specific locations, use :class:`VOXE`.
                 """)


gx_defines = [
    Define('VOX_DIR',
           doc="Voxel direction",
           constants=[
               Constant('VOX_DIR_XY', value='0', type=Type.INT32_T,
                        doc="X/Y Plane (Fastest)"),
               Constant('VOX_DIR_XZ', value='1', type=Type.INT32_T,
                        doc="X/Z Plane (Middle)"),
               Constant('VOX_DIR_YZ', value='2', type=Type.INT32_T,
                        doc="Y/Z Plane (Slowest)")
           ]),

    Define('VOX_DIRECTION',
           doc="Voxel export direction",
           constants=[
               Constant('VOX_3D_DIR_XYZ', value='0', type=Type.INT32_T,
                        doc="XYZ"),
               Constant('VOX_3D_DIR_YXZ', value='1', type=Type.INT32_T,
                        doc="YXZ"),
               Constant('VOX_3D_DIR_XZY', value='2', type=Type.INT32_T,
                        doc="XZY"),
               Constant('VOX_3D_DIR_YZX', value='3', type=Type.INT32_T,
                        doc="YZX"),
               Constant('VOX_3D_DIR_ZXY', value='4', type=Type.INT32_T,
                        doc="ZXY"),
               Constant('VOX_3D_DIR_ZYX', value='5', type=Type.INT32_T,
                        doc="ZYX")
           ]),

    Define('VOX_FILTER3D',
           doc="Voxel filter type",
           constants=[
               Constant('VOX_FILTER3D_FILE', value='0', type=Type.INT32_T,
                        doc="Specify a file containing the 27-point filter"),
               Constant('VOX_FILTER3D_SMOOTHING', value='1', type=Type.INT32_T,
                        doc="Smoothing filter"),
               Constant('VOX_FILTER3D_LAPLACE', value='2', type=Type.INT32_T,
                        doc="Laplace filter"),
               Constant('VOX_FILTER3D_X_GRADIENT', value='3', type=Type.INT32_T,
                        doc="X-Gradient filter"),
               Constant('VOX_FILTER3D_Y_GRADIENT', value='4', type=Type.INT32_T,
                        doc="Y-Gradient filter"),
               Constant('VOX_FILTER3D_Z_GRADIENT', value='5', type=Type.INT32_T,
                        doc="Z-Gradient filter"),
               Constant('VOX_FILTER3D_TOTAL_GRADIENT', value='6', type=Type.INT32_T,
                        doc="Total-Gradient filter")
           ]),

    Define('VOX_GOCAD_ORIENTATION',
           doc="GOCAD Orientations",
           constants=[
               Constant('VOX_GOCAD_ORIENTATIONS_NORMAL', value='0', type=Type.INT32_T,
                        doc="Normal"),
               Constant('VOX_GOCAD_ORIENTATIONS_INVERTED', value='1', type=Type.INT32_T,
                        doc="Inverted (Z)"),
               Constant('VOX_GOCAD_ORIENTATIONS_NORMAL_ZFIRST', value='2', type=Type.INT32_T,
                        doc="Normal (ZFirst)"),
               Constant('VOX_GOCAD_ORIENTATIONS_INVERTED_ZFIRST', value='3', type=Type.INT32_T,
                        doc="Inverted (Z) (ZFirst)")
           ]),

    Define('VOX_GRID_LOGOPT',
           doc="Voxel log gridding options",
           constants=[
               Constant('VOX_GRID_LOGOPT_LINEAR', value='0', type=Type.INT32_T,
                        doc="Linear"),
               Constant('VOX_GRID_LOGOPT_LOG_SAVELINEAR', value='-1', type=Type.INT32_T,
                        doc="Log, save as linear"),
               Constant('VOX_GRID_LOGOPT_LOGLINEAR_SAVELINEAR', value='-2', type=Type.INT32_T,
                        doc="Log-linear, save as linear"),
               Constant('VOX_GRID_LOGOPT_LOG_SAVELOG', value='1', type=Type.INT32_T,
                        doc="Log, save as log"),
               Constant('VOX_GRID_LOGOPT_LOGLINEAR_SAVELOG', value='2', type=Type.INT32_T,
                        doc="Log-linear, save as log")
           ]),

    Define('VOX_ORIGIN',
           doc="Voxel origin",
           constants=[
               Constant('VOX_ORIGIN_BOTTOM', value='0', type=Type.INT32_T,
                        doc="Bottom corner (standard Geosoft)"),
               Constant('VOX_ORIGIN_TOP', value='1', type=Type.INT32_T,
                        doc="Top corner")
           ]),

    Define('VOX_SLICE_MODE',
           doc="Voxel export direction",
           constants=[
               Constant('VOX_SLICE_MODE_LINEAR', value='1', type=Type.INT32_T,
                        doc="Linear"),
               Constant('VOX_SLICE_MODE_NEAREST', value='0', type=Type.INT32_T,
                        doc="Nearest")
           ]),

    Define('VOX_VECTORVOX_IMPORT',
           doc="Voxel direction",
           constants=[
               Constant('VOX_VECTORVOX_XYZ', value='0', type=Type.INT32_T,
                        doc="X, Y and Z"),
               Constant('VOX_VECTORVOX_UVW', value='1', type=Type.INT32_T,
                        doc="U, V and W"),
               Constant('VOX_VECTORVOX_AID', value='2', type=Type.INT32_T,
                        doc="Amplitude, Inclination and Declination")
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('CalcStats_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Calculate Statistics",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('st', type="ST",
                             doc=":class:`ST` Object")
               ]),

        Method('Create_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Create a handle to an :class:`VOX` object",
               return_type="VOX",
               return_doc=":class:`VOX` handle, terminates if creation fails",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('CreatePG_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Create a 3D :class:`PG` from a :class:`VOX` object",
               return_type="PG",
               return_doc=":class:`PG` Object",
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` Handle")
               ]),

        Method('CreateTypePG_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Create a 3D :class:`PG` from a :class:`VOX` object with a specific Type",
               return_type="PG",
               return_doc=":class:`PG` Object",
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` Handle"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`")
               ]),

        Method('Destroy_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`VOX`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` to destroy.")
               ]),

        Method('Dump_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Export all layers of this :class:`VOX` in all directions.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` Handle"),
                   Parameter('name', type=Type.STRING,
                             doc="Name of grids (each layers adds _Dir_Z to the name)")
               ]),

        Method('ExportIMG_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Export all layers of this :class:`VOX` into grid files.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` Handle"),
                   Parameter('name', type=Type.STRING,
                             doc="Name of grids (each layers adds _Number to the name)"),
                   Parameter('dir', type=Type.INT32_T,
                             doc=":def:`VOX_DIR`")
               ]),

        Method('ExportToGrids_VOX', module='geoengine.core', version='7.3.0',
               availability=Availability.PUBLIC, 
               doc="Export all layers of this :class:`VOX` into grid files, with optional cell size.",
               notes="""
               If the cell size is not specified, then:
               1. If the cell sizes are uniform in a given direction, that size is used
               2. If the cell sizes are variable in a given direction, then the smallest size is used
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` Handle"),
                   Parameter('name', type=Type.STRING,
                             doc="Name of grids (each layers adds _Number to the name)"),
                   Parameter('dir', type=Type.INT32_T,
                             doc=":def:`VOX_DIR`"),
                   Parameter('start', type=Type.INT32_T,
                             doc="Starting index"),
                   Parameter('incr', type=Type.INT32_T,
                             doc="Increment in index"),
                   Parameter('num', type=Type.INT32_T,
                             doc="Total number of grids (-1 or :def_val:`iDUMMY` for all)"),
                   Parameter('cell_size', type=Type.DOUBLE,
                             doc="Cell size (can be :def_val:`GS_R8DM`)"),
                   Parameter('interp', type=Type.INT32_T,
                             doc=":def:`VOX_SLICE_MODE`")
               ]),

        Method('ExportXML_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Export a :class:`VOX` to a compressed XML file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel', type=Type.STRING,
                             doc="Voxel file name"),
                   Parameter('crc', type="CRC", is_ref=True,
                             doc="CRC returned - not implemented - always returns 0."),
                   Parameter('file', type=Type.STRING,
                             doc="Output XML file")
               ]),

        Method('ExportSegY_VOX', module='geoengine.core', version='8.5',
               availability=Availability.PUBLIC, 
               doc="Export a voxel to a depth SEG-Y file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel to export"),
                   Parameter('output_segy_filename', type=Type.STRING,
                             doc="SEG-Y filename to create"),
                   Parameter('sample_interval', type=Type.DOUBLE,
                             doc="Sampling interval (can be :def_val:`GS_R8DM` if input voxel has constant Z cell size)")
               ]),

        Method('ExportJIGsXML_VOX', module='geoengine.core', version='8.4',
               availability=Availability.PUBLIC, 
               doc="Export a :class:`VOX` to a compressed XML file. Verbose version.",
               return_type=Type.VOID,
               return_doc="Exports all values and stats by JIG.",
               parameters = [
                   Parameter('voxel', type=Type.STRING,
                             doc="Voxel file name"),
                   Parameter('file', type=Type.STRING,
                             doc="Output XML file")
               ]),

        Method('ExportXYZ_VOX', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Export a Voxel to an XYZ File",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX"),
                   Parameter('xyz', type=Type.STRING,
                             doc="File Name"),
                   Parameter('dir', type=Type.INT32_T,
                             doc=":def:`VOX_DIRECTION`"),
                   Parameter('rev_x', type=Type.INT32_T,
                             doc="Reverse X ? (0/1)"),
                   Parameter('rev_y', type=Type.INT32_T,
                             doc="Reverse Y ? (0/1)"),
                   Parameter('rev_z', type=Type.INT32_T,
                             doc="Reverse Z ? (0/1)"),
                   Parameter('dummies', type=Type.INT32_T,
                             doc="Write Dummies? (0/1)")
               ]),

        Method('Filter_VOX', module='geoengine.core', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Apply a 3D filter to a voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('filter', type=Type.INT32_T,
                             doc=":def:`VOX_FILTER3D`"),
                   Parameter('filter_file', type=Type.STRING,
                             doc="Filter file, if filter is :def_val:`VOX_FILTER3D_FILE`"),
                   Parameter('n_passes', type=Type.INT32_T,
                             doc="Number of filter passes"),
                   Parameter('interpolate_dummies', type=Type.INT32_T,
                             doc="(1: interpolate dummies)"),
                   Parameter('output_vox', type=Type.STRING,
                             doc="Output voxel file name.")
               ]),

        Method('GenerateDB_VOX', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a :class:`VOX` from a Database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel_file', type=Type.STRING,
                             doc="Voxel Name"),
                   Parameter('db', type="DB",
                             doc=":class:`DB` To import from"),
                   Parameter('symb', type="DB_SYMB",
                             doc="Symbol to import data from")
               ]),

        Method('GenerateVectorVoxelFromDB_VOX', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Generate a vector voxel :class:`VOX` from a Database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel_file', type=Type.STRING,
                             doc="Voxel Name"),
                   Parameter('db', type="DB",
                             doc=":class:`DB` To import from"),
                   Parameter('type', type=Type.INT32_T,
                             doc="VOX_VECTORVOX_IMPORTImport XYZ, UVW or Amplitude/Inclination/Declination channels"),
                   Parameter('symb_x', type="DB_SYMB",
                             doc="Symbol to import X, U or Amplitude data from"),
                   Parameter('symb_y', type="DB_SYMB",
                             doc="Symbol to import Y, V or Inclination data from"),
                   Parameter('symb_z', type="DB_SYMB",
                             doc="Symbol to import Z, W or Declination data from"),
                   Parameter('inc', type=Type.DOUBLE,
                             doc="Inclination value for :def_val:`VOX_VECTORVOX_UVW` (-90° to 90°)"),
                   Parameter('dec', type=Type.DOUBLE,
                             doc="Declination value for :def_val:`VOX_VECTORVOX_UVW` (-180° to 180°)")
               ]),

        Method('GeneratePG_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Generate a :class:`VOX` from a 3D Pager",
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('pg', type="PG",
                             doc="Pager with the Voxel Data"),
                   Parameter('ox', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('oy', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('oz', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('cx', type=Type.DOUBLE,
                             doc="Cell Size X"),
                   Parameter('cy', type=Type.DOUBLE,
                             doc="Cell Size Y"),
                   Parameter('cz', type=Type.DOUBLE,
                             doc="Cell Size Z"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection"),
                   Parameter('meta', type="META",
                             doc="Metadata")
               ]),

        Method('GenerateConstantValue_VOX', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Generate a :class:`VOX` with a constant value",
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('value', type=Type.DOUBLE,
                             doc="Value to use"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`"),
                   Parameter('ox', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('oy', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('oz', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('cx', type=Type.DOUBLE,
                             doc="Cell Size X"),
                   Parameter('cy', type=Type.DOUBLE,
                             doc="Cell Size Y"),
                   Parameter('cz', type=Type.DOUBLE,
                             doc="Cell Size Z"),
                   Parameter('cell_count_x', type=Type.INT32_T,
                             doc="Cell Count X"),
                   Parameter('cell_count_y', type=Type.INT32_T,
                             doc="Cell Count Y"),
                   Parameter('cell_count_z', type=Type.INT32_T,
                             doc="Cell Count Z"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection"),
                   Parameter('meta', type="META",
                             doc="Metadata")
               ]),

        Method('GeneratePGVV_VOX', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Generate a :class:`VOX` from a 3D Pager, cells sizes passed in VVs.",
               notes="The input cell size VVs' lengths must match the input :class:`PG` dimensions.",
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('pg', type="PG",
                             doc="Pager with the Voxel Data"),
                   Parameter('ox', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('oy', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('oz', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('cx', type="VV",
                             doc="Cell Sizes X"),
                   Parameter('cy', type="VV",
                             doc="Cell Sizes Y"),
                   Parameter('cz', type="VV",
                             doc="Cell Sizes Z"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection"),
                   Parameter('meta', type="META",
                             doc="Metadata")
               ]),

        Method('GenerateConstantValueVV_VOX', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Generate a :class:`VOX` with a constant value, cells sizes passed in VVs.",
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('value', type=Type.DOUBLE,
                             doc="The Value to use"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`"),
                   Parameter('ox', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('oy', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('oz', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('cx', type="VV",
                             doc="Cell Sizes X"),
                   Parameter('cy', type="VV",
                             doc="Cell Sizes Y"),
                   Parameter('cz', type="VV",
                             doc="Cell Sizes Z"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection"),
                   Parameter('meta', type="META",
                             doc="Metadata")
               ]),

        Method('InitGenerateBySubsetPG_VOX', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Initialize the generate of a :class:`VOX` from a series of 3D subset pagers",
               notes="""
               Call :func:`InitGenerateBySubsetPG_VOX` first, then add a series of subset PGs using :func:`AddGenerateBySubsetPG_VOX`, and finally
               serialize using :func:`EndGenerateBySubsetPG_VOX`
               """,
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('data_type', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`"),
                   Parameter('nx', type=Type.INT32_T,
                             doc="Points in X"),
                   Parameter('ny', type=Type.INT32_T,
                             doc="Points in Y"),
                   Parameter('nz', type=Type.INT32_T,
                             doc="Points in Z")
               ]),

        Method('AddGenerateBySubsetPG_VOX', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="""
               Add a subset 3D  pagers. These should be "slabs", 16 wide in the input direction, and the size of the
               full voxel in the other two directions.
               """,
               notes="See :func:`InitGenerateBySubsetPG_VOX` and :func:`EndGenerateBySubsetPG_VOX`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('pg', type="PG",
                             doc="Subset pager with the Voxel Data"),
                   Parameter('dir', type=Type.INT32_T,
                             doc='Subset orientation - the "16" (thin) dimension is in the other axis.:def:`VOX_DIR`'),
                   Parameter('offset', type=Type.INT32_T,
                             doc='Offset of the subset :class:`PG` corner, along the "thin" dimension.')
               ]),

        Method('EndGenerateBySubsetPG_VOX', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Output the voxel, after adding all the subset PGs.",
               notes="You must begin by calling :func:`InitGenerateBySubsetPG_VOX` and add data using :func:`AddGenerateBySubsetPG_VOX`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('ox', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('oy', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('oz', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('cx', type=Type.DOUBLE,
                             doc="Cell Size X"),
                   Parameter('cy', type=Type.DOUBLE,
                             doc="Cell Size Y"),
                   Parameter('cz', type=Type.DOUBLE,
                             doc="Cell Size Z"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection"),
                   Parameter('meta', type="META",
                             doc="Metadata")
               ]),

        Method('GetArea_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the area of the voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
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

        Method('GetGOCADLocation_VOX', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the location of a voxel with origin and scaled xyz vectors for use with GOCAD.",
               notes="""
               This is used for GOCAD voxel calculations, and begins with the
               origin at (0,0,0), not the actual location of the corner point.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('origin_x', type=Type.DOUBLE, is_ref=True,
                             doc="Origin X"),
                   Parameter('origin_y', type=Type.DOUBLE, is_ref=True,
                             doc="Origin Y"),
                   Parameter('origin_z', type=Type.DOUBLE, is_ref=True,
                             doc="Origin Z"),
                   Parameter('vect_xx', type=Type.DOUBLE, is_ref=True,
                             doc="VectX X"),
                   Parameter('vect_xy', type=Type.DOUBLE, is_ref=True,
                             doc="VectX Y"),
                   Parameter('vect_xz', type=Type.DOUBLE, is_ref=True,
                             doc="VectX Z"),
                   Parameter('vect_yx', type=Type.DOUBLE, is_ref=True,
                             doc="VectY X"),
                   Parameter('vect_yy', type=Type.DOUBLE, is_ref=True,
                             doc="VectY Y"),
                   Parameter('vect_yz', type=Type.DOUBLE, is_ref=True,
                             doc="VectY Z"),
                   Parameter('vect_zx', type=Type.DOUBLE, is_ref=True,
                             doc="VectZ X"),
                   Parameter('vect_zy', type=Type.DOUBLE, is_ref=True,
                             doc="VectZ Y"),
                   Parameter('vect_zz', type=Type.DOUBLE, is_ref=True,
                             doc="VectZ Z")
               ]),

        Method('GetGridSectionCellSizes_VOX', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Get default cell sizes in X and Y for a section grid.",
               notes="""
               This function determines default cell sizes for a vertical grid
               slicing a voxel. It tries to match the "X" and "Y" sizes (in the grid
               coordinates) with the projection of the voxel's cells onto the grid
               plane. It uses a few simple rules:
               
               If the voxel is rotated about a horizontal axis (i.e. if its own "Z" axis
               is not vertical, then both cell sizes are set to the smallest voxel dimension
               (a single volume pixel) in X, Y and Z.
               
               If the voxel is "horizontal", then the angle between the
               section azimuth and the voxel's own X and Y axes is used to
               calculate a value which varies between the minimum X size and the
               minimum Y size, and this is used for the grid's "X" cell size.
               (in other words, if the section is parallel to the voxel "X" axis,
               then the returned "X" cells size is equal to the voxel's minimum "Y" cell size.
               The grid's "Y" cell size is set to the voxel's minimum "Z" cell size.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel object"),
                   Parameter('az', type=Type.DOUBLE,
                             doc="Input section azimuth (degrees CCW from North)"),
                   Parameter('cell_size_x', type=Type.DOUBLE, is_ref=True,
                             doc="Returned X cell size (horizontal) in m"),
                   Parameter('cell_size_y', type=Type.DOUBLE, is_ref=True,
                             doc="Returned Y cell size (vertical) in m")
               ]),

        Method('GetInfo_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get information about a voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('type', type=Type.INT32_T, is_ref=True,
                             doc="Data Type"),
                   Parameter('array', type=Type.INT32_T, is_ref=True,
                             doc="Array Size"),
                   Parameter('x', type=Type.INT32_T, is_ref=True,
                             doc="Elements in X"),
                   Parameter('y', type=Type.INT32_T, is_ref=True,
                             doc="Elements in Y"),
                   Parameter('z', type=Type.INT32_T, is_ref=True,
                             doc="Elements in Z")
               ]),

        Method('GetIPJ_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the projection of the voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` object to save :class:`VOX`'s meta to")
               ]),

        Method('GetLimits_VOX', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the range of indices with non-dummy data.",
               notes="""
               Find the non-dummy volume of a :class:`VOX` object. If the voxel is all dummies,
               returns :def_val:`iMAX` for the minima, and :def_val:`iMIN` for the maxima.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel object"),
                   Parameter('min_x', type=Type.INT32_T, is_ref=True,
                             doc="Index of minimum valid data in X."),
                   Parameter('min_y', type=Type.INT32_T, is_ref=True,
                             doc="Index of minimum valid data in Y."),
                   Parameter('min_z', type=Type.INT32_T, is_ref=True,
                             doc="Index of minimum valid data in Z."),
                   Parameter('max_x', type=Type.INT32_T, is_ref=True,
                             doc="Index of maximum valid data in X."),
                   Parameter('max_y', type=Type.INT32_T, is_ref=True,
                             doc="Index of maximum valid data in Y."),
                   Parameter('max_z', type=Type.INT32_T, is_ref=True,
                             doc="Index of maximum valid data in Z.")
               ]),

        Method('GetLimitsXYZ_VOX', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the range in true XYZ of non-dummy data.",
               notes="""
               Find the non-dummy volume of a :class:`VOX` in true (X, Y, Z). This method
               works for voxels which are rotated or oriented in 3D, and returns
               the true min and max X, Y and Z limits in the data.
               The bounds are the bounds for the voxel
               center points. If the voxel is all dummies,
               returns :def_val:`rMAX` for the minima, and :def_val:`rMIN` for the maxima.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel object"),
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum valid data in X."),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum valid data in Y."),
                   Parameter('min_z', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum valid data in Z."),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum valid data in X."),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum valid data in Y."),
                   Parameter('max_z', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum valid data in Z.")
               ]),

        Method('GetLocation_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get Location information",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('origin_x', type=Type.DOUBLE, is_ref=True,
                             doc="Origin X"),
                   Parameter('origin_y', type=Type.DOUBLE, is_ref=True,
                             doc="Origin Y"),
                   Parameter('origin_z', type=Type.DOUBLE, is_ref=True,
                             doc="Origin Z"),
                   Parameter('vv_x', type="VV",
                             doc="Cell sizes in X"),
                   Parameter('vv_y', type="VV",
                             doc="Cell sizes in Y"),
                   Parameter('vv_z', type="VV",
                             doc="Cell sizes in Z")
               ]),

        Method('GetLocationPoints_VOX', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the computed location points.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('vv_x', type="VV",
                             doc="Locations in X"),
                   Parameter('vv_y', type="VV",
                             doc="Locations in Y"),
                   Parameter('vv_z', type="VV",
                             doc="Locations in Z")
               ]),

        Method('GetMETA_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the metadata of a voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('meta', type="META",
                             doc=":class:`META` object to save :class:`VOX`'s meta to")
               ]),

        Method('GetRealLocation_VOX', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the location of a voxel with origin and scaled xyz vectors",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('origin_x', type=Type.DOUBLE, is_ref=True,
                             doc="Origin X"),
                   Parameter('origin_y', type=Type.DOUBLE, is_ref=True,
                             doc="Origin Y"),
                   Parameter('origin_z', type=Type.DOUBLE, is_ref=True,
                             doc="Origin Z"),
                   Parameter('vect_xx', type=Type.DOUBLE, is_ref=True,
                             doc="VectX X"),
                   Parameter('vect_xy', type=Type.DOUBLE, is_ref=True,
                             doc="VectX Y"),
                   Parameter('vect_xz', type=Type.DOUBLE, is_ref=True,
                             doc="VectX Z"),
                   Parameter('vect_yx', type=Type.DOUBLE, is_ref=True,
                             doc="VectY X"),
                   Parameter('vect_yy', type=Type.DOUBLE, is_ref=True,
                             doc="VectY Y"),
                   Parameter('vect_yz', type=Type.DOUBLE, is_ref=True,
                             doc="VectY Z"),
                   Parameter('vect_zx', type=Type.DOUBLE, is_ref=True,
                             doc="VectZ X"),
                   Parameter('vect_zy', type=Type.DOUBLE, is_ref=True,
                             doc="VectZ Y"),
                   Parameter('vect_zz', type=Type.DOUBLE, is_ref=True,
                             doc="VectZ Z")
               ]),

        Method('GetSimpleLocation_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get Simple Location information",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('origin_x', type=Type.DOUBLE, is_ref=True,
                             doc="Origin X"),
                   Parameter('origin_y', type=Type.DOUBLE, is_ref=True,
                             doc="Origin Y"),
                   Parameter('origin_z', type=Type.DOUBLE, is_ref=True,
                             doc="Origin Z"),
                   Parameter('cell_x', type=Type.DOUBLE, is_ref=True,
                             doc="Cell Sizes in X (:def_val:`rDUMMY` if not uniform)"),
                   Parameter('cell_y', type=Type.DOUBLE, is_ref=True,
                             doc="Cell Sizes in Y (:def_val:`rDUMMY` if not uniform)"),
                   Parameter('cell_z', type=Type.DOUBLE, is_ref=True,
                             doc="Cell Sizes in Z (:def_val:`rDUMMY` if not uniform)")
               ]),

        Method('GetStats_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get precomputed statistics on this object.",
               return_type="ST",
               return_doc=":class:`ST` object",
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object")
               ]),

        Method('GetTPAT_VOX', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a copy of a thematic voxel's :class:`TPAT` object.",
               notes="""
               Each row in the :class:`TPAT` object corresponds to a stored index
               value in the thematic voxel. The :class:`TPAT` should NOT be modified
               by the addition or deletion of items, if it is to be
               restored into the :class:`VOX` object, but the CODE, LABEL, DESCRIPTION
               or COLOR info can be changed.
               The :class:`TPAT` object is stored inside the :class:`VOX` :class:`META` object.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('tpat', type="TPAT",
                             doc=":class:`TPAT` object to get")
               ]),

        Method('GridPoints_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Grid a :class:`VOX` from point :class:`VV`'s.",
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('error', type=Type.STRING,
                             doc='Name of error :class:`VOX` ("" for none)'),
                   Parameter('cell_size', type=Type.DOUBLE,
                             doc="Cell size (DUMMY for default)"),
                   Parameter('var_only', type=Type.INT32_T,
                             doc="Variogram Only"),
                   Parameter('min_radius', type=Type.DOUBLE,
                             doc="Minimum Search Radius (DUMMY for none)"),
                   Parameter('max_radius', type=Type.DOUBLE,
                             doc="Maximum Search Radius (DUMMY for none)"),
                   Parameter('min_points', type=Type.INT32_T,
                             doc="Minimum Search Points"),
                   Parameter('max_points', type=Type.INT32_T,
                             doc="Maximum Search Points"),
                   Parameter('model', type=Type.INT32_T,
                             doc="Model number 1-power, 2-sperical, 3-gaussian, 4-exponential"),
                   Parameter('power', type=Type.DOUBLE,
                             doc="Power"),
                   Parameter('slope', type=Type.DOUBLE,
                             doc="Slope"),
                   Parameter('range', type=Type.DOUBLE,
                             doc="Range"),
                   Parameter('nugget', type=Type.DOUBLE,
                             doc="Nugget"),
                   Parameter('sill', type=Type.DOUBLE,
                             doc="Sill"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('vv_z', type="VV",
                             doc="Z :class:`VV`"),
                   Parameter('vv_d', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('ipj', type="IPJ")
               ]),

        Method('GridPointsZ_VOX', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Grid a :class:`VOX` from point :class:`VV`'s (using variable Z's)",
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('error', type=Type.STRING,
                             doc='Name of error :class:`VOX` ("" for none)'),
                   Parameter('cell_size', type=Type.DOUBLE,
                             doc="Cell size (DUMMY for default)"),
                   Parameter('cell_size_z', type=Type.STRING,
                             doc='Cell size in Z ("" for default)'),
                   Parameter('var_only', type=Type.INT32_T,
                             doc="Variogram Only"),
                   Parameter('min_radius', type=Type.DOUBLE,
                             doc="Minimum Search Radius (DUMMY for none)"),
                   Parameter('max_radius', type=Type.DOUBLE,
                             doc="Maximum Search Radius (DUMMY for none)"),
                   Parameter('min_points', type=Type.INT32_T,
                             doc="Minimum Search Points"),
                   Parameter('max_points', type=Type.INT32_T,
                             doc="Maximum Search Points"),
                   Parameter('model', type=Type.INT32_T,
                             doc="Model number 1-power, 2-sperical, 3-gaussian, 4-exponential"),
                   Parameter('power', type=Type.DOUBLE,
                             doc="Power"),
                   Parameter('slope', type=Type.DOUBLE,
                             doc="Slope"),
                   Parameter('range', type=Type.DOUBLE,
                             doc="Range"),
                   Parameter('nugget', type=Type.DOUBLE,
                             doc="Nugget"),
                   Parameter('sill', type=Type.DOUBLE,
                             doc="Sill"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('vv_z', type="VV",
                             doc="Z :class:`VV`"),
                   Parameter('vv_d', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('ipj', type="IPJ")
               ]),

        Method('GridPointsZEx_VOX', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Grid a :class:`VOX` from point :class:`VV`'s (using variable Z's)",
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('error', type=Type.STRING,
                             doc='Name of error :class:`VOX` ("" for none)'),
                   Parameter('cell_size', type=Type.DOUBLE,
                             doc="Cell size (DUMMY for default)"),
                   Parameter('cell_size_z', type=Type.STRING,
                             doc='Cell size in Z ("" for default)'),
                   Parameter('var_only', type=Type.INT32_T,
                             doc="Variogram Only"),
                   Parameter('min_radius', type=Type.DOUBLE,
                             doc="Minimum Search Radius (DUMMY for none)"),
                   Parameter('max_radius', type=Type.DOUBLE,
                             doc="Maximum Search Radius (DUMMY for none)"),
                   Parameter('min_points', type=Type.INT32_T,
                             doc="Minimum Search Points"),
                   Parameter('max_points', type=Type.INT32_T,
                             doc="Maximum Search Points"),
                   Parameter('model', type=Type.INT32_T,
                             doc="Model number 1-power, 2-sperical, 3-gaussian, 4-exponential"),
                   Parameter('power', type=Type.DOUBLE,
                             doc="Power"),
                   Parameter('slope', type=Type.DOUBLE, is_ref=True,
                             doc="Slope"),
                   Parameter('range', type=Type.DOUBLE, is_ref=True,
                             doc="Range"),
                   Parameter('nugget', type=Type.DOUBLE,
                             doc="Nugget"),
                   Parameter('sill', type=Type.DOUBLE, is_ref=True,
                             doc="Sill"),
                   Parameter('strike', type=Type.DOUBLE,
                             doc="Strike"),
                   Parameter('dip', type=Type.DOUBLE,
                             doc="Dip"),
                   Parameter('plunge', type=Type.DOUBLE,
                             doc="Plunge"),
                   Parameter('along_strike_weight', type=Type.DOUBLE,
                             doc="Strike Weight"),
                   Parameter('down_dip_weight', type=Type.DOUBLE,
                             doc="Dip Plane Weight"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('vv_z', type="VV",
                             doc="Z :class:`VV`"),
                   Parameter('vv_d', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('ipj', type="IPJ")
               ]),

        Method('iCanAppendTo_VOX', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Check if this voxel can append to a surface file.",
               return_type=Type.INT32_T,
               return_doc="1 if can append",
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel object"),
                   Parameter('surface_file', type=Type.STRING,
                             doc="Surface file")
               ]),

        Method('IGetCellSizeStrings_VOX', module='geoengine.core', version='6.3.1',
               availability=Availability.PUBLIC, 
               doc="Get the Location Strings",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel"),
                   Parameter('loc_x', type=Type.STRING, is_ref=True, size_of_param='loc_size_x',
                             doc="X String"),
                   Parameter('loc_size_x', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="X String Size"),
                   Parameter('loc_y', type=Type.STRING, is_ref=True, size_of_param='loc_size_y',
                             doc="Y String"),
                   Parameter('loc_size_y', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Y String Size"),
                   Parameter('loc_z', type=Type.STRING, is_ref=True, size_of_param='loc_size_z',
                             doc="Z String"),
                   Parameter('loc_size_z', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Z String Size"),
                   Parameter('scale_x', type=Type.DOUBLE,
                             doc="Scale to multiply X"),
                   Parameter('scale_y', type=Type.DOUBLE,
                             doc="Scale to multiply Y"),
                   Parameter('scale_z', type=Type.DOUBLE,
                             doc="Scale to multiply Z")
               ]),

        Method('iIsThematic_VOX', module='geoengine.core', version='7.0.0',
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
                   Parameter('vox', type="VOX",
                             doc="Voxel object")
               ]),

        Method('iIsVectorVoxel_VOX', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Is this a vector voxel?",
               notes="""
               A vector voxel is one where each data element consists of 3 4-byte float values.
               Vector voxels normally have the file type "geosoft_vectorvoxel".
               """,
               return_type=Type.INT32_T,
               return_doc="1 if :class:`VOX` is a vector voxel",
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel object")
               ]),

        Method('iSetCellSizeStrings_VOX', module='geoengine.core', version='6.3.1',
               availability=Availability.PUBLIC, 
               doc="Set the Location Strings",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Invalid data
               """,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel"),
                   Parameter('loc_x', type=Type.STRING,
                             doc="X String"),
                   Parameter('loc_y', type=Type.STRING,
                             doc="Y String"),
                   Parameter('loc_z', type=Type.STRING,
                             doc="Z String")
               ]),

        Method('LogGridPointsZEx_VOX', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Log grid a :class:`VOX` from point :class:`VV`'s (using variable Z's)",
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('error', type=Type.STRING,
                             doc='Name of error :class:`VOX` ("" for none)'),
                   Parameter('cell_size', type=Type.DOUBLE,
                             doc="Cell size (DUMMY for default)"),
                   Parameter('cell_size_z', type=Type.STRING,
                             doc='Cell size in Z ("" for default)'),
                   Parameter('var_only', type=Type.INT32_T,
                             doc="Variogram Only"),
                   Parameter('min_radius', type=Type.DOUBLE,
                             doc="Minimum Search Radius (DUMMY for none)"),
                   Parameter('max_radius', type=Type.DOUBLE,
                             doc="Maximum Search Radius (DUMMY for none)"),
                   Parameter('min_points', type=Type.INT32_T,
                             doc="Minimum Search Points"),
                   Parameter('max_points', type=Type.INT32_T,
                             doc="Maximum Search Points"),
                   Parameter('model', type=Type.INT32_T,
                             doc="Model number 1-power, 2-sperical, 3-gaussian, 4-exponential"),
                   Parameter('power', type=Type.DOUBLE,
                             doc="Power"),
                   Parameter('slope', type=Type.DOUBLE, is_ref=True,
                             doc="Slope"),
                   Parameter('range', type=Type.DOUBLE, is_ref=True,
                             doc="Range"),
                   Parameter('nugget', type=Type.DOUBLE,
                             doc="Nugget"),
                   Parameter('sill', type=Type.DOUBLE, is_ref=True,
                             doc="Sill"),
                   Parameter('strike', type=Type.DOUBLE,
                             doc="Strike"),
                   Parameter('dip', type=Type.DOUBLE,
                             doc="Dip"),
                   Parameter('plunge', type=Type.DOUBLE,
                             doc="Plunge"),
                   Parameter('along_strike_weight', type=Type.DOUBLE,
                             doc="Strike Weight"),
                   Parameter('down_dip_weight', type=Type.DOUBLE,
                             doc="Dip Plane Weight"),
                   Parameter('log_opt', type=Type.INT32_T,
                             doc=":def:`VOX_GRID_LOGOPT` Log Option"),
                   Parameter('min_log', type=Type.DOUBLE,
                             doc="Minimum log"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('vv_z', type="VV",
                             doc="Z :class:`VV`"),
                   Parameter('vv_d', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('ipj', type="IPJ")
               ]),

        Method('Krig_VOX', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="A more compact and extensible form of :func:`LogGridPointsZEx_VOX`.",
               notes="""
               Optional Parameters.
               
               If these values are not set in the :class:`REG`, then default parameters will be used.
               
               ERROR_VOXEL:		Name of error :class:`VOX` ("" for none)
               CELLSIZEZ:      Z Cell size string (space delimited, "" for default)
               RADIUS_MIN:		Minimum Search Radius (REAL) (Default = 4) (Blanking Distance)
               RADIUS_MAX:		Maximum Search Radius (REAL) (Default = 16)
               SEARCH_MIN:		Minimum Search Points (INT) (Default = 16)
               SEARCH_MAX:		Maximum Search Points (INT) (Default = 32)
               VARIOGRAM_ONLY: Set to 1 to calculate the variogram only (INT) (Default = 0)
               MODEL:				Variogram Model number 1-power, 2-sperical, 3-gaussian, 4-exponential  (INT) (Default = 2)
               POWER:          Power (Default = DUMMY)
               SLOPE:          Slope (REAL) (if input is DUMMY, value calculated and set on return)
               RANGE:          Range (REAL) (if input is DUMMY, value calculated and set on return)
               SILL :          Sill (REAL) (if input is DUMMY, value calculated and set on return)
               STRIKE:				Strike (REAL) (Default = 0)
               DIP:					Dip (REAL)	(Default = 90)
               PLUNGE:				Plunge (REAL) (Default = 0)
               STRIKE WEIGHT:	Along-Strike Weight (REAL) (Default = 1)
               DIP_WEIGHT:      Down-Dip Weight (REAL) (Default = 1)
               LOG_OPT:			One of :def:`VOX_GRID_LOGOPT` (Default = 0)
               MIN_LOG:			Log Minimum (REAL)	(Default = 1)
               MIN_X:				Minimum X (REAL) (default = DUMMY to determine from the data. If input, nearest lt. or eq. multiple of cell size chosen)
               MAX_X:				Maximum X (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)
               MIN_Y:				Minimum Y (REAL) (default = DUMMY to determine from the data. If input, nearest lt. or eq. external multiple of cell size chosen)
               MAX_Y:				Maximum Y (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)
               MIN_Z:				Minimum Z (REAL) (default = DUMMY to determine from the data. If input, nearest lt. or eq. multiple of cell size chosen)
               MAX_Z:				Maximum Z (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)A more compact and extensible form of :func:`LogGridPointsZEx_VOX`. Only the most
               basic parameters are entered directly. Optional parameters are passed via a :class:`REG` object.
               """,
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('cell_size', type=Type.DOUBLE,
                             doc="Cell size (DUMMY for default)"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('vv_z', type="VV",
                             doc="Z :class:`VV`"),
                   Parameter('vv_d', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('ipj', type="IPJ"),
                   Parameter('reg', type="REG")
               ]),

        Method('Math_VOX', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Produces a new voxes using a formula on existing voxels/Grids",
               notes="The input voxels must all be of the same type.",
               return_type="VOX",
               return_doc="VOXEL handle",
               parameters = [
                   Parameter('master', type=Type.STRING,
                             doc="Master :class:`VOX` Name"),
                   Parameter('mastervar', type=Type.STRING,
                             doc="Master :class:`VOX` Variable Name"),
                   Parameter('output', type=Type.STRING,
                             doc="Output :class:`VOX` Name"),
                   Parameter('outvar', type=Type.STRING,
                             doc="Output :class:`VOX` Variable Name"),
                   Parameter('formula', type=Type.STRING,
                             doc="Formula"),
                   Parameter('lst', type="LST",
                             doc="List of Voxels/Grids to use as inputs")
               ]),

        Method('Merge_VOX', module='geoengine.core', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Merge two Voxels.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox1', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('vox2', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('reg', type="REG",
                             doc="Parameters (see above)"),
                   Parameter('output_vox', type=Type.STRING,
                             doc="Output voxel file name.")
               ]),

        Method('NearestNeighbourGrid_VOX', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Grid a :class:`VOX` from point :class:`VV`'s using the Nearest Neighbours method.",
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('cell_size', type=Type.DOUBLE,
                             doc="Cell size (DUMMY for default)"),
                   Parameter('max_radius', type=Type.DOUBLE,
                             doc="Maximum radius (DUMMY for none)"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('vv_z', type="VV",
                             doc="Z :class:`VV`"),
                   Parameter('vv_d', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('ipj', type="IPJ")
               ]),

        Method('rComputeCellSize_VOX', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Compute the Cell size based on specific Area",
               return_type=Type.DOUBLE,
               return_doc="Cell Size",
               parameters = [
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="MinX"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="MinY"),
                   Parameter('min_z', type=Type.DOUBLE,
                             doc="MinZ"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="MaxX"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="MaxY"),
                   Parameter('max_z', type=Type.DOUBLE,
                             doc="MaxZ")
               ]),

        Method('ReGrid_VOX', module='geoengine.core', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Regrid a Voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox_master', type="VOX",
                             doc=":class:`VOX` object to match"),
                   Parameter('vox_to_regrid', type="VOX",
                             doc=":class:`VOX` object to regrid"),
                   Parameter('reg', type="REG",
                             doc="Parameters (not implemented)"),
                   Parameter('output_vox', type=Type.STRING,
                             doc="Output voxel file name.")
               ]),

        Method('ResamplePG_VOX', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Resample a voxel over an input volume to a :class:`PG`.",
               notes="""
               Creates and dummies a :class:`PG` object based on the input
               dimensions, then resamples the voxel to the pager
               at the locations determined by input projection, origin and spacings.
               """,
               return_type="PG",
               return_doc=":class:`PG` object, terminates on error",
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection to use for Origin, Spacing values"),
                   Parameter('orig_x', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('orig_y', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('orig_z', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('spacing_x', type=Type.DOUBLE,
                             doc="Spacing in X"),
                   Parameter('spacing_y', type=Type.DOUBLE,
                             doc="Spacing in Y"),
                   Parameter('spacing_z', type=Type.DOUBLE,
                             doc="Spacing in Z"),
                   Parameter('size_x', type=Type.INT32_T,
                             doc="Samples in X"),
                   Parameter('size_y', type=Type.INT32_T,
                             doc="Samples in Y"),
                   Parameter('size_z', type=Type.INT32_T,
                             doc="Samples in Z"),
                   Parameter('min_z', type=Type.DOUBLE,
                             doc="Minimum Z to resample (can be :def_val:`rDUMMY`)"),
                   Parameter('max_z', type=Type.DOUBLE,
                             doc="Maximum Z to resample (can be :def_val:`rDUMMY`)"),
                   Parameter('interp', type=Type.INT32_T,
                             doc=":def:`VOX_SLICE_MODE`")
               ]),

        Method('RescaleCellSizes_VOX', module='geoengine.core', version='7.3.0',
               availability=Availability.PUBLIC, 
               doc="Multiply all cell sizes by a fixed factor.",
               notes="""
               This is useful, for instance for converting sizes in one
               unit to sizes in another unit if changing the projection
               and the projection's unit changes, since the voxel inherits
               its projection's units.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="Scaling factor (>0)")
               ]),

        Method('SampleCDI_VOX', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Sample a voxel at locations/elevations in a CDI database.",
               notes="""
               A "CDI" database does not need to be conductivity/depth.
               It normally contains an array channel of depth values for
               each (X, Y) location, with corresponding data array channels of
               values taken at those (X, Y, Z) locations.
               If the optional elevation channel is used, its value is used as an
               offset to the depth channel values. Depths are positive down by
               default; use the "Negative depths down" parameter if the depths
               become more negative as you go deeper.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel"),
                   Parameter('db', type="DB",
                             doc="CDI Database handle"),
                   Parameter('line', type=Type.INT32_T,
                             doc="Line handle"),
                   Parameter('x_ch', type=Type.INT32_T,
                             doc="X channel handle"),
                   Parameter('y_ch', type=Type.INT32_T,
                             doc="Y channel handle"),
                   Parameter('elev_ch', type=Type.INT32_T,
                             doc="Depth array channel handle"),
                   Parameter('negative_depths_down', type=Type.INT32_T,
                             doc="Depths sign: 0 - positive down, 1 - negative down"),
                   Parameter('topo_ch', type=Type.INT32_T,
                             doc="Elevation channel handle (can be :def_val:`NULLSYMB`)"),
                   Parameter('mode', type=Type.INT32_T,
                             doc="Interpolation mode: 0 - linear, 1 - nearest"),
                   Parameter('out_ch', type=Type.STRING,
                             doc="Output channel name")
               ]),

        Method('SampleCDIToTopography_VOX', module='geoengine.core', version='8.2',
               availability=Availability.PUBLIC, 
               doc="""
               Sample a voxel at fixed elevations along a path in a CDI database, and output them to an array channel, deleting leading dummy values, and
               writing the elevation of the first non-dummy item to a topography channel.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel"),
                   Parameter('db', type="DB",
                             doc="CDI Database handle"),
                   Parameter('line', type=Type.INT32_T,
                             doc="Line handle"),
                   Parameter('x_ch', type=Type.INT32_T,
                             doc="X channel handle"),
                   Parameter('y_ch', type=Type.INT32_T,
                             doc="Y channel handle"),
                   Parameter('zvv', type="VV",
                             doc="Z values to sample at each X, Y"),
                   Parameter('mode', type=Type.INT32_T,
                             doc="Interpolation mode: 0 - linear, 1 - nearest"),
                   Parameter('out_ch', type=Type.STRING,
                             doc="Output data array channel name"),
                   Parameter('topo_ch', type=Type.STRING,
                             doc="Output topography channel name")
               ]),

        Method('SampleVV_VOX', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Sample a voxel at multiple locations.",
               notes="Sample at voxel at XYZ locations input in VVs. Values returned in a :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel"),
                   Parameter('xvv', type="VV",
                             doc="X locations (input)"),
                   Parameter('yvv', type="VV",
                             doc="Y locations (input)"),
                   Parameter('zvv', type="VV",
                             doc="Z locations (input)"),
                   Parameter('interp', type=Type.INT32_T,
                             doc="Interpolation mode: 0 - linear, 1 - nearest"),
                   Parameter('dvv', type="VV",
                             doc="Returned values")
               ]),

        Method('SetIPJ_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Set the projection of the voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` object to save :class:`VOX`'s meta to")
               ]),

        Method('SetLocation_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Set Location information",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('origin_x', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('origin_y', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('origin_z', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('vv_x', type="VV",
                             doc="Cell sizes in X"),
                   Parameter('vv_y', type="VV",
                             doc="Cell sizes in Y"),
                   Parameter('vv_z', type="VV",
                             doc="Cell sizes in Z")
               ]),

        Method('SetMETA_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Set the metadata of a voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Source :class:`VOX`"),
                   Parameter('meta', type="META",
                             doc=":class:`META` object to add to :class:`VOX`'s meta")
               ]),

        Method('SetOrigin_VOX', module='geoengine.core', version='6.3.1',
               availability=Availability.PUBLIC, 
               doc="Set the Voxel Origin",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('origin', type=Type.INT32_T,
                             doc="Type of origin being set :def:`VOX_ORIGIN`"),
                   Parameter('origin_x', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('origin_y', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('origin_z', type=Type.DOUBLE,
                             doc="Origin Z")
               ]),

        Method('SetSimpleLocation_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Set Simple Location information",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('origin_x', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('origin_y', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('origin_z', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('cell_x', type=Type.DOUBLE,
                             doc="Cell Sizes in X (:def_val:`rDUMMY` if not changed)"),
                   Parameter('cell_y', type=Type.DOUBLE,
                             doc="Cell Sizes in Y (:def_val:`rDUMMY` if not changed)"),
                   Parameter('cell_z', type=Type.DOUBLE,
                             doc="Cell Sizes in Z (:def_val:`rDUMMY` if not changed)")
               ]),

        Method('SetTPAT_VOX', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a thematic voxel's :class:`TPAT` object.",
               notes="""
               Each row in the :class:`TPAT` object corresponds to a stored index
               value in the thematic voxel. The :class:`TPAT` should NOT be modified
               by the addition or deletion of items, if it is to be
               restored into the :class:`VOX` object, but the CODE, LABEL, DESCRIPTION
               or COLOR info can be changed.
               The :class:`TPAT` object is stored inside the :class:`VOX` :class:`META` object.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('tpat', type="TPAT",
                             doc=":class:`TPAT` object to store")
               ]),

        Method('SliceIPJ_VOX', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Extract a slice of a voxel based on an :class:`IPJ`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel"),
                   Parameter('name', type=Type.STRING,
                             doc="Grid Name"),
                   Parameter('ipj', type="IPJ",
                             doc="Grid :class:`IPJ` (includes orientation, etc)"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`VOX_SLICE_MODE`"),
                   Parameter('orig_x', type=Type.DOUBLE,
                             doc="Grid Origin X"),
                   Parameter('orig_y', type=Type.DOUBLE,
                             doc="Grid Origin Y"),
                   Parameter('cell_size_x', type=Type.DOUBLE,
                             doc="Grid Cell Size in X"),
                   Parameter('cell_size_y', type=Type.DOUBLE,
                             doc="Grid Cell Size in Y"),
                   Parameter('size_x', type=Type.INT32_T,
                             doc="Grid cells in X"),
                   Parameter('size_y', type=Type.INT32_T,
                             doc="Grid cells in Y")
               ]),

        Method('SliceMultiLayerIPJ_VOX', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Extract multiple slices of a voxel based on an :class:`IPJ`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Voxel"),
                   Parameter('name', type=Type.STRING,
                             doc="Grid Name"),
                   Parameter('ipj', type="IPJ",
                             doc="Grid :class:`IPJ` (includes orientation, etc)"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`VOX_SLICE_MODE`"),
                   Parameter('orig_x', type=Type.DOUBLE,
                             doc="Grid Origin X"),
                   Parameter('orig_y', type=Type.DOUBLE,
                             doc="Grid Origin Y"),
                   Parameter('cell_size_x', type=Type.DOUBLE,
                             doc="Grid Cell Size in X"),
                   Parameter('cell_size_y', type=Type.DOUBLE,
                             doc="Grid Cell Size in Y"),
                   Parameter('size_x', type=Type.INT32_T,
                             doc="Grid cells in X"),
                   Parameter('size_y', type=Type.INT32_T,
                             doc="Grid cells in Y"),
                   Parameter('layers', type=Type.INT32_T,
                             doc="Number of layers to extract"),
                   Parameter('start_elev', type=Type.DOUBLE,
                             doc="Start elevation"),
                   Parameter('elev_inc', type=Type.DOUBLE,
                             doc="Elevation increment")
               ]),

        Method('SubsetToRealExtents_VOX', module='geoengine.core', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Subset a :class:`VOX` to real extents.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('output_vox', type=Type.STRING,
                             doc="Output voxel file name.")
               ]),

        Method('Sync_VOX', module='geoengine.core', version='7.0.0',
               availability=Availability.LICENSED, 
               doc="Syncronize the Metadata for this Voxel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Voxel name")
               ]),

        Method('WindowPLY_VOX', module='geoengine.core', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Window a :class:`VOX` to a :class:`PLY` file and Z.",
               notes="""
               The voxel is windowed horizontally to the input :class:`PLY` file.
               Optionally, it will be windowed to the input Z range as well.
               The output can be clipped to the non-dummied cells.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('pply', type="PLY",
                             doc=":class:`PLY` object"),
                   Parameter('mask', type=Type.INT32_T,
                             doc="Mask (0: inside :class:`PLY`, 1: outside :class:`PLY`)"),
                   Parameter('min_z', type=Type.DOUBLE,
                             doc="Minimum Z (optional, :def_val:`rDUMMY` for no minimum)"),
                   Parameter('max_z', type=Type.DOUBLE,
                             doc="Maximum Z (optional, :def_val:`rDUMMY` for no maximun)"),
                   Parameter('output_vox', type=Type.STRING,
                             doc="Output voxel file name."),
                   Parameter('clip_dummies', type=Type.INT32_T,
                             doc="Clip extents to remove dummies (0: no (same size), 1: yes (smaller))")
               ]),

        Method('WindowXYZ_VOX', module='geoengine.core', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Window a :class:`VOX` to ranges in X, Y and Z.",
               notes="""
               The six minima and maxima are optional.
               The output can be clipped to the non-dummied cells.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` object"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Minimum X (optional, :def_val:`rDUMMY` for no minimum)"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Minimum Y (optional, :def_val:`rDUMMY` for no minimum)"),
                   Parameter('min_z', type=Type.DOUBLE,
                             doc="Minimum Z (optional, :def_val:`rDUMMY` for no minimum)"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Maximum X (optional, :def_val:`rDUMMY` for no maximun)"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Maximum Y (optional, :def_val:`rDUMMY` for no maximun)"),
                   Parameter('max_z', type=Type.DOUBLE,
                             doc="Maximum Z (optional, :def_val:`rDUMMY` for no maximun)"),
                   Parameter('output_vox', type=Type.STRING,
                             doc="Output voxel file name."),
                   Parameter('clip_dummies', type=Type.INT32_T,
                             doc="Clip extents to remove dummies (0: no (same size), 1: yes (smaller))")
               ]),

        Method('WriteXML_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Export the :class:`VOX` to XML",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` Handle"),
                   Parameter('file', type=Type.STRING,
                             doc="XML file to create")
               ]),

        Method('ConvertNumericToThematic_VOX', module='geoengine.core', version='8.4',
               availability=Availability.PUBLIC, 
               doc="Convert numeric voxel to thematic (lithology) voxel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Numeric :class:`VOX` Handle."),
                   Parameter('vv_translate', type="VV",
                             doc="Translation :class:`VV` handle."),
                   Parameter('output_vox', type=Type.STRING,
                             doc="Output voxel file name.")
               ]),

        Method('ConvertThematicToNumeric_VOX', module='geoengine.core', version='8.4',
               availability=Availability.PUBLIC, 
               doc="Convert thematic (lithology) voxel to numeric voxel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Thematic :class:`VOX` Handle."),
                   Parameter('vv_translate', type="VV",
                             doc="Translation :class:`VV` handle."),
                   Parameter('output_vox', type=Type.STRING,
                             doc="Output voxel file name.")
               ]),

        Method('ConvertVelocityToDensity_VOX', module='geoengine.core', version='8.4',
               availability=Availability.PUBLIC, 
               doc="Produces a density voxel using the velocity values in this voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Velocity :class:`VOX` Handle."),
                   Parameter('input_scaling_factor', type=Type.DOUBLE,
                             doc="1.0, if this voxel is in meters per second. Otherwise, a value by which each input cell is multiplied to convert it into meters per second."),
                   Parameter('a5', type=Type.DOUBLE,
                             doc="Coefficient of fifth-order polynomial term."),
                   Parameter('a4', type=Type.DOUBLE,
                             doc="Coefficient of fourth-order polynomial term."),
                   Parameter('a3', type=Type.DOUBLE,
                             doc="Coefficient of third-order polynomial term."),
                   Parameter('a2', type=Type.DOUBLE,
                             doc="Coefficient of second-order polynomial term."),
                   Parameter('a1', type=Type.DOUBLE,
                             doc="Coefficient of first-order polynomial term."),
                   Parameter('a0', type=Type.DOUBLE,
                             doc="Constant offset of output."),
                   Parameter('output_scaling_factor', type=Type.DOUBLE,
                             doc="1.0, to produce an output voxel that has units of g/cm^3. If different units are desired, pass in a different value, which will be multiplied into each output voxel cell."),
                   Parameter('output_voxel_filename', type=Type.STRING,
                             doc="Filename of the output voxel.")
               ]),

        Method('ConvertVelocityInRangeToDensity_VOX', module='geoengine.core', version='8.4',
               availability=Availability.PUBLIC, 
               doc="Produces a density voxel using the velocity values in this voxel, as long as the velocity values are in range.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Velocity :class:`VOX` Handle."),
                   Parameter('input_scaling_factor', type=Type.DOUBLE,
                             doc="1.0, if this voxel is in meters per second. Otherwise, a value by which each input cell is multiplied to convert it into meters per second."),
                   Parameter('input_lower_bound', type=Type.DOUBLE,
                             doc="Lower bound on velocity values, in meters per second. If the input value (after being pre-multiplied by dInputScalingFactor) is less than this value, the output cell value will be DUMMY."),
                   Parameter('input_upper_bound', type=Type.DOUBLE,
                             doc="Upper bound on velocity values, in meters per second. If the input value (after being pre-multiplied by dInputScalingFactor) is greater than this value, the output cell value will be DUMMY."),
                   Parameter('a5', type=Type.DOUBLE,
                             doc="Coefficient of fifth-order polynomial term."),
                   Parameter('a4', type=Type.DOUBLE,
                             doc="Coefficient of fourth-order polynomial term."),
                   Parameter('a3', type=Type.DOUBLE,
                             doc="Coefficient of third-order polynomial term."),
                   Parameter('a2', type=Type.DOUBLE,
                             doc="Coefficient of second-order polynomial term."),
                   Parameter('a1', type=Type.DOUBLE,
                             doc="Coefficient of first-order polynomial term."),
                   Parameter('a0', type=Type.DOUBLE,
                             doc="Constant offset of output."),
                   Parameter('output_scaling_factor', type=Type.DOUBLE,
                             doc="1.0, to produce an output voxel that has units of g/cm^3. If different units are desired, pass in a different value, which will be multiplied into each output voxel cell."),
                   Parameter('output_voxel_filename', type=Type.STRING,
                             doc="Filename of the output voxel.")
               ]),

        Method('ConvertDensityToVelocity_VOX', module='geoengine.core', version='8.4',
               availability=Availability.PUBLIC, 
               doc="Produces a velocity voxel using the density values in this voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Density :class:`VOX` Handle."),
                   Parameter('input_scaling_factor', type=Type.DOUBLE,
                             doc="1.0, if this voxel is in g/cm^3. Otherwise, a value by which each input cell is multiplied to convert it into g/cm^3."),
                   Parameter('input_lower_bound', type=Type.DOUBLE,
                             doc="Lower bound on velocity values, in g/vm^3. If the input value (after being pre-multiplied by dInputScalingFactor) is less than this value, the output cell value will be DUMMY."),
                   Parameter('input_upper_bound', type=Type.DOUBLE,
                             doc="Upper bound on velocity values, in g/cm^3. If the input value (after being pre-multiplied by dInputScalingFactor) is greater than this value, the output cell value will be DUMMY."),
                   Parameter('a5', type=Type.DOUBLE,
                             doc="Coefficient of fifth-order polynomial term."),
                   Parameter('a4', type=Type.DOUBLE,
                             doc="Coefficient of fourth-order polynomial term."),
                   Parameter('a3', type=Type.DOUBLE,
                             doc="Coefficient of third-order polynomial term."),
                   Parameter('a2', type=Type.DOUBLE,
                             doc="Coefficient of second-order polynomial term."),
                   Parameter('a1', type=Type.DOUBLE,
                             doc="Coefficient of first-order polynomial term."),
                   Parameter('a0', type=Type.DOUBLE,
                             doc="Constant offset of output."),
                   Parameter('output_scaling_factor', type=Type.DOUBLE,
                             doc="1.0, to produce an output voxel that has units of meters per second. If different units are desired, pass in a different value, which will be multiplied into each output voxel cell."),
                   Parameter('output_voxel_filename', type=Type.STRING,
                             doc="Filename of the output voxel.")
               ]),

        Method('InvertZ_VOX', module='geoengine.core', version='8.4',
               availability=Availability.PUBLIC, 
               doc="Convert an inverted voxel to normal orientation",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc="Input :class:`VOX` Handle."),
                   Parameter('output_voxel_filename', type=Type.STRING,
                             doc="Output voxel file name.")
               ]),

        Method('IDWGridDB_VOX', module='geoengine.core', version='8.4.0',
               availability=Availability.LICENSED, 
               doc=":func:`IDWGridDB_VOX`     Inverse-distance weighting gridding method, :class:`DB` version, 3D.",
               notes="""
               3D cells take on the averaged values within a search radius, weighted inversely by distance.
               
               Weighting can be controlled using the power and slope properties;
               
               weighting = 1 / (distance^wtpower + 1/slope) where distance is in
               units of grid cells (X dimenstion). Default is 0.0,
               
               If the blanking distance is set, all cells whose center point is not within the blanking distance of
               at least one data point are set to dummy.
               
               :class:`REG` Parameters:
               
               X0, Y0, Z0, DX, DY, DZ: Voxel origin, and cell sizes (required)
               WT_POWER (default=2), WT_SLOPE (default=1) Weighting function parameters
               SEARCH_RADIUS: Distance weighting limit (default = 4 * CUBE_ROOT(DX*DY*DZ))
               BLANKING_DISTANCE: Dummy values farther from data than this distance. (default = 4 * CUBE_ROOT(DX*DY*DZ))
               LOG: Apply log transform to input data before gridding (0:No (default), 1:Yes)?
               LOG_BASE: One of :def_val:`VV_LOG_BASE_10` (default) or :def_val:`VV_LOG_BASE_E`
               LOG_NEGATIVE: One of :def_val:`VV_LOG_NEGATIVE_NO` (default) or :def_val:`VV_LOG_NEGATIVE_YES`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel', type=Type.STRING,
                             doc="Output voxel name"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('x', type="DB_SYMB",
                             doc="X Channel [READONLY]"),
                   Parameter('y', type="DB_SYMB",
                             doc="Y Channel [READONLY]"),
                   Parameter('z', type="DB_SYMB",
                             doc="Z Channel [READONLY]"),
                   Parameter('data', type="DB_SYMB",
                             doc="Data Channel [READONLY]"),
                   Parameter('reg', type="REG",
                             doc="Parameters (see above)")
               ]),

        Method('TINGridDB_VOX', module='geoengine.core', version='8.5.0',
               availability=Availability.LICENSED, 
               doc=":func:`TINGridDB_VOX`   :class:`TIN`-Gridding, :class:`DB` version, 3D.",
               notes="""
               Designed for data in array channels position vertically at single XY locations.
               Creates a :class:`TIN` using the XY locations and uses the coefficients for the top layer on
               each layer below to make it efficient.
               
               :class:`REG` Parameters:
               
               X0, Y0, Z0, DX, DY, DZ: Voxel origin, and cell sizes (required)
               NX, NY, NZ: Voxel dimensions.
               DZ and NZ are used only if the input cell sizes :class:`VV` is of zero length.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel', type=Type.STRING,
                             doc="Output voxel name"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('x', type="DB_SYMB",
                             doc="X Channel [READONLY]"),
                   Parameter('y', type="DB_SYMB",
                             doc="Y Channel [READONLY]"),
                   Parameter('z', type="DB_SYMB",
                             doc="Z Channel [READONLY]"),
                   Parameter('data', type="DB_SYMB",
                             doc="Data Channel [READONLY]"),
                   Parameter('method', type=Type.INT32_T,
                             doc="Gridding method (0: Linear, 1: Natural Neighbour, 2: Nearest Neightbour"),
                   Parameter('z_cell', type="VV",
                             doc="Z Cell sizes (bottom to top)"),
                   Parameter('reg', type="REG",
                             doc="Parameters (see above)")
               ]),

        Method('IGetMultiVoxsetGUID_VOX', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the UUID",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel_file', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('p_uuid_string', type=Type.STRING, is_ref=True, size_of_param='p_uuid_string_len',
                             doc="UUID string returned"),
                   Parameter('p_uuid_string_len', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of UUID string")
               ]),

        Method('GenerateGOCAD_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Generate a :class:`VOX` from a GOCAD File",
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('header', type=Type.STRING,
                             doc="Name of GOCAD Voxel file"),
                   Parameter('property', type=Type.STRING,
                             doc="Propert name to import"),
                   Parameter('ipj', type="IPJ")
               ]),

        Method('GenerateOrientedGOCAD_VOX', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a :class:`VOX` from a GOCAD File",
               notes="Allows the Orientation flag to be specified.",
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('header', type=Type.STRING,
                             doc="Name of GOCAD Voxel file"),
                   Parameter('property', type=Type.STRING,
                             doc="Propert name to import"),
                   Parameter('ipj', type="IPJ"),
                   Parameter('orientation', type=Type.INT32_T,
                             doc=":def:`VOX_GOCAD_ORIENTATION`")
               ]),

        Method('GenerateUBC_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Generate a :class:`VOX` from a UBC File",
               return_type="VOX",
               return_doc=":class:`VOX` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('mesh', type=Type.STRING,
                             doc="Name of UBC Mesh File"),
                   Parameter('mod', type=Type.STRING,
                             doc="Name of UBC Mod File"),
                   Parameter('dummy', type=Type.DOUBLE,
                             doc="Dummy Value"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection")
               ]),

        Method('GenerateXYZ_VOX', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a :class:`VOX` from an XYZ File",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Voxel Name"),
                   Parameter('ra', type="RA",
                             doc=":class:`RA` To import from"),
                   Parameter('type', type=Type.INT32_T,
                             doc="Data Type :def:`GS_TYPES`"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection")
               ]),

        Method('ListGOCADProperties_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="List all the properties available in this GOCAD file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('header', type=Type.STRING,
                             doc="Name of GOCAD Voxel file"),
                   Parameter('lst', type="LST",
                             doc="List object to populate")
               ]),

        Method('ExportDB_VOX', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Export a Voxel to a database",
               notes="The database lines contain a slice of the voxel at a time.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel Name"),
                   Parameter('dir', type=Type.INT32_T,
                             doc=":def:`VOX_DIRECTION`"),
                   Parameter('rev_x', type=Type.INT32_T,
                             doc="Reverse X ? (0/1)"),
                   Parameter('rev_y', type=Type.INT32_T,
                             doc="Reverse Y ? (0/1)"),
                   Parameter('rev_z', type=Type.INT32_T,
                             doc="Reverse Z ? (0/1)"),
                   Parameter('dummies', type=Type.INT32_T,
                             doc="Write Dummies? (0/1)")
               ])
    ],
    'Obsolete': [

        Method('Sample_VOX', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Sample the Voxel",
               notes="Never properly implemented. Use :func:`Profile_VOXE` instead.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vox', type="VOX",
                             doc=":class:`VOX` Handle"),
                   Parameter('pg', type="PG",
                             doc=":class:`VOX` :class:`PG` Data"),
                   Parameter('vv_x', type="VV",
                             doc=":class:`VV` X Location     (must be a DOUBLE)"),
                   Parameter('vv_y', type="VV",
                             doc=":class:`VV` Y Location     (must be a DOUBLE)"),
                   Parameter('vv_z', type="VV",
                             doc=":class:`VV` Z Location     (must be a DOUBLE)"),
                   Parameter('vv_d', type="VV",
                             doc=":class:`VV` Data Returned  (must be a DOUBLE)")
               ])
    ]
}

