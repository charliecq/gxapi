from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MULTIVOXSET',
                 doc="High Performance 3D Grid.")


gx_defines = [
    Define('DIRECTION3D',
           doc="Direction in 3D",
           constants=[
               Constant('DIRECTION3D_XYZ', value='0', type=Type.INT32_T,
                        doc="XYZ"),
               Constant('DIRECTION3D_YXZ', value='1', type=Type.INT32_T,
                        doc="YXZ"),
               Constant('DIRECTION3D_XZY', value='2', type=Type.INT32_T,
                        doc="XZY"),
               Constant('DIRECTION3D_YZX', value='3', type=Type.INT32_T,
                        doc="YZX"),
               Constant('DIRECTION3D_ZXY', value='4', type=Type.INT32_T,
                        doc="ZXY"),
               Constant('DIRECTION3D_ZYX', value='5', type=Type.INT32_T,
                        doc="ZYX")
           ]),

    Define('GOCAD_ORIENTATION',
           doc="GOCAD Orientations",
           constants=[
               Constant('GOCAD_ORIENTATIONS_NORMAL', value='0', type=Type.INT32_T,
                        doc="Normal"),
               Constant('GOCAD_ORIENTATIONS_INVERTED', value='1', type=Type.INT32_T,
                        doc="Inverted (Z)"),
               Constant('GOCAD_ORIENTATIONS_NORMAL_ZFIRST', value='2', type=Type.INT32_T,
                        doc="Normal (ZFirst)"),
               Constant('GOCAD_ORIENTATIONS_INVERTED_ZFIRST', value='3', type=Type.INT32_T,
                        doc="Inverted (Z) (ZFirst)")
           ]),

    Define('VECTOR_IMPORT',
           doc="Vector voxel import direction",
           constants=[
               Constant('VECTOR_IMPORT_XYZ', value='0', type=Type.INT32_T,
                        doc="X, Y and Z"),
               Constant('VECTOR_IMPORT_UVW', value='1', type=Type.INT32_T,
                        doc="U, V and W"),
               Constant('VECTOR_IMPORT_AID', value='2', type=Type.INT32_T,
                        doc="Amplitude, Inclination and Declination")
           ]),

    Define('FILTER3D',
           doc="Voxel filter type",
           constants=[
               Constant('FILTER3D_FILE', value='0', type=Type.INT32_T,
                        doc="Specify a file containing the 27-point filter"),
               Constant('FILTER3D_SMOOTHING', value='1', type=Type.INT32_T,
                        doc="Smoothing filter"),
               Constant('FILTER3D_LAPLACE', value='2', type=Type.INT32_T,
                        doc="Laplace filter"),
               Constant('FILTER3D_X_GRADIENT', value='3', type=Type.INT32_T,
                        doc="X-Gradient filter"),
               Constant('FILTER3D_Y_GRADIENT', value='4', type=Type.INT32_T,
                        doc="Y-Gradient filter"),
               Constant('FILTER3D_Z_GRADIENT', value='5', type=Type.INT32_T,
                        doc="Z-Gradient filter"),
               Constant('FILTER3D_TOTAL_GRADIENT', value='6', type=Type.INT32_T,
                        doc="Total-Gradient filter")
           ]),

    Define('MULTIVOXSET_DIRECTGRID_METHOD',
           doc="How to calculate the cell values for direct gridding.",
           constants=[
               Constant('MULTIVOXSET_DIRECTGRID_MIN', value='0', type=Type.INT32_T),
               Constant('MULTIVOXSET_DIRECTGRID_MAX', value='1', type=Type.INT32_T),
               Constant('MULTIVOXSET_DIRECTGRID_MEAN', value='2', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('ImportFromXYZ_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Import XYZ file into a Multi-Voxset",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output Voxel file"),
                   Parameter('ra', type="RA",
                             doc=":class:`RA` To import from"),
                   Parameter('type', type=Type.INT32_T,
                             doc="Data Type :def:`GS_TYPES`"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection")
               ]),

        Method('ExportToXYZ_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export a :class:`MULTIVOXSET` to an XYZ File",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel_file', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('xyz', type=Type.STRING,
                             doc="File Name"),
                   Parameter('dir', type=Type.INT32_T,
                             doc=":def:`DIRECTION3D`"),
                   Parameter('rev_x', type=Type.BOOL,
                             doc="Reverse X?"),
                   Parameter('rev_y', type=Type.BOOL,
                             doc="Reverse Y?"),
                   Parameter('rev_z', type=Type.BOOL,
                             doc="Reverse Z?"),
                   Parameter('dummies', type=Type.BOOL,
                             doc="Write Dummies?")
               ]),

        Method('ExportToBinary_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.LICENSED, 
               doc="Export contents of :class:`MULTIVOXSET` to a Binary File.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel_file', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('binary_file', type=Type.STRING,
                             doc="Binary file to write to"),
                   Parameter('dir', type=Type.INT32_T,
                             doc=":def:`DIRECTION3D`"),
                   Parameter('rev_x', type=Type.BOOL,
                             doc="Reverse X?"),
                   Parameter('rev_y', type=Type.BOOL,
                             doc="Reverse Y?"),
                   Parameter('rev_z', type=Type.BOOL,
                             doc="Reverse Z?"),
                   Parameter('swap', type=Type.BOOL,
                             doc="Swap Bytes?"),
                   Parameter('output_type', type=Type.INT32_T,
                             doc="Output Type (Geosoft Type)")
               ]),

        Method('ExportToXML_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export a :class:`MULTIVOXSET` to XML",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel_file', type=Type.STRING,
                             doc="Voxel file"),
                   Parameter('xml_file', type=Type.STRING,
                             doc="XML file")
               ]),

        Method('CheckEqualToLegacyVoxel_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Compare :class:`MULTIVOXSET` to Legacy Voxel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel_file', type=Type.STRING,
                             doc="Voxel file"),
                   Parameter('legacy_voxel_file', type=Type.STRING,
                             doc="Legacy Voxel file")
               ]),

        Method('ImportFromUBC_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Import UBC file into a MultiVoxset",
               return_type=Type.VOID,
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

        Method('ImportFromGOCAD_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Imports a MultiVoxset from a GOCAD File",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('header', type=Type.STRING,
                             doc="Name of GOCAD Voxel file"),
                   Parameter('property', type=Type.STRING,
                             doc="Propert name to import"),
                   Parameter('ipj', type="IPJ"),
                   Parameter('orientation', type=Type.INT32_T,
                             doc=":def:`GOCAD_ORIENTATION`")
               ]),

        Method('ListPropertiesGOCAD_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="List all the properties available in this GOCAD file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('header', type=Type.STRING,
                             doc="Name of GOCAD Voxel file"),
                   Parameter('lst', type="LST",
                             doc="List object to populate")
               ]),

        Method('ImportFromGDB_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Imports from a Geosoft Database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel_file', type=Type.STRING,
                             doc="Name of output Voxel file"),
                   Parameter('db', type="DB",
                             doc=":class:`DB` To import from"),
                   Parameter('symb', type="DB_SYMB",
                             doc="Symbol to import data from")
               ]),

        Method('ImportFromVectorGDB_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Imports from a Vector Geosoft Database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel_file', type=Type.STRING,
                             doc="Voxel Name"),
                   Parameter('db', type="DB",
                             doc=":class:`DB` To import from"),
                   Parameter('vector_type', type=Type.INT32_T,
                             doc="VECTOR_IMPORTImport XYZ, UVW or Amplitude/Inclination/Declination channels"),
                   Parameter('symb_x', type="DB_SYMB",
                             doc="Symbol to import X, U or Amplitude data from"),
                   Parameter('symb_y', type="DB_SYMB",
                             doc="Symbol to import Y, V or Inclination data from"),
                   Parameter('symb_z', type="DB_SYMB",
                             doc="Symbol to import Z, W or Declination data from"),
                   Parameter('inc', type=Type.DOUBLE,
                             doc="Inclination value for :const:`VOX_VECTORVOX_UVW` (-90° to 90°)"),
                   Parameter('dec', type=Type.DOUBLE,
                             doc="Declination value for :const:`VOX_VECTORVOX_UVW` (-180° to 180°)")
               ]),

        Method('ExportToSEGY_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export To SEGY",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel_file', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('voxel_name', type=Type.STRING,
                             doc="Voxel Name"),
                   Parameter('output_segy_filename', type=Type.STRING,
                             doc="Output Segy file"),
                   Parameter('sample_interval', type=Type.DOUBLE,
                             doc="Sampling Internal")
               ]),

        Method('ExportToGDB_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export To GDB",
               return_type=Type.VOID,
               parameters = [
                   Parameter('voxel_file', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel Name"),
                   Parameter('dir', type=Type.INT32_T,
                             doc=":def:`DIRECTION3D`"),
                   Parameter('rev_x', type=Type.BOOL,
                             doc="Reverse X?"),
                   Parameter('rev_y', type=Type.BOOL,
                             doc="Reverse Y?"),
                   Parameter('rev_z', type=Type.BOOL,
                             doc="Reverse Z?"),
                   Parameter('dummies', type=Type.BOOL,
                             doc="Write Dummies?")
               ]),

        Method('ExportToWA_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export To GDB",
               return_type=Type.VOID,
               parameters = [
                   Parameter('file_name', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('wa', type="WA",
                             doc=":class:`WA` File"),
                   Parameter('dir', type=Type.INT32_T,
                             doc=":def:`DIRECTION3D`"),
                   Parameter('rev_x', type=Type.BOOL,
                             doc="Reverse X?"),
                   Parameter('rev_y', type=Type.BOOL,
                             doc="Reverse Y?"),
                   Parameter('rev_z', type=Type.BOOL,
                             doc="Reverse Z?"),
                   Parameter('dummy', type=Type.STRING,
                             doc="The Dummy string to write")
               ]),

        Method('ConvertDoubleToVector_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Convert 3 Double Voxels to a Vector Voxel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('x_file_name', type=Type.STRING,
                             doc="Input X Voxel file"),
                   Parameter('y_file_name', type=Type.STRING,
                             doc="Input Y Voxel file"),
                   Parameter('z_file_name', type=Type.STRING,
                             doc="Input Z Voxel file"),
                   Parameter('out_file_name', type=Type.STRING,
                             doc="Output Vector Voxel file"),
                   Parameter('inclination', type=Type.DOUBLE,
                             doc="Inclination"),
                   Parameter('declination', type=Type.DOUBLE,
                             doc="Declination"),
                   Parameter('rotated', type=Type.BOOL,
                             doc="Rotated?")
               ]),

        Method('ConvertVectorToDouble_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Convert a Vector Voxel to 3 double Voxels",
               return_type=Type.VOID,
               parameters = [
                   Parameter('file_name', type=Type.STRING,
                             doc="Input Vector Voxel file"),
                   Parameter('x_file_name', type=Type.STRING,
                             doc="Output X Voxel file"),
                   Parameter('y_file_name', type=Type.STRING,
                             doc="Output Y Voxel file"),
                   Parameter('z_file_name', type=Type.STRING,
                             doc="Output Z Voxel file"),
                   Parameter('rotated', type=Type.BOOL,
                             doc="Rotated?")
               ]),

        Method('ConvertThematicToDouble_MULTIVOXSET', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Convert Thematic MultiVoxset to Double MultiVoxset",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_voxel_filename', type=Type.STRING,
                             doc="Input voxel filename"),
                   Parameter('translate_vv', type="VV",
                             doc="Translation VV handle"),
                   Parameter('output_voxel_filename', type=Type.STRING,
                             doc="Output voxel filename")
               ]),

        Method('ConvertDoubleToThematic_MULTIVOXSET', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Convert Double MultiVoxset to Thematic MultiVoxset",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_voxel_filename', type=Type.STRING,
                             doc="Input voxel filename"),
                   Parameter('translate_vv', type="VV",
                             doc="Translation VV handle"),
                   Parameter('output_voxel_filename', type=Type.STRING,
                             doc="Output voxel filename")
               ]),

        Method('ConvertVelocityToDensity_MULTIVOXSET', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Convert Velocity MultiVoxset to Density MultiVoxset",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_voxel_filename', type=Type.STRING,
                             doc="Input voxel filename"),
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
                             doc="Output voxel filename")
               ]),

        Method('ConvertDensityToVelocity_MULTIVOXSET', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Convert Density MultiVoxset to Velocity MultiVoxset",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_voxel_filename', type=Type.STRING,
                             doc="Input voxel filename"),
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
                             doc="Output voxel filename")
               ]),

        Method('CreateDoubleConstant_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output Voxel File"),
                   Parameter('value', type=Type.DOUBLE,
                             doc="Constant Value to use - DUMMY for a trully sparse voxel"),
                   Parameter('ox', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('oy', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('oz', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('cell_x', type=Type.DOUBLE,
                             doc="Cell Size X"),
                   Parameter('cell_y', type=Type.DOUBLE,
                             doc="Cell Size Y"),
                   Parameter('cell_z', type=Type.DOUBLE,
                             doc="Cell Size Z"),
                   Parameter('size_x', type=Type.INT32_T,
                             doc="Cell Count X"),
                   Parameter('size_y', type=Type.INT32_T,
                             doc="Cell Count Y"),
                   Parameter('size_z', type=Type.INT32_T,
                             doc="Cell Count Z"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection")
               ]),

        Method('CreateThematicConstant_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output Voxel File"),
                   Parameter('value', type=Type.INT32_T,
                             doc="Constant Value to use - DUMMY for a trully sparse voxel"),
                   Parameter('ox', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('oy', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('oz', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('cell_x', type=Type.DOUBLE,
                             doc="Cell Size X"),
                   Parameter('cell_y', type=Type.DOUBLE,
                             doc="Cell Size Y"),
                   Parameter('cell_z', type=Type.DOUBLE,
                             doc="Cell Size Z"),
                   Parameter('size_x', type=Type.INT32_T,
                             doc="Cell Count X"),
                   Parameter('size_y', type=Type.INT32_T,
                             doc="Cell Count Y"),
                   Parameter('size_z', type=Type.INT32_T,
                             doc="Cell Count Z"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection")
               ]),

        Method('CreateVectorConstant_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output Voxel File"),
                   Parameter('value_x', type=Type.DOUBLE,
                             doc="X Constant Value to use - DUMMY for a trully sparse voxel"),
                   Parameter('value_y', type=Type.DOUBLE,
                             doc="Y Constant Value to use - DUMMY for a trully sparse voxel"),
                   Parameter('value_z', type=Type.DOUBLE,
                             doc="Z Constant Value to use - DUMMY for a trully sparse voxel"),
                   Parameter('ox', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('oy', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('oz', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('cell_x', type=Type.DOUBLE,
                             doc="Cell Size X"),
                   Parameter('cell_y', type=Type.DOUBLE,
                             doc="Cell Size Y"),
                   Parameter('cell_z', type=Type.DOUBLE,
                             doc="Cell Size Z"),
                   Parameter('size_x', type=Type.INT32_T,
                             doc="Cell Count X"),
                   Parameter('size_y', type=Type.INT32_T,
                             doc="Cell Count Y"),
                   Parameter('size_z', type=Type.INT32_T,
                             doc="Cell Count Z"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection")
               ]),

        Method('CreateDoubleConstantVV_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value and non-uniform cell sizes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output Voxel"),
                   Parameter('value', type=Type.DOUBLE,
                             doc="The contant Value to fill with - DUMMY for a trully sparse voxel"),
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
                             doc="Projection")
               ]),

        Method('CreateThematicConstantVV_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value and non-uniform cell sizes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output Voxel"),
                   Parameter('value', type=Type.INT32_T,
                             doc="The contant Value to fill with - DUMMY for a trully sparse voxel"),
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
                             doc="Projection")
               ]),

        Method('CreateVectorConstantVV_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value and non-uniform cell sizes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output Voxel"),
                   Parameter('x_value', type=Type.DOUBLE,
                             doc="The X contant Value to fill with - DUMMY for a trully sparse voxel"),
                   Parameter('y_value', type=Type.DOUBLE,
                             doc="The Y contant Value to fill with - DUMMY for a trully sparse voxel"),
                   Parameter('z_value', type=Type.DOUBLE,
                             doc="The Z contant Value to fill with - DUMMY for a trully sparse voxel"),
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
                             doc="Projection")
               ]),

        Method('ExportToVoxel_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Exports a Multi-Voxset into a Voxel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('project_file', type=Type.STRING,
                             doc="Project file"),
                   Parameter('multi_voxset_uuid', type=Type.STRING,
                             doc="Multi-Voxset UUID"),
                   Parameter('multi_voxset_attribute', type=Type.STRING,
                             doc="Multi-Voxset attribute"),
                   Parameter('voxel_file', type=Type.STRING,
                             doc="Output Voxel file")
               ]),

        Method('ImportFromVoxel_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Import a Voxel directly into a Multi-Voxset",
               return_type=Type.VOID,
               parameters = [
                   Parameter('project_file', type=Type.STRING,
                             doc="Project file"),
                   Parameter('voxel_file', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('multi_voxset_attribute', type=Type.STRING,
                             doc="Multi-Voxset attribute"),
                   Parameter('p_uuid_string', type=Type.STRING, is_ref=True, size_of_param='p_uuid_string_len',
                             doc="UUID string returned"),
                   Parameter('p_uuid_string_len', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of UUID string")
               ]),

        Method('ImportFromDATAMINE_MULTIVOXSET', module='geoengine.interoperability', version='9.3.0',
               availability=Availability.LICENSED, 
               doc="Create a Geosoft Voxel file from a Datamine block model file.",
               notes="Create a Geosoft Voxel file from a Datamine block model file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="Datamine file name"),
                   Parameter('field', type=Type.STRING,
                             doc="Field to use for data"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection to set"),
                   Parameter('voxel', type=Type.STRING,
                             doc="Output voxel file name")
               ]),

        Method('rComputeDefaultCellSize_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.LICENSED, 
               doc="Used if the user does not provide a default cell size.",
               notes="Compute a default cell size for a voxel given a data range.",
               return_type=Type.DOUBLE,
               return_doc="Default Cell Size",
               parameters = [
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="MinX"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="MaxX"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="MinY"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="MaxY"),
                   Parameter('min_z', type=Type.DOUBLE,
                             doc="MinZ"),
                   Parameter('max_z', type=Type.DOUBLE,
                             doc="MaxZ")
               ]),

        Method('Filter_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.LICENSED, 
               doc="Apply a 3D filter to a voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_file', type=Type.STRING,
                             doc="Name of the input voxel"),
                   Parameter('output_file', type=Type.STRING,
                             doc="Name of the output voxel"),
                   Parameter('filter', type=Type.INT32_T,
                             doc=":def:`FILTER3D`"),
                   Parameter('filter_file', type=Type.STRING,
                             doc="Filter file, if filter is :const:`VOX_FILTER3D_FILE`"),
                   Parameter('n_passes', type=Type.INT32_T,
                             doc="Number of filter passes"),
                   Parameter('interpolate_dummies', type=Type.INT32_T,
                             doc="(1: interpolate dummies)")
               ]),

        Method('GridDirectFromGDB_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.LICENSED, 
               doc="Create a voxel using direct gridding.",
               notes="The Z and Data channels may be array channels. If they are, the array sizes must match.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('output_voxel_filename', type=Type.STRING,
                             doc="Output voxel filename"),
                   Parameter('origin_x', type=Type.DOUBLE,
                             doc="Voxel origin X"),
                   Parameter('origin_y', type=Type.DOUBLE,
                             doc="Voxel origin Y"),
                   Parameter('origin_z', type=Type.DOUBLE,
                             doc="Voxel origin Z"),
                   Parameter('cell_count_x', type=Type.INT32_T,
                             doc="Voxel cell count X"),
                   Parameter('cell_count_y', type=Type.INT32_T,
                             doc="Voxel cell count Y"),
                   Parameter('cell_count_z', type=Type.INT32_T,
                             doc="Voxel cell count Z"),
                   Parameter('cell_size_x', type=Type.DOUBLE,
                             doc="Voxel cell size X"),
                   Parameter('cell_size_y', type=Type.DOUBLE,
                             doc="Voxel cell size Y"),
                   Parameter('cell_size_z', type=Type.DOUBLE,
                             doc="Voxel cell size Z"),
                   Parameter('method', type=Type.INT32_T,
                             doc=":def:`MULTIVOXSET_DIRECTGRID_METHOD`"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('x_channel', type="DB_SYMB",
                             doc="X channel [:const:`DB_LOCK_READONLY`]"),
                   Parameter('y_channel', type="DB_SYMB",
                             doc="Y channel [:const:`DB_LOCK_READONLY`]"),
                   Parameter('z_channel', type="DB_SYMB",
                             doc="Z channel [:const:`DB_LOCK_READONLY`]"),
                   Parameter('data_channel', type="DB_SYMB",
                             doc="Data channel [:const:`DB_LOCK_READONLY`]")
               ])
    ]
}

