from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('PAT',
                 doc="""
                 A :class:`PAT` object is created from a Geosoft format pattern file.
                 It contains all the individual patterns listed in the file.
                 
                 Notes: You may create your own fill patterns. They can be added to the "user.pat"
                 file in the <geosoft>\\user\\etc directory. User pattern numbers should be in the 
                 range between 20000 and 29999.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('Create_PAT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates a pattern object with current default patterns.",
               return_type="PAT",
               return_doc=":class:`PAT` object"),

        Method('Destroy_PAT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys a pattern object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('pat', type="PAT",
                             doc=":class:`PAT` Handle")
               ]),

        Method('GetLST_PAT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copies all pattern names into a :class:`LST` object.",
               notes="""
               Returns a list of the available patterns.
               There will always be at least two items,
               "None" and "Solid Fill"
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('pat', type="PAT",
                             doc=":class:`PAT` Handle"),
                   Parameter('cl', type=Type.STRING,
                             doc='Class name ("" for all classes)'),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` Handle")
               ])
    ],
    'Obsolete': [

        Method('Copy_PAT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Copy one :class:`PAT` object to another.",
               notes="Was not correctly implemented or used",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dest', type="PAT",
                             doc="Destination :class:`PAT` to copy to"),
                   Parameter('source', type="PAT",
                             doc="Source :class:`PAT` to Copy from")
               ]),

        Method('Load_PAT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Load patterns from a file",
               notes="Was not correctly implemented or used",
               return_type=Type.VOID,
               parameters = [
                   Parameter('pat', type="PAT",
                             doc=":class:`PAT` handle"),
                   Parameter('file', type=Type.STRING,
                             doc="Pattern file name")
               ])
    ]
}

