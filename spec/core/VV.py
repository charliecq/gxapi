from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('VV',
                 doc="""
                 The :class:`VV` class stores very long vector (array) data (such
                 as channel data from an OASIS database) in memory and
                 performs specific actions on the data. This set of
                 functions is similar to the :class:`VM` functions except that
                 you cannot access data directly and therefore you cannot
                 use a :class:`VV` to pass data to an external (non-Geosoft)
                 Dynamic Link Library (DLL) object function.
                 
                 If you want to pass data to a DLL, you must move a subset
                 of the data stored in memory to a small vector object and
                 then use the :func:`GetPtrVM_GEO` function to pass a pointer to the
                 data on to the external function.
                 
                 See :class:`VVU` for more utility methods.
                 """)


gx_defines = [
    Define('VV_DOUBLE_CRC_BITS',
           doc="Number of bits to use in double CRC's",
           constants=[
               Constant('VV_DOUBLE_CRC_BITS_EXACT', value='0', type=Type.INT32_T,
                        doc="Exact CRC"),
               Constant('VV_DOUBLE_CRC_BITS_DEFAULT', value='10', type=Type.INT32_T,
                        doc="Default inaccuracy in double (10 Bits)"),
               Constant('VV_DOUBLE_CRC_BITS_MAX', value='51', type=Type.INT32_T,
                        doc="Maximum number of inaccuracy bits")
           ]),

    Define('VV_FLOAT_CRC_BITS',
           doc="Number of bits to use in float CRC's",
           constants=[
               Constant('VV_FLOAT_CRC_BITS_EXACT', value='0', type=Type.INT32_T,
                        doc="Exact CRC"),
               Constant('VV_FLOAT_CRC_BITS_DEFAULT', value='7', type=Type.INT32_T,
                        doc="Default inaccuracy in floats (7 Bits)"),
               Constant('VV_FLOAT_CRC_BITS_MAX', value='22', type=Type.INT32_T,
                        doc="Maximum number of inaccuracy bits")
           ]),

    Define('VV_LOG_BASE',
           doc="Type of log to use",
           constants=[
               Constant('VV_LOG_BASE_10', value='0', type=Type.INT32_T,
                        doc="Base 10"),
               Constant('VV_LOG_BASE_E', value='1', type=Type.INT32_T,
                        doc="Base e")
           ]),

    Define('VV_LOG_NEGATIVE',
           doc="Ways to handle negatives",
           constants=[
               Constant('VV_LOG_NEGATIVE_NO', value='0', type=Type.INT32_T,
                        doc="Dummies out value less than the minimum."),
               Constant('VV_LOG_NEGATIVE_YES', value='1', type=Type.INT32_T,
                        doc="""
                        if the data is in the range +/- minimum,
                        it is left alone.  Otherwise, the data
                        is divided by the minimum, the log is
                        applied, the minimum is added and the
                        sign is reapplied. Use :func:`_LogLinear_VV` function
                        if decades in results are required.
                        """)
           ]),

    Define('VV_LOOKUP',
           doc="Lookup style",
           constants=[
               Constant('VV_LOOKUP_EXACT', value='0', type=Type.INT32_T,
                        doc="Only exact matches are used"),
               Constant('VV_LOOKUP_NEAREST', value='1', type=Type.INT32_T,
                        doc="Nearest match is used (regardless of sampling range)"),
               Constant('VV_LOOKUP_INTERPOLATE', value='2', type=Type.INT32_T,
                        doc="Interpolate between values (regardless of sampling range)"),
               Constant('VV_LOOKUP_NEARESTCLOSE', value='3', type=Type.INT32_T,
                        doc="Use nearest match only if within sampling range"),
               Constant('VV_LOOKUP_INTERPCLOSE', value='4', type=Type.INT32_T,
                        doc="Interpolate only if within sampling range")
           ]),

    Define('VV_MASK',
           doc="Where to mask",
           constants=[
               Constant('VV_MASK_INSIDE', value='0', type=Type.INT32_T),
               Constant('VV_MASK_OUTSIDE', value='1', type=Type.INT32_T)
           ]),

    Define('VV_ORDER',
           doc="Specify if the data is montonically increasing or decreasing.",
           constants=[
               Constant('VV_ORDER_NONE', value='0', type=Type.INT32_T,
                        doc="There is no specific data size ordering in the :class:`VV`."),
               Constant('VV_ORDER_INCREASING', value='1', type=Type.INT32_T,
                        doc="Every value is greater than or equal to the previous value."),
               Constant('VV_ORDER_DECREASING', value='2', type=Type.INT32_T,
                        doc="Every value is less than or equal to the previous value.")
           ]),

    Define('VV_SORT',
           doc="Sort order",
           constants=[
               Constant('VV_SORT_ASCENDING', value='0', type=Type.INT32_T),
               Constant('VV_SORT_DESCENDING', value='1', type=Type.INT32_T)
           ]),

    Define('VV_WINDOW',
           doc="How to handle :class:`VV` limits",
           constants=[
               Constant('VV_WINDOW_DUMMY', value='0', type=Type.INT32_T,
                        doc="Dummy values outside the limits"),
               Constant('VV_WINDOW_LIMIT', value='1', type=Type.INT32_T,
                        doc="Set values outside the limits to the limits")
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('iGetData_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, 
               doc="Copy data from user memory to a :class:`VV`",
               return_type=Type.VOID,
               return_doc="Nothing",
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` object"),
                   Parameter('start', type=Type.INT32_T, is_val=True,
                             doc="Start Location"),
                   Parameter('elements', type=Type.INT32_T, is_val=True,
                             doc="Number of Elements"),
                   Parameter('data', type="void*",
                             doc="Data buffer copy data into from :class:`VV`"),
                   Parameter('gs_type', type=Type.INT32_T, is_val=True,
                             doc=":def:`GS_TYPES`")
               ]),

        Method('iSetData_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, 
               doc="Copy data from user memory to a :class:`VV`",
               return_type=Type.VOID,
               return_doc="Nothing",
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` object"),
                   Parameter('start', type=Type.INT32_T, is_val=True,
                             doc="Start Location"),
                   Parameter('elements', type=Type.INT32_T, is_val=True,
                             doc="Number of Elements"),
                   Parameter('data', type="const void*",
                             doc="Data buffer to copy into into :class:`VV`"),
                   Parameter('gs_type', type=Type.INT32_T, is_val=True,
                             doc=":def:`GS_TYPES`")
               ]),

        Method('_Copy_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy one :class:`VV` to another.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_d', type="VV",
                             doc="Destination"),
                   Parameter('vv_s', type="VV",
                             doc="Source")
               ]),

        Method('_Copy2_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy part of a vector into part of another vector.",
               notes="""
               1. Unlike Copy_VV destination :class:`VV` is not reallocated, nor is
               the length changed. The caller must make any desired changes.
               
               2. All :class:`VV` types are supported and will be converted using
               Convert_GS if necessary.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_d', type="VV",
                             doc="Destination :class:`VV`"),
                   Parameter('dest', type=Type.INT32_T,
                             doc="Destination start element"),
                   Parameter('vv_s', type="VV",
                             doc="Source :class:`VV` (can be the same as Destination)"),
                   Parameter('source', type=Type.INT32_T,
                             doc="Source start element"),
                   Parameter('n', type=Type.INT32_T,
                             doc="Number of points")
               ]),

        Method('_Log_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Apply log to the vv.",
               notes="""
               Minimum value will be defaulted to 1.0 if it is 0.0 or
               less than 0.0
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` handle"),
                   Parameter('log_base', type=Type.INT32_T,
                             doc=":def:`VV_LOG_BASE`"),
                   Parameter('log_neg', type=Type.INT32_T,
                             doc=":def:`VV_LOG_NEGATIVE`"),
                   Parameter('log_min', type=Type.DOUBLE,
                             doc="Minimum value for :def:`VV_LOG_NEGATIVE`")
               ]),

        Method('_LogLinear_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Take the log10 or original value of a :class:`VV`.",
               notes="""
               If the data is in the range +/- minimum value,
               it is left alone. Otherwise, the result is calculated as
               
               ::

                    d = dMin * (log10(fabs(d)/dMin)+1.0)
               
               Sign is reapplied to d.
               
               Minimum value will be defaulted to 1.0 if it is negative
               or 0.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` handle"),
                   Parameter('log_min', type=Type.DOUBLE,
                             doc="Minimum value")
               ]),

        Method('_Mask_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Mask one :class:`VV` against another.",
               notes="""
               All elements in the mask :class:`VV` that are dummies will replace
               the value in the original :class:`VV` with a dummy.
               
               The modified :class:`VV` will always be the same length as the mask
               :class:`VV` after this call.  If the mask is longer than the target,
               the target will be lengthenned with dummies.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc="Data :class:`VV` to be masked"),
                   Parameter('vv_m', type="VV",
                             doc="Mask :class:`VV`")
               ]),

        Method('_Reverse_VV', module='geoengine.core', version='5.1.3',
               availability=Availability.LICENSED, 
               doc="Reverses the order of the data in a :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc="Data :class:`VV`")
               ]),

        Method('_Serial_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Serialize",
               return_type=Type.VOID,
               parameters = [
                   Parameter('gvv', type="VV"),
                   Parameter('bf', type="BF")
               ]),

        Method('_Trans_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Translate (:class:`VV` + base ) * mult",
               notes="All :class:`VV` types now supported.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` handle"),
                   Parameter('base', type=Type.DOUBLE,
                             doc="Base value"),
                   Parameter('mult', type=Type.DOUBLE,
                             doc="Mult value")
               ]),

        Method('Abs_VV', module='geoengine.core', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Take the absolute value of values in a :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV")
               ]),

        Method('Add_VV', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Add two VVs: VV_A + VV_B = VV_C",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_x', type="VV",
                             doc=":class:`VV` A"),
                   Parameter('vv_y', type="VV",
                             doc=":class:`VV` B"),
                   Parameter('vv_z', type="VV",
                             doc=":class:`VV` C (returned), C = A + B")
               ]),

        Method('Add2_VV', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Add two VVs with linear factors: VV_A*f1 + VV_B*f2 = VV_C",
               notes="The multipliers must be defined and within the :def_val:`GS_R8MN` :def_val:`GS_R8MX` range.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_x', type="VV",
                             doc=":class:`VV` A"),
                   Parameter('f1', type=Type.DOUBLE,
                             doc="Multiplier f1 for A"),
                   Parameter('vv_y', type="VV",
                             doc=":class:`VV` B"),
                   Parameter('f2', type=Type.DOUBLE,
                             doc="Multiplier f2 for B"),
                   Parameter('vv_z', type="VV",
                             doc=":class:`VV` C (returned), C = A*f1 + B*f2")
               ]),

        Method('Append_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Appends :class:`VV`'s",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('vv_a', type="VV",
                             doc=":class:`VV` to append")
               ]),

        Method('CopyVMtoVV_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_cpp=True, 
               doc="Copy :class:`VM` data to a :class:`VV`.",
               notes="The :class:`VV` will be resized to the length of the :class:`VM`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc="Destination :class:`VV`, will be resized to length of the :class:`VM`"),
                   Parameter('vm', type="VM",
                             doc="Source :class:`VM`")
               ]),

        Method('CopyVVtoVM_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_cpp=True, 
               doc="Copy :class:`VV` data to a :class:`VM`.",
               notes="""
               The :class:`VM` will be resized to the length of the :class:`VV`.
               The pointer to data in the :class:`VM` may move.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vm', type="VM",
                             doc="Destination :class:`VM`, will be resized to length of the :class:`VV`"),
                   Parameter('vv', type="VV",
                             doc="Source :class:`VV`")
               ]),

        Method('CRC_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Compute the CRC value of a :class:`VV`.",
               return_type="CRC",
               return_doc="CRC Value",
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('pul_crc', type="CRC",
                             doc="Previous CRC :def_val:`CRC_INIT_VALUE`")
               ]),

        Method('CRCInexact_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Compute the CRC value of a :class:`VV` and allows you to specify
               number of bits of floats/doubles to drop so that the CRC
               will be same even of this are changed.
               """,
               notes="""
               Very useful for testing where the last bits of accuracy
               are not as important.
               """,
               return_type="CRC",
               return_doc="CRC Value",
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('pul_crc', type="CRC",
                             doc="Previous CRC :def_val:`CRC_INIT_VALUE`"),
                   Parameter('float_bits', type=Type.INT32_T,
                             doc=":def:`VV_FLOAT_CRC_BITS`"),
                   Parameter('double_bits', type=Type.INT32_T,
                             doc=":def:`VV_DOUBLE_CRC_BITS`")
               ]),

        Method('Create_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`VV`.",
               notes="""
               To set the fiducial start and increment for the data in the :class:`VV`
               you need to call :func:`SetFidStart_VV` and :func:`SetFidIncr_VV`.
               
               If you are basing the :class:`VV` data on fiducial information from a
               different :class:`VV`, call GetFidStart_VV and GetFidIncr_VV to obtain
               that :class:`VV`'s fiducial information. Do this prior to setting the
               new :class:`VV`'s fiducial start and increment.
               
               If you do not know the required length for a :class:`VV`, use 0
               and the :class:`VV` length will be adjusted as needed.  This is
               a bit less efficient than setting the length when you
               know it.
               """,
               return_type="VV",
               return_doc=":class:`VV` Object",
               parameters = [
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GEO_VAR`"),
                   Parameter('elements', type=Type.INT32_T,
                             doc="Maximum number of elements in the :class:`VV`, >= 0")
               ]),

        Method('CreateExt_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`VV`, using one of the :def:`GS_TYPES` special data types.",
               notes="""
               See :func:`Create_VV`
               
               Do not use data type flags: :def_val:`GS_INT` or :def_val:`GS_REAL`,
               this will result in a respective data type of unsigned byte or
               short for the :class:`VV`.
               """,
               return_type="VV",
               return_doc=":class:`VV` Object",
               parameters = [
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`"),
                   Parameter('elements', type=Type.INT32_T,
                             doc="Maximum number of elements in the :class:`VV`, >= 0")
               ]),

        Method('CreateS_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`VV`  from serialized source.",
               return_type="VV",
               return_doc=":class:`VV` Object",
               parameters = [
                   Parameter('bf', type="BF")
               ]),

        Method('Destroy_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to destroy.")
               ]),

        Method('Diff_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate differences.",
               notes="""
               Differences with dummies result in dummies.
               An even number of differences locates data accurately.
               An odd number of differences locates result 1/2 element lower
               in the :class:`VV`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to be processed"),
                   Parameter('n', type=Type.INT32_T,
                             doc="Number of differences")
               ]),

        Method('Divide_VV', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Divide one :class:`VV` by another: VV_A / VV_B = VV_C",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_x', type="VV",
                             doc=":class:`VV` A"),
                   Parameter('vv_y', type="VV",
                             doc=":class:`VV` B"),
                   Parameter('vv_z', type="VV",
                             doc=":class:`VV` C (returned), C = A / B")
               ]),

        Method('FidNorm_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Re-sample a pair of :class:`VV`'s to match each other.",
               notes="""
               Both :class:`VV`'s will return with the same start
               fid and fid increment.  The smaller start fid
               and fid increment will be used.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv1', type="VV",
                             doc=":class:`VV` to resample"),
                   Parameter('vv2', type="VV",
                             doc=":class:`VV` to resample")
               ]),

        Method('FillInt_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Fill a :class:`VV` with an int value.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('int', type=Type.INT32_T,
                             doc="Value to fill with")
               ]),

        Method('FillReal_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Fill a :class:`VV` with a real value.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('val', type=Type.DOUBLE,
                             doc="Value to fill with")
               ]),

        Method('FillString_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Fill a :class:`VV` with a string value.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('str_val', type=Type.STRING,
                             doc="String")
               ]),

        Method('GetVM_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_cpp=True, 
               doc="Get :class:`VV` data and place it in a :class:`VM`. (OBSOLETE)",
               notes="""
               See :func:`CopyVVtoVM_VV`, which is a prefered method to move :class:`VV` data
               into a :class:`VM`.  This method is mainly provided for old compatibility.
               
               The :class:`VM` will be lengthened if required.
               
               If the :class:`VM` is longer than required, extra data past the end
               of the :class:`VV` will be set to dummy in the :class:`VM`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` from which to read data"),
                   Parameter('vm', type="VM",
                             doc=":class:`VM` in which to place the data"),
                   Parameter('loc', type=Type.INT32_T,
                             doc="Start :class:`VV` location of data to get, 0 is first.")
               ]),

        Method('iCountDummies_VV', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Count the number of dummies in a :class:`VV`",
               return_type=Type.INT32_T,
               return_doc="The count",
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to search"),
                   Parameter('start', type=Type.INT32_T,
                             doc="Starting point in :class:`VV` (0 for all)"),
                   Parameter('elem', type=Type.INT32_T,
                             doc="Number of elements to process (-1 for all)")
               ]),

        Method('iFindDum_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Finds the first dummy or non-dummy value in a :class:`VV`",
               notes="""
               If a decreasing order search is performed, it will start
               at the highest element specified. (Conversely, an increasing
               order starts at the lowest element specified.)
               """,
               return_type=Type.INT32_T,
               return_doc="""
               The index of the first dummy or non-dummy value.
               -1 if not found, 0 if the length of the :class:`VV` is 0.
               """,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to search"),
                   Parameter('start', type=Type.INT32_T,
                             doc="Lowest element in :class:`VV` element to search"),
                   Parameter('end', type=Type.INT32_T,
                             doc="Highest element in :class:`VV` to search"),
                   Parameter('yn', type=Type.INT32_T,
                             doc="0 = find first dummy / 1 = find first non-dummy"),
                   Parameter('order', type=Type.INT32_T,
                             doc="0 = use increasing order / 1 = use decreasing order")
               ]),

        Method('iGetFidExpansion_VV', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Gets the Fiducial expansion from a :class:`VV`",
               return_type=Type.INT32_T,
               return_doc="Number of expanions for this :class:`VV` (see :func:`ReFidVV_VV`)",
               parameters = [
                   Parameter('vv', type="VV")
               ]),

        Method('iGetInt_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get an integer element from a :class:`VV`.",
               return_type=Type.INT32_T,
               return_doc="""
               Element wanted, or :def_val:`iDUMMY`
               if the value is dummy or outside of the range of data.
               """,
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('element', type=Type.INT32_T,
                             doc="Element wanted")
               ]),

        Method('IGetString_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a string element from a :class:`VV`.",
               notes="""
               Returns Element wanted, or blank string
               if the value is dummy or outside of the range of data.
               
               Type conversions are performed if necessary.  Dummy values
               are converted to "*" string.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('element', type=Type.INT32_T,
                             doc="Element wanted"),
                   Parameter('str_val', type=Type.STRING, is_ref=True, size_of_param='str_size',
                             doc="String in which to place element"),
                   Parameter('str_size', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Maximum length of the string")
               ]),

        Method('iIndexMax_VV', module='geoengine.core', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Get the index where the maximum value occurs.",
               notes="""
               If more than one value has the same maximum value, the index of the
               first is returned.
               """,
               return_type=Type.INT32_T,
               return_doc="Index of the maximum value, :def_val:`iDUMMY` if no valid data.",
               parameters = [
                   Parameter('vv', type="VV",
                             doc="Points :class:`VV` (must be one of the 4 supported types)"),
                   Parameter('max', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum value (:def_val:`rDUMMY` if all dummies or no data)")
               ]),

        Method('iLength_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns current :class:`VV` length.",
               return_type=Type.INT32_T,
               return_doc="# of elements in the :class:`VV`.",
               parameters = [
                   Parameter('vv', type="VV")
               ]),

        Method('IndexInsert_VV', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Insert items into a :class:`VV` using an index :class:`VV`.",
               notes="""
               The items in the input data :class:`VV` are inserted into
               the output :class:`VV` using the indices in the index :class:`VV`.
               Values not referenced are not altered, so the output
               :class:`VV` should be pre-initialized. The output :class:`VV` length
               will NOT be changed, and index values referencing
               beyond the end of the output :class:`VV` data will return an
               error.
               
               This function is useful when working with channel data that include
               dummies, but where the dummies must be removed before processing.
               Create and initialize an index (0, 1, 2...) :class:`VV`, using the :func:`InitIndex_VV`
               function, and when you remove
               the dummies, remove the corresponding index values as well.
               After processing, init a :class:`VV` to dummies, then use :func:`IndexInsert_VV` to
               put the processed values at the correct locations in the data :class:`VV`
               before you write it back to the channel.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_o', type="VV",
                             doc="Output Data :class:`VV` (modified with inserted data)"),
                   Parameter('vv_d', type="VV",
                             doc="Data items to insert (must be same type as output data :class:`VV`)"),
                   Parameter('vv_i', type="VV",
                             doc="Index :class:`VV` (must be type INT)")
               ]),

        Method('IndexOrder_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Reorder a :class:`VV`.",
               notes="""
               Given an index :class:`VV` (of type INT), this method reorders a
               :class:`VV`. Please make sure that the index holds valid information.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_i', type="VV",
                             doc="Index :class:`VV` of type INT"),
                   Parameter('vv_d', type="VV",
                             doc=":class:`VV` to order")
               ]),

        Method('InitIndex_VV', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Initialize an index :class:`VV` to values 0, 1, 2, etc...",
               notes="""
               Populates a :class:`VV` with the values 0, 1, 2, 3, 4 etc., to be
               used for various indexing functions, such as :func:`IndexInsert_VV` or
               :func:`IndexOrder_VV`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc="Index :class:`VV` to initialize (type INT)"),
                   Parameter('n', type=Type.INT32_T,
                             doc="Final length of :class:`VV` (-1 to use current length).")
               ]),

        Method('InvLog_VV', module='geoengine.core', version='7.3.0',
               availability=Availability.PUBLIC, 
               doc="Inverse of the :func:`_Log_VV` function.",
               notes="""
               This is the inverse function for :func:`_Log_VV`, with the same inputs.
               
               NEGATIVE_NO    - will not return values smaller than the input minimum
               NEGATIVE_YES   - if the data is in the range +/- minimum,
               it is left alone.  Otherwise, the sign is removed,
               the minimum is subtracted, the log of the minimum is added,
               and the exponential (base e or base 10) is taken of the
               sum. The sign is then reapplied.
               Minimum value will be defaulted to 1.0 if it is 0.0 or
               less than 0.0
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` handle"),
                   Parameter('log_base', type=Type.INT32_T,
                             doc=":def:`VV_LOG_BASE`"),
                   Parameter('log_neg', type=Type.INT32_T,
                             doc=":def:`VV_LOG_NEGATIVE`"),
                   Parameter('log_min', type=Type.DOUBLE,
                             doc="Minimum value for :def:`VV_LOG_NEGATIVE`")
               ]),

        Method('iOrder_VV', module='geoengine.core', version='6.4.0',
               availability=Availability.LICENSED, 
               doc="Identifies the data size order of the elements.",
               return_type=Type.INT32_T,
               return_doc=":def:`VV_ORDER`",
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to check order"),
                   Parameter('rep', type=Type.INT32_T, is_ref=True,
                             doc="Returned: Do any values repeat (0: No, 1: Yes)?")
               ]),

        Method('LinesToXY_VV', module='geoengine.core', version='8.0.0',
               availability=Availability.LICENSED, 
               doc="Convert a 2D Line segment :class:`VV` into X and Y VVs.",
               notes="""
               Some GX functions (such as :func:`GetVoronoiEdges_TIN`) return
               a special :class:`VV` where each element contains the start and end
               points of lines, (X_1, Y_1) and (X_2, Y_2).
               This GX dumps the individual X and Y values into individual
               X and Y VVs of type :def_val:`GS_DOUBLE` (REAL). N lines produces 2*N
               X and Y values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc="Input :class:`VV` of GS_D2LINE type (create with type -32)"),
                   Parameter('vv_x', type="VV",
                             doc="Output :class:`VV` with X locations (:def_val:`GS_DOUBLE`)"),
                   Parameter('vv_y', type="VV",
                             doc="Output :class:`VV` with Y locations (:def_val:`GS_DOUBLE`)")
               ]),

        Method('LookupIndex_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Lookup a :class:`VV` from another :class:`VV` using an index :class:`VV`.",
               notes="""
               This method assigns index values of 0.0, 1.0, 2.0 etc. to the individual
               values in the input Data :class:`VV`, and uses linear interpolation to calculate the values of
               Result :class:`VV` at the input indices contained in the Index :class:`VV`.
               
               If the input Data :class:`VV` is string type, then only values at the integral index values
               are returned.
               
               See also :func:`SetupIndex_VV` for an example of how this can be implemented.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vvd', type="VV",
                             doc="Input Data :class:`VV` (numeric)"),
                   Parameter('vvi', type="VV",
                             doc="Index :class:`VV` of REAL"),
                   Parameter('vvr', type="VV",
                             doc="Result :class:`VV` (same type as Data :class:`VV`)")
               ]),

        Method('MakeMemBased_VV', module='geoengine.core', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Make this :class:`VV` use regular instead of virtual memory.",
               notes="""
               This function should be called immediately aftter
               :func:`Create_VV`.
               
               Normal VVs are optimised to prevent thrashing, and to
               efficiently support many extremely large VVs, although
               there is a small performance penalty.
               This function is intended for :class:`VV`'s that you know can be
               handled by the operating system virtual memory manager,
               and will be used heavily.  By using a memory based :class:`VV`, you
               can achieve some performance improvements provided your
               application does not cause the memory manager to "thrash".
               
               External programs that use the GX API may prefer to use
               memory-based :class:`VV`'s because you can get direct access to
               the :class:`VV` through the :func:`GetPtrVV_GEO` function (see gx_extern.h).
               """,
               see_also=":func:`GetPtrVV_GEO` in gx_extern.h",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV")
               ]),

        Method('MaskAND_VV', module='geoengine.core', version='5.1.2',
               availability=Availability.LICENSED, 
               doc="Create mask from logical AND of two VVs.",
               notes="If both values are non-dummies, then result is 1, else dummy.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_x', type="VV",
                             doc=":class:`VV` A"),
                   Parameter('vv_y', type="VV",
                             doc=":class:`VV` B"),
                   Parameter('vv_z', type="VV",
                             doc=":class:`VV` C (returned)")
               ]),

        Method('MaskOR_VV', module='geoengine.core', version='5.1.2',
               availability=Availability.LICENSED, 
               doc="Create mask from logical OR of two VVs.",
               notes="If either values is non-dummy, then result is 1, else dummy.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_x', type="VV",
                             doc=":class:`VV` A"),
                   Parameter('vv_y', type="VV",
                             doc=":class:`VV` B"),
                   Parameter('vv_z', type="VV",
                             doc=":class:`VV` C (returned)")
               ]),

        Method('MaskStr_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Mask one :class:`VV` against another using a string.",
               notes="""
               All elements in the mask :class:`VV` that are same as string will replace
               the original :class:`VV` with a 1.
               
               The modified :class:`VV` will always be expanded to the MaskVV size but
               not shortened after this call.  If the mask is longer than the target,
               the target will be lengthenned with dummies before applying the mask.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_d', type="VV",
                             doc=":class:`VV` to be masked"),
                   Parameter('vv_m', type="VV",
                             doc="Mask :class:`VV`"),
                   Parameter('str_val', type=Type.STRING,
                             doc="String to compare")
               ]),

        Method('Multiply_VV', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Multiply two VVs: VV_A * VV_B = VV_C",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_x', type="VV",
                             doc=":class:`VV` A"),
                   Parameter('vv_y', type="VV",
                             doc=":class:`VV` B"),
                   Parameter('vv_z', type="VV",
                             doc=":class:`VV` C (returned), C = A * B")
               ]),

        Method('Amplitude3D_VV', module='geoengine.core', version='8.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate the 3D length for XYZ component VVs",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_a', type="VV",
                             doc="Amplitude :class:`VV` (returned)"),
                   Parameter('v_vx', type="VV",
                             doc="X component :class:`VV`"),
                   Parameter('v_vy', type="VV",
                             doc="Y component :class:`VV`"),
                   Parameter('v_vz', type="VV",
                             doc="Z component :class:`VV`")
               ]),

        Method('PolygonMask_VV', module='geoengine.core', version='5.1.3',
               availability=Availability.LICENSED, 
               doc="Mask a :class:`VV` using XY data and a polygon",
               notes="The VVs has to be the same length",
               return_type=Type.VOID,
               parameters = [
                   Parameter('xvv', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('yvv', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('rvv', type="VV",
                             doc=":class:`VV` to be masked"),
                   Parameter('pply', type="PLY",
                             doc="Polygon Object"),
                   Parameter('dummy', type=Type.INT32_T,
                             doc=":def:`VV_MASK`")
               ]),

        Method('Project_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="This method projects an X and Y :class:`VV`.",
               notes="This function is equivalent to :func:`ConvertVV_PJ`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('pj', type="PJ"),
                   Parameter('vv_x', type="VV",
                             doc="X"),
                   Parameter('vv_y', type="VV",
                             doc="Y")
               ]),

        Method('Project3D_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="This method projects an X,Y,Z :class:`VV`.",
               notes="This function is equivalent to :func:`ConvertVV3_PJ`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('pj', type="PJ"),
                   Parameter('vv_x', type="VV",
                             doc="X"),
                   Parameter('vv_y', type="VV",
                             doc="Y"),
                   Parameter('vv_z', type="VV",
                             doc="Z")
               ]),

        Method('RangeDouble_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the min. and max. values of a :class:`VV` while ignoring dummies.",
               notes="Minimum and maximum become :def_val:`GS_R8DM` if entire :class:`VV` is dummy.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('min', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum value - returned"),
                   Parameter('max', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum value - returned")
               ]),

        Method('ReFid_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Re-sample a :class:`VV` to a new fid start/icrement",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to resample"),
                   Parameter('start', type=Type.DOUBLE,
                             doc="New fid start"),
                   Parameter('incr', type=Type.DOUBLE,
                             doc="New fid increment"),
                   Parameter('length', type=Type.INT32_T,
                             doc="New length")
               ]),

        Method('ReFidVV_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Re-sample a :class:`VV` to match another :class:`VV`.",
               notes="""
               This method will honor the :class:`VV` FID Expansion and will expand/contract
               :class:`VV`'s based on this flag if it is used.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to resample"),
                   Parameter('vv_m', type="VV",
                             doc=":class:`VV` model (fid increment and start)")
               ]),

        Method('ReSample_VV', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Resamples a :class:`VV` from one fid/incr to another fid/incr.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to resample"),
                   Parameter('c_start', type=Type.DOUBLE,
                             doc="Current start fid"),
                   Parameter('c_incr', type=Type.DOUBLE,
                             doc="Current increment"),
                   Parameter('n_start', type=Type.DOUBLE,
                             doc="New fid start"),
                   Parameter('n_incr', type=Type.DOUBLE,
                             doc="New fid increment"),
                   Parameter('length', type=Type.INT32_T,
                             doc="New length"),
                   Parameter('extr', type=Type.INT32_T,
                             doc="Extrapolate Endpoints (0 - No, 1 - Yes)")
               ]),

        Method('rGetFidIncr_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the Fiducial increment from a :class:`VV`",
               return_type=Type.DOUBLE,
               return_doc="Fiducial increment of the :class:`VV`.",
               parameters = [
                   Parameter('vv', type="VV")
               ]),

        Method('rGetFidStart_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the Fiducial start from a :class:`VV`",
               return_type=Type.DOUBLE,
               return_doc="Fiducial start of the :class:`VV`.",
               parameters = [
                   Parameter('vv', type="VV")
               ]),

        Method('rGetReal_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a real element from a :class:`VV`.",
               notes="""
               Type conversions are performed if necessary.  Dummy values
               are converted to "*" string.
               """,
               return_type=Type.DOUBLE,
               return_doc="""
               Element wanted, or :def_val:`rDUMMY`
               if the value is dummy or outside of the range of data.
               """,
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('element', type=Type.INT32_T,
                             doc="Element wanted")
               ]),

        Method('rSum_VV', module='geoengine.core', version='7.2.0',
               availability=Availability.LICENSED, 
               doc="Calculate the sum of the values in a :class:`VV`.",
               notes="Dummy value is treated as Zero(0)",
               return_type=Type.DOUBLE,
               return_doc="The sum of the elements.",
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to be processed")
               ]),

        Method('rWeightedMean_VV', module='geoengine.core', version='7.2.0',
               availability=Availability.LICENSED, 
               doc="Calculate the weighted average of the values.",
               notes="Dummy values are ignored.",
               return_type=Type.DOUBLE,
               return_doc="The weighted average of the values.",
               parameters = [
                   Parameter('vv_elements', type="VV",
                             doc=":class:`VV` to be processed"),
                   Parameter('vv_weights', type="VV",
                             doc=":class:`VV` of weights")
               ]),

        Method('SetFidExpansion_VV', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Sets the Fiducial expansion from a :class:`VV`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('expand', type=Type.INT32_T,
                             doc="Expansion setting (1 or greater)")
               ]),

        Method('SetFidIncr_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the Fiducial increment of a :class:`VV`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to set fiducial increment of"),
                   Parameter('incr', type=Type.DOUBLE,
                             doc="New increment")
               ]),

        Method('SetFidStart_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the Fiducial start of a :class:`VV`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to set fiducial start of"),
                   Parameter('start', type=Type.DOUBLE,
                             doc="New start")
               ]),

        Method('SetInt_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set an integer element in a :class:`VV`.",
               notes="""
               Element being set cannot be < 0.
               If the element is > current :class:`VV` length, the :class:`VV` length is
               increased.
               It is good practice to set the length ahead of time to the
               expected maximum value, as some :class:`VV` processes rely on the
               current maximum length of the :class:`VV` when you pass it in as an
               argument, and unexpected results may occur if the length is
               not what you expect it to be because of dynamic allocation at
               an earlier time.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('element', type=Type.INT32_T,
                             doc="Element to set"),
                   Parameter('value', type=Type.INT32_T,
                             doc="Value to set")
               ]),

        Method('SetIntN_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set N integer elements in a :class:`VV`.",
               notes="""
               Element being set cannot be < 0.
               If the element is > current :class:`VV` length, the :class:`VV` length is
               increased.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('start', type=Type.INT32_T,
                             doc="Start element (>= 0)"),
                   Parameter('n', type=Type.INT32_T,
                             doc="# elements to set (-1 sets all elements to end)"),
                   Parameter('value', type=Type.INT32_T,
                             doc="Value to set")
               ]),

        Method('SetLen_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the length of a :class:`VV`.",
               notes="""
               If increasing the :class:`VV` size, new elements are set to dummies.
               
               It is good practice to set the length ahead of time to the
               expected maximum value, as some :class:`VV` processes rely on the
               current maximum length of the :class:`VV` when you pass it in as an
               argument, and unexpected results may occur if the length is
               not what you expect it to be because of dynamic allocation at
               an earlier time.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to set length of"),
                   Parameter('size', type=Type.INT32_T,
                             doc="New length (number of elements)")
               ]),

        Method('SetReal_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a real element in a :class:`VV`.",
               notes="""
               Element being set cannot be < 0.
               If the element is > current :class:`VV` length, the :class:`VV` length is
               increased.
               It is good practice to set the length ahead of time to the
               expected maximum value, as some :class:`VV` processes rely on the
               current maximum length of the :class:`VV` when you pass it in as an
               argument, and unexpected results may occur if the length is
               not what you expect it to be because of dynamic allocation at
               an earlier time.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('element', type=Type.INT32_T,
                             doc="Element to set"),
                   Parameter('value', type=Type.DOUBLE,
                             doc="Value to set")
               ]),

        Method('SetRealN_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set N real elements in a :class:`VV`.",
               notes="""
               Element being set cannot be < 0.
               If the element is > current :class:`VV` length, the :class:`VV` length is
               increased.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('start', type=Type.INT32_T,
                             doc="Start element (>= 0)"),
                   Parameter('n', type=Type.INT32_T,
                             doc="# elements to set (-1 sets all elements to end)"),
                   Parameter('value', type=Type.DOUBLE,
                             doc="Value to set")
               ]),

        Method('SetString_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a string element in a :class:`VV`.",
               notes="""
               Element being set cannot be < 0.
               If the element is > current :class:`VV` length, the :class:`VV` length is
               increased.
               It is good practice to set the length ahead of time to the
               expected maximum value, as some :class:`VV` processes rely on the
               current maximum length of the :class:`VV` when you pass it in as an
               argument, and unexpected results may occur if the length is
               not what you expect it to be because of dynamic allocation at
               an earlier time.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('element', type=Type.INT32_T,
                             doc="Element to set"),
                   Parameter('value', type=Type.STRING,
                             doc="String to set")
               ]),

        Method('SetStringN_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set N string elements in a :class:`VV`.",
               notes="""
               Element being set cannot be < 0.
               If the element is > current :class:`VV` length, the :class:`VV` length is
               increased.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV"),
                   Parameter('start', type=Type.INT32_T,
                             doc="Start element (>= 0)"),
                   Parameter('n', type=Type.INT32_T,
                             doc="# elements to set (-1 sets all elements to end)"),
                   Parameter('value', type=Type.STRING,
                             doc="String to set")
               ]),

        Method('SetupIndex_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Setup an index :class:`VV` from VV1 to VV2.",
               notes="""
               The input reference :class:`VV` must be in ascending numerical order.
               If your reference data is NOT ordered, then use the :func:`SortIndex1_VV` 
               function to create an order index, then sort both the reference and data VVs 
               using this index :class:`VV` before you call :func:`SetupIndex_VV`.
               
               Example: You have a reference data set taken at specific times, ``hVVt``, ``hVVy``
               and you want to calculate/estimate/interpolate the values ``hVVy2`` at a second set
               of times ``hVVt2``
               
               Step 1: Create an index, ``hVVi``, type :def_val:`GS_DOUBLE`, and call :func:`SetupIndex_VV`.
               
               with: ``hVVt2, hVVi, VV_LOOKUP_XXX, rSpacing``
               
               Internally, this assigns index values of 0.0, 1.0, 2.0 etc. to the individual
               values in ``hVVt``, then, depending on the lookup method chosen, assigns
               fractional index values to the input values in ``hVVt2``.
               
               Step 2: To determine what the lookup values ``hVVy2`` should be at times ``hVVt2``,
               call the :func:`LookupIndex_VV` function for hVVy with ``hVVi, hVVy2``
               
               Internally, this assigns index values of 0.0, 1.0, 2.0 etc. to the individual
               values in ``hVVy``, and uses linear interpolation to calculate the values of
               ``hVVy2`` at the input indices contained in ``hVVi``.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vvd', type="VV",
                             doc="Original Data :class:`VV`"),
                   Parameter('vvq', type="VV",
                             doc="Query :class:`VV` (same type as Data :class:`VV`)"),
                   Parameter('vvi', type="VV",
                             doc=":class:`VV` index :class:`VV` of type REAL"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`VV_LOOKUP`"),
                   Parameter('space', type=Type.DOUBLE,
                             doc="Spacing for some modes")
               ]),

        Method('SetVM_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_cpp=True, 
               doc="Set :class:`VV` data from a :class:`VM`. (OBSOLETE)",
               notes="""
               See :func:`CopyVMtoVV_VV`, which is a prefered method to move :class:`VM` data
               into a :class:`VV`.  This method is mainly provided for old compatibility.
               
               The :class:`VM` will be lengthened if required to hold the entire :class:`VV`.
               
               If the :class:`VM` is longer than required, extra data past the end
               of the :class:`VV` will be set to dummy.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` in which to place data"),
                   Parameter('vm', type="VM",
                             doc=":class:`VM` from which to read the data"),
                   Parameter('loc', type=Type.INT32_T,
                             doc="Start :class:`VV` location of data to set, 0 is first.")
               ]),

        Method('Sort_VV', module='geoengine.core', version='5.1.5',
               availability=Availability.LICENSED, 
               doc="Sort a :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dvv', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('order', type=Type.INT32_T,
                             doc=":def:`VV_SORT`")
               ]),

        Method('SortIndex_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Sort index :class:`VV` based on a data :class:`VV`.",
               notes="""
               Create an Index :class:`VV` (of type :def_val:`GS_LONG`) based on a data :class:`VV`.
               This index vv can then be used by the IndexOrder method
               to order a group of :class:`VV`'s.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('dvv', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('ivv', type="VV",
                             doc="Index :class:`VV` of type INT")
               ]),

        Method('SortIndex1_VV', module='geoengine.core', version='5.0.2',
               availability=Availability.LICENSED, 
               doc="Sort index :class:`VV` based on 1 data :class:`VV` - set orders.",
               notes="""
               Create an Index :class:`VV` (of type :def_val:`GS_LONG`) based on a data :class:`VV`.
               This index vv can then be used by the IndexOrder method
               to order a group of :class:`VV`'s. The individual VVs may be ordered
               in ascending or descending order.
               If the primary :class:`VV` values of two indices are the same, then
               the secondary :class:`VV` values are compared. If the secondary values
               are the same, the ternary values are compared, etc.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('dvv', type="VV",
                             doc="Primary Data :class:`VV`"),
                   Parameter('ivv', type="VV",
                             doc="Index :class:`VV` of type INT"),
                   Parameter('ord1', type=Type.INT32_T,
                             doc=":def:`VV_SORT`")
               ]),

        Method('SortIndex2_VV', module='geoengine.core', version='5.0.2',
               availability=Availability.LICENSED, 
               doc="Sort index :class:`VV` based on 2 data VVs - set orders.",
               notes="""
               Create an Index :class:`VV` (of type :def_val:`GS_LONG`) based on a data :class:`VV`.
               This index vv can then be used by the IndexOrder method
               to order a group of :class:`VV`'s. The individual VVs may be ordered
               in ascending or descending order.
               If the primary :class:`VV` values of two indices are the same, then
               the secondary :class:`VV` values are compared. If the secondary values
               are the same, the ternary values are compared, etc
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('d1_vv', type="VV",
                             doc="Primary Data :class:`VV`"),
                   Parameter('d2_vv', type="VV",
                             doc="Secondary Data :class:`VV`"),
                   Parameter('ivv', type="VV",
                             doc="Index :class:`VV` of type INT"),
                   Parameter('ord1', type=Type.INT32_T,
                             doc="Primary Sort order :def:`VV_SORT`"),
                   Parameter('ord2', type=Type.INT32_T,
                             doc="Secondary Sort order :def:`VV_SORT`")
               ]),

        Method('SortIndex3_VV', module='geoengine.core', version='5.0.2',
               availability=Availability.LICENSED, 
               doc="Sort index :class:`VV` based on 3 data VVs - set orders.",
               notes="""
               Create an Index :class:`VV` (of type :def_val:`GS_LONG`) based on a data :class:`VV`.
               This index vv can then be used by the IndexOrder method
               to order a group of :class:`VV`'s. The individual VVs may be ordered
               in ascending or descending order.
               If the primary :class:`VV` values of two indices are the same, then
               the secondary :class:`VV` values are compared. If the secondary values
               are the same, the third values are compared, etc
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('d1_vv', type="VV",
                             doc="Primary Data :class:`VV`"),
                   Parameter('d2_vv', type="VV",
                             doc="Secondary Data :class:`VV`"),
                   Parameter('d3_vv', type="VV",
                             doc="Ternary Data :class:`VV`"),
                   Parameter('ivv', type="VV",
                             doc="Index :class:`VV` of type INT"),
                   Parameter('ord1', type=Type.INT32_T,
                             doc="Primary Sort order :def:`VV_SORT`"),
                   Parameter('ord2', type=Type.INT32_T,
                             doc="Secondary sort order :def:`VV_SORT`"),
                   Parameter('ord3', type=Type.INT32_T,
                             doc="Third Sort order :def:`VV_SORT`")
               ]),

        Method('SortIndex4_VV', module='geoengine.core', version='5.0.2',
               availability=Availability.LICENSED, 
               doc="Sort index :class:`VV` based on 4 data VVs - set orders.",
               notes="""
               Create an Index :class:`VV` (of type :def_val:`GS_LONG`) based on a data :class:`VV`.
               This index vv can then be used by the IndexOrder method
               to order a group of :class:`VV`'s. The individual VVs may be ordered
               in ascending or descending order.
               If the primary :class:`VV` values of two indices are the same, then
               the secondary :class:`VV` values are compared. If the secondary values
               are the same, the third values are compared, etc
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('d1_vv', type="VV",
                             doc="Primary Data :class:`VV`"),
                   Parameter('d2_vv', type="VV",
                             doc="Secondary Data :class:`VV`"),
                   Parameter('d3_vv', type="VV",
                             doc="Ternary Data :class:`VV`"),
                   Parameter('d4_vv', type="VV",
                             doc="Quaternary Data :class:`VV`"),
                   Parameter('ivv', type="VV",
                             doc="Index :class:`VV` of type INT"),
                   Parameter('ord1', type=Type.INT32_T,
                             doc="Primary Ssort order :def:`VV_SORT`"),
                   Parameter('ord2', type=Type.INT32_T,
                             doc="Secondary Sort order :def:`VV_SORT`"),
                   Parameter('ord3', type=Type.INT32_T,
                             doc="Third Sort order :def:`VV_SORT`"),
                   Parameter('ord4', type=Type.INT32_T,
                             doc="Fourth Sort order :def:`VV_SORT`")
               ]),

        Method('Statistics_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Add a :class:`VV` to a :class:`ST`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('st', type="ST",
                             doc=":class:`ST` Handle"),
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to add to :class:`ST`")
               ]),

        Method('Subtract_VV', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Subtract one :class:`VV` from another: VV_A - VV_B = VV_C",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_x', type="VV",
                             doc=":class:`VV` A"),
                   Parameter('vv_y', type="VV",
                             doc=":class:`VV` B"),
                   Parameter('vv_z', type="VV",
                             doc=":class:`VV` C (returned), C = A - B")
               ]),

        Method('Swap_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               Swaps the bytes of the SHORT, USHORT, LONG, FLOAT and DOUBLE vv's.
               Other vv's are not affected by this method. This is used
               primarily with changing the order of bytes for other machine
               created data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` object")
               ]),

        Method('Window_VV', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Limit the elements of a vv to a range.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc="Data :class:`VV` (numeric)"),
                   Parameter('min', type=Type.DOUBLE,
                             doc="Min Val"),
                   Parameter('max', type=Type.DOUBLE,
                             doc="Max Val"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`VV_WINDOW`")
               ]),

        Method('WriteXML_VV', module='geoengine.core', version='8.0.0',
               availability=Availability.LICENSED, 
               doc="Write the :class:`VV` data as an XML object with bytes and formating.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv', type="VV",
                             doc=":class:`VV` to save"),
                   Parameter('file', type=Type.STRING,
                             doc="XML file to create"),
                   Parameter('format', type=Type.INT32_T,
                             doc="Format"),
                   Parameter('decimal', type=Type.INT32_T,
                             doc="Significant digits/decimals")
               ])
    ]
}