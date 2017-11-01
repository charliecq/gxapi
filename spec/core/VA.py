from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('VA',
                 doc="""
                 The :class:`VA` class is the 2-Dimensional analogue to the :class:`VV` class.
                 When displayed in a database, :class:`VA` objects are displayed graphically
                 as profiles, one to a cell, and can also be displayed one column of
                 data at a time by specifying an index; e.g. CH[0]. A :class:`VA` object is
                 declared with a fixed number of columns, which cannot be altered.
                 The number of rows, however can be changed, in the same way that
                 the length of a :class:`VV` can be changed. Data can be added or extracted
                 using VVs, either by row or column.
                 
                 A :class:`VA` is used to store an array of data in which each element may have
                 multiple elements.  For example, 256-channel radiometric data can
                 be stored in a :class:`VA` that is 256 elements wide.
                 """)


gx_defines = [
    Define('VA_AVERAGE',
           doc=":class:`VA` Object to average",
           constants=[
               Constant('VA_AVERAGE_ROWS', value='0', type=Type.INT32_T,
                        doc="Average the Rows"),
               Constant('VA_AVERAGE_COLUMNS', value='1', type=Type.INT32_T,
                        doc="Average the Columns")
           ]),

    Define('VA_OBJECT',
           doc=":class:`VA` Object to select",
           constants=[
               Constant('VA_ROW', value='0', type=Type.INT32_T,
                        doc="Row"),
               Constant('VA_COL', value='1', type=Type.INT32_T,
                        doc="Column")
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('iGetArray_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, 
               doc="Get an array of data from a :class:`VA`.",
               return_type=Type.VOID,
               return_doc="Nothing",
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` object"),
                   Parameter('start_row', type=Type.INT32_T, is_val=True,
                             doc="Starting Row"),
                   Parameter('start_col', type=Type.INT32_T, is_val=True,
                             doc="Starting Column"),
                   Parameter('rows', type=Type.INT32_T, is_val=True,
                             doc="# rows"),
                   Parameter('cols', type=Type.INT32_T, is_val=True,
                             doc="# cols"),
                   Parameter('data', type="void*",
                             doc="Data buffer to copy :class:`VA` data into"),
                   Parameter('gs_type', type=Type.INT32_T, is_val=True,
                             doc=":def:`GS_TYPES`")
               ]),

        Method('iSetArray_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, 
               doc="Set a range of data in an array",
               return_type=Type.VOID,
               return_doc="Nothing",
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` object"),
                   Parameter('start_row', type=Type.INT32_T, is_val=True,
                             doc="Starting Row"),
                   Parameter('start_col', type=Type.INT32_T, is_val=True,
                             doc="Starting Column"),
                   Parameter('rows', type=Type.INT32_T, is_val=True,
                             doc="# rows"),
                   Parameter('cols', type=Type.INT32_T, is_val=True,
                             doc="# cols"),
                   Parameter('data', type="const void*",
                             doc="Data buffer to copy into :class:`VA`"),
                   Parameter('gs_type', type=Type.INT32_T, is_val=True,
                             doc=":def:`GS_TYPES`")
               ]),

        Method('AddElevationsVVToDepths_VA', module='geoengine.core', version='7.2.0',
               availability=Availability.LICENSED, 
               doc="Add one :class:`VV` value to each row of the :class:`VA`, output true elevation.",
               notes="""
               Adds each value in an input elevation :class:`VV` to all the values at
               the same fid in a depths :class:`VA`. Includes an option for negative depths down
               (e.g. a relative level).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` handle (modified)"),
                   Parameter('vv', type="VV",
                             doc="Elevations to add"),
                   Parameter('negative_depths', type=Type.INT32_T,
                             doc="Use negative :class:`VA` depths (0:No, 1:Yes)?")
               ]),

        Method('Append_VA', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Appends VAs",
               notes="""
               If the VAs have different numbers of columns, the smaller number
               is used in the copy operation.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA"),
                   Parameter('v_aa', type="VA",
                             doc=":class:`VA` to append")
               ]),

        Method('Average_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Average elements in a :class:`VA` by row or column",
               notes="""
               The output :class:`VV` will be dimensioned by the number of
               rows or columns in the input :class:`VV` depending on the
               :def:`VA_AVERAGE` setting.
               
               Dummies are not included in the average.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` to window"),
                   Parameter('vv', type="VV",
                             doc=":class:`VV` in which to place average results"),
                   Parameter('rc', type=Type.INT32_T,
                             doc=":def:`VA_AVERAGE`")
               ]),

        Method('Copy_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy one :class:`VA` to another.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('v_ad', type="VA",
                             doc="destination"),
                   Parameter('v_as', type="VA",
                             doc="source")
               ]),

        Method('Copy2_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy part of a vector into part of another vector.",
               notes="""
               1. Unlike :func:`Copy_VA` destination :class:`VA` is not reallocated, nor are
               the dimensions changed. The caller must make any desired changes.
               
               2. All :class:`VA` types are supported and will be converted using
               Convert_GS if necessary.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('v_ad', type="VA",
                             doc="Destination :class:`VA`"),
                   Parameter('d_row', type=Type.INT32_T,
                             doc="Destination start row"),
                   Parameter('d_col', type=Type.INT32_T,
                             doc="Destination start column"),
                   Parameter('v_as', type="VA",
                             doc="Source :class:`VA` (can be the same as Destination)"),
                   Parameter('s_row', type=Type.INT32_T,
                             doc="Source start row"),
                   Parameter('s_col', type=Type.INT32_T,
                             doc="Source start column"),
                   Parameter('rows', type=Type.INT32_T,
                             doc="Number of rows"),
                   Parameter('cols', type=Type.INT32_T,
                             doc="Number of columns")
               ]),

        Method('Create_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`VA`.",
               return_type="VA",
               return_doc=":class:`VA` Object",
               parameters = [
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GEO_VAR`"),
                   Parameter('rows', type=Type.INT32_T,
                             doc="Maximum number of rows in the :class:`VA`, >= 0"),
                   Parameter('cols', type=Type.INT32_T,
                             doc="Number of columns in the :class:`VA`, > 0")
               ]),

        Method('CreateExt_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`VA`, using one of the :def:`GS_TYPES` special data types.",
               notes="See :func:`Create_VV`",
               return_type="VA",
               return_doc=":class:`VA`, aborts if creation fails",
               parameters = [
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`"),
                   Parameter('rows', type=Type.INT32_T,
                             doc="Maximum number of rows in the :class:`VA`, >= 0"),
                   Parameter('cols', type=Type.INT32_T,
                             doc="Number of columns in the :class:`VA`, > 0")
               ]),

        Method('CreateVV_VA', module='geoengine.core', version='7.2.1',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`VA` using the data in a :class:`VV`.",
               notes="See :func:`Create_VV`",
               return_type="VA",
               return_doc=":class:`VA`, aborts if creation fails",
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` with the data"),
                   Parameter('rows', type=Type.INT32_T,
                             doc="# of rows"),
                   Parameter('columns', type=Type.INT32_T,
                             doc="# of columns")
               ]),

        Method('Destroy_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`VA`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` to destroy.")
               ]),

        Method('GetFullVV_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the full :class:`VV` from the :class:`VA`.",
               notes="""
               No data is copied, this is the handle to the data :class:`VV` in the :class:`VA`.
               The fid start/increment of the :class:`VA` is passed to the :class:`VV` at the time
               of the call.  If a new :class:`VA` is read, you must call GetFull_VV_VA
               to get the new fid in the :class:`VV`.
               """,
               return_type="VV",
               return_doc=":class:`VV` Object",
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` object")
               ]),

        Method('GetVV_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a row or column of data as a :class:`VV` from an array.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` handle"),
                   Parameter('no', type=Type.INT32_T,
                             doc="Row or Column # (0 is first)"),
                   Parameter('row_col', type=Type.INT32_T,
                             doc=":def:`VA_OBJECT`"),
                   Parameter('vv', type="VV",
                             doc=":class:`VV` in which to place data")
               ]),

        Method('iCol_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return number of columns in :class:`VA`",
               notes=":func:`iLen_VA` returns the number of rows.",
               return_type=Type.INT32_T,
               return_doc="Columns in :class:`VA`",
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` object")
               ]),

        Method('iGetInt_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get an integer element from a :class:`VA`.",
               notes="""
               Type conversions are performed if necessary.  Dummy values
               are converted to "*" string.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               Element wanted, :def_val:`rDUMMY`, :def_val:`iDUMMY` or blank string
               if the value is dummy or outside of the range of data.
               """,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA`, element want"),
                   Parameter('row', type=Type.INT32_T,
                             doc="Row"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column")
               ]),

        Method('IGetString_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a string element from a :class:`VA`.",
               notes="""
               Returns element wanted, :def_val:`rDUMMY`, :def_val:`iDUMMY` or blank string
               if the value is dummy or outside of the range of data.
               
               Type conversions are performed if necessary.  Dummy values
               are converted to "*" string.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA`, element wanted"),
                   Parameter('row', type=Type.INT32_T,
                             doc="Row"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column"),
                   Parameter('str_val', type=Type.STRING, is_ref=True, size_of_param='str_size',
                             doc="String in which to place element"),
                   Parameter('str_size', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Maximum length of the string")
               ]),

        Method('iLen_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return length (number of rows) in a :class:`VA`.",
               notes=":func:`iCol_VA` returns the number of columns.",
               return_type=Type.INT32_T,
               return_doc="Length of :class:`VA`",
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` object")
               ]),

        Method('IndexOrder_VA', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Reorder a :class:`VA` based on an index :class:`VV`",
               notes="""
               Given a row index :class:`VV` (of type INT), this method reorders a
               :class:`VA`. Please make sure that the index holds valid information.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc="Index :class:`VV` of type INT"),
                   Parameter('va', type="VA",
                             doc=":class:`VA` to order")
               ]),

        Method('LookupIndex_VA', module='geoengine.core', version='6.4.2',
               availability=Availability.LICENSED, 
               doc="Lookup a :class:`VA` from another :class:`VA` using an index :class:`VV`.",
               notes="""
               Fractional values in the :class:`VV` will interpolate between the value
               at the whole integer value and the next whole integer, dummy
               if outside the :class:`VA`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vad', type="VA",
                             doc="Original Data :class:`VA` (numeric)"),
                   Parameter('vvi', type="VV",
                             doc="Index :class:`VV` of REAL"),
                   Parameter('var', type="VA",
                             doc=":class:`VA` to output results (same type as Data :class:`VA`)")
               ]),

        Method('RangeDouble_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Computes the minimum and maximum range of the data, in doubles,
               in a vector while ignoring dummies.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` object"),
                   Parameter('min', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum value - returned"),
                   Parameter('max', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum value - returned")
               ]),

        Method('ReFid_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Re-sample a :class:`VA` to a new fid start/icrement",
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VV` to resample"),
                   Parameter('start', type=Type.DOUBLE,
                             doc="New fid start"),
                   Parameter('incr', type=Type.DOUBLE,
                             doc="New fid increment"),
                   Parameter('length', type=Type.INT32_T,
                             doc="New length")
               ]),

        Method('Reverse_VA', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Reverses the order of the rows in a :class:`VA`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` to reverse")
               ]),

        Method('rGetFidIncr_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the Fiducial increment from a :class:`VA`",
               return_type=Type.DOUBLE,
               return_doc="Fiducial increment of the :class:`VA`.",
               parameters = [
                   Parameter('va', type="VA")
               ]),

        Method('rGetFidStart_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the Fiducial start from a :class:`VA`",
               return_type=Type.DOUBLE,
               return_doc="Fiducial start of the :class:`VA`.",
               parameters = [
                   Parameter('va', type="VA")
               ]),

        Method('rGetReal_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a real element from a :class:`VA`.",
               notes="""
               Type conversions are performed if necessary.  Dummy values
               are converted to "*" string.
               """,
               return_type=Type.DOUBLE,
               return_doc="""
               Element wanted, :def_val:`rDUMMY`, :def_val:`iDUMMY` or blank string
               if the value is dummy or outside of the range of data.
               """,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA`, element want"),
                   Parameter('row', type=Type.INT32_T,
                             doc="Row"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column")
               ]),

        Method('SetFidIncr_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the Fiducial increment of a :class:`VA`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` to set fiducial increment of"),
                   Parameter('incr', type=Type.DOUBLE,
                             doc="New increment")
               ]),

        Method('SetFidStart_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the Fiducial start of a :class:`VA`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` to set fiducial start of"),
                   Parameter('start', type=Type.DOUBLE,
                             doc="New start")
               ]),

        Method('SetInt_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set an integer element in a :class:`VA`.",
               notes="""
               Element being set cannot be < 0.
               If the element is > current :class:`VA` length, the :class:`VA` length is
               increased.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA`, element want"),
                   Parameter('row', type=Type.INT32_T,
                             doc="Row"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column"),
                   Parameter('value', type=Type.INT32_T,
                             doc="Value to set")
               ]),

        Method('SetLn_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the length (number of rows) of the :class:`VA`",
               notes="""
               The number of columns in a :class:`VA` is fixed, and cannot be
               altered once the :class:`VA` is created.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA"),
                   Parameter('rows', type=Type.INT32_T,
                             doc="Length")
               ]),

        Method('SetReal_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a real element in a :class:`VA`.",
               notes="""
               Element being set cannot be < 0.
               If the element is > current :class:`VA` length, the :class:`VA` length is
               increased.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA`, element want"),
                   Parameter('row', type=Type.INT32_T,
                             doc="Row"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column"),
                   Parameter('value', type=Type.DOUBLE,
                             doc="Value to set")
               ]),

        Method('SetString_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a string element in a :class:`VA`.",
               notes="""
               Element being set cannot be < 0.
               If the element is > current :class:`VA` length, the :class:`VA` length is
               increased.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA`, element wanted"),
                   Parameter('row', type=Type.INT32_T,
                             doc="Row"),
                   Parameter('col', type=Type.INT32_T,
                             doc="Column"),
                   Parameter('value', type=Type.STRING,
                             doc="String to set")
               ]),

        Method('SetVV_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a row or column of data in an array from a :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` handle"),
                   Parameter('no', type=Type.INT32_T,
                             doc="Row or Column # (0 is first)"),
                   Parameter('row_col', type=Type.INT32_T,
                             doc=":def:`VA_OBJECT`"),
                   Parameter('vv', type="VV",
                             doc=":class:`VV` from which to get data")
               ]),

        Method('Trans_VA', module='geoengine.core', version='7.2.0',
               availability=Availability.LICENSED, 
               doc="Translate (:class:`VA` + base ) * mult",
               notes="Supports all :class:`VA` types using an internal double :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` handle"),
                   Parameter('base', type=Type.DOUBLE,
                             doc="Base value"),
                   Parameter('mult', type=Type.DOUBLE,
                             doc="Mult value")
               ]),

        Method('Window_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Window a :class:`VA` to a :class:`VV` based in intergral frame",
               notes="""
               The defined window must be within the :class:`VA` element dimensions.
               The windowed result will be the simple sum of all
               values in the window.
               If any values are dummy, the result will be dummy.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` to window"),
                   Parameter('start', type=Type.INT32_T,
                             doc="First element in the window"),
                   Parameter('count', type=Type.INT32_T,
                             doc="Number of elements in the window"),
                   Parameter('vv', type="VV",
                             doc=":class:`VV` in which to place results")
               ]),

        Method('Window2_VA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Window a :class:`VA` to a :class:`VV` based on fractional frame",
               notes="""
               The defined window must be within the :class:`VA` element dimensions.
               The windowed result will be the simple sum of all
               values in the window.
               If any values are dummy, the result will be dummy.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` to window"),
                   Parameter('start', type=Type.DOUBLE,
                             doc="Start point (from 0.0)"),
                   Parameter('end', type=Type.DOUBLE,
                             doc="End point (< :class:`VA` elements - 1.0)"),
                   Parameter('vv', type="VV",
                             doc=":class:`VV` in which to place results")
               ]),

        Method('iCheckForRepeating_VA', module='geoengine.core', version='8.2.0',
               availability=Availability.LICENSED, 
               doc="Window a :class:`VA` to a :class:`VV` based on fractional frame",
               notes="""
               Returns 1 if all rows contain values which match the input values.
               Optionally, row values can be offset by amounts specified with a secondary :class:`VV`.
               This function was designed to detect "depth" array channels, including those which might
               have been offset with topography on each row.
               An absolute tolerance can be specified to ignore numerical noise.
               """,
               return_type=Type.INT32_T,
               return_doc="1 if rows repeat, 0 if not.",
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` to check"),
                   Parameter('vv_t', type="VV",
                             doc="Items to test for repeats (length equal to the number of columns in the :class:`VA`)"),
                   Parameter('subtract_vv', type=Type.INT32_T,
                             doc="If set to 1, subtract single values in the following :class:`VV` from every array row item before testing (e.g. an elevation value)"),
                   Parameter('vv_sub', type="VV",
                             doc="Values to subtract from each row before doing the comparison test (length equal to the length of the :class:`VA`). Can be VV_NULL (-1) if above subtraction parameter is zero"),
                   Parameter('tol', type=Type.DOUBLE,
                             doc="Comparison tolerance - set to zero or dummy for exact match")
               ]),

        Method('iCheckForRepeating2_VA', module='geoengine.core', version='8.2.0',
               availability=Availability.LICENSED, 
               doc="Window a :class:`VA` to a :class:`VV` based on fractional frame",
               notes="""
               Returns 1 if all rows contain values which match the input values.
               Optionally, row values can be offset by amounts specified with a secondary :class:`VV`.
               This function was designed to detect "depth" array channels, including those which might
               have been offset with topography on each row.
               An absolute tolerance can be specified to ignore numerical noise.
               This version returns the row and column index of first mismatch.
               """,
               return_type=Type.INT32_T,
               return_doc="1 if rows repeat, 0 if not.",
               parameters = [
                   Parameter('va', type="VA",
                             doc=":class:`VA` to check"),
                   Parameter('vv_t', type="VV",
                             doc="Items to test for repeats (length equal to the number of columns in the :class:`VA`)"),
                   Parameter('subtract_vv', type=Type.INT32_T,
                             doc="If set to 1, subtract single values in the following :class:`VV` from every array row item before testing (e.g. an elevation value)"),
                   Parameter('vv_sub', type="VV",
                             doc="Values to subtract from each row before doing the comparison test (length equal to the length of the :class:`VA`). Can be VV_NULL (-1) if above subtraction parameter is zero"),
                   Parameter('tol', type=Type.DOUBLE,
                             doc="Comparison tolerance - set to zero or dummy for exact match"),
                   Parameter('bad_row', type=Type.INT32_T, is_ref=True,
                             doc="Row index of first mismatch"),
                   Parameter('bad_col', type=Type.INT32_T, is_ref=True,
                             doc="Column index of first mismatch")
               ])
    ]
}

