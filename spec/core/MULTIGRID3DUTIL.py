﻿from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MULTIGRID3DUTIL',
                 doc="High Performance 3D Grid.")


gx_defines = [
]


gx_methods = {
    'Miscellaneous': [	

        Method('ImportFromXYZ_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
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

        Method('ExportToXYZ_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Export a :class:`MULTIGRID3D` to an XYZ File",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d_file', type=Type.STRING,
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

        Method('ExportToBinary_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.LICENSED, 
               doc="Export contents of :class:`MULTIGRID3D` to a Binary File.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d_file', type=Type.STRING,
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

        Method('ExportToXML_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Export a :class:`MULTIGRID3D` to XML",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d_file', type=Type.STRING,
                             doc="Voxel file"),
                   Parameter('xml_file', type=Type.STRING,
                             doc="XML file")
               ]),

        Method('CheckEqualToLegacyVoxel_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Compare :class:`MULTIGRID3D` to Legacy Voxel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d_file', type=Type.STRING,
                             doc="Voxel file"),
                   Parameter('legacy_grid3d_file', type=Type.STRING,
                             doc="Legacy Voxel file")
               ]),

        Method('ImportFromUBC_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
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

        Method('ImportFromGOCAD_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
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

        Method('ListPropertiesGOCAD_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="List all the properties available in this GOCAD file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('header', type=Type.STRING,
                             doc="Name of GOCAD Voxel file"),
                   Parameter('lst', type="LST",
                             doc="List object to populate")
               ]),

        Method('ImportFromGDB_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Imports from a Geosoft Database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d_file', type=Type.STRING,
                             doc="Name of output Voxel file"),
                   Parameter('db', type="DB",
                             doc=":class:`DB` To import from"),
                   Parameter('symb', type="DB_SYMB",
                             doc="Symbol to import data from")
               ]),

        Method('ImportFromVectorGDB_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Imports from a Vector Geosoft Database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d_file', type=Type.STRING,
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

        Method('ExportToSEGY_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Export To SEGY",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d_file', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('grid3d_name', type=Type.STRING,
                             doc="Voxel Name"),
                   Parameter('output_segy_filename', type=Type.STRING,
                             doc="Output Segy file"),
                   Parameter('sample_interval', type=Type.DOUBLE,
                             doc="Sampling Internal")
               ]),

        Method('ExportToGDB_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Export To GDB",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d_file', type=Type.STRING,
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

        Method('ExportToWA_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
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

        Method('ConvertDoubleToVector_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
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

        Method('ConvertVectorToDouble_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
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

        Method('ConvertThematicToDouble_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Convert Thematic MultiVoxset to Double MultiVoxset",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_grid3d_filename', type=Type.STRING,
                             doc="Input grid3d filename"),
                   Parameter('translate_vv', type="VV",
                             doc="Translation VV handle"),
                   Parameter('output_grid3d_filename', type=Type.STRING,
                             doc="Output grid3d filename")
               ]),

        Method('ConvertDoubleToThematic_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Convert Double MultiVoxset to Thematic MultiVoxset",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_grid3d_filename', type=Type.STRING,
                             doc="Input grid3d filename"),
                   Parameter('translate_vv', type="VV",
                             doc="Translation VV handle"),
                   Parameter('output_grid3d_filename', type=Type.STRING,
                             doc="Output grid3d filename")
               ]),

        Method('ConvertVelocityToDensity_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Convert Velocity MultiVoxset to Density MultiVoxset",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_grid3d_filename', type=Type.STRING,
                             doc="Input grid3d filename"),
                   Parameter('input_scaling_factor', type=Type.DOUBLE,
                             doc="1.0, if this grid3d is in meters per second. Otherwise, a value by which each input cell is multiplied to convert it into meters per second."),
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
                             doc="1.0, to produce an output grid3d that has units of g/cm^3. If different units are desired, pass in a different value, which will be multiplied into each output grid3d cell."),
                   Parameter('output_grid3d_filename', type=Type.STRING,
                             doc="Output grid3d filename")
               ]),

        Method('ConvertDensityToVelocity_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Convert Density MultiVoxset to Velocity MultiVoxset",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_grid3d_filename', type=Type.STRING,
                             doc="Input grid3d filename"),
                   Parameter('input_scaling_factor', type=Type.DOUBLE,
                             doc="1.0, if this grid3d is in meters per second. Otherwise, a value by which each input cell is multiplied to convert it into meters per second."),
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
                             doc="1.0, to produce an output grid3d that has units of g/cm^3. If different units are desired, pass in a different value, which will be multiplied into each output grid3d cell."),
                   Parameter('output_grid3d_filename', type=Type.STRING,
                             doc="Output grid3d filename")
               ]),

        Method('GetGOCADLocation_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the location of a grid3d with origin and scaled xyz vectors for use with GOCAD.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_grid3d_filename', type=Type.STRING,
                             doc="Input grid3d filename"),
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

        Method('CreateDoubleConstant_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output Voxel File"),
                   Parameter('value', type=Type.DOUBLE,
                             doc="Constant Value to use - DUMMY for a trully sparse grid3d"),
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

        Method('CreateThematicConstant_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output Voxel File"),
                   Parameter('value', type=Type.INT32_T,
                             doc="Constant Value to use - DUMMY for a trully sparse grid3d"),
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

        Method('CreateVectorConstant_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output Voxel File"),
                   Parameter('value_x', type=Type.DOUBLE,
                             doc="X Constant Value to use - DUMMY for a trully sparse grid3d"),
                   Parameter('value_y', type=Type.DOUBLE,
                             doc="Y Constant Value to use - DUMMY for a trully sparse grid3d"),
                   Parameter('value_z', type=Type.DOUBLE,
                             doc="Z Constant Value to use - DUMMY for a trully sparse grid3d"),
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

        Method('CreateDoubleConstantVV_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value and non-uniform cell sizes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output Voxel"),
                   Parameter('value', type=Type.DOUBLE,
                             doc="The contant Value to fill with - DUMMY for a trully sparse grid3d"),
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

        Method('CreateThematicConstantVV_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value and non-uniform cell sizes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output Voxel"),
                   Parameter('value', type=Type.INT32_T,
                             doc="The contant Value to fill with - DUMMY for a trully sparse grid3d"),
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

        Method('CreateVectorConstantVV_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value and non-uniform cell sizes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of output Voxel"),
                   Parameter('x_value', type=Type.DOUBLE,
                             doc="The X contant Value to fill with - DUMMY for a trully sparse grid3d"),
                   Parameter('y_value', type=Type.DOUBLE,
                             doc="The Y contant Value to fill with - DUMMY for a trully sparse grid3d"),
                   Parameter('z_value', type=Type.DOUBLE,
                             doc="The Z contant Value to fill with - DUMMY for a trully sparse grid3d"),
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

        Method('ExportToVoxel_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
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
                   Parameter('grid3d_file', type=Type.STRING,
                             doc="Output Voxel file")
               ]),

        Method('ImportFromVoxel_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Import a Voxel directly into a Multi-Voxset",
               return_type=Type.VOID,
               parameters = [
                   Parameter('project_file', type=Type.STRING,
                             doc="Project file"),
                   Parameter('grid3d_file', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('multi_voxset_attribute', type=Type.STRING,
                             doc="Multi-Voxset attribute"),
                   Parameter('p_uuid_string', type=Type.STRING, is_ref=True, size_of_param='p_uuid_string_len',
                             doc="UUID string returned"),
                   Parameter('p_uuid_string_len', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of UUID string")
               ]),

        Method('ImportFromDATAMINE_MULTIGRID3DUTIL', module='geoengine.interoperability', version='9.4.0',
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
                   Parameter('grid3d', type=Type.STRING,
                             doc="Output grid3d file name")
               ]),

        Method('rComputeDefaultCellSize_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.LICENSED, 
               doc="Used if the user does not provide a default cell size.",
               notes="Compute a default cell size for a grid3d given a data range.",
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

        Method('Filter_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.LICENSED, 
               doc="Apply a 3D filter to a grid3d.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_file', type=Type.STRING,
                             doc="Name of the input grid3d"),
                   Parameter('output_file', type=Type.STRING,
                             doc="Name of the output grid3d"),
                   Parameter('filter', type=Type.INT32_T,
                             doc=":def:`FILTER3D`"),
                   Parameter('filter_file', type=Type.STRING,
                             doc="Filter file, if filter is :const:`VOX_FILTER3D_FILE`"),
                   Parameter('n_passes', type=Type.INT32_T,
                             doc="Number of filter passes"),
                   Parameter('interpolate_dummies', type=Type.INT32_T,
                             doc="(1: interpolate dummies)")
               ]),

        Method('GridDirectFromGDB_MULTIGRID3DUTIL', module='geoengine.core', version='9.4.0',
               availability=Availability.LICENSED, 
               doc="Create a grid3d using direct gridding.",
               notes="The Z and Data channels may be array channels. If they are, the array sizes must match.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('output_grid3d_filename', type=Type.STRING,
                             doc="Output grid3d filename"),
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
                             doc=":def:`MULTIGRID3D_DIRECTGRID_METHOD`"),
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
               ]),


    ]
}

