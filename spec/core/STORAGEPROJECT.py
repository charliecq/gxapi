from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('STORAGEPROJECT',
                 doc="Project Storage.")


gx_defines = []


gx_methods = {
    'Miscellaneous': [	  

		Method('Open_STORAGEPROJECT', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Open a project storage.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Project File Name")
               ]),

		Method('Close_STORAGEPROJECT', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Close the project storage.",
               return_type=Type.VOID,
               parameters = [
               ]),
			   
		Method('RemoveDataset_STORAGEPROJECT', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, 
               doc="Remove this dataset from the project.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Dataset File Name")
               ]),
    ]
}

