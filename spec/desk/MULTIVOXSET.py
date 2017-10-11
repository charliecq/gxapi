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
                   Parameter('p1', type=Type.STRING,
                             doc="Name of output Voxel file"),
                   Parameter('p2', type="RA",
                             doc=":class:`RA` To import from"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Data Type :def:`GS_TYPES`"),
                   Parameter('p4', type="IPJ",
                             doc="Projection")
               ]),

        Method('ExportToXYZ_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export a :class:`MULTIVOXSET` to an XYZ File",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DIRECTION3D`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Reverse X ? (0/1)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Reverse Y ? (0/1)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Reverse Z ? (0/1)"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Write Dummies? (0/1)")
               ]),

        Method('ExportToBinary_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.LICENSED, 
               doc="Export contents of :class:`MULTIVOXSET` to a Binary File.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('p2', type=Type.STRING,
                             doc="Binary file to write to"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DIRECTION3D`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Reverse X ? (0/1)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Reverse Y ? (0/1)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Reverse Z ? (0/1)"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Swap Bytes ? (0/1)"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Output Type (Geosoft Type)")
               ]),

        Method('ExportToXML_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export a :class:`MULTIVOXSET` to XML",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Voxel file"),
                   Parameter('p2', type=Type.STRING,
                             doc="XML file")
               ]),

        Method('CheckEqualToLegacyVoxel_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Compare :class:`MULTIVOXSET` to Legacy Voxel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Voxel file"),
                   Parameter('p2', type=Type.STRING,
                             doc="Legacy Voxel file")
               ]),

        Method('ImportFromUBC_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Import UBC file into a MultiVoxset",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of UBC Mesh File"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of UBC Mod File"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Dummy Value"),
                   Parameter('p5', type="IPJ",
                             doc="Projection")
               ]),

        Method('ImportFromGOCAD_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Imports a MultiVoxset from a GOCAD File",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of output :class:`VOX`"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of GOCAD Voxel file"),
                   Parameter('p3', type=Type.STRING,
                             doc="Propert name to import"),
                   Parameter('p4', type="IPJ"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`GOCAD_ORIENTATION`")
               ]),

        Method('ListPropertiesGOCAD_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="List all the properties available in this GOCAD file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of GOCAD Voxel file"),
                   Parameter('p2', type="LST",
                             doc="List object to populate")
               ]),

        Method('ImportFromGDB_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Imports from a Geosoft Database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of output Voxel file"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` To import from"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Symbol to import data from")
               ]),

        Method('ImportFromVectorGDB_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Imports from a Vector Geosoft Database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Voxel Name"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` To import from"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="VECTOR_IMPORTImport XYZ, UVW or Amplitude/Inclination/Declination channels"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Symbol to import X, U or Amplitude data from"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Symbol to import Y, V or Inclination data from"),
                   Parameter('p6', type="DB_SYMB",
                             doc="Symbol to import Z, W or Declination data from"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Inclination value for :def_val:`VOX_VECTORVOX_UVW` (-90° to 90°)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Declination value for :def_val:`VOX_VECTORVOX_UVW` (-180° to 180°)")
               ]),

        Method('ExportToSEGY_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export To SEGY",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('p2', type=Type.STRING,
                             doc="Voxel Name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Output Segy file"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Sampling Internal")
               ]),

        Method('ExportToGDB_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export To GDB",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type=Type.STRING,
                             doc="Channel Name"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DIRECTION3D`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Reverse X ? (0/1)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Reverse Y ? (0/1)"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Reverse Z ? (0/1)"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Write Dummies? (0/1)")
               ]),

        Method('ExportToWA_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export To GDB",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('p2', type="WA",
                             doc=":class:`WA` File"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DIRECTION3D`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Reverse X ? (0/1)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Reverse Y ? (0/1)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Reverse Z ? (0/1)"),
                   Parameter('p7', type=Type.STRING,
                             doc="The Dummy string to write")
               ]),

        Method('ConvertDoubleToVector_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Convert 3 Double Voxels to a Vector Voxel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input X Voxel file"),
                   Parameter('p2', type=Type.STRING,
                             doc="Input Y Voxel file"),
                   Parameter('p3', type=Type.STRING,
                             doc="Input Z Voxel file"),
                   Parameter('p4', type=Type.STRING,
                             doc="Output Vector Voxel file"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Inclination"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Declination"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Rotated ? (0/1)")
               ]),

        Method('ConvertVectorToDouble_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Convert a Vector Voxel to 3 double Voxels",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input Vector Voxel file"),
                   Parameter('p2', type=Type.STRING,
                             doc="Output X Voxel file"),
                   Parameter('p3', type=Type.STRING,
                             doc="Output Y Voxel file"),
                   Parameter('p4', type=Type.STRING,
                             doc="Output Z Voxel file")
               ]),

        Method('CreateDoubleConstant_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of output Voxel File"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Constant Value to use - DUMMY for a trully sparse voxel"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Cell Size X"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Cell Size Y"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Cell Size Z"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Cell Count X"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Cell Count Y"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="Cell Count Z"),
                   Parameter('p12', type="IPJ",
                             doc="Projection")
               ]),

        Method('CreateThematicConstant_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of output Voxel File"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Constant Value to use - DUMMY for a trully sparse voxel"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Cell Size X"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Cell Size Y"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Cell Size Z"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Cell Count X"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Cell Count Y"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="Cell Count Z"),
                   Parameter('p12', type="IPJ",
                             doc="Projection")
               ]),

        Method('CreateVectorConstant_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of output Voxel File"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X Constant Value to use - DUMMY for a trully sparse voxel"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y Constant Value to use - DUMMY for a trully sparse voxel"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z Constant Value to use - DUMMY for a trully sparse voxel"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Cell Size X"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Cell Size Y"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Cell Size Z"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="Cell Count X"),
                   Parameter('p12', type=Type.INT32_T,
                             doc="Cell Count Y"),
                   Parameter('p13', type=Type.INT32_T,
                             doc="Cell Count Z"),
                   Parameter('p14', type="IPJ",
                             doc="Projection")
               ]),

        Method('CreateDoubleConstantVV_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value and non-uniform cell sizes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of output Voxel"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="The contant Value to fill with - DUMMY for a trully sparse voxel"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('p6', type="VV",
                             doc="Cell Sizes X"),
                   Parameter('p7', type="VV",
                             doc="Cell Sizes Y"),
                   Parameter('p8', type="VV",
                             doc="Cell Sizes Z"),
                   Parameter('p9', type="IPJ",
                             doc="Projection")
               ]),

        Method('CreateThematicConstantVV_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value and non-uniform cell sizes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of output Voxel"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="The contant Value to fill with - DUMMY for a trully sparse voxel"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('p6', type="VV",
                             doc="Cell Sizes X"),
                   Parameter('p7', type="VV",
                             doc="Cell Sizes Y"),
                   Parameter('p8', type="VV",
                             doc="Cell Sizes Z"),
                   Parameter('p9', type="IPJ",
                             doc="Projection")
               ]),

        Method('CreateVectorConstantVV_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a double MultiVoxset with a constant value and non-uniform cell sizes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of output Voxel"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="The X contant Value to fill with - DUMMY for a trully sparse voxel"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="The Y contant Value to fill with - DUMMY for a trully sparse voxel"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="The Z contant Value to fill with - DUMMY for a trully sparse voxel"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Origin Z"),
                   Parameter('p8', type="VV",
                             doc="Cell Sizes X"),
                   Parameter('p9', type="VV",
                             doc="Cell Sizes Y"),
                   Parameter('p10', type="VV",
                             doc="Cell Sizes Z"),
                   Parameter('p11', type="IPJ",
                             doc="Projection")
               ]),

        Method('ExportToVoxel_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Exports a Multi-Voxset into a Voxel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Project file"),
                   Parameter('p2', type=Type.STRING,
                             doc="Multi-Voxset UUID"),
                   Parameter('p3', type=Type.STRING,
                             doc="Multi-Voxset attribute"),
                   Parameter('p4', type=Type.STRING,
                             doc="Output Voxel file")
               ]),

        Method('ImportFromVoxel_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Import a Voxel directly into a Multi-Voxset",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Project file"),
                   Parameter('p2', type=Type.STRING,
                             doc="Input Voxel file"),
                   Parameter('p3', type=Type.STRING,
                             doc="Multi-Voxset attribute"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="UUID string returned"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of UUID string")
               ]),

        Method('ImportFromDATAMINE_MULTIVOXSET', module='geoengine.interoperability', version='9.3.0',
               availability=Availability.LICENSED, 
               doc="Create a Geosoft Voxel file from a Datamine block model file.",
               notes="Create a Geosoft Voxel file from a Datamine block model file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Datamine file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Field to use for data"),
                   Parameter('p3', type="IPJ",
                             doc="Projection to set"),
                   Parameter('p4', type=Type.STRING,
                             doc="Output voxel file name")
               ]),

        Method('rComputeDefaultCellSize_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.LICENSED, 
               doc="Used if the user does not provide a default cell size.",
               notes="Compute a default cell size for a voxel given a data range.",
               return_type=Type.DOUBLE,
               return_doc="Default Cell Size",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="MinX"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="MaxX"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="MinY"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="MaxY"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="MinZ"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="MaxZ")
               ]),

        Method('Filter_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.LICENSED, 
               doc="Apply a 3D filter to a voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the input voxel"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the output voxel"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`FILTER3D`"),
                   Parameter('p4', type=Type.STRING,
                             doc="filter file, if filter is :def_val:`VOX_FILTER3D_FILE`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="number of filter passes"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="(1: interpolate dummies)")
               ]),

        Method('GridDirectFromGDB_MULTIVOXSET', module='geoengine.core', version='9.3.0',
               availability=Availability.LICENSED, 
               doc="Create a voxel using direct gridding.",
               notes="The Z and Data channels may be array channels. If they are, the array sizes must match.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Output voxel filename"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Voxel origin X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Voxel origin Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Voxel origin Z"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Voxel cell count X"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Voxel cell count Y"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Voxel cell count Z"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Voxel cell size X"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Voxel cell size Y"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Voxel cell size Z"),
                   Parameter('p11', type=Type.INT32_T,
                             doc=":def:`MULTIVOXSET_DIRECTGRID_METHOD`"),
                   Parameter('p12', type="DB",
                             doc="Database"),
                   Parameter('p13', type="DB_SYMB",
                             doc="X channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p14', type="DB_SYMB",
                             doc="Y channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p15', type="DB_SYMB",
                             doc="Z channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p16', type="DB_SYMB",
                             doc="Data channel [:def_val:`DB_LOCK_READONLY`]")
               ])
    ]
}

