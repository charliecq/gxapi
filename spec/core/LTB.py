from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('LTB',
                 doc="""
                 An :class:`LTB` object is typically created from a CSV (comma-separated values)
                 file, and is a table of information that may be accessed by row
                 or column. The :class:`LTB` class is recommended for use with small tables
                 produced from short lists (of the order of 1000's or records) such
                 as the different geographic projections and their defining parameters.
                 Large tables, such as those required for table-lookup functions, should
                 be accessed using the :class:`TB` class.
                 """,
                 notes="""
                 An :class:`LTB` ASCII table file has the following structure:
                 
                 / comments
                 key_name,col_1,col_2,col_3,etc...    /field names
                 key_1,token,token,token,etc...       /data lines
                 key_2,token,token,token,etc...
                 etc...
                 
                 The first column must be the key column (all entries unique).
                 
                 The header line is optional and can be used to find entries.
                 
                 Comment and empty lines are ignored.
                 """)


gx_defines = [
    Define('LTB_CASE',
           doc="Case handling of :class:`LTB` strings",
           constants=[
               Constant('LTB_CASE_INSENSITIVE', value='0', type=Type.INT32_T,
                        doc="Ignore case"),
               Constant('LTB_CASE_SENSITIVE', value='1', type=Type.INT32_T,
                        doc="Case is used")
           ]),

    Define('LTB_CONLST',
           doc="Matching types",
           constants=[
               Constant('LTB_CONLST_EXACT', value='0', type=Type.INT32_T),
               Constant('LTB_CONLST_ANY', value='1', type=Type.INT32_T)
           ]),

    Define('LTB_DELIM',
           doc="Types of :class:`LTB` Delimiters",
           constants=[
               Constant('LTB_DELIM_SPACE', value='0', type=Type.INT32_T,
                        doc="Spaces"),
               Constant('LTB_DELIM_COMMA', value='1', type=Type.INT32_T,
                        doc="Commas"),
               Constant('LTB_DELIM_SPACECOMMA', value='2', type=Type.INT32_T,
                        doc="Spaces and Commas")
           ]),

    Define('LTB_TYPE',
           doc="Types of :class:`LTB` Headers",
           constants=[
               Constant('LTB_TYPE_HEADER', value='0', type=Type.INT32_T,
                        doc="Has a header"),
               Constant('LTB_TYPE_NOHEADER', value='1', type=Type.INT32_T,
                        doc="Has no header")
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('AddRecord_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a new record.",
               notes="""
               If the record exists, the existing record is cleared
               and the record number is returned.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('key', type=Type.STRING,
                             doc="Key name"),
                   Parameter('rec', type=Type.INT32_T, is_ref=True,
                             doc="Returned record number")
               ]),

        Method('Contract_LTB', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Contract the contents of two same-key and same-fields tables.",
               notes="""
               The "Key" of the child must be the same as the "Key" of the Master.
               The fields of two :class:`LTB` must be the same.
               
               Contracting takes place as follows:
               
               1. The Master :class:`LTB` is copied to the New :class:`LTB`.
               2. All records in the contract LIB are deleted from the New :class:`LTB` (if there are any)
               3. The New :class:`LTB` is returned.
               """,
               return_type="LTB",
               return_doc="""
               x    - Handle to :class:`LTB` object
               NULL - Error of some kind
               """,
               parameters = [
                   Parameter('lt_bm', type="LTB",
                             doc="Master :class:`LTB`"),
                   Parameter('lt_bc', type="LTB",
                             doc="Contract :class:`LTB`")
               ]),

        Method('Create_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates a :class:`LTB` object from a file.",
               notes='If the file has no header, field names are assumed to be "0", "1", etc.',
               return_type="LTB",
               return_doc="""
               x    - Handle to :class:`LTB` object
               NULL - Error of some kind
               """,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="File name, .csv assumed, searched locally then in GEOSOFT."),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`LTB_TYPE`"),
                   Parameter('delim', type=Type.INT32_T,
                             doc=":def:`LTB_DELIM`"),
                   Parameter('key', type=Type.STRING,
                             doc='Key to find if only one record required, "" to read entire table.')
               ]),

        Method('CreateCrypt_LTB', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Creates a :class:`LTB` object from an encrypted file.",
               notes='If the file has no header, field names are assumed to be "0", "1", etc.',
               return_type="LTB",
               return_doc="""
               x    - Handle to :class:`LTB` object
               NULL - Error of some kind
               """,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="File name, .csv assumed, searched locally then in GEOSOFT."),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`LTB_TYPE`"),
                   Parameter('delim', type=Type.INT32_T,
                             doc=":def:`LTB_DELIM`"),
                   Parameter('case', type=Type.INT32_T,
                             doc=":def:`LTB_CASE`"),
                   Parameter('key', type=Type.STRING,
                             doc='Key to find if only one record required, "" to read entire table.'),
                   Parameter('crypt', type=Type.STRING,
                             doc="Decryption Key :def:`SYS_CRYPT_KEY`")
               ]),

        Method('CreateEx_LTB', module='geoengine.core', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="Creates a :class:`LTB` object from a file.",
               notes='If the file has no header, field names are assumed to be "0", "1", etc.',
               return_type="LTB",
               return_doc="""
               x    - Handle to :class:`LTB` object
               NULL - Error of some kind
               """,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="File name, .csv assumed, searched locally then in GEOSOFT."),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`LTB_TYPE`"),
                   Parameter('delim', type=Type.INT32_T,
                             doc=":def:`LTB_DELIM`"),
                   Parameter('case', type=Type.INT32_T,
                             doc=":def:`LTB_CASE`"),
                   Parameter('key', type=Type.STRING,
                             doc='Key to find if only one record required, "" to read entire table.')
               ]),

        Method('DeleteRecord_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Delete a record.",
               notes="""
               Record numbers after the deleted record will be reduced
               by 1.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('rec', type=Type.INT32_T,
                             doc="Record number to delete")
               ]),

        Method('Destroy_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object to destroy")
               ]),

        Method('GetConLST_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Populate a :class:`LST` with :class:`LTB` names from matching fields.",
               notes="""
               The :class:`LST` object will be in the order of the file.
               The :class:`LST` names will be the :class:`LTB` key fields and the
               :class:`LST` values will be the :class:`LTB` record numbers.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('fld', type=Type.INT32_T,
                             doc="Field"),
                   Parameter('match', type=Type.STRING,
                             doc="String to match to field, must be lower-case"),
                   Parameter('match_type', type=Type.INT32_T,
                             doc=":def:`LTB_CONLST`"),
                   Parameter('lst', type="LST",
                             doc="List to populate")
               ]),

        Method('GetLST_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Populate an :class:`LST` with :class:`LTB` names",
               notes="""
               The :class:`LST` object will be in the order of the file.
               The :class:`LST` names will be the :class:`LTB` fields and the
               :class:`LST` values will be the :class:`LTB` record numbers.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('fld', type=Type.INT32_T,
                             doc="Field to get, 0 for key field"),
                   Parameter('lst', type="LST",
                             doc="List to populate")
               ]),

        Method('GetLST2_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Populate an :class:`LST` with :class:`LTB` names and values",
               notes="""
               The :class:`LST` object will be in the order of the file.
               The :class:`LST` names will come from the :class:`LTB` name field and the
               :class:`LST` values will come from value field specified.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('fld_n', type=Type.INT32_T,
                             doc="Field for names, 0 for key field"),
                   Parameter('fld_v', type=Type.INT32_T,
                             doc="Field for values, 0 for key field"),
                   Parameter('lst', type="LST",
                             doc="List to populate")
               ]),

        Method('iFields_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get number of fields.",
               return_type=Type.INT32_T,
               return_doc="Number of fields in the :class:`LTB`.",
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object")
               ]),

        Method('iFindField_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return the field number for the specified field.",
               return_type=Type.INT32_T,
               return_doc="""
               -1 if field does not exist.
               field number if field does exist.
               """,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('field', type=Type.STRING,
                             doc="Field name")
               ]),

        Method('iFindKey_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return the key index of a record.",
               return_type=Type.INT32_T,
               return_doc="""
               -1 if key does not exist.
               record number if key does exist.
               """,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('key', type=Type.STRING,
                             doc="Key name")
               ]),

        Method('IGetField_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a field name by index.",
               notes="If the record or field are out of range, an empty string is returned.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('field_num', type=Type.INT32_T,
                             doc="Field number"),
                   Parameter('field', type=Type.STRING, is_ref=True, size_of_param='length',
                             doc="Returned field name"),
                   Parameter('length', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Maximum field name string length")
               ]),

        Method('iGetInt_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a int entry from the :class:`LTB`",
               return_type=Type.INT32_T,
               return_doc="""
               If the record or field are out of range,
               an empty string or dummy value is returned.
               """,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('record', type=Type.INT32_T,
                             doc="Record number"),
                   Parameter('field', type=Type.INT32_T,
                             doc="Field number")
               ]),

        Method('IGetString_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get an entry from the :class:`LTB`",
               notes="""
               If the record or field are out of range,
               an empty string or dummy value is returned.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('record', type=Type.INT32_T,
                             doc="Record number"),
                   Parameter('field', type=Type.INT32_T,
                             doc="Field number"),
                   Parameter('token', type=Type.STRING, is_ref=True, size_of_param='length',
                             doc="Returned field token"),
                   Parameter('length', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Maximum field token string length")
               ]),

        Method('IGetEnglishString_LTB', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the English entry from the :class:`LTB`",
               notes="""
               If the record or field are out of range,
               an empty string or dummy value is returned.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('record', type=Type.INT32_T,
                             doc="Record number"),
                   Parameter('field', type=Type.INT32_T,
                             doc="Field number"),
                   Parameter('token', type=Type.STRING, is_ref=True, size_of_param='length',
                             doc="Returned field token"),
                   Parameter('length', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Maximum field token string length")
               ]),

        Method('iRecords_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get number of records in :class:`LTB`.",
               return_type=Type.INT32_T,
               return_doc="Number of records in the :class:`LTB`.",
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object")
               ]),

        Method('iSearch_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Search for a record containing field value",
               return_type=Type.INT32_T,
               return_doc="""
               -1 if search failed.
               record number if search succeeds
               """,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('rec', type=Type.INT32_T,
                             doc="Search start record"),
                   Parameter('fld', type=Type.INT32_T,
                             doc="Field number"),
                   Parameter('field', type=Type.STRING,
                             doc="Search string (case sensitive)")
               ]),

        Method('Merge_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Merge the contents of two same-key tables.",
               notes="""
               Merging takes place as follows:
               
               1. The "Key" of the child must be the same as the "Key" of the Master.
               2. The fields of the Master :class:`LTB` are collected in-order.
               3. Any new fields of the Child :class:`LTB` are added to the end of the list.
               4. A new :class:`LTB` is created to contain the new field list (in-order).
               5. The Child table contents are added to the New :class:`LTB`.
               6. The Master table contents are added/replace the New :class:`LTB`.
               7. The New :class:`LTB` is returned.
               
               If the fields of the Master and Child are the same, steps 4, 5, 6 are
               replaced by:
               
               4. The Master :class:`LTB` is copied to the New :class:`LTB`.
               5. Any New records found in the child are added to the New :class:`LTB`
               """,
               return_type="LTB",
               return_doc="""
               x    - Handle to :class:`LTB` object
               NULL - Error of some kind
               """,
               parameters = [
                   Parameter('lt_bm', type="LTB",
                             doc="Master :class:`LTB`"),
                   Parameter('lt_bc', type="LTB",
                             doc="Child :class:`LTB`")
               ]),

        Method('rGetReal_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a real entry from the :class:`LTB`",
               return_type=Type.DOUBLE,
               return_doc="""
               If the record or field are out of range,
               an empty string or dummy value is returned.
               """,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('record', type=Type.INT32_T,
                             doc="Record number"),
                   Parameter('field', type=Type.INT32_T,
                             doc="Field number")
               ]),

        Method('Save_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Save :class:`LTB` changes to existing or new file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB"),
                   Parameter('file', type=Type.STRING,
                             doc='File name, .csv assumed.  If "", save to original file.')
               ]),

        Method('SaveCrypt_LTB', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Save :class:`LTB` to a new file using encryption",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB"),
                   Parameter('file', type=Type.STRING,
                             doc='File name, .csv assumed.  If "", save to original file.'),
                   Parameter('crypt', type=Type.STRING,
                             doc="Encryption key  :def:`SYS_CRYPT_KEY`")
               ]),

        Method('SetInt_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a long entry",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('record', type=Type.INT32_T,
                             doc="Record number"),
                   Parameter('field', type=Type.INT32_T,
                             doc="Field number"),
                   Parameter('data', type=Type.INT32_T,
                             doc="Entry")
               ]),

        Method('SetReal_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a double entry",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('record', type=Type.INT32_T,
                             doc="Record number"),
                   Parameter('field', type=Type.INT32_T,
                             doc="Field number"),
                   Parameter('data', type=Type.DOUBLE,
                             doc="Entry")
               ]),

        Method('SetString_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set an entry",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('record', type=Type.INT32_T,
                             doc="Record number"),
                   Parameter('field', type=Type.INT32_T,
                             doc="Field number"),
                   Parameter('token', type=Type.STRING,
                             doc="Entry")
               ])
    ]
}

