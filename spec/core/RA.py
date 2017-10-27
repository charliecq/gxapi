from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('RA',
                 doc="""
                 The :class:`RA` class is used to access ASCII files sequentially or
                 by line number. The files are opened in read-only mode, so no
                 write operations are defined
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('Create_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates :class:`RA`",
               return_type="RA",
               return_doc=":class:`RA` Object",
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="Name of the file")
               ]),

        Method('CreateSBF_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates :class:`RA` on an :class:`SBF`",
               notes="""
               This method allows you to open an :class:`RA` in a structured file
               storage (an :class:`SBF`).  SBFs can be created inside other data
               containers, such as workspaces, maps, images and databases.
               This lets you store application specific information together
               with the data to which it applies.
               """,
               see_also="sbf.gxh",
               return_type="RA",
               return_doc=":class:`RA` Object",
               parameters = [
                   Parameter('sbf', type="SBF",
                             doc="Storage"),
                   Parameter('file', type=Type.STRING,
                             doc="Name of the file")
               ]),

        Method('Destroy_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`RA`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ra', type="RA",
                             doc=":class:`RA` to destroy")
               ]),

        Method('IiGets_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get next full line from :class:`RA`",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - End of file
               """,
               parameters = [
                   Parameter('ra', type="RA",
                             doc=":class:`RA` handle"),
                   Parameter('strbuff', type=Type.STRING, is_ref=True, size_of_param='str_size',
                             doc="Buffer in which to place string"),
                   Parameter('str_size', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Maximum length of the string buffer")
               ]),

        Method('iLen_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the total number of lines in :class:`RA`",
               return_type=Type.INT32_T,
               return_doc="# of lines in the :class:`RA`.",
               parameters = [
                   Parameter('ra', type="RA",
                             doc=":class:`RA` handle")
               ]),

        Method('iLine_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns current line #, 0 is the first",
               notes="This will be the next line read.",
               return_type=Type.INT32_T,
               return_doc="The current read line location.",
               parameters = [
                   Parameter('ra', type="RA",
                             doc=":class:`RA` handle")
               ]),

        Method('iSeek_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Position next read to specified line #",
               return_type=Type.INT32_T,
               return_doc="""
               0 if seeked line is within the range of lines,
               1 if outside range, line pointer will not be moved.
               """,
               parameters = [
                   Parameter('ra', type="RA",
                             doc=":class:`RA` handle"),
                   Parameter('line', type=Type.INT32_T,
                             doc="Line #, 0 is the first.")
               ])
    ]
}

