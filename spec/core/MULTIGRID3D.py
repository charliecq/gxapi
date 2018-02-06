from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MULTIGRID3D',
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
           doc="Vector grid3d import direction",
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

    Define('MULTIGRID3D_DIRECTGRID_METHOD',
           doc="How to calculate the cell values for direct gridding.",
           constants=[
               Constant('MULTIGRID3D_DIRECTGRID_MIN', value='0', type=Type.INT32_T),
               Constant('MULTIGRID3D_DIRECTGRID_MAX', value='1', type=Type.INT32_T),
               Constant('MULTIGRID3D_DIRECTGRID_MEAN', value='2', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

		Method('Open_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Opens an existing Multivoxset",
               return_type="MULTIGRID3D",
               return_doc=":class:`MULTIGRID3D` handle, terminates if creation fails",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="File Name")
               ]),

		Method('Modify_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Opens an existing Multivoxset with an plan to modify it",
               return_type="MULTIGRID3D",
               return_doc=":class:`MULTIGRID3D` handle, terminates if creation fails",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="File Name")
               ]),

			   
		Method('Create_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Creates a new Multivoxset",
               return_type="MULTIGRID3D",
               return_doc=":class:`MULTIGRID3D` handle, terminates if creation fails",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="File Name"),
                   Parameter('size_x', type=Type.INT32_T,
                             doc="Size in X."),
                   Parameter('size_y', type=Type.INT32_T,
                             doc="Size in Y."),
                   Parameter('size_z', type=Type.INT32_T,
                             doc="Size in Z.")
               ]),

		Method('Duplicate_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Creates an MULTIGRID3D with identical geometry to the input",
               return_type="MULTIGRID3D",
               return_doc=":class:`MULTIGRID3D` handle, terminates if creation fails",
               parameters = [
			       Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
                   Parameter('name', type=Type.STRING,
                             doc="File Name")
               ]),

		Method('GetDefault_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the default voxset",
               return_type="GRID3D",
			   return_doc=":class:`GRID3D` handle, terminates if creation fails",
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object")
               ]),

		Method('CreateDefault_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the default voxset",
               return_type="GRID3D",
			   return_doc=":class:`GRID3D` handle, terminates if creation fails",
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GRID3D_TYPE`"),
               ]),

		Method('iIsUniformCellSizeX_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Is the cell uniform in the X direction",
               return_type=Type.BOOL,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object")
               ]),

		Method('iIsUniformCellSizeY_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Is the cell uniform in the Y direction",
               return_type=Type.BOOL,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object")
               ]),

		Method('iIsUniformCellSizeZ_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Is the cell uniform in the Z direction",
               return_type=Type.BOOL,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object")
               ]),



		Method('GetSizeX_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of cells in the X direction",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object")
               ]),

		Method('GetSizeY_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of cells in the X direction",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object")
               ]),

		Method('GetSizeZ_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of cells in the X direction",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object")
               ]),



		Method('GetCellSizesX_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the cell sizes in the X direction",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
                   Parameter('vv', type="VV",
                             doc="X :class:`VV`"),
               ]),

		Method('GetCellSizesY_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the cell sizes in the Y direction",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
                   Parameter('vv', type="VV",
                             doc="Y :class:`VV`"),
               ]),

		Method('GetCellSizesZ_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the cell sizes in the Z direction",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
                   Parameter('vv', type="VV",
                             doc="Z :class:`VV`"),
               ]),


			   

		Method('SetCellSizesX_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Set the cell sizes in the X direction",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
                   Parameter('vv', type="VV",
                             doc="X :class:`VV`"),
               ]),

		Method('SetCellSizesY_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Set the cell sizes in the Y direction",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
                   Parameter('vv', type="VV",
                             doc="Y :class:`VV`"),
               ]),

		Method('SetCellSizesZ_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Set the cell sizes in the Z direction",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
                   Parameter('vv', type="VV",
                             doc="Z :class:`VV`"),
               ]),
			   

		Method('rGetUniformCellSizeX_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the uniform cell size in the X direction",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object")
               ]),

		Method('rGetUniformCellSizeY_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the uniform cell size in the Y direction",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object")
               ]),
			   
		Method('rGetUniformCellSizeZ_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the uniform cell size in the Z direction",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object")
               ]),




		Method('SetUniformCellSizeX_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Set the uniform cell size in the X direction",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
					Parameter('cellsize', type=Type.DOUBLE,
                             doc="cell size")
               ]),

		Method('SetUniformCellSizeY_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the uniform cell size in the Y direction",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
					Parameter('cellsize', type=Type.DOUBLE,
                             doc="cell size")
               ]),
			   
		Method('SetUniformCellSizeZ_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the uniform cell size in the Z direction",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
					Parameter('cellsize', type=Type.DOUBLE,
                             doc="cell size")
               ]),




		Method('GetOrigin_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the origin",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
					Parameter('origin_x', type=Type.DOUBLE,is_ref=True,
                             doc="x"),
					Parameter('origin_y', type=Type.DOUBLE,is_ref=True,
                             doc="y"),
					Parameter('origin_z', type=Type.DOUBLE,is_ref=True,
                             doc="z")
               ]),

		Method('SetOrigin_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Set the origin",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
					Parameter('origin_x', type=Type.DOUBLE,
                             doc="x"),
					Parameter('origin_y', type=Type.DOUBLE,
                             doc="y"),
					Parameter('origin_z', type=Type.DOUBLE,
                             doc="z")
               ]),


		Method('GetBoundingBox_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the bounding box",
               return_type=Type.VOID,
               parameters = [
					Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
					Parameter('min_x', type=Type.DOUBLE,is_ref=True,
                             doc="minx"),
					Parameter('min_y', type=Type.DOUBLE,is_ref=True,
                             doc="miny"),
					Parameter('min_z', type=Type.DOUBLE,is_ref=True,
                             doc="minz"),
					Parameter('max_x', type=Type.DOUBLE,is_ref=True,
                             doc="maxx"),
					Parameter('min_y', type=Type.DOUBLE,is_ref=True,
                             doc="maxy"),
					Parameter('min_z', type=Type.DOUBLE,is_ref=True,
                             doc="maxz"),
               ]),

		Method('GetVolumeVectors_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the direction of the volume",
               return_type=Type.VOID,
               parameters = [
					Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
					Parameter('origin_x', type=Type.DOUBLE,is_ref=True,
                             doc="origin_x"),
					Parameter('origin_y', type=Type.DOUBLE,is_ref=True,
                             doc="origin_y"),
					Parameter('origin_z', type=Type.DOUBLE,is_ref=True,
                             doc="origin_z"),
					Parameter('X_vector_x', type=Type.DOUBLE,is_ref=True,
                             doc="X Vector x"),
					Parameter('X_vector_y', type=Type.DOUBLE,is_ref=True,
                             doc="X Vector y"),
					Parameter('X_vector_z', type=Type.DOUBLE,is_ref=True,
                             doc="X Vector z"),
					Parameter('Y_vector_x', type=Type.DOUBLE,is_ref=True,
                             doc="Y Vector x"),
					Parameter('Y_vector_y', type=Type.DOUBLE,is_ref=True,
                             doc="Y Vector y"),
					Parameter('Y_vector_z', type=Type.DOUBLE,is_ref=True,
                             doc="Y Vector z"),
					Parameter('Z_vector_x', type=Type.DOUBLE,is_ref=True,
                             doc="Z Vector x"),
					Parameter('Z_vector_y', type=Type.DOUBLE,is_ref=True,
                             doc="Z Vector y"),
					Parameter('Z_vector_z', type=Type.DOUBLE,is_ref=True,
                             doc="Z Vector z")
               ]),

		Method('GetOrientedDataExtents_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the data extents based on an orientation",
               return_type=Type.VOID,
               parameters = [
					Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
					Parameter('oriented_origin_x', type=Type.DOUBLE,
                             doc="oriented_origin_x"),
					Parameter('oriented_origin_y', type=Type.DOUBLE,
                             doc="oriented_origin_y"),
					Parameter('oriented_origin_z', type=Type.DOUBLE,
                             doc="oriented_origin_z"),
					Parameter('X_vector_x', type=Type.DOUBLE,
                             doc="X Vector x"),
					Parameter('X_vector_y', type=Type.DOUBLE,
                             doc="X Vector y"),
					Parameter('X_vector_z', type=Type.DOUBLE,
                             doc="X Vector z"),
					Parameter('Y_vector_x', type=Type.DOUBLE,
                             doc="Y Vector x"),
					Parameter('Y_vector_y', type=Type.DOUBLE,
                             doc="Y Vector y"),
					Parameter('Y_vector_z', type=Type.DOUBLE,
                             doc="Y Vector z"),
					Parameter('Z_vector_x', type=Type.DOUBLE,
                             doc="Z Vector x"),
					Parameter('Z_vector_y', type=Type.DOUBLE,
                             doc="Z Vector y"),
					Parameter('Z_vector_z', type=Type.DOUBLE,
                             doc="Z Vector z"),
					Parameter('p1_x', type=Type.DOUBLE,is_ref=True,
                             doc="Point1 x"),
					Parameter('p1_y', type=Type.DOUBLE,is_ref=True,
                             doc="Point1 y"),
					Parameter('p1_z', type=Type.DOUBLE,is_ref=True,
                             doc="Point1 z"),
					Parameter('p2_x', type=Type.DOUBLE,is_ref=True,
                             doc="Point2 x"),
					Parameter('p2_y', type=Type.DOUBLE,is_ref=True,
                             doc="Point2 y"),
					Parameter('p2_z', type=Type.DOUBLE,is_ref=True,
                             doc="Point2 z")
               ]),


		Method('GetSectionCellSizes_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the cell sizes of a section",
               return_type=Type.VOID,
               parameters = [
					Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
					Parameter('azimuth', type=Type.DOUBLE,
                             doc="azimuth"),
					Parameter('scale', type=Type.DOUBLE,
                             doc="scale"),
					Parameter('origin_x', type=Type.DOUBLE,
                             doc="x origin"),
					Parameter('origin_y', type=Type.DOUBLE,
                             doc="y origin"),
					Parameter('origin_z', type=Type.DOUBLE,
                             doc="z origin"),
					Parameter('cell_size_x', type=Type.DOUBLE,is_ref=True,
                             doc="cell size in x"),
					Parameter('cell_size_y', type=Type.DOUBLE,is_ref=True,
                             doc="cell size in y")
               ]),


		Method('Fill_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.LICENSED, 
               doc="Fill a grid3d.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
                   Parameter('output_file', type=Type.STRING,
                             doc="Name of the output grid3d"),
                   Parameter('method', type=Type.INT32_T,
                             doc=":def:`PGU_INTERP_ORDER`"),
				   Parameter('fill_value', type=Type.DOUBLE,
                             doc="Fill Value")
				]),
	

		Method('GetIPJ_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the projection of the multigrid3d.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` object")
               ]),

		Method('SetIPJ_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Set the projection of the multigrid3d.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` object")
               ]),

		Method('ExportToXYZ_MULTIGRID3D', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export a :class:`MULTIGRID3D` to an XYZ File",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
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

		Method('ExportToBinary_MULTIGRID3D', module='geoengine.core', version='9.3.0',
               availability=Availability.LICENSED, 
               doc="Export contents of :class:`MULTIGRID3D` to a Binary File.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
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

        Method('ExportToXML_MULTIGRID3D', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export a :class:`MULTIGRID3D` to XML",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
                   Parameter('xml_file', type=Type.STRING,
                             doc="XML file")
               ]),		

		Method('ExportToWA_MULTIGRID3D', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export To GDB",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
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

		Method('ExportToGDB_MULTIGRID3D', module='geoengine.core', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Export To GDB",
               return_type=Type.VOID,
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object"),
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

        Method('ExportToPG_MULTIGRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Export a MULTIGRID3D To a PG",
               return_type="PG",
               return_doc=":class:`PG` Object",
               parameters = [
                   Parameter('multigrid3d', type="MULTIGRID3D",
                             doc=":class:`MULTIGRID3D` object")
               ]),

    ]
}

