from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DBREAD',
                 doc="""
                 The :class:`DBREAD` class is used to open and read from databases. Very large lines
                 are split into blocks and served up sequentially to prevent the over-use of virtual memory when channels are read into VVs or VAs.
                 Individual data blocks are limited by default to 1 MB (which is user-alterable). Single lines smaller than the block size
                 are served up whole, one block per line.
                 """)





gx_methods = {
    'Create Methods': [

        Method('Create_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="""
               Create a :class:`DBREAD` object
               Add channels using the :func:`iAddChannel_DBREAD` method.channel.
               """,
               return_type="DBREAD",
               return_doc=":class:`DBREAD` object",
               parameters = [
                   Parameter('db', type="DB",
                             doc="Database input"),
                   Parameter('line_lst', type="LST",
                             doc="List of lines to process NAME = line name, VALUE = line symbol")
               ]),

        Method('CreateXY_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="""
               Create a :class:`DBREAD` object for a XY-located data. Add channels using the
               :func:`iAddChannel_DBREAD` method.
               """,
               return_type="DBREAD",
               return_doc=":class:`DBREAD` object",
               parameters = [
                   Parameter('db', type="DB",
                             doc="Database input"),
                   Parameter('line_lst', type="LST",
                             doc="List of lines to process NAME = line name, VALUE = line symbol")
               ]),

        Method('CreateXYZ_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="""
               Create a :class:`DBREAD` object for a XYZ-located data.
               Add channels using the :func:`iAddChannel_DBREAD`method.channel
               """,
               return_type="DBREAD",
               return_doc=":class:`DBREAD` object",
               parameters = [
                   Parameter('db', type="DB",
                             doc="Database input"),
                   Parameter('line_lst', type="LST",
                             doc="List of lines to process NAME = line name, VALUE = line symbol")
               ]),

        Method('Destroy_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`DBREAD` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dbread', type="DBREAD",
                             doc=":class:`DBREAD` handle")
               ]),

        Method('iAddChannel_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Add a data channel to the :class:`DBREAD` object.",
               return_type=Type.INT32_T,
               return_doc="Channel index. Use for getting the correct :class:`VV` or :class:`VA` object.",
               parameters = [
                   Parameter('dbread', type="DBREAD",
                             doc=":class:`DBREAD` handle"),
                   Parameter('chan', type="DB_SYMB",
                             doc="Channel handle (does not need to be locked, but can be.)")
               ])
    ],
    'Data Access Methods': [

        Method('GetVV_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`VV` handle for a channel.",
               notes="""
               Call only for single-column (regular) channels. You can call the :func:`iGetChanArraySize_DBREAD`
               function to find the number fo columns in a given channel. The :class:`VV` is filled anew for 
               each block served up.
               """,
               return_type="VV",
               return_doc=":class:`VV` handle",
               parameters = [
                   Parameter('dbread', type="DBREAD",
                             doc=":class:`DBREAD` handle"),
                   Parameter('chan', type=Type.INT32_T,
                             doc="Index of channel to access.")
               ]),

        Method('GetVA_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`VA` handle for an array channel.",
               notes="""
               Call only for array (multi-column) channels. You can call the :func:`iGetChanArraySize_DBREAD`
               function to find the number fo columns in a given channel, or you can call :func:`iCol_VA` on the returned :class:`VA` handle.
               The :class:`VA` is filled anew for each block served up.
               """,
               return_type="VA",
               return_doc=":class:`VA` handle",
               parameters = [
                   Parameter('dbread', type="DBREAD",
                             doc=":class:`DBREAD` handle"),
                   Parameter('chan', type=Type.INT32_T,
                             doc="Index of channel to access.")
               ]),

        Method('GetVVx_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the X channel :class:`VV` handle.",
               notes="""
               Only available for the CreateXY or CreateXYZ methods.
               The :class:`VV` is filled anew for each block served up.
               """,
               return_type="VV",
               return_doc=":class:`VV` handle",
               parameters = [
                   Parameter('dbread', type="DBREAD",
                             doc=":class:`DBREAD` handle")
               ]),

        Method('GetVVy_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the Y channel :class:`VV` handle.",
               notes="""
               Only available for the CreateXY or CreateXYZ methods.
               The :class:`VV` is filled anew for each block served up.
               """,
               return_type="VV",
               return_doc=":class:`VV` handle",
               parameters = [
                   Parameter('dbread', type="DBREAD",
                             doc=":class:`DBREAD` handle")
               ]),

        Method('GetVVz_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the Z channel :class:`VV` handle.",
               notes="""
               Only available for the CreateXY or CreateXYZ methods.
               The :class:`VV` is filled anew for each block served up.
               If the Z channel is an array channel, the returned :class:`VV` is the "base" :class:`VV` of the :class:`VA` and contains all items sequentially.
               """,
               return_type="VV",
               return_doc=":class:`VV` handle",
               parameters = [
                   Parameter('dbread', type="DBREAD",
                             doc=":class:`DBREAD` handle")
               ]),

        Method('iGetChanArraySize_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of columns of data in a channel.",
               notes="""
               Regular channels have one column of data. Array channels have more than one column of data.
               This function should be called to determine whether to use :func:`GetVV_DBREAD` or :func:`GetVA_DBREAD` to access data
               for a channel.
               """,
               return_type=Type.INT32_T,
               return_doc="The number of columns (array size) for a channel",
               parameters = [
                   Parameter('dbread', type="DBREAD",
                             doc=":class:`DBREAD` handle"),
                   Parameter('chan', type=Type.INT32_T,
                             doc="Index of channel to access.")
               ]),

        Method('iGetNumberOfBlocksToProcess_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of blocks to be served up.",
               notes="""
               The selected lines are scanned. All lines where the served up data is less than the maximum block size for
               all channels are served as a single block. Any lines where any channel's data exceeds the maximum block size are split up into blocks.
               The value returned can be used as the progress message maximum iteration value.
               """,
               return_type=Type.INT32_T,
               return_doc="The number of blocks to process in the selected lines.",
               parameters = [
                   Parameter('dbread', type="DBREAD",
                             doc=":class:`DBREAD` handle")
               ])
    ],
    'Processing': [

        Method('iGetNextBlock_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the next block of data.",
               notes="""
               The next block of data is read and copied into the channel :class:`VV` and/or :class:`VA` objects, accessed using
               the :func:`GetVV_DBREAD` and :func:`GetVA_DBREAD` functions.
               """,
               return_type=Type.INT32_T,
               return_doc="Returns the current block index, or -1 if at end of file (no new data returned).",
               parameters = [
                   Parameter('dbread', type="DBREAD",
                             doc=":class:`DBREAD` handle"),
                   Parameter('line', type=Type.INT32_T, is_ref=True,
                             doc="(returned) The index into the input selected line list of the line whose data is contained in the current block"),
                   Parameter('block', type=Type.INT32_T, is_ref=True,
                             doc="(returned) The block index (0 to NBlocks-1) for the current line of data."),
                   Parameter('n_blocks', type=Type.INT32_T, is_ref=True,
                             doc="(returned) The number of blocks that the current line is split into.")
               ])
    ]
}

