from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DB',
                 doc="""
                 The :class:`DB` class is used to create, open and work with databases and database symbols.
                 Database symbols are objects inside databases, such as lines, channels and blobs
                 """,
                 notes="""
                 The follwing defines are not used by any methods but are
                 used by GX's:
                 
                 :def_val:`DB_ACTIVITY_BLOB`
                 """,
                 verbatim_gxh_defines="""
#define LOCK_RW(A,B) LockSymb_DB(A,B,DB_LOCK_READWRITE,DB_WAIT_NONE)
#define LOCK_R(A,B)  LockSymb_DB(A,B,DB_LOCK_READONLY,DB_WAIT_NONE)
#define UNLOCK(A,B)  UnLockSymb_DB(A,B)
""")


gx_defines = [
    Define('DB_ACTIVITY_BLOB',
           is_constant=True,
           is_single_constant=True,
           doc="Activity Blob",
           constants=[
               Constant('DB_ACTIVITY_BLOB', value='OE.DB_ACTIVITY_LOG', type=Type.STRING)                        
           ]),

    Define('DB_CATEGORY_BLOB',
           doc="Blob Categories",
           constants=[
               Constant('DB_CATEGORY_BLOB_NORMAL', value='0', type=Type.INT32_T)                        
           ]),

    Define('DB_CATEGORY_CHAN',
           doc="""
           Channel Categories
           For STRING type channels, use negative integers
           to specify channel width. For example, use -10
           to define a string channel with up to 10 characters.
           Use the GS_SIMPLE_TYPE() macro to convert to INT,REAL or string.
           """,
           constants=[
               Constant('DB_CATEGORY_CHAN_BYTE', value='GS_BYTE', type=Type.INT32_T)                        ,
               Constant('DB_CATEGORY_CHAN_USHORT', value='GS_USHORT', type=Type.INT32_T)                        ,
               Constant('DB_CATEGORY_CHAN_SHORT', value='GS_SHORT', type=Type.INT32_T)                        ,
               Constant('DB_CATEGORY_CHAN_LONG', value='GS_LONG', type=Type.INT32_T)                        ,
               Constant('DB_CATEGORY_CHAN_FLOAT', value='GS_FLOAT', type=Type.INT32_T)                        ,
               Constant('DB_CATEGORY_CHAN_DOUBLE', value='GS_DOUBLE', type=Type.INT32_T)                        ,
               Constant('DB_CATEGORY_CHAN_UBYTE', value='GS_UBYTE', type=Type.INT32_T)                        ,
               Constant('DB_CATEGORY_CHAN_ULONG', value='GS_ULONG', type=Type.INT32_T)                        ,
               Constant('DB_CATEGORY_CHAN_LONG64', value='GS_LONG64', type=Type.INT32_T)                        ,
               Constant('DB_CATEGORY_CHAN_ULONG64', value='GS_ULONG64', type=Type.INT32_T)                        
           ]),

    Define('DB_CATEGORY_LINE',
           doc="Line Categories",
           constants=[
               Constant('DB_CATEGORY_LINE_FLIGHT', value='100', type=Type.INT32_T)                        ,
               Constant('DB_CATEGORY_LINE_GROUP', value='200', type=Type.INT32_T)                        ,
               Constant('DB_CATEGORY_LINE_NORMAL', value='DB_CATEGORY_LINE_FLIGHT', type=Type.INT32_T,
                        doc="Same as :def_val:`DB_CATEGORY_LINE_FLIGHT`")                        
           ]),

    Define('DB_CATEGORY_USER',
           doc="User Categories",
           constants=[
               Constant('DB_CATEGORY_USER_NORMAL', value='0', type=Type.INT32_T)                        
           ]),

    Define('DB_CHAN_FORMAT',
           doc="Channel formats",
           constants=[
               Constant('DB_CHAN_FORMAT_NORMAL', value='FORMAT_DECIMAL', type=Type.INT32_T)                        ,
               Constant('DB_CHAN_FORMAT_EXP', value='FORMAT_EXP', type=Type.INT32_T)                        ,
               Constant('DB_CHAN_FORMAT_TIME', value='FORMAT_TIME_COLON', type=Type.INT32_T)                        ,
               Constant('DB_CHAN_FORMAT_DATE', value='FORMAT_DATE_YYYYMMDD', type=Type.INT32_T)                        ,
               Constant('DB_CHAN_FORMAT_GEOGR', value='FORMAT_GEOGRAPHIC', type=Type.INT32_T)                        ,
               Constant('DB_CHAN_FORMAT_SIGDIG', value='FORMAT_SIG_DIG', type=Type.INT32_T)                        ,
               Constant('DB_CHAN_FORMAT_HEX', value='6', type=Type.INT32_T)                        
           ]),

    Define('DB_CHAN_PROTECTION',
           doc="Channel Read-only Protection Status",
           constants=[
               Constant('DB_CHAN_UNPROTECTED', value='0', type=Type.INT32_T)                        ,
               Constant('DB_CHAN_PROTECTED', value='1', type=Type.INT32_T)                        
           ]),

    Define('DB_CHAN_SYMBOL',
           doc="Channel symbol for special channels",
           constants=[
               Constant('DB_CHAN_X', value='0', type=Type.INT32_T)                        ,
               Constant('DB_CHAN_Y', value='1', type=Type.INT32_T)                        ,
               Constant('DB_CHAN_Z', value='2', type=Type.INT32_T)                        
           ]),

    Define('DB_COMP',
           doc="Supported compression levels",
           constants=[
               Constant('DB_COMP_NONE', value='0', type=Type.INT32_T)                        ,
               Constant('DB_COMP_SPEED', value='1', type=Type.INT32_T)                        ,
               Constant('DB_COMP_SIZE', value='2', type=Type.INT32_T)                        
           ]),

    Define('DB_COORDPAIR',
           constants=[
               Constant('DB_COORDPAIR_NONE', value='0', type=Type.INT32_T)                        ,
               Constant('DB_COORDPAIR_X', value='1', type=Type.INT32_T)                        ,
               Constant('DB_COORDPAIR_Y', value='2', type=Type.INT32_T)                        
           ]),

    Define('DB_GROUP_CLASS_SIZE',
           is_constant=True,
           is_single_constant=True,
           doc="Class name max size",
           constants=[
               Constant('DB_GROUP_CLASS_SIZE', value='16', type=Type.INT32_T)                        
           ]),

    Define('DB_INFO',
           doc="Integer Database Information",
           constants=[
               Constant('DB_INFO_BLOBS_MAX', value='0', type=Type.INT32_T,
                        doc="Maximum Number of Blobs in the Database")                        ,
               Constant('DB_INFO_LINES_MAX', value='1', type=Type.INT32_T,
                        doc="Maximum number of lines in the database")                        ,
               Constant('DB_INFO_CHANS_MAX', value='2', type=Type.INT32_T,
                        doc="Maximum Number of Channels in the Database")                        ,
               Constant('DB_INFO_USERS_MAX', value='3', type=Type.INT32_T,
                        doc="Maximum number of Users")                        ,
               Constant('DB_INFO_BLOBS_USED', value='4', type=Type.INT32_T,
                        doc="Number of Blobs currently used")                        ,
               Constant('DB_INFO_LINES_USED', value='5', type=Type.INT32_T,
                        doc="Number of Lines currently used")                        ,
               Constant('DB_INFO_CHANS_USED', value='6', type=Type.INT32_T,
                        doc="Number of Channels currently used")                        ,
               Constant('DB_INFO_USERS_USED', value='7', type=Type.INT32_T,
                        doc="Number of Users in the database")                        ,
               Constant('DB_INFO_PAGE_SIZE', value='8', type=Type.INT32_T,
                        doc="Size of the smallest database block in bytes")                        ,
               Constant('DB_INFO_DATA_SIZE', value='9', type=Type.INT32_T,
                        doc="Number of Blocks in Entire Database")                        ,
               Constant('DB_INFO_LOST_SIZE', value='10', type=Type.INT32_T,
                        doc="Number of Lost Blocks in the Database")                        ,
               Constant('DB_INFO_FREE_SIZE', value='11', type=Type.INT32_T,
                        doc="Number of Free Blocks in the Database")                        ,
               Constant('DB_INFO_COMP_LEVEL', value='16', type=Type.INT32_T,
                        doc="Compression Level in use")                        ,
               Constant('DB_INFO_BLOB_SIZE', value='19', type=Type.INT32_T,
                        doc="Number of pages given to blobs")                        ,
               Constant('DB_INFO_FILE_SIZE', value='17', type=Type.INT32_T,
                        doc="Entire Size of File (in kbytes)")                        ,
               Constant('DB_INFO_INDEX_SIZE', value='18', type=Type.INT32_T,
                        doc="Size of Index (in kbytes)")                        ,
               Constant('DB_INFO_MAX_BLOCK_SIZE', value='20', type=Type.INT32_T,
                        doc="Naximum number of bytes in a block")                        ,
               Constant('DB_INFO_CHANGESLOST', value='21', type=Type.INT32_T,
                        doc="Will changes to this database be lost when this database is closed?")                        
           ]),

    Define('DB_LINE_LABEL_FORMAT',
           doc="Line Label Formats",
           constants=[
               Constant('DB_LINE_LABEL_FORMAT_LINE', value='1', type=Type.INT32_T)                        ,
               Constant('DB_LINE_LABEL_FORMAT_VERSION', value='2', type=Type.INT32_T)                        ,
               Constant('DB_LINE_LABEL_FORMAT_TYPE', value='4', type=Type.INT32_T)                        ,
               Constant('DB_LINE_LABEL_FORMAT_FLIGHT', value='8', type=Type.INT32_T)                        ,
               Constant('DB_LINE_LABEL_FORMAT_FULL', value='15', type=Type.INT32_T)                        ,
               Constant('DB_LINE_LABEL_FORMAT_DATE', value='16', type=Type.INT32_T)                        ,
               Constant('DB_LINE_LABEL_FORMAT_LINK', value='7', type=Type.INT32_T)                        
           ]),

    Define('DB_LINE_SELECT',
           doc="Select modes",
           constants=[
               Constant('DB_LINE_SELECT_INCLUDE', value='0', type=Type.INT32_T)                        ,
               Constant('DB_LINE_SELECT_EXCLUDE', value='1', type=Type.INT32_T)                        
           ]),

    Define('DB_LINE_TYPE',
           doc="Line types",
           constants=[
               Constant('DB_LINE_TYPE_NORMAL', value='0', type=Type.INT32_T)                        ,
               Constant('DB_LINE_TYPE_BASE', value='1', type=Type.INT32_T)                        ,
               Constant('DB_LINE_TYPE_TIE', value='2', type=Type.INT32_T)                        ,
               Constant('DB_LINE_TYPE_TEST', value='3', type=Type.INT32_T)                        ,
               Constant('DB_LINE_TYPE_TREND', value='4', type=Type.INT32_T)                        ,
               Constant('DB_LINE_TYPE_SPECIAL', value='5', type=Type.INT32_T)                        ,
               Constant('DB_LINE_TYPE_RANDOM', value='6', type=Type.INT32_T)                        
           ]),

    Define('DB_LOCK',
           doc="Lock Modes",
           constants=[
               Constant('DB_LOCK_NONE', value='-1', type=Type.INT32_T,
                        doc="Used only by GetSymbLock_DB")                        ,
               Constant('DB_LOCK_READONLY', value='0', type=Type.INT32_T)                        ,
               Constant('DB_LOCK_READWRITE', value='1', type=Type.INT32_T)                        
           ]),

    Define('DB_NAME',
           doc="Get Database file names",
           constants=[
               Constant('DB_NAME_FILE', value='0', type=Type.INT32_T)                        
           ]),

    Define('DB_NULL',
           is_null_handle=True,
           doc="Database Null"),

    Define('DB_OWN',
           doc="Symbol Ownership",
           constants=[
               Constant('DB_OWN_SHARED', value='0', type=Type.INT32_T)                        ,
               Constant('DB_OWN_USER', value='1', type=Type.INT32_T)                        
           ]),

    Define('DB_SYMB_TYPE',
           doc="Symbol types",
           constants=[
               Constant('DB_SYMB_BLOB', value='0', type=Type.INT32_T)                        ,
               Constant('DB_SYMB_LINE', value='1', type=Type.INT32_T)                        ,
               Constant('DB_SYMB_CHAN', value='2', type=Type.INT32_T)                        ,
               Constant('DB_SYMB_USER', value='3', type=Type.INT32_T)                        
           ]),

    Define('DB_SYMB_NAME_SIZE',
           is_constant=True,
           is_single_constant=True,
           doc="Size of Symbol Names",
           constants=[
               Constant('DB_SYMB_NAME_SIZE', value='STR_DB_SYMBOL', type=Type.INT32_T,
                        doc="Same :def_val:`STR_DB_SYMBOL`")                        
           ]),

    Define('DB_WAIT',
           doc="Wait Times",
           constants=[
               Constant('DB_WAIT_NONE', value='0', type=Type.INT32_T)                        ,
               Constant('DB_WAIT_INFINITY', value='-1', type=Type.INT32_T)                        
           ]),

    Define('DB_ARRAY_BASETYPE',
           constants=[
               Constant('DB_ARRAY_BASETYPE_NONE', value='0', type=Type.INT32_T)                        ,
               Constant('DB_ARRAY_BASETYPE_TIME_WINDOWS', value='1', type=Type.INT32_T)                        ,
               Constant('DB_ARRAY_BASETYPE_TIMES', value='2', type=Type.INT32_T)                        ,
               Constant('DB_ARRAY_BASETYPE_FREQUENCIES', value='3', type=Type.INT32_T)                        ,
               Constant('DB_ARRAY_BASETYPE_ELEVATIONS', value='4', type=Type.INT32_T)                        ,
               Constant('DB_ARRAY_BASETYPE_DEPTHS', value='5', type=Type.INT32_T)                        ,
               Constant('DB_ARRAY_BASETYPE_VELOCITIES', value='6', type=Type.INT32_T)                        ,
               Constant('DB_ARRAY_BASETYPE_DISCRETE_TIME_WINDOWS', value='7', type=Type.INT32_T)                        
           ]),

    Define('NULLSYMB',
           is_constant=True,
           is_single_constant=True,
           doc="Database Null",
           constants=[
               Constant('NULLSYMB', value='-1', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Channel': [

        Method('CreateDup_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method makes a brand new database identical to the input
               Database in-size.
               The database is opened in ReadWrite Mode.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc=":class:`DB` input"),
                   Parameter('p2', type=Type.STRING,
                             doc="name of the Database File to Create")
               ]),

        Method('CreateDupComp_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method makes a brand new database identical to the input
               Database in-size except it changes the compression.
               The database is opened in ReadWrite Mode.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc=":class:`DB` input"),
                   Parameter('p2', type=Type.STRING,
                             doc="name of the Database File to Create"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_COMP`")
               ]),

        Method('DupSymbAcross_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Create a new Symbol by duplicating an existing symbol.
               exactly the same type but in output database. The symbol must
               not already exist in the output database.
               """,
               return_type="DB_SYMB",
               return_doc="New Symbol Handle",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Input"),
                   Parameter('p2', type="DB",
                             doc="Database output"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Symbol Handle to duplicate")
               ]),

        Method('EasyMakerSymb_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Adds a Maker to the database symbol based on current GX",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol to create maker for"),
                   Parameter('p3', type=Type.STRING,
                             doc="Maker name, used in menu prompt"),
                   Parameter('p4', type=Type.STRING,
                             doc='INI groups (terminate each with a ";")')
               ]),

        Method('GetChanStr_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get individual elements in a channel.",
               notes="""
               These methods are slow and should only be used when
               performance is not an issue.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="channel"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="index"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='p6',
                             doc="string"),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="length")
               ]),

        Method('GetChanVV_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Place the contents of a channel in a :class:`VV`.",
               notes="""
               If a :class:`VA` channel is specified, then element [0] of this
               :class:`VA` channel is used to populated the :class:`VV`.
               """,
               see_also=":class:`VV` class.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` in which to place the data")
               ]),

        Method('GetChanVVExpanded_DB', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="""
               Read a channel into a :class:`VV`. If the channel is a :class:`VA` channel it is
               treaded as a :class:`VV` channel with multiple values per fid and the FID expation
               is set to the array size.
               """,
               notes="""
               This method is to be used in conjunction with the :func:`ReFidVV_VV` method
               that will honor the FID Expansion setting.
               """,
               see_also=":class:`VV` class.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` in which to place the data")
               ]),

        Method('GetIPJ_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get georeference information in an :class:`IPJ`.",
               notes="""
               If the channel does not have an :class:`IPJ`, the :class:`IPJ` that is
               returned will have an unknown projection.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Shared Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol"),
                   Parameter('p3', type="IPJ",
                             doc=":class:`IPJ` to fill in")
               ]),

        Method('GetITR_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get :class:`ITR` for a channel.",
               notes="""
               If a channel does not have an :class:`ITR`, :func:`GetITR_DB` will not change
               the passed :class:`ITR`.
               Channel must be locked for READONLY or READWRITE.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel"),
                   Parameter('p3', type="ITR",
                             doc=":class:`ITR` to fill in")
               ]),

        Method('GetRegSymb_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a :class:`REG` object from a symbol",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Shared Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol, :def_val:`NULLSYMB` for the database :class:`REG`"),
                   Parameter('p3', type="REG",
                             doc=":class:`REG` to copy data into")
               ]),

        Method('GetRegSymbSetting_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a :class:`REG` string setting from a symbol reg",
               notes="""
               The symbol :class:`REG` is used to store a variety of attribute
               about the symbol.  Following a conventionally used entries:
               
               UNITS                   - channel units
               CLASS                   - symbol class name (i.e. "Assay")
               _PJ_ipj                 - projection blob name
               _PJ_x                   - projection coordinate pair
               _PJ_y
               _PJ_name                - projection GXF-style info
               _PJ_ellipsoid
               _PJ_projection
               _PJ_units
               _PJ_datum_transform
               
               This is a convenient but low-performance way to get/set :class:`REG`
               settings.  If performance is an issue, and more than one
               setting is to be Get and or Set, use the :class:`REG` directly.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol, :def_val:`NULLSYMB` for the database :class:`REG`"),
                   Parameter('p3', type=Type.STRING,
                             doc=":class:`REG` entry name"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="returned setting"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="string length")
               ]),

        Method('GetVaChanVV_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Place the contents of a specific part of a channel in a :class:`VV`.",
               notes="""
               If a :class:`VA` channel is specified, then element [0] of this
               :class:`VA` channel is used to populated the :class:`VV`.
               """,
               see_also=":class:`VV` class.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` in which to place the data"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Offset"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Number to Write")
               ]),

        Method('iBlobsMax_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Gets Maximum Number of Blobs in the Database",
               return_type=Type.INT32_T,
               return_doc="Maximum Number of Blobs in the Database",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object")
               ]),

        Method('iChansMax_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Gets Maximum Number of Channels in the Database",
               return_type=Type.INT32_T,
               return_doc="Maximum Number of Channels in the Database",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object")
               ]),

        Method('IFormatChan_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Format a real value based on a channel format.",
               notes="""
               If the passed string is too short, the result will be
               "**".
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel handle"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="value to format"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="string"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="string length")
               ]),

        Method('iGetChanArraySize_DB', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="""
               This method Gets a channel's array size for a
               given channel handle.
               """,
               return_type=Type.INT32_T,
               return_doc="Channel type",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle")
               ]),

        Method('IGetChanClass_DB', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="This method gets a channel's label",
               notes="""
               The channel label is stored in the "CLASS" parameter
               of the channel reg. If no class is defined, then an
               empty string is returned.
               The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="returned class into"),
                   Parameter('p4', type=Type.INT32_T, default_length='DB_GROUP_CLASS_SIZE',
                             doc="size of string")
               ]),

        Method('iGetChanDecimal_DB', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="""
               This method gets a channel's number of digits displayed
               to the right of the decimal point.
               """,
               notes="The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.INT32_T,
               return_doc="Number of digits displayed to right of decimal",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle")
               ]),

        Method('iGetChanFormat_DB', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="""
               This method Gets a channel's display format for a
               given channel handle.
               """,
               notes="""
               The returned format is one of the :def:`DB_CHAN_FORMAT`.
               The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`
               """,
               return_type=Type.INT32_T,
               return_doc="Channel display format",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle")
               ]),

        Method('iGetChanInt_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get individual elements in a channel.",
               notes="""
               These methods are slow and should only be used when
               performance is not an issue.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               Value, or dummy if out of range.
               For settings, terminates if error.
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="channel"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="index")
               ]),

        Method('IGetChanLabel_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method gets a channel's label",
               notes="""
               The channel label is stored in the "LABEL" parameter
               of the channel reg.  If the setting is empty, the
               channel name is returned.
               The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="returned label into"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="size of string")
               ]),

        Method('IGetChanName_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method Gets a channel's name for a
               given channel handle.
               """,
               notes="The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="string to place name into"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="maximum length of string, should be :def_val:`DB_SYMB_NAME_SIZE` to hold all possible channel names.")
               ]),

        Method('iGetChanProtect_DB', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="This method gets a channel's read-only protection status.",
               notes="The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.INT32_T,
               return_doc=":def:`DB_CHAN_PROTECTION`",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle")
               ]),

        Method('iGetChanType_DB', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="""
               This method Gets a channel's type for a
               given channel handle.
               """,
               notes="""
               The type returned is one of the :def:`DB_CATEGORY_CHAN`.
               Use the GS_SIMPLE_TYPE() macro to convert to INT,REAL
               or string types.
               The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`
               """,
               return_type=Type.INT32_T,
               return_doc="Channel type",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle")
               ]),

        Method('IGetChanUnit_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method Gets a channel's unit",
               notes="""
               The unit label is stored in the "UNITS" parameter
               of the channel reg.
               The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="string to place unit into"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="size of string")
               ]),

        Method('iGetChanWidth_DB', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="""
               This method gets a channel's display width for a
               given channel handle.
               """,
               notes="The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.INT32_T,
               return_doc="Channel display width",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle")
               ]),

        Method('IGetName_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets a name from the database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DB_NAME`"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="name returned"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="string size")
               ]),

        Method('iGetRegSymbSetting_DB', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get an integer-valued :class:`REG` setting from a symbol reg",
               notes="""
               Same as :func:`GetRegSymbSetting_DB`, but converts
               the setting automatically to an integer value.
               
               This is a convenient but low-performance way to get/set :class:`REG`
               settings.  If performance is an issue, and more than one
               setting is to be Get and or Set, use the :class:`REG` directly.
               """,
               return_type=Type.INT32_T,
               return_doc="The setting, or :def_val:`iDUMMY` if not found or not convertable.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol, :def_val:`NULLSYMB` for the database :class:`REG`"),
                   Parameter('p3', type=Type.STRING,
                             doc=":class:`REG` entry name")
               ]),

        Method('IGetSymbName_DB', module='geoengine.core', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="This method gets a symbol's name",
               notes="""
               See GetChanName_DB for more information
               The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol handle"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="string to place name into"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="maximum length of string, should be :def_val:`DB_SYMB_NAME_SIZE` to hold all possible channel names.")
               ]),

        Method('iHaveITR_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns TRUE if channel has an :class:`ITR`.",
               notes="""
               If a channel has an :class:`ITR`, the :class:`ITR` colours are  used to
               display channel values in the spreadsheet.
               
               If a channel does not have an :class:`ITR`, :func:`GetITR_DB` will not change
               the passed :class:`ITR`.
               """,
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel")
               ]),

        Method('IiCoordPair_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the matching coordinate pair of a channel.",
               notes="""
               If the channel does not have a matching coordinate
               pair, or of the channel does not exist, the returned
               string will be empty.
               """,
               return_type=Type.INT32_T,
               return_doc=":def:`DB_COORDPAIR`",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Shared Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="channel name"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="string in which to place paired channel name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="string length")
               ]),

        Method('iLinesMax_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Gets Maximum number of lines in the database",
               return_type=Type.INT32_T,
               return_doc="Maximum number of lines in the database",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object")
               ]),

        Method('iUsersMax_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Gets Maximum number of Users",
               return_type=Type.INT32_T,
               return_doc="Maximum number of Users",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object")
               ]),

        Method('MakerSymb_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Adds a Maker to the database symbol",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol to create maker for"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of program"),
                   Parameter('p4', type=Type.STRING,
                             doc="Maker name, used in menu prompt"),
                   Parameter('p5', type=Type.STRING,
                             doc='INI groups (terminate each with a ";")')
               ]),

        Method('PutChanVV_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Place the contents of a :class:`VV` in a channel.",
               notes="""
               If a :class:`VA` channel is specified, then element [0] of this
               :class:`VA` channel will be populated with the :class:`VV`.
               
               There is a limit of 2000 elements for non-licensed users.
               """,
               see_also=":class:`VV` class.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` from which to get the data")
               ]),

        Method('PutVaChanVV_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.LICENSED, 
               doc="Place the contents of a :class:`VV` at a specific part of a channel.",
               notes="""
               If a :class:`VA` channel is specified, then element [0] of this
               :class:`VA` channel will be populated with the :class:`VV`.
               """,
               see_also=":class:`VV` class.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` from which to get the data"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Offset"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Number to Write")
               ]),

        Method('ReadBlobBF_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Read a blob from a database into a file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc=":class:`DB` handle"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Blob (:def_val:`DB_SYMB_BLOB`) to read into :class:`BF` from database"),
                   Parameter('p3', type="BF",
                             doc="File to read blob from")
               ]),

        Method('rGetChanReal_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get individual elements in a channel.",
               notes="""
               These methods are slow and should only be used when
               performance is not an issue.
               """,
               return_type=Type.DOUBLE,
               return_doc="""
               Value, or dummy if out of range.
               For settings, terminates if error.
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="channel"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="index")
               ]),

        Method('rGetRegSymbSetting_DB', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get a real-valued :class:`REG` setting from a symbol reg",
               notes="""
               Same as :func:`GetRegSymbSetting_DB`, but converts
               the setting automatically to a real value.
               
               This is a convenient but low-performance way to get/set :class:`REG`
               settings.  If performance is an issue, and more than one
               setting is to be Get and or Set, use the :class:`REG` directly.
               """,
               return_type=Type.DOUBLE,
               return_doc="The setting, or :def_val:`rDUMMY` if not found or not convertable.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol, :def_val:`NULLSYMB` for the database :class:`REG`"),
                   Parameter('p3', type=Type.STRING,
                             doc=":class:`REG` entry name")
               ]),

        Method('SetAllChanProtect_DB', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="This method sets all the channels' read-only protection status.",
               notes="""
               Value to set must be either :def_val:`DB_CHAN_PROTECTED` or
               :def_val:`DB_CHAN_UNPROTECTED`
               This method does its own channel locking/unlocking.
               Channels already lock :def_val:`DB_LOCK_READONLY` are ignored.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DB_CHAN_PROTECTION`")
               ]),

        Method('SetChanClass_DB', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Set a channel class",
               notes="""
               The channel class is stored in the "CLASS" parameter
               of the channel reg.
               The channel must be locked :def_val:`DB_LOCK_READWRITE`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle"),
                   Parameter('p3', type=Type.STRING,
                             doc="class")
               ]),

        Method('SetChanDecimal_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method sets a channel's number of digits displayed
               to the right of the decimal point.
               """,
               notes="""
               The number of display digits must be from 0 to 50.
               The channel must be locked :def_val:`DB_LOCK_READWRITE`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Number of digits to display right of the decimal")
               ]),

        Method('SetChanFormat_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method sets a channel's display format.",
               notes="The channel must be locked :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_CHAN_FORMAT`")
               ]),

        Method('SetChanInt_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set individual elements in a channel.",
               notes="""
               These methods are slow and should only be used when
               performance is not an issue.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="channel"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="index"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="value")
               ]),

        Method('SetChanLabel_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a channel label",
               notes="""
               The channel label is stored in the "LABEL" parameter
               of the channel reg.
               The channel must be locked :def_val:`DB_LOCK_READWRITE`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle"),
                   Parameter('p3', type=Type.STRING,
                             doc="label")
               ]),

        Method('SetChanName_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method sets a channel's name.",
               notes="The channel must be locked :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle"),
                   Parameter('p3', type=Type.STRING,
                             doc="string to set channel name to")
               ]),

        Method('SetChanProtect_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method sets a channel's read-only protection
               status.
               """,
               notes="""
               Value to set must be either :def_val:`DB_CHAN_PROTECTED` or
               :def_val:`DB_CHAN_UNPROTECTED`
               The channel must be locked :def_val:`DB_LOCK_READWRITE`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_CHAN_PROTECTION`")
               ]),

        Method('SetChanReal_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set individual elements in a channel.",
               notes="""
               These methods are slow and should only be used when
               performance is not an issue.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="channel"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="index"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="value")
               ]),

        Method('SetChanStr_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set individual elements in a channel.",
               notes="""
               These methods are slow and should only be used when
               performance is not an issue.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="channel"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="index"),
                   Parameter('p5', type=Type.STRING)
               ]),

        Method('SetChanUnit_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method sets a channel's unit for a
               given channel handle.
               """,
               notes="The channel must be locked :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle"),
                   Parameter('p3', type=Type.STRING,
                             doc="string to put channel unit")
               ]),

        Method('SetChanWidth_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method sets a channel's display width",
               notes="""
               The number of display digits must be from 0 to 50.
               The channel must be locked :def_val:`DB_LOCK_READWRITE`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Display width")
               ]),

        Method('SetIPJ_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a :class:`REG` object into a symbol",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Shared Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="X channel"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Y channel"),
                   Parameter('p4', type="IPJ")
               ]),

        Method('SetITR_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set :class:`ITR` for a channel.",
               notes="""
               Use :def_val:`ITR_NULL` to clear the channel :class:`ITR`.
               Channel must be locked for READONLY or READWRITE.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel"),
                   Parameter('p3', type="ITR",
                             doc=":class:`ITR` to fill in")
               ]),

        Method('SetRegSymb_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a :class:`REG` object into a symbol",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Shared Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol, :def_val:`NULLSYMB` for the database :class:`REG`"),
                   Parameter('p3', type="REG",
                             doc=":class:`REG` to set into Blob")
               ]),

        Method('SetRegSymbSetting_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a :class:`REG` string setting in a symbol reg",
               notes="""
               The symbol :class:`REG` is used to store a variety of attribute
               about the symbol.  Following a conventionally used entries:
               
               UNITS                   - channel units
               CLASS                   - symbol class name (i.e. "Assay")
               _PJ_ipj                 - projection blob name
               _PJ_x                   - projection coordinate pair
               _PJ_y
               _PJ_name                - projection GXF-style info
               _PJ_ellipsoid
               _PJ_projection
               _PJ_units
               _PJ_datum_transform
               
               This is a convenient but low-performance way to get/set :class:`REG`
               settings.  If performance is an issue, and more than one
               setting is to be Get and or Set, use the :class:`REG` directly.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Shared Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol, :def_val:`NULLSYMB` for the database :class:`REG`"),
                   Parameter('p3', type=Type.STRING,
                             doc=":class:`REG` entry name"),
                   Parameter('p4', type=Type.STRING,
                             doc="setting")
               ]),

        Method('WriteBlobBF_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Write a blob from a file into a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc=":class:`DB` handle"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Blob (:def_val:`DB_SYMB_BLOB`) to write into database from file"),
                   Parameter('p3', type="BF",
                             doc="File to write blob into")
               ])
    ],
    'Control': [

        Method('Commit_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method forces all changes to the database to be saved.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ]),

        Method('Compact_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="""
               Removes any extra space from the database. This will
               reduce the database to its smallest size.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ]),

        Method('Create_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method makes a brand new database of the specified size.
               The database is opened in ReadWrite Mode.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of the Database File to Create"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Max Lines in the Database    (200)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Max Channels in the Database (50)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Max Blobs in the Database    (Channels+Lines+20)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Max Users in the Database    (10)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Number of Erase Caches       (100)"),
                   Parameter('p7', type=Type.STRING,
                             doc='Name of the Super User       "SUPER"'),
                   Parameter('p8', type=Type.STRING,
                             doc='Password of the Super User   ""')
               ]),

        Method('CreateComp_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method makes a brand new database of the specified size.
               The database is opened in ReadWrite Mode. Also allows you to
               set paging size and the Compression Level.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of the Database File to Create"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Max Lines in the Database    (200)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Max Channels in the Database (50)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Max Blobs in the Database    (Channels+Lines+20)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Max Users in the Database    (10)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Number of Erase Caches       (100)"),
                   Parameter('p7', type=Type.STRING,
                             doc='Name of the Super User       "SUPER"'),
                   Parameter('p8', type=Type.STRING,
                             doc='Password of the Super User   ""'),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Page Size Must be (64,128,256,512,1024,2048,4096) normally 1024"),
                   Parameter('p10', type=Type.INT32_T,
                             doc=":def:`DB_COMP`")
               ]),

        Method('CreateEx_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method makes a brand new database of the specified size.
               The database is opened in ReadWrite Mode. Also allows you to
               set paging size.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of the Database File to Create"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Max Lines in the Database    (200)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Max Channels in the Database (50)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Max Blobs in the Database    (Channels+Lines+20)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Max Users in the Database    (10)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Number of Erase Caches       (100)"),
                   Parameter('p7', type=Type.STRING,
                             doc='Name of the Super User       "SUPER"'),
                   Parameter('p8', type=Type.STRING,
                             doc='Password of the Super User   ""'),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Page Size Must be (64,128,256,512,1024,2048,4096) normally 1024")
               ]),

        Method('DelLine0_DB', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Delete Empty Line 0.",
               notes="""
               A new database is created with a single, empty line L0, but many processes
               create databases then create their own lines, so the empty line L0 may remain
               after the process finishes. This function will delete a line L0
               a) If it exists and is empty
               b) It is not the only line in the database.
               """,
               see_also=":func:`DelLine0_EDB` - deletes an empty line 0 from the currently edited database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB")
               ]),

        Method('Destroy_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method closes a database and destroys the :class:`DB` object.",
               notes="""
               This method has been largely superceded by the use of the :class:`EDB` object,
               which when locked returns a :class:`DB` object that must NOT be destroyed.
               
               EData = :func:`Current_EDB`();       // get current edited database
               Data = :func:`Lock_EDB`(EData);      // lock the database
               ... (Process using the :class:`DB` object Data)
               :func:`UnLock_EDB`(EData);           // unlock the database
               
               It may still be reasonably used to destroy a :class:`DB` handle returned when
               a database is opened using a call to :func:`Open_DB`().
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database to Destroy")
               ]),

        Method('Discard_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method discards all changes made to the database since
               the last commit or opening.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ]),

        Method('Grow_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Enlarges the database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of the Database File to Create"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Max Lines in the Database    (200)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Max Channels in the Database (50)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Max Blobs in the Database    (Channels+Lines+20)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Max Users in the Database    (10)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Number of Erase Caches       (100)")
               ]),

        Method('iCanOpen_DB', module='geoengine.core', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="This method checks whether it is possible to open a database.",
               notes="""
               This method is useful to determine if another session already locked a database.
               By using this method before an :func:`Open_DB` a GX may handle errors like this more gracefully.
               """,
               see_also=":func:`Open_DB`, :func:`OpenReadOnly_DB`, :func:`iCanOpenReadOnly_DB`",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of the Database File to Open"),
                   Parameter('p2', type=Type.STRING,
                             doc='Name of the user ("SUPER" normally)'),
                   Parameter('p3', type=Type.STRING,
                             doc='Password of the user ("" normally)')
               ]),

        Method('iCanOpenReadOnly_DB', module='geoengine.core', version='6.4.2',
               availability=Availability.PUBLIC, 
               doc="This method checks whether it is possible to open a database in read-only mode.",
               notes="""
               This method is useful to determine if another session already locked a database.
               By using this method before an :func:`OpenReadOnly_DB` a GX may handle errors like this more gracefully.
               """,
               see_also=":func:`Open_DB`, :func:`OpenReadOnly_DB`, :func:`iCanOpen_DB`",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of the Database File to Open"),
                   Parameter('p2', type=Type.STRING,
                             doc='Name of the user ("SUPER" normally)'),
                   Parameter('p3', type=Type.STRING,
                             doc='Password of the user ("" normally)')
               ]),

        Method('iCheck_DB', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="""
               Does an integrity check of the data in the database to
               ensure it is valid.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Invalid Blocks in the Database
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ]),

        Method('iIsEmpty_DB', module='geoengine.core', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="See if a database contains only empty lines.",
               notes="""
               This function does not check for other information or blobs,
               it merely looks at all lines in the database to see if they
               are empty. If all are empty, it returns 1.
               """,
               return_type=Type.INT32_T,
               return_doc="1 if the database contains only empty lines.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ]),

        Method('iIsLineEmpty_DB', module='geoengine.core', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="See if a specific line in the database is empty.",
               return_type=Type.INT32_T,
               return_doc="1 if the database contains only empty lines.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line symbol")
               ]),

        Method('Open_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method opens a database.",
               see_also=":func:`OpenReadOnly_DB`, :func:`iCanOpen_DB`, :func:`iCanOpenReadOnly_DB`",
               return_type="DB",
               return_doc=":class:`DB` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of the Database File to Open"),
                   Parameter('p2', type=Type.STRING,
                             doc='Name of the user ("SUPER" normally)'),
                   Parameter('p3', type=Type.STRING,
                             doc='Password of the user ("" normally)')
               ]),

        Method('OpenReadOnly_DB', module='geoengine.core', version='6.4.2',
               availability=Availability.PUBLIC, 
               doc="This method opens a database.",
               notes="""
               This method is useful to open multiple reader instances on the same database. This call will fail
               if a :class:`DB` has already been opened with :func:`Open_DB` or locked in the application with :func:`Lock_EDB`.
               """,
               see_also=":func:`Open_DB`, :func:`iCanOpen_DB`, :func:`iCanOpenReadOnly_DB`",
               return_type="DB",
               return_doc=":class:`DB` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of the Database File to Open"),
                   Parameter('p2', type=Type.STRING,
                             doc='Name of the user ("SUPER" normally)'),
                   Parameter('p3', type=Type.STRING,
                             doc='Password of the user ("" normally)')
               ]),

        Method('Repair_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Cleans the database by removing invalid blocks",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of the Database File to Create")
               ]),

        Method('Sync_DB', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Syncronize the Metadata from this database to the XML",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ])
    ],
    'Data': [

        Method('CopyData_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method copies the data from one channel to another on
               on the specified line. The data is converted if such
               conversion in neccessary.
               """,
               notes="""
               All the data in the destination channel is destroyed along
               with the fiducial start and increment.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel to Copy Data From"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Channel to Copy Data To")
               ]),

        Method('iGetColVA_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the # of columns in a :class:`VA` channel.",
               notes="If the channel is :class:`VV`, this function returns 1.",
               return_type=Type.INT32_T,
               return_doc="""
               # of columns
               0 if error
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel (read locked)")
               ]),

        Method('iGetChannelLength_DB', module='geoengine.core', version='8.1.0',
               availability=Availability.PUBLIC, 
               doc="Returns the # of elements in a channel.",
               notes="""
               Returns the actual number of data items (rows) in a channel. For :class:`VA` channels no correction is
               necessary for the number of columns (which was true of the obsoleted function :func:`iGetLength_DB`).
               """,
               return_type=Type.INT32_T,
               return_doc="# of elements",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line    (read or write locked)"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel (read or write locked)")
               ]),

        Method('rGetFidIncr_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method returns the fiducial increment value of a
               specified Channel.
               """,
               return_type=Type.DOUBLE,
               return_doc="Fiducial Start.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line (read or write locked)"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel (read locked)")
               ]),

        Method('rGetFidStart_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method returns the fiducial start value of a
               specified Channel.
               """,
               return_type=Type.DOUBLE,
               return_doc="Fiducial Start.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line (read or write locked)"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel (read locked)")
               ]),

        Method('SetFid_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method allows the user to set the fiducial start and
               increment of a channel. The Increment should never be 0.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line (read or write locked)"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel to set fiducial (write locked)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Start Fiducial Value"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Increment Fiducial Value")
               ]),

        Method('WindowVACh_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy a window of data in a channel into a new channel",
               notes="""
               This function normally used for :class:`VA` channels. A copy of the
               original channel will be made if start and end column
               numbers to copy are dummies.
               All the columns including start and end columns will be copied
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Original channel"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Output channel"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Start column number to copy, 0 is first column"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="End column number to copy")
               ]),

        Method('WindowVACh2_DB', module='geoengine.core', version='5.0.1',
               availability=Availability.PUBLIC, 
               doc="Copy a windowed version of data in a channel into a new channel",
               notes="""
               Similar to :func:`WindowVACh_DB`, but the input and output channels must
               contain the same number of columns. The input :class:`VV` tells which columns
               to copy over; 0 values indicate that the output column is to be
               dummied, and non-zero values indicate the column is to be copied.
               The :class:`VV` length must be the same as the number of columns.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Original channel"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Output channel"),
                   Parameter('p5', type="VV",
                             doc=":class:`VV` containing 0/1 values for each channel.")
               ])
    ],
    'Line': [

        Method('SetLineSelection_DB', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the selection status for a line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Handle of line to select/deselect"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_LINE_SELECT`")
               ]),

        Method('iGetLineSelection_DB', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the selection status for a line.",
               return_type=Type.INT32_T,
               return_doc="One of :def:`DB_LINE_SELECT`",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle")
               ]),

        Method('FirstSelLine_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method will return a handle to the first selected
               line in the database.
               """,
               return_type="DB_SYMB",
               return_doc="Line Handle (use iIsLineValid method to see if valid)",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ]),

        Method('GetLineMapFid_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="This method gets a line map clip fiducial.",
               notes="The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle to look at"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Start Fid"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="End Fid")
               ]),

        Method('GetSelect_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the Line Selections.",
               return_type="DB_SELECT",
               return_doc="Selections Object.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ]),

        Method('iCountSelLines_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method counts the number of selected lines in
               the database.
               """,
               return_type=Type.INT32_T,
               return_doc="x - Number of selected lines in the database",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ]),

        Method('iIsChanName_DB', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Is this a valid channel name?",
               notes="""
               Channel names must only contain alpha-numeric characters or the
               underscore character "_", and the first letter must be a letter
               or an underscore.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               1 if it is a valid channel name
               0 if it is not a valid channel name
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name to test")
               ]),

        Method('iIsChanValid_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="""
               This method checks to see if the channel handle is a
               valid channel.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Not a valid channel
               1 - Valid
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle to check")
               ]),

        Method('iIsLineName_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Is this a valid line name.",
               return_type=Type.INT32_T,
               return_doc="""
               1 if it is a valid line name
               0 if it is not a valid line name
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name to test")
               ]),

        Method('iIsLineValid_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method checks to see if the line handle returned by
               the Line methods is a valid line.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Not a valid line
               1 - Valid
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle to check")
               ]),

        Method('iLineCategory_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method returns the category (group, line) of a line.",
               notes="The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.INT32_T,
               return_doc=":def:`DB_CATEGORY_LINE` or :def_val:`iDUMMY`.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle to look at")
               ]),

        Method('iLineFlight_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method returns the flight number of a line.",
               notes="The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.INT32_T,
               return_doc="Line Flight Number.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle to look at")
               ]),

        Method('ILineLabel_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a line label",
               notes="""
               Label formats.
               
               example full format is
               "L1023.4 13"   type "L"
               number "1023"
               version "4"
               flight "13"
               
               formats can be added to get combined format
               
               Use LINK format to create a database link label.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line symbol"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="string in which to place label"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="string length"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DB_LINE_LABEL_FORMAT`")
               ]),

        Method('iLineNumber_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method returns the number of a line.",
               notes="The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.INT32_T,
               return_doc="Line Number.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle to look at")
               ]),

        Method('ILineNumber2_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the string form of the line number (can be alphanumeric)",
               notes="The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle to look at"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Line number"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Line number buffer size")
               ]),

        Method('iLineType_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method returns the type of a line.",
               notes="The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.INT32_T,
               return_doc=":def:`DB_LINE_TYPE`",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle to look at")
               ]),

        Method('iLineVersion_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method returns the version number of a line.",
               notes="The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.INT32_T,
               return_doc="Line Number.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle to look at")
               ]),

        Method('ISetLineName_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method sets up a line name given the line's number,
               type, and version.
               """,
               notes="""
               This MUST be called to generate a line name when calls
               are made to :func:`iExistSymb_DB`, :func:`CreateSymb_DB` or :func:`DeleteSymb_DB`
               for an operation on a line.
               See also SetLineName2_DB.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Line number"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Line type"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Line version"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="String to set line name to"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Maximum length of string")
               ]),

        Method('ISetLineName2_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Like SetLineName_DB, but can use alphanumeric for line number",
               notes="""
               This MUST be called to generate a line name when calls
               are made to :func:`iExistSymb_DB`, :func:`CreateSymb_DB` or :func:`DeleteSymb_DB`
               for an operation on a line.
               The line number can be any combination of letters and numbers,
               i.e. XU324, 98765, A, 23NGV etc.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Line number (alphanumeric)"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Line type"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Line version"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="String to set line name to"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Maximum length of string")
               ]),

        Method('LoadSelect_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Load selections to from a file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('NextSelLine_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method will advance to the next selected line based
               on the currently selected line handle.
               """,
               return_type="DB_SYMB",
               return_doc="Line Handle (use iIsLineValid method to see if valid).",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Previous Line")
               ]),

        Method('rLineBearing_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="This method returns the bearing of a line.",
               notes="""
               The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`
               
               This function simply returns a value set using the :func:`SetLineBearing_DB`
               function. It returns :def_val:`rDUMMY` for line categories other than
               :def_val:`DB_CATEGORY_LINE_FLIGHT`.
               
               To calculate the line azimuth based on the first and
               last non-dummy locations, use the :func:`rDirection_DU` function.
               """,
               see_also=":func:`SetLineBearing_DB`, :func:`rDirection_DU`",
               return_type=Type.DOUBLE,
               return_doc="Bearing value, :def_val:`rDUMMY` if not set.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle to look at")
               ]),

        Method('rLineDate_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method returns the date of a line.",
               notes="The channel must be locked :def_val:`DB_LOCK_READONLY` or :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.DOUBLE,
               return_doc="Date value.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle to look at")
               ]),

        Method('SaveSelect_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Saves current selections to a file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('Select_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Select/deselect lines based on selection string",
               notes="""
               Selections/deselections are cumulative. If lines had already
               been selected, then any further selection/deselection will
               affect that set of selections.
               
               E.g. "L99:800" is the string to select all normal lines from
               99 to 800. If :func:`Select_DB` is called again to select "L1000",
               then lines 99 to 800 and 1000 would all be selected.
               
               Use a "T" prefix for Tie lines.
               Use an "F" prefix to specify lines of a specific flight.
               E.g. "F10" would select all lines of flight 10.
               Use an empty string ("") to select/deselect ALL lines.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Selection"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_LINE_SELECT`")
               ]),

        Method('SetLineBearing_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Sets a line's bearing.",
               notes="""
               The channel must be locked :def_val:`DB_LOCK_READWRITE`
               
               This function simply sets a value in the line's metadata
               that is retrieved using the :func:`rLineBearing_DB`
               function. It terminates for line categories other than
               :def_val:`DB_CATEGORY_LINE_FLIGHT`.
               """,
               see_also=":func:`rLineBearing_DB`, :func:`rDirection_DU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Value to set bearing to")
               ]),

        Method('SetLineDate_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method sets a line's date.",
               notes="The channel must be locked :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Value to set date to")
               ]),

        Method('SetLineFlight_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method sets a line's flight.",
               notes="The channel must be locked :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Value to set line flight to")
               ]),

        Method('SetLineMapFid_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method changes a line map clip fiducial.",
               notes="""
               for full range, set Start Fid to :def_val:`rMIN` and End Fid to :def_val:`rMAX`.
               for no data, set Start and End Fids to :def_val:`rDUMMY`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle to look at"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Start Fid"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="End Fid")
               ]),

        Method('SetLineNum_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method sets a line's number.",
               notes="The channel must be locked :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Value to set line number to")
               ]),

        Method('SetLineType_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method sets a line's type.",
               notes="The channel must be locked :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_LINE_TYPE`")
               ]),

        Method('SetLineVer_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method sets a line's version.",
               notes="The channel must be locked :def_val:`DB_LOCK_READWRITE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Value to set line version to")
               ]),

        Method('SetSelect_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the Line Selections.",
               notes="This method also destroys the DB_SELECT object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SELECT",
                             doc="Selections")
               ])
    ],
    'META': [

        Method('GetMETA_DB', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Get the metadata of a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="META",
                             doc="Meta object to fill with database's meta")
               ]),

        Method('SetMETA_DB', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Set the metadata of a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="source :class:`DB`"),
                   Parameter('p2', type="META",
                             doc="Meta object to add to database's meta")
               ])
    ],
    'Symbols': [

        Method('ArrayLST_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`LST` object with array (:class:`VA`) channel symbols.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="LST",
                             doc="List to Populate")
               ]),

        Method('ArraySizeLST_DB', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`LST` object with array (:class:`VA`) channel symbols with a particular number of columns.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Number of columns in array ( > 1 )"),
                   Parameter('p3', type="LST",
                             doc="List to Populate")
               ]),

        Method('ChanLST_DB', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`LST` with database channels.",
               notes="""
               Populates a :class:`LST` with channel symbols.
               The name is put into the "Name" part of the :class:`LST` (0),
               and the handle, an integer value written as a string, is
               placed in the value part of the :class:`LST` (1).
               Array channels are included, as well as virtual channels (array channel single columns loaded in the database like \\"Chan[1]\\".
               
               The :class:`LST` is cleared first, and the items are sorted by name.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="LST",
                             doc="List to Populate")
               ]),

        Method('NormalChanLST_DB', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`LST` with non-array database channels.",
               notes="Like :func:`ChanLST_DB`, but does not include array channels or virtual channels.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="LST",
                             doc="List to Populate")
               ]),

        Method('ClassChanLST_DB', module='geoengine.core', version='5.0.3',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`LST` with channels in a particular class.",
               notes="""
               The Name of the symbol is placed in the
               item name and the item value is set to the symbol handle.
               Only channels with the given class name are included,
               e.g. use "ASSAY" for assay channels in :class:`CHIMERA`.
               
               The :class:`LST` is cleared first, and the items are sorted by name.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Database Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object to populate"),
                   Parameter('p3', type=Type.STRING,
                             doc='CLASS name for the channel ("" for all)')
               ]),

        Method('ClassGroupLST_DB', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`LST` with group lines in a particular class.",
               notes="""
               The Name of the symbol is placed in the
               item name and the item value is set to the symbol handle.
               Only group lines with the given class name are included,
               e.g. use "TARGETS" for UX-Detect Target groups.
               
               The :class:`LST` is cleared first, and the items are sorted by name.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Database Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object to populate"),
                   Parameter('p3', type=Type.STRING,
                             doc='CLASS name for the group ("" for all)')
               ]),

        Method('CreateSymb_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a new Symbol.",
               notes="""
               If symbol already exits, and it is the same type
               simply returns a handle to the existing symbol.
               
               This method simple calls :func:`CreateSymbEx_DB` with the
               extra info set to 1.
               
               STRING-type channels: To create a string-type channel,
               enter a negative number for the channel category below.
               For instance, "-32" will create a string channel with
               32 characters per item.
               
               BLOBS: Blobs (Binary Large Objects) can be used for storing
               miscellaneous data which does not fit well into any of the
               other various storage objects, such as a :class:`REG`. Generally,
               one or more objects is serialized to a :class:`BF` object, which
               is then written to the blob using the sWriteBlobBF_DB()
               function. Retrieval is done in the reverse order, using
               sWriteBlobBF_DB() first, then extracting the objects from the
               :class:`BF` object.
               To avoid namespace problems, Geosoft reserves the following
               name prefixes:
               
               OE.   (Core functions)
               GS.   (Applications)
               CS.   (Custom Solutions applications)
               
               Programmers should avoid using the above prefixes as the starting
               letters of their blob names to avoid any possible conflicts.
               """,
               return_type="DB_SYMB",
               return_doc="DB_SYMB Object",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Symbol Name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_SYMB_TYPE`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DB_OWN`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DB_CATEGORY_USER`, :def:`DB_CATEGORY_LINE`, :def:`DB_CATEGORY_CHAN`, :def:`DB_CATEGORY_BLOB`")
               ]),

        Method('CreateSymbEx_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a new Symbol.",
               notes="""
               If symbol already exits it is returned.
               
               STRING-type channels: To create a string-type channel,
               enter a negative number for the channel category below.
               For instance, "-32" will create a string channel with
               32 characters per item.
               
               Symbol name for :def_val:`DB_CATEGORY_LINE_FLIGHT` must conform to
               the following line naming syntax:
               
               [type][number.version:flight]
               
               Type can be: L - normal line
               B - base line
               T - tie line
               R - trend line
               S - test line
               P - special line
               
               Examples: L100,
               T100.1:16
               
               Note the "Flight" is any whole number that may be useful
               to differentiate processing tasks.
               
               The ability to create a :class:`VA` channel is not available in the
               free interface and requires a Montaj license.
               """,
               return_type="DB_SYMB",
               return_doc="DB_SYMB handle.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Symbol Name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_SYMB_TYPE`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DB_OWN`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DB_CATEGORY_USER`, :def:`DB_CATEGORY_LINE`, :def:`DB_CATEGORY_CHAN`, :def:`DB_CATEGORY_BLOB`"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Extra info, which depends on :def:`DB_SYMB_TYPE` :def_val:`DB_SYMB_CHAN` - element width for a :class:`VA` channel ignores for all other :def:`DB_SYMB_TYPE` types")
               ]),

        Method('CSVChanLST_DB', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`LST` with channels in a comma-separated list.",
               notes="""
               The Name of the symbol is placed in the
               item name and the item value is set to the symbol handle.
               Only channels in the list which are present in the database
               are included.
               
               The :class:`LST` is cleared first.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Database Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object to populate"),
                   Parameter('p3', type=Type.STRING,
                             doc="comma-separated list of channels")
               ]),

        Method('DeleteSymb_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method destroys a symbol in the database and all
               the data associated with it. The symbol's lock is
               automatically removed.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol to Delete (must be READWRITE locked)")
               ]),

        Method('DupLineSymb_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Duplicate a line symbol from a group or line symbol.
               The new name must not already exist in the database.
               """,
               return_type="DB_SYMB",
               return_doc="New Symbol Handle",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol Handle to duplicate"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of the New Symbol")
               ]),

        Method('DupSymb_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="New Symbol by duplicating an existing symbol, LOCKED",
               notes="""
               The symbol will be locked READWRITE.
               The new name must not already exist in the database.
               """,
               see_also=":func:`DupSymbNoLock_DB`",
               return_type="DB_SYMB",
               return_doc="New Symbol Handle",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol Handle to duplicate"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of the New Symbol")
               ]),

        Method('DupSymbNoLock_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="New Symbol by duplicating an existing symbol, NO LOCK.",
               notes="""
               The symbol will be NOT be locked.
               The new name must not already exist in the database.
               """,
               see_also=":func:`DupSymb_DB`",
               return_type="DB_SYMB",
               return_doc="New Symbol Handle",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol Handle to duplicate"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of the New Symbol")
               ]),

        Method('FindChan_DB', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Get handle to the specified channel.",
               notes="""
               To work with a specific column from a :class:`VA` channel,
               specify the :class:`VA` element number in square brackets as part
               of the :class:`VA` channel name (e.g. "EM[3]" will treat the fourth
               column of the :class:`VA` channel as a :class:`VV`).
               
               See notes for :func:`FindSymb_DB`.
               Introduced in v5.1.3.
               The new :func:`FindChan_DB` searches using the exact channel name.
               """,
               return_type="DB_SYMB",
               return_doc="Channel Handle, :def_val:`NULLSYMB` if not defined",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of channel")
               ]),

        Method('FindSymb_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get handle to the specified symbol.",
               notes="""
               To work with a specific column from a :class:`VA` channel,
               specify the :class:`VA` element number in square brackets as part
               of the :class:`VA` channel name (e.g. "EM[3]" will treat the fourth
               column of the :class:`VA` channel as a :class:`VV`).
               
               For backward compatibility with GXs not employing the
               :func:`GetXYZChanSymb_DB` function, the following behaviour has
               been introduced as of v5.1.3:  (also true for "Y").
               
               :func:`FindSymb_DB`(hDB, "X", :def_val:`DB_SYMB_CHAN`) is now equivalent to:
               
               :func:`GetXYZChanSymb_DB`(hDB, :def_val:`DB_CHAN_X`);
               
               In other words, the current X or Y is searched for, not
               necessarily the literal "X" or "Y". This ensures that newer
               databases, which might have "Easting" and "Northing"
               (or other similar names) instead of "X" and "Y" will still
               work with older GXs expecting "X" and "Y".
               
               The new :func:`FindChan_DB` searches using the exact channel name.
               """,
               return_type="DB_SYMB",
               return_doc="Symbol Handle, :def_val:`NULLSYMB` if not defined",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of symbol"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_SYMB_TYPE`")
               ]),

        Method('GetChanOrderLST_DB', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="""
               This method gets the channel display order for a
               database. The list will be stored in an :class:`LST` object.
               In order to modify this displayed channels list,
               call :func:`SetChanOrderLST_DB` after.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object to populate")
               ]),

        Method('GetXYZChanSymb_DB', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Searches for current X, Y or Z channel symbol",
               return_type="DB_SYMB",
               return_doc="""
               x - Symbol Handle
               :def_val:`NULLSYMB` - Symbol not found
               
               searches for the "current" X, Y or Z channel.
               If none is defined, then looks for "X", "Y" or "Z" channel
               If the channel is defined, but not present, returns :def_val:`NULLSYMB`.
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Database object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DB_CHAN_SYMBOL`")
               ]),

        Method('iClassChanList_DB', module='geoengine.core', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Place a list of channels for a given class in a :class:`VV`.",
               notes="""
               This method generates a list of symbols in the database
               and places their handles into a :class:`VV`. The list is not
               sorted.
               Only channels with the given class name are included,
               e.g. use "ASSAY" for assay channels used in :class:`CHIMERA`.
               """,
               return_type=Type.INT32_T,
               return_doc="Number of symbols.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` to populate, must be type INT."),
                   Parameter('p3', type=Type.STRING,
                             doc='Class name to match ("" for all)')
               ]),

        Method('iExistChan_DB', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="See if the specified channel exists in the database.",
               notes="""
               See notes for :func:`iExistSymb_DB`.
               Introduced in v5.1.3.
               :func:`iExistChan_DB` searches using the exact channel name.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Symbol does not exist in the database
               1 - Symbol Exists
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of Channel")
               ]),

        Method('iExistSymb_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method checks to see if the specified symbol exists
               in the database.
               """,
               notes="""
               For backward compatibility with GXs not employing the
               GetXYZChan_DB function, the following behaviour has
               been introduced as of v5.1.3:  (also true for "Y").
               
               :func:`iExistSymb_DB`(hDB, "X", :def_val:`DB_SYMB_CHAN`) is now equivalent to:
               
               GetXYZChan_DB(hDB, :def_val:`DB_CHAN_X`, sXCh);
               :func:`iExistSymb_DB`(hDB, sXCh, :def_val:`DB_SYMB_CHAN`);
               
               In other words, the current X or Y is searched for, not
               necessarily the literal "X" or "Y". This ensures that newer
               databases, which might have "Easting" and "Northing"
               (or other similar names) instead of "X" and "Y" will still
               work with older GXs expecting "X" and "Y".
               
               The new :func:`iExistChan_DB` searches using the exact channel name.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Symbol does not exist in the database
               1 - Symbol Exists
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of Symbol"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_SYMB_TYPE`")
               ]),

        Method('iValidSymb_DB', module='geoengine.core', version='9.1.0',
               availability=Availability.PUBLIC, 
               doc="This method checks to see if the specified symbol is a valid symbol in the database.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Invalid symbol 
               1 - Symbol is valid
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol to check"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_SYMB_TYPE`")
               ]),

        Method('iGetSymbLock_DB', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Determines if a symbol is locked",
               return_type=Type.INT32_T,
               return_doc=":def:`DB_LOCK`",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol to Lock")
               ]),

        Method('IGetXYZChan_DB', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Gets current X, Y or Z channel name",
               notes="""
               searches for the "current" X, Y or Z channel.
               If none is defined, then returns "X", "Y" or "Z".
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Database object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DB_CHAN_SYMBOL`"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="returned name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="buffer length")
               ]),

        Method('iSymbList_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Place a list of symbols in a :class:`VV`.",
               return_type=Type.INT32_T,
               return_doc="Number of symbols.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` to populate, must be type INT."),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_SYMB_TYPE`")
               ]),

        Method('LineLST_DB', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`LST` with database lines.",
               notes="""
               Populates a :class:`LST` with channel symbols.
               The name is put into the "Name" part of the :class:`LST` (0),
               and the handle, an integer value written as a string, is
               placed in the value part of the :class:`LST` (1).
               The :class:`LST` is cleared first, and the items are sorted in logical line order.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="LST",
                             doc="List to Populate")
               ]),

        Method('LockSymb_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Locks a symbol for READONLY or READWRITE.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol to Lock"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_LOCK`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DB_WAIT`")
               ]),

        Method('MaskChanLST_DB', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`LST` with mask channels.",
               notes="""
               Loads a :class:`LST` with all channels with CLASS "MASK", as well
               as all channels containing the string "MASK", as long
               as the CLASS for these channels is not set to something
               other than "" or "MASK".
               
               This function is a duplicate of the :func:`MaskChanLST_CHIMERA`
               function, and can be used if :class:`CHIMERA` is not installed.
               
               The :class:`LST` is cleared first, and the items are sorted by name.
               "None" is added at the end, with a handle value of "-1".
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Database Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object to populate")
               ]),

        Method('SelectedLineLST_DB', module='geoengine.core', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`LST` with the selected lines.",
               notes="""
               This method populates a :class:`LST` object with all of the symbols
               of the selected lines in the database.
               The name is put into the "Name" part of the :class:`LST` (0),
               and the handle, an integer value written as a string, is
               placed in the value part of the :class:`LST` (1).
               
               Symbols are automatically sorted in logical line order.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="LST",
                             doc="List to Populate")
               ]),

        Method('SetChanOrderLST_DB', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="""
               This method sets the channel display order for a
               database. The list to modify will be stored in an :class:`LST`
               object. Call :func:`GetChanOrderLST_DB` to populate the :class:`LST`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object to modify")
               ]),

        Method('SetXYZChan_DB', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Sets current X, Y or Z channel name",
               notes="""
               If the value specified is "", the internally stored value
               is cleared, and GetXYZChan_DB will return "X", "Y" or "Z"
               
               This can be used, for instance, to make "Easting" and "Northing"
               the current X and Y channels, and have GXs using the
               :func:`GetXYZChanSymb_DB` function to load "X" and "Y" work as desired.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Database object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DB_CHAN_SYMBOL`"),
                   Parameter('p3', type=Type.STRING,
                             doc="channel name")
               ]),

        Method('StringChanLST_DB', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`LST` with string-type channels.",
               notes="""
               The Name of the symbol is placed in the
               item name and the item value is set to the symbol handle.
               Only channels with the string-type data (sChanType_DB < 0)
               are included.
               
               The :class:`LST` is cleared first, and the items are sorted by name.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Database Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object to populate")
               ]),

        Method('SymbLST_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Populate a :class:`LST` with database symbols.",
               notes="""
               Populates a :class:`LST` with channel, line, blob or user symbols.
               The name is put into the "Name" part of the :class:`LST` (0),
               and the handle, an integer value written as a string, is
               placed in the value part of the :class:`LST` (1).
               
               Line symbols are automatically sorted in logical line order.
               
               NOTE: The :class:`LST` is NOT cleared before being filled. If you
               want to clear the :class:`LST` and get sorted values, use the
               :func:`ChanLST_DB` and :func:`LineLST_DB` functions.
               """,
               see_also=":func:`ChanLST_DB`, :func:`LineLST_DB`, :func:`SelectedLineLST_DB`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="LST",
                             doc="List to Populate"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_SYMB_TYPE`")
               ]),

        Method('UnLockAllSymb_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="UnLocks all symbols.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ]),

        Method('UnLockSymb_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="UnLocks a symbol.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Symbol to Lock")
               ])
    ],
    'VA Channels': [

        Method('AddAssociatedLoad_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add this channel to the auto-load feature of the group.",
               notes="""
               If the channel is not yet associated, it is first associated.
               If the channel is already in the associated-load list, this
               does nothing.
               
               As of v6.0, the load-status of channels is no longer stored
               in the database, but in the project, so this function is
               equivalent to calling :func:`Associate_DB`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Shared Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel")
               ]),

        Method('AddComment_DB', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Add a comment with a string to the activity log of the database.",
               notes="""
               The comment is written in the form:
               
               Comment: String2
               
               and is followed by a carriage return.
               The activity log is created automatically if it does not exist.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Comment"),
                   Parameter('p3', type=Type.STRING,
                             doc="String"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Indent comment one tab? (TRUE or FALSE)")
               ]),

        Method('AddIntComment_DB', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Add a comment with an integer to the activity log of the database.",
               notes="""
               The comment is written in the form:
               
               Comment: Value
               
               and is followed by a carriage return.
               The activity log is created automatically if it does not exist.
               
               See Notes in :func:`AddComment_DB`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Comment"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="value"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Indent comment one tab? :def:`GEO_BOOL`")
               ]),

        Method('AddRealComment_DB', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Add a comment with a float value to the activity log of the database.",
               notes="""
               The comment is written in the form:
               
               Comment: Value
               
               and if followed by a carriage return.
               The activity log is created automatically if it does not exist.
               
               See Notes in :func:`AddComment_DB`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Comment"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Value"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Indent comment one tab? :def:`GEO_BOOL`")
               ]),

        Method('AddTimeComment_DB', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Add a comment with the date and time to the activity log of the database.",
               notes="""
               The comment is written in the form:
               
               Comment: 2001/12/31 23:59:59
               
               and is followed by a carriage return.
               The activity log is created automatically if it does not exist.
               
               See Notes in :func:`AddComment_DB`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Comment"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Indent comment one tab? :def:`GEO_BOOL`")
               ]),

        Method('Associate_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Associate a channel with a group.",
               notes="""
               If it is already associated, or if the group has no
               defined group class, does nothing.
               
               As of v6.3, if a group line has no class defined, then ALL
               channels are assumed to be associated with it. This means
               that you need to associate a new channel with a group only in
               those cases where the group class is defined.
               
               If this function is used on a group with a group class, then
               the channel is added to class's association list, and the
               channel will be recognized as being associated with all
               groups of that class.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Shared Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="group line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel")
               ]),

        Method('AssociateAll_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Associate all channels with a group.",
               notes="""
               As of v6.3, if a group line has no class defined, then ALL
               channels are already assumed to be associated with it, and this
               function does nothing.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Shared Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="group line")
               ]),

        Method('AssociateClass_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Associate a channel with all groups of a specific class.",
               notes="""
               As of v6.3, if a group line has no class defined, then ALL
               channels are automatically assumed to be associated with it.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Shared Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel"),
                   Parameter('p3', type=Type.STRING,
                             doc="Class name of groups to associate the channel with. (Must be defined).")
               ]),

        Method('GenValidChanSymb_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Generate a valid channel name from a name candidate",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input string"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Outout string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Max output string length")
               ]),

        Method('GenValidLineSymb_DB', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Generate a valid line symb name string from given string.",
               notes="""
               The returned name is either the same size as the input
               or shorter. Escapes, leading and trailing spaces are removed, then
               all illegal characters are replaced with an underscore.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input string"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Outout string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Max output string length")
               ]),

        Method('GetChanVA_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Place the contents of a channel in a :class:`VA`.",
               see_also=":class:`VA` class.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel"),
                   Parameter('p4', type="VA",
                             doc=":class:`VA` in which to place the data")
               ]),

        Method('GetVAScaling_DB', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Get base and range for :class:`VA` channel cell display.",
               notes="See :func:`SetVAScaling_DB`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel (Locked :def_val:`DB_LOCK_READWRITE`)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Base value (rDummy for none)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Range value (rDummy for none)")
               ]),

        Method('GetVAWindows_DB', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Get the range of windows displayed for a :class:`VA` channel.",
               notes="See :func:`SetVAWindows_DB`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel (Locked :def_val:`DB_LOCK_READWRITE`)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="First window (0 to N-2, iDummy for default)"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Last window (1 to N-1, iDummy for default)")
               ]),

        Method('SetVABaseCoordinateInfo_DB', module='geoengine.core', version='8.2',
               availability=Availability.PUBLIC, 
               doc="Set the array channel base coordinate type, offset and values.",
               notes="See :func:`GetVABaseCoordinateInfo_DB`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel (Locked :def_val:`DB_LOCK_READWRITE`)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_ARRAY_BASETYPE`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Optional offset or base frequency"),
                   Parameter('p5', type="VV",
                             doc="Values (one per array channel column) (REAL)"),
                   Parameter('p6', type=Type.STRING,
                             doc="Units"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Allow changes to existing values?:def:`GEO_BOOL`")
               ]),

        Method('GetVABaseCoordinateInfo_DB', module='geoengine.core', version='8.2',
               availability=Availability.PUBLIC, 
               doc="Set the array channel base coordinate type, offset and values.",
               notes="See :func:`SetVABaseCoordinateInfo_DB`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel (Locked :def_val:`DB_LOCK_READONLY`)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc=":def:`DB_ARRAY_BASETYPE`"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Optional offset or base frequency"),
                   Parameter('p5', type="VV",
                             doc="Values (one per array channel column) (REAL)"),
                   Parameter('p6', type=Type.STRING, is_ref=True, size_of_param='p7',
                             doc="Units"),
                   Parameter('p7', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="size of units string")
               ]),

        Method('IGetGroupClass_DB', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Set the Class name for a group line.",
               notes="""
               This method fails if the line is not a group line.
               Group classes are used to identify group lines used for
               special purposes, e.g.: "COLLAR" for the Wholeplot collar table,
               or "TARGETS" for the UX-Detect Targets list.
               """,
               see_also=":func:`iLineCategory_DB` - to see if a line is a group line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Shared Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Group line - :def_val:`DB_LOCK_READWRITE` or :def_val:`DB_LOCK_READONLY`"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="returned class name - max size = :def_val:`DB_GROUP_CLASS_SIZE` - 1"),
                   Parameter('p4', type=Type.INT32_T, default_length='DB_GROUP_CLASS_SIZE',
                             doc="buffer size")
               ]),

        Method('iGetInfo_DB', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get information about the database.",
               return_type=Type.INT32_T,
               return_doc="x - Return Value",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DB_INFO`")
               ]),

        Method('IGetVAProfColorFile_DB', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Get colours for a :class:`VA` channel when displayed in the profile window.",
               notes="See :func:`SetVAProfColorFile_DB`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel (Locked :def_val:`DB_LOCK_READWRITE`)"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc='zone file name, "" to clear.'),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="buffer size for string")
               ]),

        Method('IGetVAProfSectOption_DB', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Get the display options of :class:`VA` channels",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel (Locked :def_val:`DB_LOCK_READWRITE`)"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc='Option  "Profile", "Section" or "Section and Profile"'),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="buffer size for string")
               ]),

        Method('IGetVASectColorFile_DB', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Get colours for a :class:`VA` channel when displayed section in the profile window.",
               notes="Fails in the channel is not an array channel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel (Locked :def_val:`DB_LOCK_READWRITE`)"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="zone file name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="buffer size for string")
               ]),

        Method('iIsAssociated_DB', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Check to see if a channel is associated with group.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if not a group line, or if the channel is not associated.
               
               As of v6.3, if a group line has no class defined, then ALL
               channels are automatically assumed to be associated with it.
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Shared Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel")
               ]),

        Method('iIsWholeplot_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Is this a Wholeplot database?",
               notes="Currently checks to see if the DH_COLLAR line exists.",
               return_type=Type.INT32_T,
               return_doc="""
               1 if it is a Wholeplot database
               0 if it is not.
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ]),

        Method('PutChanVA_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Place the contents of a :class:`VA` in a channel.",
               see_also=":class:`VA` class.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel"),
                   Parameter('p4', type="VA",
                             doc=":class:`VA` from which to get the data")
               ]),

        Method('SetGroupClass_DB', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Set the Class name for a group line.",
               notes="""
               This method fails if the line is not a group line.
               Group classes are used to identify group lines used for
               special purposes. All group lines with the same class share
               the same list of associated channels.
               
               As of v6.3, if a group line has no class defined, then ALL
               channels are assumed to be associated with it. This means
               that a group class should only be defined when you wish to
               associate a subset of the available channels to group line.
               """,
               see_also="""
               :func:`iLineCategory_DB` - to see if a line is a group line.
               :func:`Associate_DB` - Associate a channel with a group.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Shared Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Group line - :def_val:`DB_LOCK_READWRITE`"),
                   Parameter('p3', type=Type.STRING,
                             doc=":def_val:`DB_GROUP_CLASS_SIZE`")
               ]),

        Method('SetVAProfColorFile_DB', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Set colours for a :class:`VA` channel when displayed in the profile window.",
               notes="""
               Fails in the channel is not an array channel, if the
               file does not exist, or if it is not a valid colour zone file.
               
               The individual columns in the array channel are displayed using the input
               zone file colours. A linear :class:`ITR` from 0 to 1 is created on the colour zones
               to map to individual channel indices (expressed as a fraction as shown below).
               
               For instance, for a file with 8 colours the ranges are as follows:
               
               Colour Range
               Colour 1    0        > value >=  0.125
               Colour 2    0.125    > value >=  0.25
               Colour 3    0.25     > value >=  0.375
               Colour 4    0.375    > value >=  0.5
               Colour 5    0.5      > value >=  0.625
               Colour 6    0.625    > value >=  0.75
               Colour 7    0.75     > value >=  0.875
               Colour 8    0.875    > value >=  1.0
               
               When an array channel is displayed, the index of each element (column) is mapped
               into the corresponding range above using the following formula:
               
               value = (column index) / (# of columns - 1)
               
               For an array with 8 columns, you get the following values:
               
               Column   Value    Colour
               0        0        1
               1        0.14     2
               2        0.28     3
               3        0.43     4
               4        0.57     5
               5        0.71     6
               6        0.86     7
               7        1.0      8
               
               The colour file search path is: Local directory, then oasismontaj\\tbl.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel (Locked :def_val:`DB_LOCK_READWRITE`)"),
                   Parameter('p3', type=Type.STRING,
                             doc='zone file name, "" to clear.')
               ]),

        Method('SetVAProfSectOption_DB', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Set the display options of :class:`VA` channels",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel (Locked :def_val:`DB_LOCK_READWRITE`)"),
                   Parameter('p3', type=Type.STRING,
                             doc='Option  "Profile", "Section" or "Section and Profile"')
               ]),

        Method('SetVAScaling_DB', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Set base and range for :class:`VA` channel cell display.",
               notes="""
               By default, :class:`VA` profiles autoscale to fit in the database cell.
               This lets the user set a single base and range for all cells.
               If either input is a dummy, both are set as dummies, and autoscaling
               is used.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel (Locked :def_val:`DB_LOCK_READWRITE`)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Base value (rDummy for none)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Range value (rDummy for none)")
               ]),

        Method('SetVASectColorFile_DB', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Set colours for a :class:`VA` channel when displayed section in the profile window.",
               notes="""
               Fails in the channel is not an array channel, if the
               file does not exist, or if it is not a valid colour zone file.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel (Locked :def_val:`DB_LOCK_READWRITE`)"),
                   Parameter('p3', type=Type.STRING,
                             doc="zone file name")
               ]),

        Method('SetVAWindows_DB', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Set the range of windows to display for a :class:`VA` channel.",
               notes="""
               Use to display a subset of the :class:`VA` channel windows in the GDB.
               Windows index from 0.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB"),
                   Parameter('p2', type="DB_SYMB",
                             doc="channel (Locked :def_val:`DB_LOCK_READWRITE`)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="First window (0 to N-1, iDummy for default)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Last window (0 to N-1, iDummy for default)")
               ])
    ],
    'Miscellaneous': [

    ],
    'Obsolete': [

        Method('CreateSymbEx2_DB', module='geoengine.core', version='6.3.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Create a new Symbol.",
               notes="""
               This method is identical to :func:`CreateSymbEx_DB` but does not
               have any restrictions based on license.
               """,
               return_type="DB_SYMB",
               return_doc="DB_SYMB handle.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Symbol Name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DB_SYMB_TYPE`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DB_OWN`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DB_CATEGORY_USER`, :def:`DB_CATEGORY_LINE`, :def:`DB_CATEGORY_CHAN`, :def:`DB_CATEGORY_BLOB`"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Extra info, which depends on DB_SYMB_ :def_val:`DB_SYMB_CHAN` - element width for a :class:`VA` channel ignores for all other DB_SYMB types")
               ]),

        Method('Current_DB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="This method returns the Current Database opened (obsolete)",
               notes="""
               This method combines the operations:
               
               EData = :func:`Current_EDB`();       // get current edited database
               Data = :func:`Lock_EDB`(EData);      // lock the database
               
               and has been superceded by this construction in all Geosoft GXs.
               """,
               return_type="DB",
               return_doc=":class:`DB` Object"),

        Method('Destruct_DB', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Destructs a Database Object. (obsolete)",
               notes="""
               This function is is called to destruct database handle object.
               
               This method has been superceded by the use of the :class:`EDB` object,
               which when locked returns a :class:`DB` object that must NOT be destroyed.
               
               EData = :func:`Current_EDB`();       // get current edited database
               Data = :func:`Lock_EDB`(EData);      // lock the database
               ... (Process using the :class:`DB` object Data)
               :func:`UnLock_EDB`(EData);           // unlock the database
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database to Destroy")
               ]),

        Method('PutChanVVEx_DB', module='geoengine.core', version='6.0.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Place the contents of a :class:`VV` in a channel.",
               notes="""
               This method is identical to :func:`PutChanVV_DB` except that it
               does not have a limit for the Free viewer. It is licensed
               and cannot be called without a license.
               """,
               see_also=":class:`VV` class.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` from which to get the data")
               ]),

        Method('SetCurrent_DB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Sets the current database to this database (obsolete).",
               notes="""
               This method has been superceded by the following usage:
               
               :func:`MakeCurrent_EDB`(EData);
               Data = :func:`Lock_EDB`(EData);      // lock the database
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ]),

        Method('iGetLength_DB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Returns the # of elements in a channel.",
               notes="""
               This method did not account for array channels correctly (you had to divide by the number of columns
               to get the correct number of rows). Superceded by :func:`iGetChannelLength_DB`.
               """,
               return_type=Type.INT32_T,
               return_doc="# of elements",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line    (read or write locked)"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel (read or write locked)")
               ])
    ]
}

