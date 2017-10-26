from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('3DN',
                 doc="""
                 This class manages the rendering of a 3D view. It allows
                 the positioning of the camera, specification of the zoom
                 as well as some rendering controls for the axis. It is
                 directly related to the :class:`MVIEW` class.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('Copy_3DN', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Copy one :class:`3DN` object to another.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dest', type="3DN",
                             doc="Destination :class:`3DN` to copy to"),
                   Parameter('source', type="3DN",
                             doc="Source :class:`3DN` to Copy from")
               ]),

        Method('Create_3DN', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Creates a :class:`3DN`.",
               return_type="3DN",
               return_doc=":class:`3DN` Object"),

        Method('Destroy_3DN', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Destroys a :class:`3DN` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle")
               ]),

        Method('GetPointOfView_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get location of the point we are looking from",
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('distance', type=Type.DOUBLE, is_ref=True,
                             doc="Distance from center relative to longest grid dimension (which is 1.0)"),
                   Parameter('declination', type=Type.DOUBLE, is_ref=True,
                             doc="Declination, 0 to 360 CW from Y"),
                   Parameter('inclination', type=Type.DOUBLE, is_ref=True,
                             doc="Inclination, -90 to +90")
               ]),

        Method('GetScale_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the axis relative scales.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="X Scale"),
                   Parameter('y', type=Type.DOUBLE, is_ref=True,
                             doc="Y Scale"),
                   Parameter('z', type=Type.DOUBLE, is_ref=True,
                             doc="Z Scale")
               ]),

        Method('iGetAxisColor_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the Axis draw color",
               return_type=Type.INT32_T,
               return_doc="Axis Color",
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle")
               ]),

        Method('IGetAxisFont_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the Axis font",
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('font', type=Type.STRING, is_ref=True, size_of_param='font_size',
                             doc="Font name"),
                   Parameter('font_size', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Font Buffer Size")
               ]),

        Method('iGetBackgroundColor_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the window background color",
               return_type=Type.INT32_T,
               return_doc="Background Color value",
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle")
               ]),

        Method('IGetRenderControls_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the rendering controls",
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('box', type=Type.INT32_T, is_ref=True,
                             doc="Render Bounding Box (0 or 1)"),
                   Parameter('axis', type=Type.INT32_T, is_ref=True,
                             doc="Render Axis (0 or 1)"),
                   Parameter('label_x', type=Type.STRING, is_ref=True, size_of_param='label_size_x',
                             doc="Label for X axis"),
                   Parameter('label_size_x', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of X Buffer"),
                   Parameter('label_y', type=Type.STRING, is_ref=True, size_of_param='label_size_y',
                             doc="Label for Y axis"),
                   Parameter('label_size_y', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of Y Buffer"),
                   Parameter('label_z', type=Type.STRING, is_ref=True, size_of_param='label_size_z',
                             doc="Label for Z axis"),
                   Parameter('label_size_z', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of Z Buffer")
               ]),

        Method('iGetShading_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set the shading control on or off",
               return_type=Type.INT32_T,
               return_doc="Shading On/Off",
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle")
               ]),

        Method('_SetAxisColor_3DN', module='geoengine.map', version='5.1.6',
               external_name='SetAxisColor_3DN',
               availability=Availability.PUBLIC, 
               doc="Set the Axis draw color",
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('color', type=Type.INT32_T,
                             doc="Axis Color")
               ]),

        Method('_SetAxisFont_3DN', module='geoengine.map', version='5.1.6',
               external_name='SetAxisFont_3DN',
               availability=Availability.PUBLIC, 
               doc="Set the Axis font",
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('font', type=Type.STRING,
                             doc="Font name")
               ]),

        Method('_SetBackgroundColor_3DN', module='geoengine.map', version='5.1.6',
               external_name='SetBackgroundColor_3DN',
               availability=Availability.PUBLIC, 
               doc="Set the window background color",
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('color', type=Type.INT32_T,
                             doc="Background Color")
               ]),

        Method('SetPointOfView_3DN', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set location of the point we are looking from",
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('distance', type=Type.DOUBLE,
                             doc="Distance from center relative to longest grid dimension (which is 1.0)"),
                   Parameter('declination', type=Type.DOUBLE,
                             doc="Declination, 0 to 360 CW from Y"),
                   Parameter('inclination', type=Type.DOUBLE,
                             doc="Inclination, -90 to +90")
               ]),

        Method('SetRenderControls_3DN', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the rendering controls",
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('box', type=Type.INT32_T,
                             doc="Render Bounding Box (0 or 1)"),
                   Parameter('axis', type=Type.INT32_T,
                             doc="Render Axis (0 or 1)"),
                   Parameter('label_x', type=Type.STRING,
                             doc="Label for X axis"),
                   Parameter('label_y', type=Type.STRING,
                             doc="Label for Y axis"),
                   Parameter('label_z', type=Type.STRING,
                             doc="Label for Z axis")
               ]),

        Method('SetScale_3DN', module='geoengine.map', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="Set the axis relative scales.",
               notes="""
               By default all scales are equal (1.0). By setting
               these scales, relative adjustments to the overall
               view of the 3D objects can be made. Note that they
               are relative to each other. Thus, setting the scaling
               to 5,5,5 is the same as 1,1,1. This is typically used
               to exaggerate one scale such as Z (1,1,5).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X Scale (default 1.0)"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y Scale (default 1.0)"),
                   Parameter('z', type=Type.DOUBLE,
                             doc="Z Scale (default 1.0)")
               ]),

        Method('SetShading_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set the shading control on or off",
               return_type=Type.VOID,
               parameters = [
                   Parameter('o3dn', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('shading', type=Type.INT32_T,
                             doc="0: Off, 1:  On.")
               ])
    ]
}

