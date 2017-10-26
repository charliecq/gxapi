from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('EXT',
                 doc="External (plug-in) image methods.")





gx_methods = {
    'Miscellaneous': [

        Method('GetInfo_EXT', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Retrieves information about an external image format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type=Type.STRING,
                             doc="Image Name"),
                   Parameter('xmin', type=Type.DOUBLE, is_ref=True,
                             doc="X Min"),
                   Parameter('ymin', type=Type.DOUBLE, is_ref=True,
                             doc="Y Min"),
                   Parameter('xmax', type=Type.DOUBLE, is_ref=True,
                             doc="X Max"),
                   Parameter('ymax', type=Type.DOUBLE, is_ref=True,
                             doc="Y Max"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection Information")
               ])
    ]
}

