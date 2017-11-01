from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('E3DV',
                 doc="Methods to manipulate an active 3D View",
                 notes="")

gx_methods = {
    'Miscellaneous': [

        Method('GetDataView_E3DV', module='geoengine.3dv', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the current data (3D) :class:`MVIEW`",
               return_type="MVIEW",
               return_doc=":class:`MVIEW` object",
               parameters = [
                   Parameter('e_3dv', type="E3DV",
                             doc=":class:`E3DV` object")
               ]),

        Method('GetBaseView_E3DV', module='geoengine.3dv', version='9.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the current Base :class:`MVIEW` (used to draw 2D legends for groups)",
               return_type="MVIEW",
               return_doc=":class:`MVIEW` object",
               parameters = [
                   Parameter('e_3dv', type="E3DV",
                             doc=":class:`E3DV` object")
               ])
    ]
}

