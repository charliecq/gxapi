from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('IMU',
                 doc="""
                 Not a class. This is a catch-all group of functions working
                 on :class:`IMG` objects (see :class:`IMG`). Grid operations include masking,
                 trending, windowing, expanding and grid stitching.
                 """)


gx_defines = [
    Define('IMU_BOOL_OLAP',
           doc="Overlapping area option",
           constants=[
               Constant('IMU_BOOL_OLAP_AVE', value='0', type=Type.INT32_T,
                        doc="Overlap values are averaged"),
               Constant('IMU_BOOL_OLAP_1', value='1', type=Type.INT32_T,
                        doc="Overlap values use grid 1 value"),
               Constant('IMU_BOOL_OLAP_2', value='2', type=Type.INT32_T,
                        doc="Overlap values use grid 2 value")
           ]),

    Define('IMU_BOOL_OPT',
           doc="Boolean logic option",
           constants=[
               Constant('IMU_BOOL_OPT_AND', value='0', type=Type.INT32_T,
                        doc="Valid areas are only where grids overlap"),
               Constant('IMU_BOOL_OPT_OR', value='1', type=Type.INT32_T,
                        doc="Valid areas are where either grid is a valid value"),
               Constant('IMU_BOOL_OPT_XOR', value='2', type=Type.INT32_T,
                        doc="Overlap areas are dummied")
           ]),

    Define('IMU_BOOL_SIZING',
           doc="Sizing option",
           constants=[
               Constant('IMU_BOOL_SIZING_MIN', value='0', type=Type.INT32_T,
                        doc="Output grid is sized to overlapping region"),
               Constant('IMU_BOOL_SIZING_0', value='1', type=Type.INT32_T,
                        doc="Output grid is sized to grid 1"),
               Constant('IMU_BOOL_SIZING_1', value='2', type=Type.INT32_T,
                        doc="Output grid is sized to grid 2"),
               Constant('IMU_BOOL_SIZING_MAX', value='3', type=Type.INT32_T,
                        doc="Output grid is sized to maximum combined area of both grids")
           ]),

    Define('IMU_DOUBLE_CRC_BITS',
           doc="Bits to use in double CRC's",
           constants=[
               Constant('IMU_DOUBLE_CRC_BITS_EXACT', value='0', type=Type.INT32_T,
                        doc="Exact CRC"),
               Constant('IMU_DOUBLE_CRC_BITS_DEFAULT', value='10', type=Type.INT32_T,
                        doc="Default inaccuracy in double (10 Bits)"),
               Constant('IMU_DOUBLE_CRC_BITS_MAX', value='51', type=Type.INT32_T,
                        doc="Maximum number of inaccuracy bits (51 Bits)")
           ]),

    Define('IMU_EXPAND_SHAPE',
           doc="Shape of output grid",
           constants=[
               Constant('IMU_EXPAND_SHAPE_RECTANGLE', value='0', type=Type.INT32_T),
               Constant('IMU_EXPAND_SHAPE_SQUARE', value='1', type=Type.INT32_T)
           ]),

    Define('IMU_FILL_ROLLOPT',
           doc="Defines for Grid Filling Method Options",
           constants=[
               Constant('IMU_FILL_ROLLOPT_LINEAR', value='1', type=Type.INT32_T),
               Constant('IMU_FILL_ROLLOPT_SQUARE', value='2', type=Type.INT32_T)
           ]),

    Define('IMU_FILT_DUMMY',
           doc="""
           Settings for placing dummy values in grid if any of filter
           values are dummy
           """,
           constants=[
               Constant('IMU_FILT_DUMMY_NO', value='0', type=Type.INT32_T),
               Constant('IMU_FILT_DUMMY_YES', value='1', type=Type.INT32_T)
           ]),

    Define('IMU_FILT_FILE',
           doc="""
           Flags which indicate if a file is to be used to read the
           filter values
           """,
           constants=[
               Constant('IMU_FILT_FILE_NO', value='0', type=Type.INT32_T),
               Constant('IMU_FILT_FILE_YES', value='1', type=Type.INT32_T)
           ]),

    Define('IMU_FILT_HZDRV',
           doc="""
           Flags which indicate which type of horizontal derivative
           is being applied (X direction, Y direction, none at all)
           """,
           constants=[
               Constant('IMU_FILT_HZDRV_NO', value='0', type=Type.INT32_T),
               Constant('IMU_FILT_HZDRV_X', value='1', type=Type.INT32_T),
               Constant('IMU_FILT_HZDRV_Y', value='2', type=Type.INT32_T)
           ]),

    Define('IMU_FLOAT_CRC_BITS',
           doc="Bits to use in float CRC's",
           constants=[
               Constant('IMU_FLOAT_CRC_BITS_EXACT', value='0', type=Type.INT32_T,
                        doc="Exact CRC"),
               Constant('IMU_FLOAT_CRC_BITS_DEFAULT', value='7', type=Type.INT32_T,
                        doc="Default inaccuracy in floats (7 Bits)"),
               Constant('IMU_FLOAT_CRC_BITS_MAX', value='22', type=Type.INT32_T,
                        doc="Maximum number of inaccuracy bits (22 Bits)")
           ]),

    Define('IMU_MASK',
           doc="Defined options for masking grids",
           constants=[
               Constant('IMU_MASK_INSIDE', value='0', type=Type.INT32_T),
               Constant('IMU_MASK_OUTSIDE', value='1', type=Type.INT32_T)
           ]),

    Define('IMU_STAT_FORCED',
           doc="Defined options for forcing recalculating the grid values",
           constants=[
               Constant('IMU_STAT_FORCED_NO', value='0', type=Type.INT32_T),
               Constant('IMU_STAT_FORCED_YES', value='1', type=Type.INT32_T)
           ]),

    Define('IMU_TRANS',
           doc="""
           Transpose Options available for :func:`GridTrns_IMU`
           implies original grid lines:
           """,
           constants=[
               Constant('IMU_TRANS_DEFAULT', value='0', type=Type.INT32_T,
                        doc="Can be ANY orientation"),
               Constant('IMU_TRANS_Y', value='1', type=Type.INT32_T,
                        doc="MUST be parallel to Y-Axis"),
               Constant('IMU_TRANS_X', value='-1', type=Type.INT32_T,
                        doc="MUST be parallel to X-Axis")
           ]),

    Define('IMU_TREND',
           doc="Points in grid to use",
           constants=[
               Constant('IMU_TREND_ALL', value='0', type=Type.INT32_T),
               Constant('IMU_TREND_EDGE', value='1', type=Type.INT32_T)
           ]),

    Define('IMU_WIND_COORD',
           doc="Output grid coordinate units",
           constants=[
               Constant('IMU_WIND_GRID', value='0', type=Type.INT32_T),
               Constant('IMU_WIND_GROUND', value='1', type=Type.INT32_T)
           ]),

    Define('IMU_WIND_DUMMIES',
           doc="Option for handling out-of-range Z values",
           constants=[
               Constant('IMU_WIND_DUMMY', value='0', type=Type.INT32_T),
               Constant('IMU_WIND_CLIP', value='1', type=Type.INT32_T)
           ]),

    Define('IMU_XYZ_INDEX',
           doc="""
           Flags whether to use grid index numbers as
           station numbers.
           """,
           constants=[
               Constant('IMU_XYZ_INDEX_NO', value='0', type=Type.INT32_T),
               Constant('IMU_XYZ_INDEX_YES', value='1', type=Type.INT32_T)
           ]),

    Define('IMU_XYZ_LABEL',
           doc="XYZ Label Flags",
           constants=[
               Constant('IMU_XYZ_LABEL_NO', value='1', type=Type.INT32_T),
               Constant('IMU_XYZ_LABEL_YES', value='0', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('AggToGeoColor_IMU', module='geoengine.core', version='5.1.6',
               availability=Availability.LICENSED, 
               doc="Create a Geosoft color grid from an aggregate.",
               notes="This consumes a very small amount of memory",
               return_type=Type.VOID,
               parameters = [
                   Parameter('agg', type="AGG",
                             doc="Input Aggregate"),
                   Parameter('grid', type=Type.STRING,
                             doc="Output image name"),
                   Parameter('ipj', type="IPJ",
                             doc="Projection to use"),
                   Parameter('res', type=Type.DOUBLE,
                             doc="Resolution (Cell Size) size to use")
               ]),

        Method('CRC_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Computes a CRC Checksum on an image.",
               return_type="CRC",
               return_doc="CRC value",
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Input image"),
                   Parameter('pul_crc', type="CRC",
                             doc="Starting CRC (use :const:`CRC_INIT_VALUE` if none)")
               ]),

        Method('CRCGrid_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Computes a CRC Checksum on a grid.",
               return_type="CRC",
               return_doc="CRC value",
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Grid"),
                   Parameter('pul_crc', type="CRC",
                             doc="Starting CRC (use :const:`CRC_INIT_VALUE` if none)")
               ]),

        Method('CRCGridInexact_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Computes a CRC Checksum on a grid and allows you to specify
               number of bits of floats/doubles to drop so that the CRC
               will be same even of this are changed.
               """,
               notes="""
               Very useful for testing where the last bits of accuracy
               are not as important.
               """,
               return_type="CRC",
               return_doc="CRC value",
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Grid"),
                   Parameter('pul_crc', type="CRC",
                             doc="Starting CRC (use :const:`CRC_INIT_VALUE` if none)"),
                   Parameter('float_bits', type=Type.INT32_T,
                             doc=":def:`IMU_FLOAT_CRC_BITS`"),
                   Parameter('double_bits', type=Type.INT32_T,
                             doc=":def:`IMU_DOUBLE_CRC_BITS`")
               ]),

        Method('CRCInexact_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Computes a CRC Checksum on an image and allows you to specify
               number of bits of floats/doubles to drop so that the CRC
               will be same even of this are changed.
               """,
               notes="""
               Very useful for testing where the last bits of accuracy
               are not as important.
               """,
               return_type="CRC",
               return_doc="CRC value",
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Input image"),
                   Parameter('pul_crc', type="CRC",
                             doc="Starting CRC (use :const:`CRC_INIT_VALUE` if none)"),
                   Parameter('float_bits', type=Type.INT32_T,
                             doc=":def:`IMU_FLOAT_CRC_BITS`"),
                   Parameter('double_bits', type=Type.INT32_T,
                             doc=":def:`IMU_DOUBLE_CRC_BITS`")
               ]),

        Method('ExportGridWithoutDataSectionXML_IMU', module='geoengine.core', version='7.2.0',
               availability=Availability.LICENSED, 
               doc="Export a Grid minus the data section as an XML file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Grid"),
                   Parameter('crc', type="CRC", is_ref=True,
                             doc="CRC returned"),
                   Parameter('file', type=Type.STRING,
                             doc="Output XML file")
               ]),

        Method('ExportGridXML_IMU', module='geoengine.core', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Export a Grid as an XML file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Grid"),
                   Parameter('crc', type="CRC", is_ref=True,
                             doc="CRC returned"),
                   Parameter('file', type=Type.STRING,
                             doc="Output XML file")
               ]),

        Method('ExportRawXML_IMU', module='geoengine.core', version='7.0.0',
               availability=Availability.LICENSED, 
               doc="Export a Grid as an XML file using a fast raw output.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Image"),
                   Parameter('crc', type="CRC", is_ref=True,
                             doc="CRC returned"),
                   Parameter('file', type=Type.STRING,
                             doc="Output XML file")
               ]),

        Method('ExportXML_IMU', module='geoengine.core', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Export a Grid as an XML file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Image"),
                   Parameter('crc', type="CRC", is_ref=True,
                             doc="CRC returned"),
                   Parameter('file', type=Type.STRING,
                             doc="Output XML file")
               ]),

        Method('GetZVV_IMU', module='geoengine.core', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Extract an interpolated image value for given XY :class:`VV` locations",
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Input grid"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('vv_z', type="VV",
                             doc="Z :class:`VV` filled with values (set to be same size as X, Y)")
               ]),

        Method('GetZPeaksVV_IMU', module='geoengine.core', version='9.0.0',
               availability=Availability.LICENSED, 
               doc="""
               Same as :func:`GetZVV_IMU`, but find the closest peak value to the input locations, and return
               				             the peak value and peak value location.
               """,
               notes="""
               The returned locations will always be a grid point location; no interpolation is performed when locating the peaks. A simple search is
               				done of all neighbouring points from the starting point, and once no neighbours can be located with a higher value, the search stops.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Input grid"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('vv_z', type="VV",
                             doc="Z :class:`VV` filled with values (set to be same size as X, Y)")
               ]),

        Method('GridAdd_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Adds two Grid images together point-by-point.",
               notes="""
               The :class:`IMG` parameters MUST be of type :const:`GS_DOUBLE`!
               If not, the method will terminate.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img1', type="IMG",
                             doc="Image of first grid"),
                   Parameter('m1', type=Type.DOUBLE,
                             doc="Multiplier to operate on first grid image"),
                   Parameter('img2', type="IMG",
                             doc="Image of second grid"),
                   Parameter('m2', type=Type.DOUBLE,
                             doc="Multiplier to operate on second grid image"),
                   Parameter('imgo', type="IMG",
                             doc="Output grid image")
               ]),

        Method('GridAGC_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Automatic Gain Compensation of a grid.",
               notes="""
               The :class:`IMG` parameters MUST be of type :const:`GS_FLOAT`!
               If not, the method will terminate.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('i_img', type="IMG",
                             doc="Image of input grid"),
                   Parameter('o_img', type="IMG",
                             doc="Image of output grid"),
                   Parameter('width', type=Type.INT32_T,
                             doc="Width of filter to separate signal from background."),
                   Parameter('max_gain', type=Type.DOUBLE,
                             doc="Maximum gain applied to the signal."),
                   Parameter('remove_background', type=Type.INT32_T,
                             doc="Remove background before applying gain?")
               ]),

        Method('GridBool_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               Mask one grid against another using boolean logic
               operations.
               """,
               notes="""
               The :class:`IMG` parameters must be of type :const:`GS_DOUBLE`!
               If not, the method will terminate.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img1', type="IMG",
                             doc="Image of first input grid"),
                   Parameter('img2', type="IMG",
                             doc="Image of second input grid"),
                   Parameter('out', type=Type.STRING,
                             doc="File name of output grid"),
                   Parameter('bool', type=Type.INT32_T,
                             doc=":def:`IMU_BOOL_OPT`"),
                   Parameter('sizing', type=Type.INT32_T,
                             doc=":def:`IMU_BOOL_SIZING`"),
                   Parameter('olap', type=Type.INT32_T,
                             doc=":def:`IMU_BOOL_OLAP`")
               ]),

        Method('GridEdge_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get grid edge points",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Grid file name"),
                   Parameter('vv_x', type="VV",
                             doc="X coordinates of edge points"),
                   Parameter('vv_y', type="VV",
                             doc="Y coordinates of edge points")
               ]),

        Method('GridEdgePLY_IMU', module='geoengine.core', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Get grid edge points",
               notes="""
               Unlike :func:`GridPLY_IMU` and GridPlyEx_IMU, the image is not
               altered. It just gives the :class:`PLY`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="The Grid"),
                   Parameter('ply', type="PLY",
                             doc=":class:`PLY` containing the edges."),
                   Parameter('min_points', type=Type.INT32_T,
                             doc="Minimum number of points in polygons (0 for all)")
               ]),

        Method('GridExpand_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               Expand a grid and place dummies in the area
               beyond the original edges.
               """,
               notes="""
               The :class:`IMG` parameter MUST be of type :const:`GS_FLOAT`!
               If not, the method will terminate.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('im_gi', type="IMG",
                             doc="Image of input grid"),
                   Parameter('out', type=Type.STRING,
                             doc="File name of output grid"),
                   Parameter('per', type=Type.DOUBLE,
                             doc="Minimum percentage to expand the grid by"),
                   Parameter('shape', type=Type.INT32_T,
                             doc=":def:`IMU_EXPAND_SHAPE`"),
                   Parameter('x', type=Type.INT32_T,
                             doc="X Dimension the output grid is expanded to"),
                   Parameter('y', type=Type.INT32_T,
                             doc="Y Dimension the output grid is expanded to")
               ]),

        Method('GridExpFill_IMU', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Extends and fills a grid for :class:`FFT2`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('in_grd', type=Type.STRING,
                             doc="Name of the input grid"),
                   Parameter('out_grd', type=Type.STRING,
                             doc="Name of the output grid"),
                   Parameter('p_ex', type=Type.DOUBLE,
                             doc="% expansion"),
                   Parameter('t_ex', type=Type.INT32_T,
                             doc="Shape of expansion: 0 - rectangle, 1 - square")
               ]),

        Method('GridFill_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Interpolates to fill dummies, generates an output grid.",
               notes="""
               The :class:`IMG` parameters MUST be of type :const:`GS_FLOAT`!
               If not, the method will terminate.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('im_gi', type="IMG",
                             doc="Image of input grid"),
                   Parameter('im_go', type="IMG",
                             doc="Image of output grid"),
                   Parameter('rollopt', type=Type.INT32_T,
                             doc=":def:`IMU_FILL_ROLLOPT`"),
                   Parameter('rolldist', type=Type.INT32_T,
                             doc="Distance at which to roll off to 0"),
                   Parameter('mxf', type=Type.INT32_T,
                             doc="Maximum prediction filter length"),
                   Parameter('mxp', type=Type.INT32_T,
                             doc="Maximum prediction filter area"),
                   Parameter('rollbase', type=Type.DOUBLE,
                             doc="Base value to roll off to"),
                   Parameter('alimit', type=Type.DOUBLE,
                             doc="Maximum amplitude allowed in grid"),
                   Parameter('elimit', type=Type.DOUBLE,
                             doc="Maximum edge amplitude allowed in grid"),
                   Parameter('width', type=Type.INT32_T,
                             doc="Width from edge to start limiting from"),
                   Parameter('npass', type=Type.INT32_T,
                             doc="Number of convolution passes to apply")
               ]),

        Method('GridFilt_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               Applies a filter to a grid any number
               of passes.
               """,
               notes="""
               The :class:`IMG` parameters MUST be of type :const:`GS_FLOAT`!
               If not, the method will terminate.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Image of first grid"),
                   Parameter('imgo', type="IMG",
                             doc="Image of second grid"),
                   Parameter('passes', type=Type.INT32_T,
                             doc="Number of passes to apply filter (>0)"),
                   Parameter('mult', type=Type.DOUBLE,
                             doc="Multiplier to apply to grid values"),
                   Parameter('dum', type=Type.INT32_T,
                             doc=":def:`IMU_FILT_DUMMY`"),
                   Parameter('hz', type=Type.INT32_T,
                             doc=":def:`IMU_FILT_HZDRV`"),
                   Parameter('usefile', type=Type.INT32_T,
                             doc=":def:`IMU_FILT_FILE`"),
                   Parameter('file', type=Type.STRING,
                             doc="Name of file containing filter values"),
                   Parameter('vv', type="VV",
                             doc=":class:`VV` containing filter values (if not using a file for the values) MUST BE OF TYPE 'real'")
               ]),

        Method('GridHead_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Modifies Statistics contained in a grid header.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Name of the grid whose header is to be modified."),
                   Parameter('esep', type=Type.DOUBLE,
                             doc="Element separation"),
                   Parameter('vsep', type=Type.DOUBLE,
                             doc="Vector separation"),
                   Parameter('x_orig', type=Type.DOUBLE,
                             doc="Grid X Origin on ground"),
                   Parameter('y_orig', type=Type.DOUBLE,
                             doc="Grid Y Origin on ground"),
                   Parameter('rot', type=Type.DOUBLE,
                             doc="Grid Rotation")
               ]),

        Method('GridInFill_IMU', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Fill in a ribbon along the edge and inside hollow areas of the grid",
               return_type=Type.VOID,
               parameters = [
                   Parameter('im_gi', type="IMG",
                             doc="Image of input grid"),
                   Parameter('out_grd', type=Type.STRING,
                             doc="Name of the output grid"),
                   Parameter('extend', type=Type.INT32_T,
                             doc="Number of cells to extend ribbon along the edge"),
                   Parameter('iter', type=Type.INT32_T,
                             doc="Number of iterations to fill inside hollow areas")
               ]),

        Method('GridMask_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               Create a mask grid using a set of polygon
               coordinates defined in a separate file, then
               masking the polygon over an input grid.
               """,
               notes="""
               The :class:`IMG` parameters MUST be of type :const:`GS_DOUBLE`!
               If not, the method will terminate.
               
               The :class:`PLY` will contain more than one polygon
               if it was loaded from a file containing
               coordinates of more than one polygon.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('in_grid', type=Type.STRING,
                             doc="Name of input grid"),
                   Parameter('m_grid', type=Type.STRING,
                             doc="Name of output mask grid file"),
                   Parameter('pply', type="PLY",
                             doc="Polygon containing mask coordinates"),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`IMU_MASK`")
               ]),

        Method('GridPeak_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Pick grid peaks.",
               notes="""
               Peak test directions defines how grid peaks are to be found.
               For example, with the 1, a grid point will be picked if its
               value is greater than it's two neighbors in at least one
               direction.  Up to 4 directions can be tested.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Grid file name"),
                   Parameter('nlmt', type=Type.INT32_T,
                             doc="Peak test directions (1 to 4)"),
                   Parameter('v_vx', type="VV",
                             doc="X of found peaks"),
                   Parameter('v_vy', type="VV",
                             doc="Y of found peaks"),
                   Parameter('v_vz', type="VV",
                             doc="Z values of found peaks")
               ]),

        Method('GridPLY_IMU', module='geoengine.core', version='5.1.0',
               availability=Availability.LICENSED, 
               doc="Get the grid edge in a :class:`PLY`",
               notes="""
               This will optionally refresh the grid boundary :class:`PLY` and return
               the :class:`PLY`.
               
               If the boundary is not refreshed and has never been calculated,
               the boundary will be the bounding rectangle of the grid.
               
               The grid :class:`PLY` will be added to existing ploygons in the passed :class:`PLY`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="The :class:`IMG`"),
                   Parameter('ply', type="PLY",
                             doc=":class:`PLY` to which the bounding polygons will be added."),
                   Parameter('refresh', type=Type.INT32_T,
                             doc="TRUE to force the boundary to be refreshed.")
               ]),

        Method('GridPLYEx_IMU', module='geoengine.core', version='5.1.6',
               availability=Availability.LICENSED, 
               doc="Get the grid edge in a :class:`PLY` (with min points)",
               notes="""
               This will optionally refresh the grid boundary :class:`PLY` and return
               the :class:`PLY`.
               
               If the boundary is not refreshed and has never been calculated,
               the boundary will be the bounding rectangle of the grid.
               
               The grid :class:`PLY` will be added to existing ploygons in the passed :class:`PLY`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="The :class:`IMG`"),
                   Parameter('ply', type="PLY",
                             doc=":class:`PLY` to which the bounding polygons will be added."),
                   Parameter('refresh', type=Type.INT32_T,
                             doc="TRUE to force the boundary to be refreshed."),
                   Parameter('min_points', type=Type.INT32_T,
                             doc="Minimum number of points in polygons refreshed (0 for all)")
               ]),

        Method('GridReprojectAndWindow_IMU', module='geoengine.core', version='7.3.0',
               availability=Availability.PUBLIC, 
               doc="Create a new grid by reprojecting an existing grid and windowing its contents",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_grid_filename', type=Type.STRING,
                             doc="Input grid filename"),
                   Parameter('output_grid_filename', type=Type.STRING,
                             doc="Output grid filename"),
                   Parameter('new_projection', type="IPJ",
                             doc="Output grid projection"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Window minX (in output projection)"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Window maxX (in output projection)"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Window minY (in output projection)"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Window maxY (in output projection)")
               ]),

        Method('GridResample_IMU', module='geoengine.core', version='7.3.0',
               availability=Availability.PUBLIC, 
               doc="Create a new grid by resampling an existing grid",
               notes="Works only for un rotated grids.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_grid_filename', type=Type.STRING,
                             doc="Input grid filename"),
                   Parameter('output_grid_filename', type=Type.STRING,
                             doc="Output grid filename"),
                   Parameter('o_x', type=Type.DOUBLE,
                             doc="Origin X"),
                   Parameter('o_y', type=Type.DOUBLE,
                             doc="Origin Y"),
                   Parameter('d_x', type=Type.DOUBLE,
                             doc="Cell spacing X"),
                   Parameter('d_y', type=Type.DOUBLE,
                             doc="Cell spacing Y"),
                   Parameter('n_x', type=Type.INT32_T,
                             doc="Elements in X"),
                   Parameter('n_y', type=Type.INT32_T,
                             doc="Elements in Y")
               ]),

        Method('GridResize_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Resize a grid to reduce the size not cover the outside dummies.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('in_grd', type=Type.STRING,
                             doc="File name of input grid"),
                   Parameter('out_grd', type=Type.STRING,
                             doc="File name of output grid")
               ]),

        Method('GridShad_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, # TODO Check if we can make these generally available
               doc="Create a shaded relief image.",
               notes="""
               Pass :const:`GS_R8DM` as parameters to obtain default values.
               The default values are returned.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('in_grid', type=Type.STRING,
                             doc="Input image name"),
                   Parameter('sh_grid', type=Type.STRING,
                             doc="Output new shaded image"),
                   Parameter('inc', type=Type.DOUBLE, is_ref=True,
                             doc="Inclination 0-90 degrees (def. 45)"),
                   Parameter('dec', type=Type.DOUBLE, is_ref=True,
                             doc="Declination 0-360 degrees azimuth (def. 45)"),
                   Parameter('scl', type=Type.DOUBLE, is_ref=True,
                             doc="Vertical scale factor (distance/z unit)")
               ]),

        Method('RefreshShad_IMU', module='geoengine.core', version='9.4.0',
               availability=Availability.PUBLIC, # TODO Check if we can make these generally available
               doc="Refresh a shaded relief image ",
               notes="""
       Pass :const:`GS_R8DM` as parameters to obtain default values.
       The default values are returned.
       """,
               return_type=Type.VOID,
               parameters=[
                   Parameter('in_img', type="IMG",
                             doc="Input grid object"),
                   Parameter('sh_img', type="IMG",
                             doc="Output shaded grid object"),
                   Parameter('inc', type=Type.DOUBLE, is_ref=True,
                             doc="Inclination 0-90 degrees (def. 45)"),
                   Parameter('dec', type=Type.DOUBLE, is_ref=True,
                             doc="Declination 0-360 degrees azimuth (def. 45)"),
                   Parameter('scl', type=Type.DOUBLE, is_ref=True,
                             doc="Vertical scale factor (distance/z unit)")
               ]),

        Method('GridST_IMU', module='geoengine.core', version='5.1.2',
               availability=Availability.LICENSED, 
               doc="Update an :class:`ST` object using a grid.",
               notes="""
               The input :class:`ST` object is not initialized by :func:`GridST_IMU`,
               so this function can be used to accumulate statistical
               info on more than a single grid.
               See :class:`ST`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Grid name"),
                   Parameter('st', type="ST",
                             doc=":class:`ST` (statistics) object to fill/update")
               ]),

        Method('GridStat_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Reports statistics contained in a grid header.",
               notes="Statistics are returned in the parameter set",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Name of the grid to get stats from"),
                   Parameter('type', type=Type.INT32_T, is_ref=True,
                             doc="Element type in bytes"),
                   Parameter('xelem', type=Type.INT32_T, is_ref=True,
                             doc="Elements in X direction"),
                   Parameter('yelem', type=Type.INT32_T, is_ref=True,
                             doc="Elements in Y direction"),
                   Parameter('xsep', type=Type.DOUBLE, is_ref=True,
                             doc="X element separation"),
                   Parameter('ysep', type=Type.DOUBLE, is_ref=True,
                             doc="Y element separation"),
                   Parameter('kx', type=Type.INT32_T, is_ref=True,
                             doc="KX (storage orientation)"),
                   Parameter('x_orig', type=Type.DOUBLE, is_ref=True,
                             doc="X origin"),
                   Parameter('y_orig', type=Type.DOUBLE, is_ref=True,
                             doc="Y origin"),
                   Parameter('rot', type=Type.DOUBLE, is_ref=True,
                             doc="Grid Rotation"),
                   Parameter('base', type=Type.DOUBLE, is_ref=True,
                             doc="Base removed"),
                   Parameter('mult', type=Type.DOUBLE, is_ref=True,
                             doc="Grid multiplier")
               ]),

        Method('GridStatComp_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Reports statistics contained in a grid header.",
               notes="Statistics are returned in the parameter set",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Name of the grid to get stats from"),
                   Parameter('type', type=Type.INT32_T, is_ref=True,
                             doc="Element type: 0 - byte 1 - USHORT 2 - SHORT 3 - LONG 4 - FLOAT 5 - DOUBLE 6 - 32 byte Color (RGBx)"),
                   Parameter('xelem', type=Type.INT32_T, is_ref=True,
                             doc="Elements in X direction"),
                   Parameter('yelem', type=Type.INT32_T, is_ref=True,
                             doc="Elements in Y direction"),
                   Parameter('xsep', type=Type.DOUBLE, is_ref=True,
                             doc="X element separation"),
                   Parameter('ysep', type=Type.DOUBLE, is_ref=True,
                             doc="Y element separation"),
                   Parameter('kx', type=Type.INT32_T, is_ref=True,
                             doc="KX (storage orientation)"),
                   Parameter('x_orig', type=Type.DOUBLE, is_ref=True,
                             doc="X origin"),
                   Parameter('y_orig', type=Type.DOUBLE, is_ref=True,
                             doc="Y origin"),
                   Parameter('rot', type=Type.DOUBLE, is_ref=True,
                             doc="Grid Rotation"),
                   Parameter('base', type=Type.DOUBLE, is_ref=True,
                             doc="Base removed"),
                   Parameter('mult', type=Type.DOUBLE, is_ref=True,
                             doc="Grid multiplier"),
                   Parameter('comp', type=Type.DOUBLE, is_ref=True,
                             doc="Compression Ratio")
               ]),

        Method('GridStatExt_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Reports statistics of a grid's elements.",
               notes="""
               If the :def:`IMU_STAT_FORCED` value is set, the
               statistics will be recalculated.
               Statistics are returned in the parameter set.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Name of the grid to get stats from"),
                   Parameter('force', type=Type.INT32_T,
                             doc=":def:`IMU_STAT_FORCED`"),
                   Parameter('items', type=Type.INT32_T, is_ref=True,
                             doc="Number of valid elements in grid"),
                   Parameter('dums', type=Type.INT32_T, is_ref=True,
                             doc="Number of dummies in grid"),
                   Parameter('min', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum grid value"),
                   Parameter('max', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum grid value"),
                   Parameter('mean', type=Type.DOUBLE, is_ref=True,
                             doc="Grid mean"),
                   Parameter('stddev', type=Type.DOUBLE, is_ref=True,
                             doc="Grid standard deviation")
               ]),

        Method('GridStatTrend_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Reports Trend Info of a grid (for first order coefficients only).",
               notes="Trend Info are returned in the parameter set",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Name of the grid to get stats from"),
                   Parameter('trend_valid', type=Type.INT32_T, is_ref=True,
                             doc="Trend Valid Flag"),
                   Parameter('co', type=Type.DOUBLE, is_ref=True,
                             doc="Trend coefficient rCo"),
                   Parameter('cx', type=Type.DOUBLE, is_ref=True,
                             doc="Trend coefficient rCx"),
                   Parameter('cy', type=Type.DOUBLE, is_ref=True,
                             doc="Trend coefficient rCy")
               ]),

        Method('GridStatTrendExt_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Reports Extended Trend Info of a grid (for up to third order coefficients).",
               notes="Trend Info are returned in the parameter set",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Grid name"),
                   Parameter('order', type=Type.INT32_T, is_ref=True,
                             doc="Trend order"),
                   Parameter('num_coef', type=Type.INT32_T, is_ref=True,
                             doc="Number of coefficients"),
                   Parameter('xo', type=Type.DOUBLE, is_ref=True,
                             doc="Trend origin Xo"),
                   Parameter('yo', type=Type.DOUBLE, is_ref=True,
                             doc="Trend origin Yo"),
                   Parameter('vm', type="VM",
                             doc=":class:`VM` hold coefficient values MUST BE OF TYPE 'real'")
               ]),

        Method('rSlopeStandardDeviation_IMU', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Return the standard deviation of the slopes.",
               notes="""
               This method calculates the standard deviation of the horizontal
               differences in the X and Y directions for the supplied
               image.  This is useful for shading routines.  A good
               default scaling factor is 2.5 / standard deviation.
               
               The image will be sub-sampled to a statistically meaningful number.
               
               The cell sizes are used to determine the slopes.
               """,
               return_type=Type.DOUBLE,
               return_doc="Standard deviation of grid slopes",
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Grid object")
               ]),

        Method('GridStitch_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Stitches together too grids",
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid1', type=Type.STRING,
                             doc="Input Grid1 name"),
                   Parameter('grid2', type=Type.STRING,
                             doc="Input Grid2 name"),
                   Parameter('grid3', type=Type.STRING,
                             doc="Output Grid name"),
                   Parameter('method', type=Type.INT32_T,
                             doc="Stitching method"),
                   Parameter('tr_order1', type=Type.INT32_T,
                             doc="Grid 1 trend removal order"),
                   Parameter('tr_order2', type=Type.INT32_T,
                             doc="Grid 2 trend removal order"),
                   Parameter('tr_calc', type=Type.INT32_T,
                             doc="Trend removal type of points to use"),
                   Parameter('gap', type=Type.DOUBLE,
                             doc="Gap for interpolation"),
                   Parameter('spline', type=Type.INT32_T,
                             doc="Interpolation spline method"),
                   Parameter('path', type=Type.INT32_T,
                             doc="Path selection"),
                   Parameter('pply', type="PLY",
                             doc=":class:`PLY` object for user path"),
                   Parameter('weighting', type=Type.DOUBLE,
                             doc="Correction weighting"),
                   Parameter('width', type=Type.INT32_T,
                             doc="Width of corrections, in grid cells (8 to 256)")
               ]),

        Method('GridStitchCtl_IMU', module='geoengine.core', version='5.1.4',
               availability=Availability.LICENSED, 
               doc="Stitches together two grids - control file for options.",
               notes="""
               Data validation is done internally, not in the GX.
               This is simply a way of avoiding writing a new GX wrapper
               every time an option is added.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ctl', type=Type.STRING,
                             doc='Control file containing all "GRIDSTCH" parameters')
               ]),

        Method('GridTiff_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Generate a Tiff (Tagged-Image file format) file with up to 16 grids.",
               notes="""
               The background color can be either selected
               from one of 8 settings, or can be specified
               as a combination of Reg,Green, and Blue values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('grds', type=Type.STRING,
                             doc="Comma-delimited string containing names of all grids to use in Tiff generation Up to 16 grids allowed."),
                   Parameter('tiff', type=Type.STRING,
                             doc="Name of Tiff file to create"),
                   Parameter('bcol', type=Type.STRING,
                             doc="Background color option. One of W (White)  K (Black) C (Cyan) M (Magenta) Y (Yellow) R (Red)  G (Green) B (Blue)"),
                   Parameter('red', type=Type.INT32_T,
                             doc="Background Red value (0-255)"),
                   Parameter('green', type=Type.INT32_T,
                             doc="Background Green (0-255)"),
                   Parameter('blue', type=Type.INT32_T,
                             doc="Background Blue  (0-255)"),
                   Parameter('csize', type=Type.DOUBLE,
                             doc="New cell size"),
                   Parameter('reg', type=Type.INT32_T,
                             doc="Pixel size of registration marks"),
                   Parameter('scale', type=Type.DOUBLE,
                             doc="Map scale")
               ]),

        Method('GridTrnd_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Remove a trend surface from a grid.",
               notes="""
               Both Images must be of type :const:`GS_DOUBLE`.
               The :class:`VM` parameter must be of type REAL,
               and be of size 10 at most.
               
               The number of coefficients must be
               compatible with the order of the
               trend removed. Following is the
               number of coefficients which should
               be present for a given order
               
               ===== ======================
               Order Number of Coefficients
               ----- ----------------------
               0      1
               1      3
               2      6
               3      10
               ===== ======================
               
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('imgi', type="IMG",
                             doc="Handle to input image"),
                   Parameter('imgo', type="IMG",
                             doc="Handle to output image"),
                   Parameter('tr_option', type=Type.INT32_T,
                             doc="0-calculate, 1-given, 2-replace"),
                   Parameter('edge', type=Type.INT32_T,
                             doc=":def:`IMU_TREND`"),
                   Parameter('order', type=Type.INT32_T,
                             doc="Trend order"),
                   Parameter('vm', type="VM",
                             doc=":class:`VM` holds coefficients"),
                   Parameter('num_coefs', type=Type.INT32_T,
                             doc="Number of coefficients")
               ]),

        Method('GridTrns_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Transpose a grid by swapping the grid rows with
               the grid columns.
               """,
               notes="""
               If the grid has a line orientation that does NOT
               match the :def:`IMU_TRANS` value, this method will
               not succeed.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Name of the grid to transpose"),
                   Parameter('tcon', type=Type.INT32_T,
                             doc="Transpose condition value :def:`IMU_TRANS`")
               ]),

        Method('GridVD_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Apply vertical derivative convolution filter to a grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('im_gi', type="IMG",
                             doc="Input image"),
                   Parameter('im_go', type="IMG",
                             doc="Output image")
               ]),

        Method('GridVol_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               Calculates the grid volumes above and below a
               reference base.
               """,
               notes="""
               Volumes are calculated above and below a
               reference base level, and reported as positive
               integers. A multiplier is applied to the final
               volume (to correct for units).
               
               The :class:`IMG` parameters MUST be of type :const:`GS_FLOAT`!
               If not, the method will terminate.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Image of the grid to calculate volume for"),
                   Parameter('rbase', type=Type.DOUBLE,
                             doc="Reference base"),
                   Parameter('mult', type=Type.DOUBLE,
                             doc="Multiplier to final volume"),
                   Parameter('vol_a', type=Type.DOUBLE, is_ref=True,
                             doc="Grid Volume above reference base"),
                   Parameter('vol_b', type=Type.DOUBLE, is_ref=True,
                             doc="Grid Volume below reference base"),
                   Parameter('diff', type=Type.DOUBLE, is_ref=True,
                             doc="Differences between volumes")
               ]),

        Method('GridWind_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Create a grid using a defined area window
               within a larger grid.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Image of input grid"),
                   Parameter('out', type=Type.STRING,
                             doc="Name of output grid file"),
                   Parameter('coord', type=Type.INT32_T,
                             doc=":def:`IMU_WIND_COORD`"),
                   Parameter('xmin', type=Type.DOUBLE,
                             doc="Min. limit of window in X direction (can be :const:`rDUMMY`)"),
                   Parameter('xmax', type=Type.DOUBLE,
                             doc="Max. limit of window in X direction (can be :const:`rDUMMY`)"),
                   Parameter('ymin', type=Type.DOUBLE,
                             doc="Min. limit of window in Y direction (can be :const:`rDUMMY`)"),
                   Parameter('ymax', type=Type.DOUBLE,
                             doc="Max. limit of window in Y direction (can be :const:`rDUMMY`)"),
                   Parameter('zmin', type=Type.DOUBLE,
                             doc="Minimum Z data value in output grid (can be :const:`rDUMMY`)"),
                   Parameter('zmax', type=Type.DOUBLE,
                             doc="Maximum Z data value in output grid (can be :const:`rDUMMY`)"),
                   Parameter('csize', type=Type.DOUBLE,
                             doc="New grid cell size"),
                   Parameter('clip', type=Type.INT32_T,
                             doc=":def:`IMU_WIND_DUMMIES`"),
                   Parameter('dec', type=Type.INT32_T,
                             doc="Decimation factor"),
                   Parameter('mdf', type=Type.STRING,
                             doc="Name of .MDF file for data clipping")
               ]),

        Method('GridWind2_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Window a grid.",
               notes="""
               To change the cell size or work in a different projection,
               first inherit the :class:`IMG` by calling
               
               The windowed grid will be adjusted/expanded to include the
               defined area and line up on an even grid cell.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Image of input grid"),
                   Parameter('out', type=Type.STRING,
                             doc="Name of output grid file"),
                   Parameter('xmin', type=Type.DOUBLE,
                             doc="Minimum X, ground units (can be :const:`rDUMMY`)"),
                   Parameter('xmax', type=Type.DOUBLE,
                             doc="Maximum X (can be :const:`rDUMMY`)"),
                   Parameter('ymin', type=Type.DOUBLE,
                             doc="Minimum Y (can be :const:`rDUMMY`)"),
                   Parameter('ymax', type=Type.DOUBLE,
                             doc="Maximum Y (can be :const:`rDUMMY`)"),
                   Parameter('zmin', type=Type.DOUBLE,
                             doc="Minimum Z (can be :const:`rDUMMY`)"),
                   Parameter('zmax', type=Type.DOUBLE,
                             doc="Maximum Z (can be :const:`rDUMMY`)"),
                   Parameter('clip', type=Type.INT32_T,
                             doc=":def:`IMU_WIND_DUMMIES`")
               ]),

        Method('GridXYZ_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Export a Grid image to an XYZ file.",
               notes="""
               The :class:`IMG` (image) of the grid to export must
               be of type :const:`GS_FLOAT`. If not, this method will
               terminate with an error.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Image of the grid to export"),
                   Parameter('xyz', type=Type.STRING,
                             doc="Name of new XYZ file"),
                   Parameter('index', type=Type.INT32_T,
                             doc=":def:`IMU_XYZ_INDEX`"),
                   Parameter('dec_x', type=Type.INT32_T,
                             doc="X direction decimation factor"),
                   Parameter('dec_y', type=Type.INT32_T,
                             doc="Y direction decimation factor"),
                   Parameter('lab', type=Type.INT32_T,
                             doc=":def:`IMU_XYZ_LABEL`")
               ]),

        Method('iGridType_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Reports the true data the of a grid (geosoft types)",
               return_type=Type.INT32_T,
               return_doc=":def:`GS_TYPES`",
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Name of the Grid")
               ]),

        Method('MakeMITabFile_IMU', module='geoengine.map', version='5.1.6',
               availability=Availability.LICENSED, 
               doc="Make a MapInfo tab file for this grid",
               return_type=Type.VOID,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="Grid file name")
               ]),

        Method('MakeMITabfromGrid_IMU', module='geoengine.map', version='5.1.5',
               availability=Availability.LICENSED, 
               doc="Make a MapInfo tab file for this grid as rendered in a map",
               return_type=Type.VOID,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="Grid file name")
               ]),

        Method('MakeMITabfromMap_IMU', module='geoengine.map', version='5.1.5',
               availability=Availability.LICENSED, 
               doc="Make a MapInfo tab file from this map",
               return_type=Type.VOID,
               parameters = [
                   Parameter('map', type=Type.STRING,
                             doc="Map file name")
               ]),

        Method('Mosaic_IMU', module='geoengine.core', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Create a mosaic image of an image list.",
               notes="""
               The images are simply placed on the output image, starting with
               the first image. Note that this function may require very large
               amounts of virtual memory.
               """,
               return_type="IMG",
               return_doc=":class:`IMG` Object",
               parameters = [
                   Parameter('grids', type=Type.STRING,
                             doc="Image names ('|' separated)"),
                   Parameter('name', type=Type.STRING,
                             doc='Output image name ("" for a memory only image)'),
                   Parameter('ipj', type="IPJ",
                             doc="Projection to use (0 to use the first grid's projection)"),
                   Parameter('cell', type=Type.DOUBLE,
                             doc="Cell size to use (rDummy to use first grid)")
               ]),

        Method('PeakSize_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Define the sizes of all the peaks in an image.",
               notes="""
               Extending from the peak location of an anomaly to the inflection
               points of the grid values along each of the 8 directions results in
               8 radii. Anomaly size is defined as the 2*mediam of the 8 radii.
               
               Precision factor is used to control definition of an inflection point.
               For points A,B, and C, B is an inflection point if (A+C)/2.0 > B. With
               the precision factor, B is an inflection point only when
               (A+C)/2.0 > B*(1.0+Precision factor).
               This factor must be within (-1.0,1.0).
               
               Note: :func:`PeakSize2_IMU` is probably a better routine...
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Grid file name"),
                   Parameter('vv_x', type="VV",
                             doc="Peaks' X"),
                   Parameter('vv_y', type="VV",
                             doc="Peaks' Y"),
                   Parameter('max', type=Type.INT32_T,
                             doc="Maximum target diameter (window) in # of cells"),
                   Parameter('prec', type=Type.DOUBLE,
                             doc="Precision factor (see note above)"),
                   Parameter('v_vz', type="VV",
                             doc="Returned peak (anomaly) sizes in data units")
               ]),

        Method('PeakSize2_IMU', module='geoengine.core', version='5.1.4',
               availability=Availability.LICENSED, 
               doc="Define the sizes of all the peaks in an image - new algorithm",
               notes="""
               Extending from the peak location of an anomaly to the inflection
               points of the grid values along each of the 8 directions results in
               8 radii. Anomaly size is defined as the 2*mediam of the 8 radii.
               
               This algorithm uses 4 successive points d1, d2, d3 and d4 in any
               direction. Given slopes m1 = d2-d1, m2 = d3-d2 and m3 = d4-d3,
               an inflection point occurs between d2 and d3 if m1>m2 and m2<m3.
               The location index is given as i3 - s2/(s2-s1), where i3 is the index
               of d3, and s1=m2-m1 and s2=m3-m2.
               
               This algorithm tends to give much smaller (and more reasonable)
               results than :func:`PeakSize_IMU`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('grid', type=Type.STRING,
                             doc="Grid file name"),
                   Parameter('vv_x', type="VV",
                             doc="Peaks' X"),
                   Parameter('vv_y', type="VV",
                             doc="Peaks' Y"),
                   Parameter('max', type=Type.INT32_T,
                             doc="Maximum target diameter (window) in # of cells"),
                   Parameter('v_vz', type="VV",
                             doc="Returned peak (anomaly) sizes in data units")
               ]),

        Method('PigeonHole_IMU', module='geoengine.core', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Pigeon-hole and count points by location into a grid.",
               notes="""
               X and Y location VVs are input. If a point (X, Y) is located within
               one-half cell width from a location in the grid, then the value of
               the grid at that location is incremented by 1.
               The cells are inclusive at the minima, and exclusive at the maxima:
               e.g. if dDx = dDy = 1, and dXo = dYo = 0, then the corner cell would
               accept values  -0.5 <= X < 0.5 and -0.5 <= Y < 0.5.
               The grid values should be set to 0 before calling this function.
               
               The number of points "pigeon-holed" is returned to the user.
               This function is useful, for instance, in determining the density of
               sample locations in a survey area.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Input grid"),
                   Parameter('vv_x', type="VV",
                             doc="X locations"),
                   Parameter('vv_y', type="VV",
                             doc="Y locations"),
                   Parameter('put', type=Type.INT32_T, is_ref=True,
                             doc="Number of points located in the grid.")
               ]),

        Method('Profile_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Extract a profile from a grid.",
               notes="""
               Returned :class:`VV` will start at X1,Y1 and will sample
               up to X2,Y2 at the specified separation.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Input image"),
                   Parameter('x1', type=Type.DOUBLE,
                             doc="X1"),
                   Parameter('y1', type=Type.DOUBLE,
                             doc="Y1"),
                   Parameter('x2', type=Type.DOUBLE,
                             doc="X2"),
                   Parameter('y2', type=Type.DOUBLE,
                             doc="Y2"),
                   Parameter('samsep', type=Type.DOUBLE,
                             doc="Sample separation, if 0.0, use grid cell size"),
                   Parameter('vv_z', type="VV",
                             doc=":class:`VV` in which to place result")
               ]),

        Method('ProfileVV_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Extract a :class:`VV` profile from a grid.",
               see_also="iGetPolyLine_DBE",
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Input image"),
                   Parameter('vv_x', type="VV",
                             doc="X :class:`VV` coordinates"),
                   Parameter('vv_y', type="VV",
                             doc="Y :class:`VV` coordinates"),
                   Parameter('vv_z', type="VV",
                             doc=":class:`VV` in which to place result")
               ]),

        Method('RangeGrids_IMU', module='geoengine.core', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Determine bounding rectangle for a set of grids",
               notes="""
               If an :class:`IPJ` is IPJ_CS_UNKNOWN, the
               :class:`IPJ` of the first grid in the list will be used and
               the :class:`IPJ` will be returned in this setting.
               Otherwise, the range in the requested :class:`IPJ` will be
               determined.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('grids', type=Type.STRING,
                             doc='List of grid files, "|" delimited'),
                   Parameter('ipj', type="IPJ",
                             doc="Projection for the range - see notes"),
                   Parameter('min_x', type=Type.DOUBLE, is_ref=True,
                             doc="Min X - returned range in the projection"),
                   Parameter('min_y', type=Type.DOUBLE, is_ref=True,
                             doc="Min Y"),
                   Parameter('max_x', type=Type.DOUBLE, is_ref=True,
                             doc="Max X"),
                   Parameter('max_y', type=Type.DOUBLE, is_ref=True,
                             doc="Max Y")
               ]),

        Method('RangeLL_IMU', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Determine the range in lat. and long. of a projected grid",
               notes="""
               This routine determines the latitude and longitudes along the
               edge of a grid and returns the minimal and maximal values.
               It scans each row and and column and finds the first non-dummy
               position at the start and end, and then determines the coordinates
               at those points.
               If the grid has no data, no :class:`IPJ` object, or if the Source Type of
               the :class:`IPJ` is not :const:`IPJ_TYPE_PCS` (projected coordinate system), then the
               returned values are dummies (:const:`GS_R8DM`).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Input image"),
                   Parameter('min_lat', type=Type.DOUBLE, is_ref=True,
                             doc="Min latitude"),
                   Parameter('min_lon', type=Type.DOUBLE, is_ref=True,
                             doc="Min longitude"),
                   Parameter('max_lat', type=Type.DOUBLE, is_ref=True,
                             doc="Max latitude"),
                   Parameter('max_lon', type=Type.DOUBLE, is_ref=True,
                             doc="Max longitude")
               ]),

        Method('StatWindow_IMU', module='geoengine.core', version='5.0.5',
               availability=Availability.LICENSED, 
               doc="Calculate grid statistics in a window",
               notes="""
               The maximum values needed will beused to
               decimate the sampling of the grid in order to
               improve performance.  100000 is often a good
               number when absolute precision is not
               required.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="Name of the grid to get stats from"),
                   Parameter('min_x', type=Type.DOUBLE,
                             doc="Min X window"),
                   Parameter('min_y', type=Type.DOUBLE,
                             doc="Min Y window"),
                   Parameter('max_x', type=Type.DOUBLE,
                             doc="Max X window"),
                   Parameter('max_y', type=Type.DOUBLE,
                             doc="Max Y window"),
                   Parameter('max', type=Type.INT32_T,
                             doc="Maximum values needed, 0 for all"),
                   Parameter('st', type="ST",
                             doc=":class:`ST` object, stats are accumulated")
               ]),

        Method('UpdatePLY_IMU', module='geoengine.core', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Update the grid boundary in the grid metadata",
               notes="""
               You can call the GridEdgePLY function to get an edge,
               perhaps alter the edge, such as thin it to a reasonable
               resolution, then put set it as the grid boundary by
               calling this funtion.  This is similar to the
               GridPLYEx function except that you get to alter the
               :class:`PLY` before it is placed back in the :class:`IMG`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('img', type="IMG",
                             doc="The Grid"),
                   Parameter('ply', type="PLY",
                             doc=":class:`PLY` containing the edges.")
               ])
    ]
}

