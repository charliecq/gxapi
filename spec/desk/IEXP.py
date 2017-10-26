from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('IEXP',
                 doc="""
                 The :class:`IEXP` class is similar to the :class:`EXP` class, but is used
                 to apply math expressions to grids (:class:`IMG` objects).
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('AddGrid_IEXP', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               This method adds an image to the :class:`IEXP` object with a
               variable name.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('iexp', type="IEXP",
                             doc=":class:`IEXP` object"),
                   Parameter('img', type="IMG",
                             doc="Image to add"),
                   Parameter('var', type=Type.STRING,
                             doc="Variable name")
               ]),

        Method('Create_IEXP', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="This method creates an :class:`IEXP` object.",
               return_type="IEXP",
               return_doc=":class:`IEXP` Object"),

        Method('Destroy_IEXP', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a :class:`IEXP` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('iexp', type="IEXP",
                             doc="Destroy a :class:`IEXP` object")
               ]),

        Method('DoFormula_IEXP', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="This method runs a formula on the grids.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('iexp', type="IEXP",
                             doc=":class:`IEXP` object"),
                   Parameter('formula', type=Type.STRING,
                             doc="Formula"),
                   Parameter('max_len', type=Type.INT32_T,
                             doc="Max. Buff size")
               ])
    ]
}

