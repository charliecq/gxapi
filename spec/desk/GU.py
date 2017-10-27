from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('GU',
                 doc="""
                 Not a class. A catch-all group of functions performing
                 various geophysical processes, including the calculation
                 of simple EM model responses, certain instrument dump
                 file imports, and 2D Euler deconvolution.
                 """)


gx_defines = [
    Define('EM_ERR',
           doc="Error Scaling",
           constants=[
               Constant('EM_ERR_UNSCALED', value='0', type=Type.INT32_T),
               Constant('EM_ERR_LOGSCALING', value='1', type=Type.INT32_T)
           ]),

    Define('EM_INV',
           doc="Type of Inversion",
           constants=[
               Constant('EM_INV_INPHASE', value='0', type=Type.INT32_T),
               Constant('EM_INV_QUADRATURE', value='1', type=Type.INT32_T),
               Constant('EM_INV_BOTH', value='2', type=Type.INT32_T)
           ]),

    Define('EMPLATE_DOMAIN',
           doc="Type of Domain",
           constants=[
               Constant('EMPLATE_FREQUENCY', value='1', type=Type.INT32_T),
               Constant('EMPLATE_TIME', value='9', type=Type.INT32_T)
           ]),

    Define('EMPLATE_TX',
           doc="Orientation",
           constants=[
               Constant('EMPLATE_TX_X', value='1', type=Type.INT32_T),
               Constant('EMPLATE_TX_Y', value='2', type=Type.INT32_T),
               Constant('EMPLATE_TX_Z', value='3', type=Type.INT32_T)
           ]),

    Define('GU_DAARC500_DATATYPE',
           doc="Supported serial data types for import",
           constants=[
               Constant('GU_DAARC500_UNKNOWN', value='0', type=Type.INT32_T),
               Constant('GU_DAARC500_GENERIC_ASCII', value='1', type=Type.INT32_T),
               Constant('GU_DAARC500_GPS', value='2', type=Type.INT32_T),
               Constant('GU_DAARC500_GR820_256D', value='3', type=Type.INT32_T),
               Constant('GU_DAARC500_GR820_256DU', value='4', type=Type.INT32_T),
               Constant('GU_DAARC500_GR820_512DU', value='5', type=Type.INT32_T),
               Constant('GU_DAARC500_NAV', value='6', type=Type.INT32_T)
           ]),

    Define('PEAKEULER_XY',
           doc="Fit Options",
           constants=[
               Constant('PEAKEULER_XY_NOFIT', value='0', type=Type.INT32_T),
               Constant('PEAKEULER_XY_FIT', value='1', type=Type.INT32_T)
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('DipoleMag_GU', module='geogxx', version='5.1.6',
               availability=Availability.LICENSED, 
               doc="Calculate a dipole magnetic field into XYZ file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('xyz_file', type=Type.STRING,
                             doc="sXYZ"),
                   Parameter('depth', type=Type.DOUBLE,
                             doc="rDepth"),
                   Parameter('inc', type=Type.DOUBLE,
                             doc="rInc"),
                   Parameter('nx', type=Type.INT32_T,
                             doc="iNX"),
                   Parameter('ny', type=Type.INT32_T,
                             doc="iNY"),
                   Parameter('dx', type=Type.DOUBLE,
                             doc="rDX"),
                   Parameter('dy', type=Type.DOUBLE,
                             doc="rDY")
               ]),

        Method('EMHalfSpaceInv_GU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Inverts EM responses to the best halfspace model.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('coil_spacing', type=Type.DOUBLE,
                             doc="Coil spacing: error if == 0"),
                   Parameter('coil_frequency', type=Type.DOUBLE,
                             doc="Frequency"),
                   Parameter('coil_configuration', type=Type.INT32_T,
                             doc=":def:`EMLAY_GEOMETRY`"),
                   Parameter('tol', type=Type.DOUBLE,
                             doc="Fractional error in best fit resistivity"),
                   Parameter('threshold', type=Type.DOUBLE,
                             doc="Don't invert values below this"),
                   Parameter('vv_height', type="VV",
                             doc="Height above ground"),
                   Parameter('vv_in_phase', type="VV",
                             doc="In-phase part (ppm)"),
                   Parameter('p8', type="VV",
                             doc="Quadrature part (ppm)"),
                   Parameter('p9', type="VV",
                             doc="On return - inverted halfspace resistivities"),
                   Parameter('p10', type=Type.INT32_T,
                             doc=":def:`EM_INV`"),
                   Parameter('p11', type=Type.INT32_T,
                             doc=":def:`EM_ERR`"),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="Starting value for inversion (can be :def_val:`rDUMMY`)")
               ]),

        Method('EMHalfSpaceVV_GU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="EM Halfspace forward model response.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('coil_spacing', type=Type.DOUBLE,
                             doc="Coil separation"),
                   Parameter('coil_frequency', type=Type.DOUBLE,
                             doc="Frequency"),
                   Parameter('coil_configuration', type=Type.INT32_T,
                             doc=":def:`EMLAY_GEOMETRY`"),
                   Parameter('rvv', type="VV",
                             doc="Input resistivity values"),
                   Parameter('hvv', type="VV",
                             doc="Input height values"),
                   Parameter('ivv', type="VV",
                             doc="Output In-phase"),
                   Parameter('qvv', type="VV",
                             doc="Output Quadrature-phase")
               ]),

        Method('Geometrics2DB_GU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Convert a Geometrics STN file to a database.",
               notes="""
               Assumes that the database is new and empty. If not, existing channels
               with names X, Y, Mag1, Mag2, Time, Date, and Mark will deleted and then created.  
               Existing lines will be erased and then created if they are the same as the new ones.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('db', type="DB",
                             doc=":class:`DB` handle"),
                   Parameter('ra', type="RA",
                             doc=":class:`RA` handle, STN file"),
                   Parameter('log_wa', type="WA",
                             doc="Log file :class:`WA` handle"),
                   Parameter('survey_mode', type=Type.INT32_T,
                             doc="Simple mode (1) or Mapped mode (2)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Survey line orientation:  North-south - 0 East-west   - 1"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Starting survey position: SW - 0, NW - 1, SE - 2, NE - 3,"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Bidirectional (0) or Unidirectional (1)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Starting position X"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Starting position Y"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Mark spacing"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Line spacing")
               ]),

        Method('Geometrics2TBL_GU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Convert a Geometrics station file (STN) to a table file (TBL)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ra', type="RA",
                             doc=":class:`RA` handle, input station file"),
                   Parameter('wa', type="WA",
                             doc="Output TBL file"),
                   Parameter('log_wa', type="WA",
                             doc="Log file :class:`WA` handle")
               ]),

        Method('GeometricsQC_GU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Correct reading positions in a database.",
               notes="""
               There are six cases to consider:
               
               ========    ====  =============  ========================================
               Case        Flag  Solutions      Symptoms
               ========    ====  =============  ========================================
               CASE 1A:    0     No correction  Recorded and actual Line lengths same
                                                Reading densities vary slightly (passed
                                                the tolerance test)
               --------    ----  -------------  ----------------------------------------
               CASE 1B     -1    No correction  Line lengths same
                                                Reading densities vary and cannot
                                                pass the tolerance test
               --------    ----  -------------  ----------------------------------------
               CASE 2A     1     Corrected by   Recorded line length too short
                                 extension      Possible high readings in segment(s)
                                                Corrected (by extending) and actual
                                                lengths become the same
               --------    ----  -------------  ----------------------------------------
               CASE 2B     2     Corrected by   Recorded line length too short
                                 interpolation  Possible high readings in segment(s)
                                                Corrected (by extending) and actual
                                                lengths are not same. Interpolation is
                                                then applied
               --------    ----  -------------  ----------------------------------------
               CASE 3A     1     Corrected by   Recorded line length too long
                                 shifting or    Possible low readings in segment(s)
                                 (shrank)       Corrected (by shifting) and actual
                                                lengths are same
               --------    ----  -------------  ----------------------------------------
               CASE 3B     2     Corrected by   Recorded line length too long
                                 interpolation  Possible low readings in segment(s)
                                                Corrected (by shifting) and actual
                                                lengths are not same. Interpolation
                                                is then applied
               ========    ====  =============  ========================================
               
               
               TERMINOLOGY:
               
               Segments
                    A segment refers to the distance and its contents between
                    two adjacent fiducial markers
               
               Normal Density
                    The density (number of readings) shared by the segments in
                    a survey line. The number of segments with the density is greater 
                    than the number of segments having a different density in a line.
               
               Tolerance and Bound:
                    Tolerance is defined as a percentage, say ``50% (=0.5)``.
                    Based on the tolerance, a lower bound and upper bound
               
                    can be defined:
               
                    ::

                        Lower bound = (Normal Density) - (Normal Density)*Tolerance
                        Upper bound = (Normal Density) - (Normal Density)*Tolerance
               
                    Segments will pass the tolerance test if the number of readings
                    falls within the Lower and Upper Bounds.

               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('wa', type="WA",
                             doc="Output error log file"),
                   Parameter('line', type=Type.STRING,
                             doc="Database line number. For output to log file only"),
                   Parameter('in_vv', type="VV",
                             doc="Input :class:`VV`, :def_val:`GS_DOUBLE`"),
                   Parameter('tol', type=Type.DOUBLE,
                             doc="Tolerance defined as percentage, say 50.0 means 50%. Must be >=0.0 Lower bound = (Normal Density) - (Normal Density)*Tolerance Upper bound = (Normal Density) + (Normal Density)*Tolerance"),
                   Parameter('min_coord', type=Type.DOUBLE,
                             doc="Minimum coordinate (X or Y)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Maximum coordinate (X or Y)"),
                   Parameter('p7', type="VV",
                             doc="Output :class:`VV`, :def_val:`GS_DOUBLE`"),
                   Parameter('p8', type="VV",
                             doc="Output Flag :class:`VV`, :def_val:`GS_LONG`")
               ]),

        Method('Geonics3138Dump2DB_GU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Convert a Geonics EM31/EM38 file in dump format to a database.",
               notes="""
               Assumes that the database is new and empty. If not, existing channels
               with names X, Y, Station, Conductivity, Inphase, Quadrature,
               and Time will deleted and then created.  Existing lines will
               be erased and then created if they are the same as the new ones.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('db', type="DB",
                             doc=":class:`DB` handle"),
                   Parameter('r_ah', type="RA",
                             doc=":class:`RA` handle, Header file"),
                   Parameter('r_ad', type="RA",
                             doc=":class:`RA` handle, Dump file"),
                   Parameter('log_wa', type="WA",
                             doc="Log file :class:`WA` handle"),
                   Parameter('line_mult', type=Type.DOUBLE,
                             doc="Line multiplier"),
                   Parameter('stat_mult', type=Type.DOUBLE,
                             doc="Station multiplier")
               ]),

        Method('Geonics61Dump2DB_GU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Convert a Geonics EM61 file in dump format to a database.",
               notes="""
               Assumes that the database is new and empty. If not, existing channels
               with names X, Y, Station, Conductivity, Inphase, Quadrature,
               and Time will deleted and then created.  Existing lines will
               be erased and then created if they are the same as the new ones.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('db', type="DB",
                             doc=":class:`DB` handle"),
                   Parameter('ra', type="RA",
                             doc=":class:`RA` handle, dump file"),
                   Parameter('log_wa', type="WA",
                             doc="Log file :class:`WA` handle"),
                   Parameter('line_mult', type=Type.DOUBLE,
                             doc="Line multiplier"),
                   Parameter('stat_mult', type=Type.DOUBLE,
                             doc="Station multiplier - Not used in the calculation")
               ]),

        Method('GeonicsDAT2DB_GU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Convert a Geonics EM31/EM38/EM61 file in :class:`DAT` format to a database.",
               notes="""
               Assumes that the database is new and empty. If not, existing channels
               with names X, Y, Station, Conductivity, Inphase, Quadrature,
               and Time will deleted and then created.  Existing lines will
               be erased and then created if they are the same as the new ones.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('db', type="DB",
                             doc=":class:`DB` handle"),
                   Parameter('ra', type="RA",
                             doc=":class:`RA` handle"),
                   Parameter('log_wa', type="WA",
                             doc="Log file :class:`WA` handle"),
                   Parameter('line_mult', type=Type.DOUBLE,
                             doc="Line multiplier"),
                   Parameter('stat_mult', type=Type.DOUBLE,
                             doc="Station multiplier - Not used in the calculation")
               ]),

        Method('GrCurvCor_GU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Gravity Curvature (Bullard B) Correction to Bouguer anomaly",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_elev', type="VV",
                             doc="Input Elevation :class:`VV`"),
                   Parameter('vv_lat', type="VV",
                             doc="Input Latitude :class:`VV`"),
                   Parameter('vv_boug', type="VV",
                             doc="Bouguer :class:`VV` for Curvature Correction")
               ]),

        Method('GrCurvCorEx_GU', module='geogxx', version='8.0.1',
               availability=Availability.LICENSED, 
               doc="Gravity Curvature (Bullard B) Correction to Bouguer anomaly, with user input cap density.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_elev', type="VV",
                             doc="Input Elevation :class:`VV`"),
                   Parameter('vv_lat', type="VV",
                             doc="Input Latitude :class:`VV`"),
                   Parameter('vv_boug', type="VV",
                             doc="Bouguer :class:`VV` for Curvature Correction"),
                   Parameter('rho', type=Type.DOUBLE,
                             doc="Cap Density (g/cm^3")
               ]),

        Method('GrDEMVV_GU', module='geogxx', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Get gravity DEM grid :class:`VV` for Bouguer anomaly",
               return_type=Type.VOID,
               parameters = [
                   Parameter('im_gdem', type="IMG",
                             doc="DEM grid"),
                   Parameter('vv_x', type="VV",
                             doc="Input X :class:`VV`"),
                   Parameter('vv_y', type="VV",
                             doc="Input Y :class:`VV`"),
                   Parameter('vv_z', type="VV",
                             doc="Output DEM :class:`VV` for Bouguer Correction")
               ]),

        Method('GrTest_GU', module='geogxx', version='5.1.4',
               availability=Availability.LICENSED, 
               doc="Test triangular prism gravity calculation",
               return_type=Type.VOID,
               parameters = [
                   Parameter('xm', type=Type.DOUBLE,
                             doc="dXm  - model dimension x"),
                   Parameter('ym', type=Type.DOUBLE,
                             doc="dYm  - model dimension y"),
                   Parameter('zm', type=Type.DOUBLE,
                             doc="dZm  - model depth"),
                   Parameter('vv_x', type="VV",
                             doc="VVx  - stations x"),
                   Parameter('vv_y', type="VV",
                             doc="VVy  - stations y"),
                   Parameter('vv_g3', type="VV",
                             doc="VVg3 - 2 triangular prism gravity results"),
                   Parameter('vv_g4', type="VV",
                             doc="VVg4 - regtangular prism gravity results"),
                   Parameter('vv_g1', type="VV",
                             doc="VVg1 - lower triangular prism gravity results"),
                   Parameter('vv_g2', type="VV",
                             doc="VVg2 - upper triangular prism gravity results")
               ]),

        Method('GravityStillReadingCorrection_GU', module='geogxx', version='8.5.0',
               availability=Availability.LICENSED, 
               doc="Gravity Still Reading Correction on selected lines.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('grav_in', type="DB_SYMB",
                             doc="Input gravity channel handle [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('date', type="DB_SYMB",
                             doc="Input date channel handle [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('time', type="DB_SYMB",
                             doc="Input time channel handle [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('still', type=Type.STRING,
                             doc="Still readings file"),
                   Parameter('grav_out', type="DB_SYMB",
                             doc="Output gravity channel handle [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('iEMLayer_GU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate the EM response of a layered earth model.",
               return_type=Type.INT32_T,
               return_doc="""
               0 of OK
               1 if some error
               """,
               parameters = [
                   Parameter('coil_spacing', type=Type.DOUBLE,
                             doc="Coil spacing, error if == 0"),
                   Parameter('coil_frequency', type=Type.DOUBLE,
                             doc="Coil frequency"),
                   Parameter('coil_height', type=Type.DOUBLE,
                             doc="Coil height above layer [0]"),
                   Parameter('coil_configuration', type=Type.INT32_T,
                             doc=":def:`EMLAY_GEOMETRY`"),
                   Parameter('n_layers', type=Type.INT32_T,
                             doc="Number of layers (including lower halfspace)"),
                   Parameter('p6', type="VV",
                             doc="sNLayer-1 thicknesses  [0] to [sNLayer-2]"),
                   Parameter('p7', type="VV",
                             doc="sNLayer conductivities [0] to [sNLayer-1]"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="On return - in-phase part (ppm)"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="On return - quadrature part (ppm)")
               ]),

        Method('iEMPlate_GU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate the conductance of a thin plate model.",
               return_type=Type.INT32_T,
               return_doc="""
               0 of OK
               1 if some error
               """,
               parameters = [
                   Parameter('strike_length', type=Type.DOUBLE,
                             doc="Plate strike length (m)"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Plate dip length (m)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Plate strike (degrees) from X axis"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Plate dip (degrees) from horizontal"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Plate plunge (degrees) from horizontal"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Rx offset in X from Tx"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Rx offset in Y from Tx"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Rx offset in Z from Tx (+'ve down)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Depth below Tx"),
                   Parameter('p10', type=Type.INT32_T,
                             doc=":def:`EMPLATE_DOMAIN`"),
                   Parameter('p11', type="VV",
                             doc="The plate conductances (:class:`VV` length <= 100)"),
                   Parameter('p12', type=Type.INT32_T,
                             doc=":def:`EMPLATE_TX`"),
                   Parameter('p13', type=Type.DOUBLE,
                             doc="Tx frequency (for :def_val:`EMPLATE_TIME`)"),
                   Parameter('p14', type=Type.DOUBLE,
                             doc="Tx time window spacing (for :def_val:`EMPLATE_TIME`)"),
                   Parameter('p15', type=Type.DOUBLE,
                             doc="The frequency/time parameters (SI units: f[Hz] or t[s])"),
                   Parameter('p16', type="VV",
                             doc="On return - X in-phase part (ppm)"),
                   Parameter('p17', type="VV",
                             doc="On return - Y in-phase part (ppm)"),
                   Parameter('p18', type="VV",
                             doc="On return - Z in-phase part (ppm)"),
                   Parameter('p19', type="VV",
                             doc="On return - X quadrature part (ppm)"),
                   Parameter('p20', type="VV",
                             doc="On return - Y quadrature part (ppm)"),
                   Parameter('p21', type="VV",
                             doc="On return - Z quadrature part (ppm)")
               ]),

        Method('IGenUXDetectSymbolsGroupName_GU', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Generate a group name string for UX-Detect symbols",
               notes="""
               Start a new group for the symbols in the UX-Detect system.
               The Target GDB is often in the form "GDB_Targets", where
               "GDB" is the original data. Cut off the part including the
               underscore when creating the map, so you don't get map group
               Names like "SYMBOLS_UxData_Targets_Targets".
               """,
               see_also=":func:`IGenGroupName_STR`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('target_gdb', type=Type.STRING,
                             doc="Input Targets database name"),
                   Parameter('targets', type=Type.STRING,
                             doc="Input Targets group (line) name"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Output group name string"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_GROUP',
                             doc="Output buffer lengths (maximum 32)")
               ]),

        Method('ImportDAARC500Ethernet_GU', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Import Ethernet data from the RMS Instruments DAARC500.",
               notes="""
               Imports Ethernet data recorded
               by the RMS Instruments DAARC500 instrument, and outputs the data
               to a new binary file, returning the number of bytes per
               block, to make it easier to import the data using the regular binary import.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="File to import"),
                   Parameter('output', type=Type.STRING,
                             doc="Output binary file"),
                   Parameter('bytes', type=Type.INT32_T, is_ref=True,
                             doc="Returned number of bytes per block")
               ]),

        Method('ImportDAARC500Serial_GU', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Import Serial data from the RMS Instruments DAARC500.",
               notes="""
               Imports a single channel of the up to 8 serial data channels recorded
               by the RMS Instruments DAARC500 instrument, and outputs the data for
               that channel to a new binary file, returning the number of bytes per
               block, to make it easier to import the data using the regular binary import.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="File to import"),
                   Parameter('channel', type=Type.INT32_T,
                             doc="Channel to import, 1-8"),
                   Parameter('output', type=Type.STRING,
                             doc="Output binary file"),
                   Parameter('bytes', type=Type.INT32_T, is_ref=True,
                             doc="Returned number of bytes per block")
               ]),

        Method('ImportP190_GU', module='geogxx', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Import navigation data in the P190 format.",
               notes="""
               Imports the data, and, if projection information is included
               set the "X" and "Y" channel projection info. (Note: the last file
               imported always takes precedence).
               Different record types are imported to separate lines, but in the
               same order as in the file. Data in existing lines is overwritten.
               If the record type is specified, only records beginning with that
               letter are imported, otherwise all records (except for the header "H"
               records) are imported.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('db', type="DB",
                             doc="Database handle"),
                   Parameter('file', type=Type.STRING,
                             doc="P190 file name"),
                   Parameter('rec_type', type=Type.STRING,
                             doc='Single letter code, e.g. "C", "E", "S", "T" or "V", or blank for all records.'),
                   Parameter('wa', type="WA",
                             doc="Log file")
               ]),

        Method('LagDAARC500GPS_GU', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Lag the GPS fid values for the DAARC500 import.",
               notes="""
               The fiducial times recorded for the GPS in the RMS Instrument DAARC500
               are delayed, and associated with the "wrong" fid value. They should actually
               be moved to the previous fid value in the mag data where the event flag is non-zero.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('mag_fid_vv', type="VV",
                             doc="Mag fid values   (:def_val:`GS_DOUBLE`)"),
                   Parameter('mag_event_vv', type="VV",
                             doc="Mag event values (:def_val:`GS_LONG`)"),
                   Parameter('gps_fid_vv', type="VV",
                             doc="GPS fid values (:def_val:`GS_DOUBLE`, altered on return)")
               ]),

        Method('MaxwellPlateCorners_GU', module='geogxx', version='6.1.0',
               availability=Availability.LICENSED, 
               doc="Calculate the corner point locations for a Maxwell Plate.",
               notes="""
               This routine calculates the corner locations of plates defined in the Maxwell Plate
               program, given the top-center location and plate geometry parameters.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('x', type=Type.DOUBLE,
                             doc="Top-center point, X"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Top-center point, Y"),
                   Parameter('z', type=Type.DOUBLE,
                             doc="Top-center point, Z"),
                   Parameter('dip', type=Type.DOUBLE,
                             doc="Dip"),
                   Parameter('dip_dir', type=Type.DOUBLE,
                             doc="Dip-direction"),
                   Parameter('plunge', type=Type.DOUBLE,
                             doc="Plunge"),
                   Parameter('length', type=Type.DOUBLE,
                             doc="Length"),
                   Parameter('width', type=Type.DOUBLE,
                             doc="Width (height)"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="[returned] Corner 1 X"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="[returned] Corner 1 Y"),
                   Parameter('p11', type=Type.DOUBLE, is_ref=True,
                             doc="[returned] Corner 1 Z"),
                   Parameter('p12', type=Type.DOUBLE, is_ref=True,
                             doc="[returned] Corner 2 X"),
                   Parameter('p13', type=Type.DOUBLE, is_ref=True,
                             doc="[returned] Corner 2 Y"),
                   Parameter('p14', type=Type.DOUBLE, is_ref=True,
                             doc="[returned] Corner 2 Z"),
                   Parameter('p15', type=Type.DOUBLE, is_ref=True,
                             doc="[returned] Corner 3 X"),
                   Parameter('p16', type=Type.DOUBLE, is_ref=True,
                             doc="[returned] Corner 3 Y"),
                   Parameter('p17', type=Type.DOUBLE, is_ref=True,
                             doc="[returned] Corner 3 Z"),
                   Parameter('p18', type=Type.DOUBLE, is_ref=True,
                             doc="[returned] Corner 4 X"),
                   Parameter('p19', type=Type.DOUBLE, is_ref=True,
                             doc="[returned] Corner 4 Y"),
                   Parameter('p20', type=Type.DOUBLE, is_ref=True,
                             doc="[returned] Corner 4 Z")
               ]),

        Method('ScanDAARC500Ethernet_GU', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Scan Ethernet data from the RMS Instruments DAARC500.",
               notes="""
               Scans the file to see what data type is in the Ethernet file.
               Currently only detects GR820 types.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="File to import"),
                   Parameter('type', type=Type.INT32_T, is_ref=True,
                             doc="Recognized type"),
                   Parameter('items', type=Type.INT32_T, is_ref=True,
                             doc="Number of items")
               ]),

        Method('ScanDAARC500Serial_GU', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Scan Serial data from the RMS Instruments DAARC500.",
               notes="Scans the file to see which of the 8 serial channels were used to store data.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="File to import"),
                   Parameter('vv_type', type="VV",
                             doc="8 Recognized types - :def_val:`GS_LONG`"),
                   Parameter('vv_items', type="VV",
                             doc="8 Numbers of items - :def_val:`GS_LONG`")
               ]),

        Method('VVEuler_GU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get Euler solutions of depth from VVs and grids.",
               notes="""
               All VVs must be REAL
               
               The output X and Y values are the same as the inputs,
               except if :def_val:`PEAKEULER_XY_FIT` is selected. All other
               output values are set to dummy if:
                    
                    a) The input X or Y is a dummy
                    b) The derived window size is a dummy.
                    c) The derived solution is outside the range
                    d) The solution is invalid (singular matrix)

               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_xin', type="VV",
                             doc="Input X :class:`VV`"),
                   Parameter('vv_yin', type="VV",
                             doc="Input Y :class:`VV`"),
                   Parameter('img_data', type="IMG",
                             doc="Field grid"),
                   Parameter('imgx', type="IMG",
                             doc="dF/dX grid"),
                   Parameter('imgy', type="IMG",
                             doc="dF/dY grid"),
                   Parameter('imgz', type="IMG",
                             doc="dF/dZ grid"),
                   Parameter('vv_xout', type="VV",
                             doc="Output X :class:`VV`"),
                   Parameter('vv_yout', type="VV",
                             doc="Output Y :class:`VV`"),
                   Parameter('vv_depth', type="VV",
                             doc="Output depth :class:`VV`"),
                   Parameter('vvdc', type="VV",
                             doc="Output background field :class:`VV`"),
                   Parameter('vv_zer', type="VV",
                             doc="Output depth uncertainty :class:`VV`"),
                   Parameter('vvx_yer', type="VV",
                             doc="Output XY uncertainty :class:`VV`"),
                   Parameter('wnd_sz', type=Type.INT32_T,
                             doc="Window size"),
                   Parameter('si', type=Type.DOUBLE,
                             doc="Structure index"),
                   Parameter('wt_pow', type=Type.DOUBLE,
                             doc="Weighting factor"),
                   Parameter('x_yfit', type=Type.INT32_T,
                             doc=":def:`PEAKEULER_XY`")
               ]),

        Method('VVEuler2_GU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get Euler solutions of depth from VVs and grids (method 2).",
               notes="All VVs must be REAL",
               see_also=":func:`VVEuler_GU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('vv_xin', type="VV",
                             doc="Input X :class:`VV`"),
                   Parameter('vv_yin', type="VV",
                             doc="Input Y :class:`VV`"),
                   Parameter('img_data', type="IMG",
                             doc="Field grid"),
                   Parameter('imgx', type="IMG",
                             doc="dF/dX grid"),
                   Parameter('imgy', type="IMG",
                             doc="dF/dY grid"),
                   Parameter('imgz', type="IMG",
                             doc="dF/dZ grid"),
                   Parameter('vv_xout', type="VV",
                             doc="Output X :class:`VV`"),
                   Parameter('vv_yout', type="VV",
                             doc="Output Y :class:`VV`"),
                   Parameter('vv_depth', type="VV",
                             doc="Output depth :class:`VV`"),
                   Parameter('vvdc', type="VV",
                             doc="Output background field :class:`VV`"),
                   Parameter('vv_zer', type="VV",
                             doc="Output depth uncertainty :class:`VV`"),
                   Parameter('vvx_yer', type="VV",
                             doc="Output XY uncertainty :class:`VV`"),
                   Parameter('vv_wnd', type="VV",
                             doc="Window size (diameters of targets)"),
                   Parameter('si', type=Type.DOUBLE,
                             doc="Structure index"),
                   Parameter('wt_pow', type=Type.DOUBLE,
                             doc="Weighting factor"),
                   Parameter('x_yfit', type=Type.INT32_T,
                             doc=":def:`PEAKEULER_XY`")
               ])
    ]
}

