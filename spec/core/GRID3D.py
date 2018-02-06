from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('GRID3D',
                 doc="High Performance 3D Grid.")


gx_defines = [ 
    Define('GRID3D_TYPE',
           doc="Type of Voxset",
           constants=[
               Constant('GRID3D_DOUBLE', value='0', type=Type.INT32_T,
                        doc="DOUBLE"),
               Constant('GRID3D_VECTOR', value='1', type=Type.INT32_T,
                        doc="VECTOR"),
               Constant('GRID3D_THEMATIC', value='2', type=Type.INT32_T,
                        doc="THEMATIC")
           ])
		   ]


gx_methods = {
    'Miscellaneous': [  	   	   

		Method('GetType_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the type of this GRID3D",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object")
               ]),


		Method('iIsThematic_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Does this grid3d contain thematic data",
               return_type=Type.BOOL,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object")
               ]),

		Method('iIsDouble_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Does this grid3d contain floating point data",
               return_type=Type.BOOL,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object")
               ]),

		Method('iIsVector_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Does this grid3d contain vector data",
               return_type=Type.BOOL,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object")
               ]),

		Method('GetTPAT_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the TPAT from the thematic grid3d.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
                   Parameter('ipj', type="TPAT",
                             doc=":class:`TPAT` object")
               ]),

		Method('SetTPAT_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Set the TPAT of a thematic grid3d.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
                   Parameter('ipj', type="TPAT",
                             doc=":class:`TPAT` object")
               ]),

	    Method('GetDoubleStats_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get Double statistics.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
				   Parameter('num_valid', type=Type.INT32_T,is_ref=True,
                             doc="Number of valid values"),
				   Parameter('num_dummies', type=Type.INT32_T,is_ref=True,
                             doc="Number of invalid values"),
				   Parameter('min', type=Type.DOUBLE,is_ref=True,
                             doc="Min value"),
			       Parameter('max', type=Type.DOUBLE,is_ref=True,
                             doc="Maximum value"),
			       Parameter('mean', type=Type.DOUBLE,is_ref=True,
                             doc="Mean value"),
			       Parameter('stddev', type=Type.DOUBLE,is_ref=True,
                             doc="Standard Deviation"),
               ]),

		Method('GetThematicStats_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get Thematic Data statistics.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
				   Parameter('num_valid', type=Type.INT32_T,is_ref=True,
                             doc="Number of valid values"),
				   Parameter('num_dummies', type=Type.INT32_T,is_ref=True,
                             doc="Number of invalid values"),
				   Parameter('min', type=Type.INT32_T,is_ref=True,
                             doc="Min value"),
			       Parameter('max', type=Type.INT32_T,is_ref=True,
                             doc="Maximum value"),
			       Parameter('mean', type=Type.INT32_T,is_ref=True,
                             doc="Mean value"),
			       Parameter('stddev', type=Type.INT32_T,is_ref=True,
                             doc="Standard Deviation"),
               ]),

	    Method('GetVectorStats_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get Vector Data statistics.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
				   Parameter('num_valid', type=Type.INT32_T,is_ref=True,
                             doc="Number of valid values"),
				   Parameter('num_dummies', type=Type.INT32_T,is_ref=True,
                             doc="Number of invalid values"),
				   Parameter('min_x', type=Type.DOUBLE,is_ref=True,
                             doc="Min X value"),
				   Parameter('min_y', type=Type.DOUBLE,is_ref=True,
                             doc="Min Y value"),
				   Parameter('min_z', type=Type.DOUBLE,is_ref=True,
                             doc="Min Z value"),
			       Parameter('max_x', type=Type.DOUBLE,is_ref=True,
                             doc="Maximum X value"),
			       Parameter('max_y', type=Type.DOUBLE,is_ref=True,
                             doc="Maximum Y value"),
			       Parameter('max_z', type=Type.DOUBLE,is_ref=True,
                             doc="Maximum Z value"),
			       Parameter('mean_x', type=Type.DOUBLE,is_ref=True,
                             doc="Mean X value"),
			       Parameter('mean_y', type=Type.DOUBLE,is_ref=True,
                             doc="Mean Y value"),
			       Parameter('mean_z', type=Type.DOUBLE,is_ref=True,
                             doc="Mean Z value"),
			       Parameter('stddev_x', type=Type.DOUBLE,is_ref=True,
                             doc="Standard X Deviation"),
			       Parameter('stddev_y', type=Type.DOUBLE,is_ref=True,
                             doc="Standard Y Deviation"),
			       Parameter('stddev_z', type=Type.DOUBLE,is_ref=True,
                             doc="Standard Z Deviation"),
               ]),

	    Method('FillDouble_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Fill the grid3d with a single double value.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
				   Parameter('value', type=Type.DOUBLE,
                             doc="Fill Value")
               ]),

	    Method('FillThematic_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Fill the grid3d with a single thematic value.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
				   Parameter('value', type=Type.INT32_T,
                             doc="Fill Value")
               ]),

	    Method('FillVector_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Fill the grid3d with a single vector value.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
				   Parameter('value_x', type=Type.DOUBLE,
                             doc="Fill Value X"),
				   Parameter('value_y', type=Type.DOUBLE,
                             doc="Fill Value Y"),
				   Parameter('value_z', type=Type.DOUBLE,
                             doc="Fill Value Z"),
               ]),
			   
		Method('GetElementsInBlockX_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of cells in the block in the X direction",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object")
               ]),

		Method('GetElementsInBlockY_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of cells in the block in the Y direction",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object")
               ]),

		Method('GetElementsInBlockZ_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of cells in the block in the Z direction",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object")
               ]),

		Method('ReadX_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Read data from a GRID3D in the x direction (MOST EFFICIENT)",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
				   Parameter('x', type=Type.INT32_T,
                             doc="X location"),
				   Parameter('y', type=Type.INT32_T,
                             doc="Y location"),
				   Parameter('z', type=Type.INT32_T,
                             doc="Z location"),
				   Parameter('VV', type="VV",
                             doc="VV Containing Data"),
	               ]),

		Method('WriteX_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Write data to a GRID3D in the X direction (MOST EFFICIENT)",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
				   Parameter('x', type=Type.INT32_T,
                             doc="X location"),
				   Parameter('y', type=Type.INT32_T,
                             doc="Y location"),
				   Parameter('z', type=Type.INT32_T,
                             doc="Z location"),
				   Parameter('VV', type="VV",
                             doc="VV Containing Data"),
	               ]),

		Method('ReadY_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Read data from a GRID3D in the Y direction",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
				   Parameter('x', type=Type.INT32_T,
                             doc="X location"),
				   Parameter('y', type=Type.INT32_T,
                             doc="Y location"),
				   Parameter('z', type=Type.INT32_T,
                             doc="Z location"),
				   Parameter('VV', type="VV",
                             doc="VV Containing Data"),
	               ]),

		Method('WriteY_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Write data to a GRID3D in the Y direction",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
				   Parameter('x', type=Type.INT32_T,
                             doc="X location"),
				   Parameter('y', type=Type.INT32_T,
                             doc="Y location"),
				   Parameter('z', type=Type.INT32_T,
                             doc="Z location"),
				   Parameter('VV', type="VV",
                             doc="VV Containing Data"),
	               ]),

		Method('ReadZ_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Read data from a GRID3D in the Z direction",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
				   Parameter('x', type=Type.INT32_T,
                             doc="X location"),
				   Parameter('y', type=Type.INT32_T,
                             doc="Y location"),
				   Parameter('z', type=Type.INT32_T,
                             doc="Z location"),
				   Parameter('VV', type="VV",
                             doc="VV Containing Data"),
	               ]),

		Method('WriteZ_GRID3D', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Write data to a GRID3D in the Z direction",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('grid3d', type="GRID3D",
                             doc=":class:`GRID3D` object"),
				   Parameter('x', type=Type.INT32_T,
                             doc="X location"),
				   Parameter('y', type=Type.INT32_T,
                             doc="Y location"),
				   Parameter('z', type=Type.INT32_T,
                             doc="Z location"),
				   Parameter('VV', type="VV",
                             doc="VV Containing Data"),
	               ]),
    ]
}

