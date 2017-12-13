from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('TB',
                 doc="""
                 The :class:`TB` class is a high-performance table class used to
                 perform table-based processing, such as leveling data in
                 an OASIS database. The :class:`LTB` class is recommended for use
                 with small tables produced from short lists such as the
                 different geographic projections and their defining parameters.
                 """)


gx_defines = [
    Define('TB_SEARCH',
           doc=":class:`TB` Searching mode",
           constants=[
               Constant('TB_SEARCH_BINARY', value='0', type=Type.INT32_T,
                        doc="Random searches in a table."),
               Constant('TB_SEARCH_LINEAR', value='1', type=Type.INT32_T,
                        doc="Linear searches up or down a table (Default).")
           ]),
    Define('TB_SORT',
           doc=":class:`TB` Sorting mode",
           constants=[
               Constant('TB_SORT_UNIQUE', value='0', type=Type.INT32_T,
                        doc="Unique values only when sorting."),
               Constant('TB_SORT_ALLOW_DUPLICATES', value='1', type=Type.INT32_T,
                        doc="Allow duplicates when sorting.")
           ])
    ]

gx_methods = {
    'Miscellaneous': [

        Method('_SetSearchMode_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the search mode of a table.",
               notes="""
               If performance is an issue, you may want to test which search
               mode provides the best performance with typical data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`TB_SEARCH`")
               ]),


        Method('SetSortMode_TB', module='geoengine.core', version='9.3.1',
               availability=Availability.PUBLIC, 
               doc="Set the sort mode of a table.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`TB_SORT`")
               ]),


        Method('Create_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Loads a table into memory and return a table handle.",
               notes="""
               If the table contains fewer data columns than are defined by the
               the table header, the :class:`TB` object will read in the table and dummy
               the elements of the missing data columns.
               """,
               return_type="TB",
               return_doc=":class:`TB` Object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="Name of the table file to load")
               ]),

        Method('CreateDB_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a table from a database.",
               notes="""
               The table will contain fields for all channels in
               the database.
               
               The database is not loaded with data.  Use the :func:`LoadDB_TB`
               function to load data into the table.
               """,
               return_type="TB",
               return_doc=":class:`TB` Object",
               parameters = [
                   Parameter('db', type="DB",
                             doc="Database")
               ]),

        Method('CreateLTB_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a table from an :class:`LTB` database.",
               return_type="TB",
               return_doc=":class:`TB` Object",
               parameters = [
                   Parameter('ltb', type="LTB",
                             doc=":class:`LTB` object")
               ]),

        Method('Destroy_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a table resource.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table Object to Destroy")
               ]),

        Method('Field_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a field handle.",
               return_type="TB_FIELD",
               return_doc="The handle to the field (must be present)",
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table"),
                   Parameter('name', type=Type.STRING,
                             doc="Field name")
               ]),

        Method('GetString_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets a string value from a table element.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle"),
                   Parameter('row', type=Type.INT32_T,
                             doc="Row of element to Get"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column of element to Get"),
                   Parameter('val', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Returned string"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Maximum string size")
               ]),

        Method('iDataType_TB', module='geoengine.core', version='5.0.1',
               availability=Availability.PUBLIC, 
               doc="Returns the data type for the specified column.",
               return_type=Type.INT32_T,
               return_doc=":def:`DB_CATEGORY_CHAN`",
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column of element to Get")
               ]),

        Method('IFindColByIndex_TB', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Finds a column's name by its index.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle"),
                   Parameter('idx', type=Type.INT32_T,
                             doc="Index of column to find"),
                   Parameter('name', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="Buffer for column name"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of buffer")
               ]),

        Method('iFindColByName_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Finds a column's index by its name.",
               return_type=Type.INT32_T,
               return_doc="""
               Index of column.
               -1 if not found.
               """,
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle"),
                   Parameter('name', type=Type.STRING,
                             doc="Name of column to find")
               ]),

        Method('iFormat_TB', module='geoengine.core', version='5.0.1',
               availability=Availability.PUBLIC, 
               doc="Returns the channel format for the specified column.",
               return_type=Type.INT32_T,
               return_doc=":def:`DB_CHAN_FORMAT`",
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column of element to Get")
               ]),

        Method('iGetInt_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets an integer value from a table element.",
               return_type=Type.INT32_T,
               return_doc="Value",
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle"),
                   Parameter('row', type=Type.INT32_T,
                             doc="Row of element to Get"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column of element to Get")
               ]),

        Method('iNumColumns_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the number of data fields (columns) in a table.",
               return_type=Type.INT32_T,
               return_doc="Number of columns",
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle")
               ]),

        Method('iNumRows_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the number of data rows in a table.",
               return_type=Type.INT32_T,
               return_doc="Number of rows",
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle")
               ]),

        Method('LoadDB_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Load a database into a :class:`TB`",
               notes="The line is appended to the data already in the table.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('line', type="DB_SYMB",
                             doc="Line")
               ]),

        Method('rGetReal_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets an real value from a table element.",
               return_type=Type.DOUBLE,
               return_doc="Value",
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle"),
                   Parameter('row', type=Type.INT32_T,
                             doc="Row of element to Get"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column of element to Get")
               ]),

        Method('Save_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Saves the data in a table to a file. The table header will be
               in ASCII and the data will be in BINARY format.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle"),
                   Parameter('name', type=Type.STRING,
                             doc="Name of File to save table into")
               ]),

        Method('SaveDB_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Save a :class:`TB` in a database line",
               notes="""
               Missing channels are created.
               Data in existing channels on the line will be replaced.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('line', type="DB_SYMB",
                             doc="Line")
               ]),

        Method('SaveToAscii_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Saves the data in a table to a file. The table header will be
               in ASCII and the data will be in ASCII format.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle"),
                   Parameter('name', type=Type.STRING,
                             doc="Name of File to save table into")
               ]),

        Method('SetInt_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets an integer value into a table element.",
               notes="""
               The table field containing the element to be set MUST be
               of type :const:`GS_BYTE`, :const:`GS_USHORT`, :const:`GS_SHORT`, or :const:`GS_LONG`.
               If the field is :const:`GS_BYTE`, :const:`GS_USHORT`, or :const:`GS_LONG`, the new data
               value will cause an overflow if the value is out of range of
               the data type. The new element value will then be invalid.
               
               If the row of the new element exceeds the number of rows in
               the table, then the table will AUTOMATICALLY be EXPANDED to
               exactly as many rows needed to hold the new element. The new
               element is placed in the proper field of the last row, and
               all other field elements have invalid data. All fields of
               the new rows up to the new element's row will also contain
               invalid data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle"),
                   Parameter('row', type=Type.INT32_T,
                             doc="Row of element to set"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column of element to set"),
                   Parameter('val', type=Type.INT32_T,
                             doc="Value to set")
               ]),

        Method('SetReal_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets an real value into a table element.",
               notes="""
               The table field containing the element to be set MUST be
               of type :const:`GS_FLOAT` or :const:`GS_DOUBLE`.
               If the field is :const:`GS_FLOAT` the new data value will cause an
               overflow if the value is out of range of the data type.
               The new element value will then be invalid.
               
               If the row of the new element exceeds the number of rows in
               the table, then the table will AUTOMATICALLY be EXPANDED to
               exactly as many rows needed to hold the new element. The new
               element is placed in the proper field of the last row, and
               all other field elements have invalid data. All fields of
               the new rows up to the new element's row will also contain
               invalid data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle"),
                   Parameter('row', type=Type.INT32_T,
                             doc="Row of element to set"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column of element to set"),
                   Parameter('val', type=Type.DOUBLE,
                             doc="Value to set")
               ]),

        Method('SetString_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets a string value into a table element.",
               notes="""
               The table field containing the element to be set MUST be
               of 'string'.
               
               If the row of the new element exceeds the number of rows in
               the table, then the table will AUTOMATICALLY be EXPANDED to
               exactly as many rows needed to hold the new element. The new
               element is placed in the proper field of the last row, and
               all other field elements have invalid data. All fields of
               the new rows up to the new element's row will also contain
               invalid data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('tb', type="TB",
                             doc="Table handle"),
                   Parameter('row', type=Type.INT32_T,
                             doc="Row of element to set"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column of element to set"),
                   Parameter('val', type=Type.STRING,
                             doc="Value to set")
               ]),

        Method('Sort_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sorts a table by a specified column.",
               notes="""
               If the column to sort by contains duplicated values, the
               sorted table is NOT guaranteed to retain the ordering of
               the duplicated values/
               E.g. Given 2 rows of values:   xx   yy   1
               bb   aa   1
               If the table is sorted on column 3, the second row
               may or may not come after the first row in the sorted
               table.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('tb', type="TB",
                             doc=":class:`TB` handle"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Index of data Column to sort table by")
               ])
    ]
}

