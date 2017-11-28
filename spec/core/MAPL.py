from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MAPL',
                 doc="""
                 The :class:`MAPL` class is the interface with the MAPPLOT program,
                 which reads a MAPPLOT control file and plots graphical
                 entities to a map. The :class:`MAPL` object is created for a given
                 control file, then passed to the MAPPLOT program, along
                 with the target :class:`MAP` object on which to do the drawing
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('Create_MAPL', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`MAPL`.",
               notes="""
               The default map groups will use the reference name with
               "_Data" and "_Base" added.  If no reference name is specified,
               the name ":class:`MAPL`" is used
               """,
               return_type="MAPL",
               return_doc=":class:`MAPL`, aborts if creation fails",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc=":class:`MAPL` file name"),
                   Parameter('ref_name', type=Type.STRING,
                             doc="Map base reference name"),
                   Parameter('line', type=Type.INT32_T,
                             doc="Start line number in file (0 is first)")
               ]),

        Method('CreateREG_MAPL', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`MAPL` with :class:`REG`.",
               notes="""
               The default map groups will use the reference name with
               "_Data" and "_Base" added.  If no reference name is specified,
               the name ":class:`MAPL`" is used
               """,
               return_type="MAPL",
               return_doc=":class:`MAPL`, aborts if creation fails",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc=":class:`MAPL` file name"),
                   Parameter('ref_name', type=Type.STRING,
                             doc="Map base reference name"),
                   Parameter('line', type=Type.INT32_T,
                             doc="Start line number in file (0 is first)"),
                   Parameter('reg', type="REG")
               ]),

        Method('Destroy_MAPL', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`MAPL` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mapl', type="MAPL",
                             doc=":class:`MAPL` Handle")
               ]),

        Method('Process_MAPL', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Process a :class:`MAPL`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mapl', type="MAPL",
                             doc=":class:`MAPL` Handle"),
                   Parameter('map', type="MAP")
               ]),

        Method('ReplaceString_MAPL', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Adds a replacement string to a mapplot control file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mapl', type="MAPL",
                             doc=":class:`MAPL` Handle"),
                   Parameter('var', type=Type.STRING,
                             doc="Variable"),
                   Parameter('repl', type=Type.STRING,
                             doc="Replacement")
               ])
    ]
}

