from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('IP',
                 doc="""
                 This class is used in the :class:`IP` System for the import, export
                 and processing of Induced Polarization data.
                 """,
                 notes="""
                 The following defines are used in GX code but are not
                 part of any functions:
                 
                 :def:`IP_ARRAY`
                 :def:`IP_CHANNELS`
                 :def:`IP_LINES`
                 """)


gx_defines = [
    Define('IP_ARRAY',
           doc=":class:`IP` Array options",
           constants=[
               Constant('IP_ARRAY_DPDP', value='0', type=Type.INT32_T),
               Constant('IP_ARRAY_PLDP', value='1', type=Type.INT32_T),
               Constant('IP_ARRAY_PLPL', value='2', type=Type.INT32_T),
               Constant('IP_ARRAY_GRAD', value='3', type=Type.INT32_T),
               Constant('IP_ARRAY_WENNER', value='5', type=Type.INT32_T),
               Constant('IP_ARRAY_SCHLUMBERGER', value='6', type=Type.INT32_T),
               Constant('IP_ARRAY_UNKNOWN', value='7', type=Type.INT32_T),
               Constant('IP_ARRAY_3D', value='9', type=Type.INT32_T),
               Constant('IP_ARRAY_3D_PLDP', value='10', type=Type.INT32_T),
               Constant('IP_ARRAY_3D_PLPL', value='11', type=Type.INT32_T)
           ]),

    Define('IP_CHANNELS',
           doc="Channels to display",
           constants=[
               Constant('IP_CHANNELS_DISPLAYED', value='0', type=Type.INT32_T),
               Constant('IP_CHANNELS_SELECTED', value='1', type=Type.INT32_T),
               Constant('IP_CHANNELS_ALL', value='2', type=Type.INT32_T)
           ]),

    Define('IP_DOMAIN',
           doc="Types of Domains",
           constants=[
               Constant('IP_DOMAIN_NONE', value='-1', type=Type.INT32_T),
               Constant('IP_DOMAIN_TIME', value='0', type=Type.INT32_T),
               Constant('IP_DOMAIN_FREQUENCY', value='1', type=Type.INT32_T),
               Constant('IP_DOMAIN_BOTH', value='2', type=Type.INT32_T)
           ]),

    Define('IP_DUPLICATE',
           doc="How to handle duplicates",
           constants=[
               Constant('IP_DUPLICATE_APPEND', value='0', type=Type.INT32_T),
               Constant('IP_DUPLICATE_OVERWRITE', value='1', type=Type.INT32_T)
           ]),

    Define('IP_FILTER',
           doc="Fraser Filters",
           constants=[
               Constant('IP_FILTER_PANTLEG', value='1', type=Type.INT32_T,
                        doc="""
                        ::

                            Regular pant-leg filter:

                        
                               _!_    
                              /*_*\   n1
                             /*/ \*\  n2`
                            /*/   \*\ n3
                               :  :
                        

                        """),
               Constant('IP_FILTER_PANTLEGP', value='2', type=Type.INT32_T,
                        doc="""
                        ::

                            Regular pant-leg filter with top at first point:

                               !  nscp:
                              /*\   n1
                             /*_*\  n2
                            /*/ \*\ n3
                              :  :

                        """),
               Constant('IP_FILTER_PYRIAMID', value='3', type=Type.INT32_T,
                        doc="""
                        ::

                            Regular pyramid filter:

                               _!_  maxn:
                              /* *\   n1
                             /* * *\  n2
                            /* * * *\ n3
                               :  :

                        """),
               Constant('IP_FILTER_PYRIAMIDP', value='4', type=Type.INT32_T,
                        doc="""
                        ::

                            Regular pyramid filter with peak on a point:

                               !  maxn:
                              /*\   n1
                             /* *\  n2
                            /* * *\ n3
                              :  :

                        """)
           ]),

    Define('IP_I2XIMPMODE',
           doc="Interpext Import Mode",
           constants=[
               Constant('IP_I2XIMPMODE_REPLACE', value='0', type=Type.INT32_T,
                        doc="Recreates the line from scratch."),
               Constant('IP_I2XIMPMODE_MERGE', value='1', type=Type.INT32_T,
                        doc="""
                        Looks for matching Tx1 and N values and
                        replaces data in matching lines only.
                        """)
           ]),

    Define('IP_I2XINV',
           doc="Type of Inversion",
           constants=[
               Constant('IP_I2XINV_IMAGE', value='0', type=Type.INT32_T),
               Constant('IP_I2XINV_ZONGE', value='1', type=Type.INT32_T)
           ]),

    Define('IP_LINES',
           doc="Lines to display",
           constants=[
               Constant('IP_LINES_DISPLAYED', value='0', type=Type.INT32_T),
               Constant('IP_LINES_SELECTED', value='1', type=Type.INT32_T),
               Constant('IP_LINES_ALL', value='2', type=Type.INT32_T)
           ]),

    Define('IP_PLOT',
           doc="Type of Plot",
           constants=[
               Constant('IP_PLOT_PSEUDOSECTION', value='0', type=Type.INT32_T),
               Constant('IP_PLOT_STACKEDSECTION', value='1', type=Type.INT32_T)
           ]),

    Define('IP_QCTYPE',
           doc="Type of Measurement",
           constants=[
               Constant('IP_QCTYPE_RESISTIVITY', value='0', type=Type.INT32_T,
                        doc="Resistivity"),
               Constant('IP_QCTYPE_IP', value='1', type=Type.INT32_T,
                        doc=":class:`IP`")
           ]),

    Define('IP_STACK_TYPE',
           doc="Spacing Types",
           constants=[
               Constant('IP_STACK_TYPE_MAP', value='0', type=Type.INT32_T,
                        doc="""
                        Use map-based spacing, and preserve the directions of the
                        original lines by rotating the sections as desired to their true
                        locations. (At present only N-S and E-W sections are supported).
                        """),
               Constant('IP_STACK_TYPE_EQUAL', value='1', type=Type.INT32_T,
                        doc="""
                        Spaces the sections equally, with enough room to
                        guarantee no overlap with high N-values or closely spaced lines.
                        """),
               Constant('IP_STACK_TYPE_GEOGRAPHIC', value='2', type=Type.INT32_T,
                        doc="Now the same as IP_STACK_MAP")
           ]),

    Define('IP_STNSCALE',
           doc="Station Scaling",
           constants=[
               Constant('IP_STNSCALE_NONE', value='0', type=Type.INT32_T,
                        doc="Station numbers become X or Y locations"),
               Constant('IP_STNSCALE_ASPACE', value='1', type=Type.INT32_T,
                        doc="Multiply station numbers by the A spacing"),
               Constant('IP_STNSCALE_VALUE', value='2', type=Type.INT32_T,
                        doc="Multiply by an input value."),
               Constant('IP_STNSCALE_FILE', value='3', type=Type.INT32_T,
                        doc="Look up locations from a CSV Line/Station/X/Y file")
           ]),

    Define('IP_SYS',
           doc="Instrument",
           constants=[
               Constant('IP_SYS_IPDATA', value='0', type=Type.INT32_T),
               Constant('IP_SYS_IP2', value='1', type=Type.INT32_T),
               Constant('IP_SYS_IP6', value='2', type=Type.INT32_T),
               Constant('IP_SYS_IP10', value='3', type=Type.INT32_T),
               Constant('IP_SYS_SYSCALR2', value='4', type=Type.INT32_T),
               Constant('IP_SYS_IPR11', value='5', type=Type.INT32_T),
               Constant('IP_SYS_IPR12', value='6', type=Type.INT32_T),
               Constant('IP_SYS_PHOENIX', value='7', type=Type.INT32_T),
               Constant('IP_SYS_PHOENIX_V2', value='8', type=Type.INT32_T),
               Constant('IP_SYS_ELREC_PRO', value='9', type=Type.INT32_T),
               Constant('IP_SYS_PROSYS_II', value='10', type=Type.INT32_T)
           ]),

    Define('IP_UBC_CONTROL',
           doc="Types of Domains",
           constants=[
               Constant('IP_UBC_CONTROL_NONE', value='-1', type=Type.INT32_T),
               Constant('IP_UBC_CONTROL_DEFAULT', value='0', type=Type.INT32_T),
               Constant('IP_UBC_CONTROL_FILE', value='1', type=Type.INT32_T),
               Constant('IP_UBC_CONTROL_VALUE', value='2', type=Type.INT32_T),
               Constant('IP_UBC_CONTROL_LENGTH', value='3', type=Type.INT32_T)
           ]),

    Define('IP_PLDP_CONV',
           doc="Types of Domains",
           constants=[
               Constant('IP_PLDP_CONV_CLOSE_RX', value='0', type=Type.INT32_T),
               Constant('IP_PLDP_CONV_MID_RX', value='1', type=Type.INT32_T),
               Constant('IP_PLDP_CONV_DISTANT_RX', value='2', type=Type.INT32_T)
           ])]


gx_methods = {
    'Plot Jobs': [

        Method('ConvertUBCIP2DToGrid_IP', module='geogxx', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Convert a UBC 2D model to a regular grid.",
               notes="""
               Uses :class:`TIN` gridding to sample the model.
               By setting the final value, a resistivity grid can be
               created from conductivity data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="Output grid file name"),
                   Parameter('pg', type="PG",
                             doc="Model data"),
                   Parameter('vv_x', type="VV",
                             doc="Model cells sizes (input)"),
                   Parameter('vv_z', type="VV",
                             doc="Model cells sizes (input)"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="Top-left corner X"),
                   Parameter('z', type=Type.DOUBLE,
                             doc="Top-left corner Z"),
                   Parameter('cx', type=Type.DOUBLE,
                             doc="Output grid cell size in X"),
                   Parameter('cz', type=Type.DOUBLE,
                             doc="Output grid cell size in Z"),
                   Parameter('reciprocal', type=Type.INT32_T,
                             doc="Output reciprocal of values (0:No, 1:Yes) for resistivity?")
               ]),

        Method('CreateDefaultJob_IP', module='geogxx', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Create a default job from scratch.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('ini', type=Type.STRING,
                             doc="File name of the INI file to create (forces correct suffix)"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`IP_PLOT`")
               ]),

        Method('ExportUBCIP3_IP', module='geogxx', version='8.1',
               availability=Availability.EXTENSION, 
               doc="Export of :class:`IP` data to UBC format.",
               notes="""
               Outputs a ``*.DAT`` file of the survey data for use in the
               UBC 2D inversion program IPINV2D.
               Include error channel output and version-specific formatting.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('line', type=Type.STRING,
                             doc="Output line name"),
                   Parameter('chan', type=Type.STRING,
                             doc="Output :class:`IP` channel name"),
                   Parameter('error_chan', type=Type.STRING,
                             doc='Output error channel name ("" for none)'),
                   Parameter('obs', type=Type.STRING,
                             doc="Output OBS file name"),
                   Parameter('topo', type=Type.STRING,
                             doc="Output TOPO file name"),
                   Parameter('version', type=Type.DOUBLE,
                             doc="Version number (3 or 5)")
               ]),

        Method('ExportUBCIPControl_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Export a control file for using in the UBC IPINV2D program.",
               notes="""
               UBC Version 3 Control file.
               Outputs a control file for use in the
               UBC 2D :class:`IP` inversion program IPINV2D.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('control', type=Type.STRING,
                             doc="Output control file name"),
                   Parameter('n_iter', type=Type.INT32_T,
                             doc="niter"),
                   Parameter('i_rest', type=Type.INT32_T,
                             doc="irest"),
                   Parameter('chi_factor', type=Type.DOUBLE,
                             doc="chifact"),
                   Parameter('obs', type=Type.STRING,
                             doc=":class:`IP` obs file"),
                   Parameter('cond', type=Type.STRING,
                             doc="Conductivity file"),
                   Parameter('mesh', type=Type.STRING,
                             doc="Mesh file"),
                   Parameter('topo', type=Type.STRING,
                             doc="Topography file"),
                   Parameter('initial', type=Type.STRING,
                             doc="Initial model file"),
                   Parameter('ref_mod', type=Type.STRING,
                             doc="Reference model"),
                   Parameter('alphas', type=Type.STRING,
                             doc="Alphas"),
                   Parameter('wts', type=Type.STRING,
                             doc="Weights file")
               ]),

        Method('ExportUBCIPControlV5_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Export a control file for using in the UBC IPINV2D program.",
               notes="UBC Version 5 Control file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('control', type=Type.STRING,
                             doc="Output control file name"),
                   Parameter('n_iter', type=Type.INT32_T,
                             doc="niter"),
                   Parameter('chi_factor', type=Type.DOUBLE,
                             doc="chifact"),
                   Parameter('obs', type=Type.STRING,
                             doc="RES obs file"),
                   Parameter('topo', type=Type.STRING,
                             doc="Topography file (required)"),
                   Parameter('cond_selection', type=Type.INT32_T,
                             doc="Conductivity type :def:`IP_UBC_CONTROL` FILE or VALUE"),
                   Parameter('cond', type=Type.STRING,
                             doc='Conductivity file (can be "") or value'),
                   Parameter('mesh_selection', type=Type.INT32_T,
                             doc="Mesh type :def:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT"),
                   Parameter('mesh', type=Type.STRING,
                             doc='Mesh file (can be "") or value'),
                   Parameter('initial_selection', type=Type.INT32_T,
                             doc="Initial model type :def:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT"),
                   Parameter('initial', type=Type.STRING,
                             doc='Initial model file (can be "") or value'),
                   Parameter('reference_selection', type=Type.INT32_T,
                             doc="Reference model type :def:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT"),
                   Parameter('ref_cond', type=Type.STRING,
                             doc='Reference model file (can be "") or value('),
                   Parameter('alphas_selection', type=Type.INT32_T,
                             doc="Alphas type :def:`IP_UBC_CONTROL` FILE, VALUE, LENGTH or DEFAULT"),
                   Parameter('alphas', type=Type.STRING,
                             doc='Alphas  file (can be ""), value or length'),
                   Parameter('wts', type=Type.STRING,
                             doc="Weights file")
               ]),

        Method('ExportUBCRes3_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Export of :class:`IP` Resistivity data to UBC format.",
               notes="""
               Outputs a ``*.DAT`` file of the survey data for use in the
               UBC 2D inversion program DCINV2D.
               Voltage and current channels should be in units such that
               V/I gives volts/amp (or mV/mA).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('line', type=Type.STRING,
                             doc="Output line name"),
                   Parameter('voltage_chan', type=Type.STRING,
                             doc="Output voltage channel name"),
                   Parameter('current_chan', type=Type.STRING,
                             doc="Output current channel name"),
                   Parameter('error_chan', type=Type.STRING,
                             doc='Output error channel name ("" for none)'),
                   Parameter('obs', type=Type.STRING,
                             doc="Output OBS file name"),
                   Parameter('topo', type=Type.STRING,
                             doc="Output TOPO file name"),
                   Parameter('version', type=Type.DOUBLE,
                             doc="Version number (3 or 5)")
               ]),

        Method('ExportUBCResControl_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Export a control file for using in the UBC DCINV2D program.",
               notes="""
               UBC Version 3.
               Outputs a control file for use in the
               UBC 2D resistivity inversion program DCINV2D.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('control', type=Type.STRING,
                             doc="Output control file name"),
                   Parameter('n_iter', type=Type.INT32_T,
                             doc="niter"),
                   Parameter('i_rest', type=Type.INT32_T,
                             doc="irest"),
                   Parameter('chi_factor', type=Type.DOUBLE,
                             doc="chifact"),
                   Parameter('obs', type=Type.STRING,
                             doc="RES obs file"),
                   Parameter('mesh', type=Type.STRING,
                             doc="Mesh file"),
                   Parameter('topo', type=Type.STRING,
                             doc="Topography file (required)"),
                   Parameter('initial', type=Type.STRING,
                             doc='Initial model file (can be "" or "NULL")'),
                   Parameter('ref_cond', type=Type.DOUBLE,
                             doc="Reference model conductivity"),
                   Parameter('alphas', type=Type.STRING,
                             doc="Alphas"),
                   Parameter('wts', type=Type.STRING,
                             doc="Weights file")
               ]),

        Method('ExportUBCResControlV5_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Export a control file for using in the UBC DCINV2D program.",
               notes="""
               UBC Version 5.
               Outputs a control file for use in the
               UBC 2D resistivity inversion program DCINV2D.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('control', type=Type.STRING,
                             doc="Output control file name"),
                   Parameter('n_iter', type=Type.INT32_T,
                             doc="niter"),
                   Parameter('chi_factor', type=Type.DOUBLE,
                             doc="chifact"),
                   Parameter('obs', type=Type.STRING,
                             doc="RES obs file"),
                   Parameter('topo', type=Type.STRING,
                             doc="Topography file (required)"),
                   Parameter('mesh_selection', type=Type.INT32_T,
                             doc="Mesh type :def:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT"),
                   Parameter('mesh', type=Type.STRING,
                             doc='Mesh file (can be "") or value'),
                   Parameter('initial_selection', type=Type.INT32_T,
                             doc="Initial model type :def:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT"),
                   Parameter('initial', type=Type.STRING,
                             doc='Initial model file (can be "") or value'),
                   Parameter('reference_selection', type=Type.INT32_T,
                             doc="Reference model type :def:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT"),
                   Parameter('ref_cond', type=Type.STRING,
                             doc='Reference model file (can be "") or value('),
                   Parameter('alphas_selection', type=Type.INT32_T,
                             doc="Alphas type :def:`IP_UBC_CONTROL` FILE, VALUE, LENGTH or DEFAULT"),
                   Parameter('alphas', type=Type.STRING,
                             doc='Alphas  file (can be ""), value or length'),
                   Parameter('wts', type=Type.STRING,
                             doc="Weights file")
               ]),

        Method('ExportDataToUBC3D_IP', module='geogxx', version='9.2',
               availability=Availability.EXTENSION, 
               doc="Export of :class:`IP` data to UBC 3D :class:`IP` format.",
               notes="""
               Outputs a ``*.DAT`` file of the survey data for use in the
               UBC :class:`IP` 3D inversion programs.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('line_lst', type="LST",
                             doc="Lines to export (Name, Symbol)"),
                   Parameter('locations_only', type=Type.INT32_T,
                             doc="Locations only (0: No, 1: Yes)?"),
                   Parameter('include_z', type=Type.INT32_T,
                             doc="Include Z values (0: No, 1: Yes)?"),
                   Parameter('chan', type=Type.STRING,
                             doc=':class:`IP` channel name (can be "" if exporting locations only)'),
                   Parameter('error_chan', type=Type.STRING,
                             doc='Error channel name (can be "" if exporting locations only)'),
                   Parameter('mask_chan', type=Type.STRING,
                             doc='Mask channel name (can be "")'),
                   Parameter('ip_type', type=Type.INT32_T,
                             doc="IPTYPE (1: Vp, 2: Chargeability)"),
                   Parameter('comments', type=Type.STRING,
                             doc='Comments (can be "")'),
                   Parameter('obs', type=Type.STRING,
                             doc="Output OBS file name")
               ]),

        Method('ImportUBC2DMOD_IP', module='geogxx', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Import a MOD file from the UBC IPINV2D program.",
               notes="""
               Imports the MOD file values to a :class:`PG` object.
               The CON/CHG selection is necessary because the import sets
               padding values to dummies based on the type of file.
               """,
               return_type="PG",
               return_doc=":class:`PG` Object",
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="UBC MOD file name to import"),
                   Parameter('type', type=Type.INT32_T,
                             doc="0 - CON, 1 - CHG")
               ]),

        Method('ImportUBC2DMSH_IP', module='geogxx', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Import a MSH file from the UBC IPINV2D program.",
               notes="Imports the MSH file geometry.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="UBC MSH file to import"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="Returned origin X (top left corner)"),
                   Parameter('z', type=Type.DOUBLE, is_ref=True,
                             doc="Returned origin Z (top left corner)"),
                   Parameter('vv_x', type="VV",
                             doc="Cell widths  (left to right) (real)"),
                   Parameter('vv_z', type="VV",
                             doc="Cell heights (top down) (real)")
               ]),

        Method('ImportUBC2DTopo_IP', module='geogxx', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Import a Topography file from the UBC IPINV2D program.",
               notes="""
               Imports the maximum elevation (top of mesh)
               as well as the topo (X, Z) values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('file', type=Type.STRING,
                             doc="UBC Topo file to import"),
                   Parameter('elev0', type=Type.DOUBLE, is_ref=True,
                             doc="Returned top of mesh elevation"),
                   Parameter('vv_x', type="VV",
                             doc="Topography X values"),
                   Parameter('vv_z', type="VV",
                             doc="Topography Z values (elevations)")
               ]),

        Method('OpenJob_IP', module='geogxx', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Open a :class:`IP` plotting job",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('job', type=Type.STRING,
                             doc="Job file name"),
                   Parameter('type', type=Type.INT32_T,
                             doc="Job type :def:`IP_PLOT`")
               ]),

        Method('SaveJob_IP', module='geogxx', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Save a :class:`IP` plotting job",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('job', type=Type.STRING,
                             doc="Job file name"),
                   Parameter('type', type=Type.INT32_T,
                             doc="Job type  :def:`IP_PLOT`")
               ]),

        Method('TrimUBC2DModel_IP', module='geogxx', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Trim the padding cells from the UBC IPINV2D Model.",
               notes="""
               The cells are removed from the left, right and bottom.
               The returned :class:`PG` is the trimmed version.
               The input cell size VVs are also trimmed to match,
               and the origin is updated (still upper left corner).
               """,
               return_type="PG",
               return_doc=":class:`PG` Object",
               parameters = [
                   Parameter('pg', type="PG",
                             doc="Input model (unchanged)"),
                   Parameter('trim_xl', type=Type.INT32_T,
                             doc="Cells to remove on left"),
                   Parameter('trim_xr', type=Type.INT32_T,
                             doc="Cells to remove on right"),
                   Parameter('trim_z', type=Type.INT32_T,
                             doc="Cells to remove on the bottom"),
                   Parameter('vv_x', type="VV",
                             doc="Column widths (modified)"),
                   Parameter('vv_z', type="VV",
                             doc="Row heights (modified)"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="Top left corner X (modified)")
               ]),

        Method('WriteDistantElectrodes_IP', module='geogxx', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc="Write distant electrode locations to channels",
               notes="Writes values for ALL lines.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object")
               ]),

        Method('WriteDistantElectrodesLST_IP', module='geogxx', version='6.4.2',
               availability=Availability.EXTENSION, 
               doc="Write distant electrode locations to channels for a :class:`LST` of lines",
               notes="Writes values for lines in the input :class:`LST`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('lst', type="LST",
                             doc="Lines to write out")
               ])
    ],
    'Miscellaneous': [

        Method('AverageDuplicatesQC_IP', module='geogxx', version='7.3.0',
               availability=Availability.EXTENSION, 
               doc="Average duplicate samples in a database.",
               notes="""
               Averages all values with shared station and N values,
               as long as the mask channel is defined at that FID.
               Previous averaged values (IP_DATA_AVG) are overwritten according to the
               overwrite flag.
               If the QC channel is selected, only those rows of data where the QC channel
               value is "1" will be included in the average.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to export from"),
                   Parameter('chan', type=Type.STRING,
                             doc="Mask or reference channel (required)"),
                   Parameter('qc_chan', type=Type.STRING,
                             doc="QC channel (can be left blank)"),
                   Parameter('out', type=Type.INT32_T,
                             doc=":def:`IP_DUPLICATE`")
               ]),

        Method('Create_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Create :class:`IP`.",
               return_type="IP",
               return_doc=":class:`IP` Object"),

        Method('Destroy_IP', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`IP` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` Handle")
               ]),

        Method('ExportI2X_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Export line(s) to an Interpex RESIX I2X format file.",
               notes='Exports a line to an ".I2X" file.',
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to export from"),
                   Parameter('file', type=Type.STRING,
                             doc="Name of the file"),
                   Parameter('line', type=Type.STRING,
                             doc="Name of the line"),
                   Parameter('res_data', type=Type.STRING,
                             doc="Resistivity (data) channel"),
                   Parameter('ip_data', type=Type.STRING,
                             doc=':class:`IP` (data) channel (can be "")'),
                   Parameter('res_model', type=Type.STRING,
                             doc='Image model resistivity channel (can be "")'),
                   Parameter('ip_model', type=Type.STRING,
                             doc='Image model :class:`IP` channel (can be "")'),
                   Parameter('res_synth', type=Type.STRING,
                             doc='Image model synthetic resistivity channel (can be "")'),
                   Parameter('ip_synth', type=Type.STRING,
                             doc='Image model synthetic :class:`IP` channel (can be "")'),
                   Parameter('res_poly', type=Type.STRING,
                             doc='Resistivity (polygon) channel (can be "")'),
                   Parameter('ip_poly', type=Type.STRING,
                             doc=':class:`IP` (polygon) channel (can be "")')
               ]),

        Method('ExportIPDATA_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Exports data in the Geosoft IPDATA format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to export from"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to export"),
                   Parameter('title', type=Type.STRING,
                             doc="Title for IPDATA files")
               ]),

        Method('ExportIPDATADir_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Exports data in the Geosoft IPDATA format in the specified directory",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to export from"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to export"),
                   Parameter('title', type=Type.STRING,
                             doc="Title for IPDATA files"),
                   Parameter('dir', type=Type.STRING,
                             doc="Directory for IPDATA files")
               ]),

        Method('ExportIPRED_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Exports pseudo-section in the Geosoft IPRED format.",
               notes="""
               The Fraser Filter weights apply to each N expansion above,
               and are listed as w1,w2,w3,...   Unspecified values beyond
               the list's end are set to 1.0.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to export from"),
                   Parameter('title', type=Type.STRING,
                             doc="Title for first line of file"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to process"),
                   Parameter('suffix', type=Type.STRING,
                             doc="File suffix (type)"),
                   Parameter('filter', type=Type.INT32_T,
                             doc=":def:`IP_FILTER`"),
                   Parameter('wts', type=Type.STRING,
                             doc="The Fraser Filter weights"),
                   Parameter('stn1', type=Type.DOUBLE,
                             doc="First Station position (:const:`rDUMMY` for default)"),
                   Parameter('stn2', type=Type.DOUBLE,
                             doc="Last Station position  (:const:`rDUMMY` for default)"),
                   Parameter('max_n', type=Type.INT32_T,
                             doc="Maximum n spacing")
               ]),

        Method('ExportIPREDDir_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Exports pseudo-section in the Geosoft IPRED format in the specified directory",
               notes="""
               The Fraser Filter weights apply to each N expansion above,
               and are listed as w1,w2,w3,...   Unspecified values beyond
               the list's end are set to 1.0.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to export from"),
                   Parameter('title', type=Type.STRING,
                             doc="Title for first line of file"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to process"),
                   Parameter('suffix', type=Type.STRING,
                             doc="File suffix (type)"),
                   Parameter('filter', type=Type.INT32_T,
                             doc=":def:`IP_FILTER`"),
                   Parameter('wts', type=Type.STRING,
                             doc="The Fraser Filter weights"),
                   Parameter('stn1', type=Type.DOUBLE,
                             doc="First Station position (:const:`rDUMMY` for default)"),
                   Parameter('stn2', type=Type.DOUBLE,
                             doc="Last Station position  (:const:`rDUMMY` for default)"),
                   Parameter('max_n', type=Type.INT32_T,
                             doc="Maximum n spacing"),
                   Parameter('dir', type=Type.STRING,
                             doc="Directory to export to")
               ]),

        Method('ExportLineIPDATA_IP', module='geogxx', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Exports one line of data in the Geosoft IPDATA format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to export from"),
                   Parameter('line', type=Type.STRING,
                             doc="Line to export"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to export"),
                   Parameter('title', type=Type.STRING,
                             doc="Title for IPDATA files")
               ]),

        Method('ExportSGDF_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Exports data to a Scintrex Geophysical Data Format file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to export from"),
                   Parameter('file', type=Type.STRING,
                             doc="SGDF file to create"),
                   Parameter('chan', type=Type.STRING,
                             doc="Time Domain channel or Frequency Amplitude Channel"),
                   Parameter('chan2', type=Type.STRING,
                             doc="Frequency Domain Phase channel (optional)")
               ]),

        Method('GetNValueLST_IP', module='geogxx', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Fill a list with unique N values in selected lines.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` object")
               ]),

        Method('GetTopoLine_IP', module='geogxx', version='6.4.2',
               availability=Availability.EXTENSION, 
               doc="Get topography values for a line.",
               notes="""
               If topography info is available, returns values calculated for
               the input line. If no topography is available, returned values
               will be dummies. Values between actual data are interpolated using
               the Akima spline. Ends are extrapolated using the end data points.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to import data to"),
                   Parameter('line', type=Type.STRING,
                             doc="Line name"),
                   Parameter('x_min', type=Type.DOUBLE,
                             doc='Starting "X" (station) value (:const:`rDUMMY` for default)'),
                   Parameter('x_max', type=Type.DOUBLE,
                             doc='Ending "X" (station) value (:const:`rDUMMY` for default)'),
                   Parameter('x_inc', type=Type.DOUBLE,
                             doc='"X" increment along the line (:const:`rDUMMY` for default = half "A" separation)'),
                   Parameter('vv', type="VV",
                             doc="Returned topography values")
               ]),

        Method('iGetChanDomain_IP', module='geogxx', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Is this channel registered as a Time or Frequency domain channel?",
               return_type=Type.INT32_T,
               return_doc=":def:`IP_DOMAIN`",
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to check")
               ]),

        Method('IGetChanLabel_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Get the default label and units for a given channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('chan', type=Type.STRING,
                             doc="Input channel"),
                   Parameter('label', type=Type.STRING, is_ref=True, size_of_param='len_label',
                             doc="Returned label"),
                   Parameter('len_label', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Label length"),
                   Parameter('units', type=Type.STRING, is_ref=True, size_of_param='len_units',
                             doc="Returned units"),
                   Parameter('len_units', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Units label length")
               ]),

        Method('GetChannelInfo_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Time Windows or Frequency info from a channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to check"),
                   Parameter('domain', type=Type.INT32_T, is_ref=True,
                             doc=":def:`IP_DOMAIN`"),
                   Parameter('delay', type=Type.DOUBLE, is_ref=True,
                             doc="Delay or Base Frequency"),
                   Parameter('n_windows', type=Type.INT32_T, is_ref=True,
                             doc="Number of time windows or frequencies"),
                   Parameter('vv', type="VV",
                             doc="Time windows or frequencies")
               ]),

        Method('SetChannelInfo_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Set Time Windows or Frequency info for a channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to check"),
                   Parameter('domain', type=Type.INT32_T,
                             doc=":def:`IP_DOMAIN`"),
                   Parameter('delay', type=Type.DOUBLE,
                             doc="Delay or Base Frequency"),
                   Parameter('n_windows', type=Type.INT32_T,
                             doc="Number of time windows or frequencies"),
                   Parameter('vv', type="VV",
                             doc="Time windows or frequencies")
               ]),

        Method('ImportDump_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports data from an :class:`IP` instrument dump file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` Handle"),
                   Parameter('ip_sys', type=Type.INT32_T,
                             doc=":def:`IP_SYS`"),
                   Parameter('db', type="DB",
                             doc=":class:`DB` Handle"),
                   Parameter('dump_file', type=Type.STRING,
                             doc="Dump file name")
               ]),

        Method('ImportGrid_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports data from a grid",
               notes="""
               Data is imported to the specified channel.
               The values are interpolated at each row's X and Y
               positions.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to import data to"),
                   Parameter('grid', type=Type.STRING,
                             doc="The name of the grid file, with decorations"),
                   Parameter('chan', type=Type.STRING,
                             doc="The name of the channel to import to")
               ]),

        Method('ImportI2X_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports an Interpex RESIX I2X format file to a line.",
               notes="""
               Imports a single ".I2X" file to a specified line.
               If the line does not exist, it will be created.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to import to"),
                   Parameter('file', type=Type.STRING,
                             doc="Name of file to import"),
                   Parameter('line', type=Type.STRING,
                             doc="Line to import to"),
                   Parameter('res_data', type=Type.STRING,
                             doc="Resistivity (data) channel"),
                   Parameter('ip_data', type=Type.STRING,
                             doc=':class:`IP` (data) channel (can be "")'),
                   Parameter('res_model', type=Type.STRING,
                             doc='Image model resistivity channel (can be "")'),
                   Parameter('ip_model', type=Type.STRING,
                             doc='Image model :class:`IP` channel (can be "")'),
                   Parameter('res_synth', type=Type.STRING,
                             doc='Image model synthetic resistivity channel (can be "")'),
                   Parameter('ip_synth', type=Type.STRING,
                             doc='Image model synthetic :class:`IP` channel (can be "")'),
                   Parameter('res_poly', type=Type.STRING,
                             doc='Resistivity (polygon) channel (can be "")'),
                   Parameter('ip_poly', type=Type.STRING,
                             doc=':class:`IP` (polygon) channel (can be "")'),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`IP_I2XIMPMODE`")
               ]),

        Method('ImportI2XEx_IP', module='geogxx', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Same as :func:`ImportI2X_IP`, with Zonge data imported as well.",
               notes="""
               Imports a single ".I2X" file to a specified line.
               If the line does not exist, it will be created.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to import to"),
                   Parameter('file', type=Type.STRING,
                             doc="Name of file to import"),
                   Parameter('line', type=Type.STRING,
                             doc="Line to import to"),
                   Parameter('res_data', type=Type.STRING,
                             doc="Resistivity (data) channel"),
                   Parameter('ip_data', type=Type.STRING,
                             doc=':class:`IP` (data) channel (can be "")'),
                   Parameter('res_model', type=Type.STRING,
                             doc='Image model resistivity channel (can be "")'),
                   Parameter('ip_model', type=Type.STRING,
                             doc='Image model :class:`IP` channel (can be "")'),
                   Parameter('res_synth', type=Type.STRING,
                             doc='Image model synthetic resistivity channel (can be "")'),
                   Parameter('ip_synth', type=Type.STRING,
                             doc='Image model synthetic :class:`IP` channel (can be "")'),
                   Parameter('res_poly', type=Type.STRING,
                             doc='Resistivity (polygon) channel (can be "")'),
                   Parameter('ip_poly', type=Type.STRING,
                             doc=':class:`IP` (polygon) channel (can be "")'),
                   Parameter('res_zonge', type=Type.STRING,
                             doc='Zonge Resistivity channel (can be "")'),
                   Parameter('ip_zonge', type=Type.STRING,
                             doc='Zonge :class:`IP` channel (can be "")'),
                   Parameter('mode', type=Type.INT32_T,
                             doc=":def:`IP_I2XIMPMODE`")
               ]),

        Method('ImportInstrumentationGDD_IP', module='geogxx', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports an Instrumentation GDD format file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to import to"),
                   Parameter('file', type=Type.STRING,
                             doc="GDD file name")
               ]),

        Method('ImportIPDATA_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports data in the Geosoft IPDATA format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to import to"),
                   Parameter('file', type=Type.STRING,
                             doc="IPDATA file name"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to import to")
               ]),

        Method('ImportIPDATA2_IP', module='geogxx', version='5.1.0',
               availability=Availability.EXTENSION, 
               doc="Imports data in the Geosoft IPDATA format - up to two arrays.",
               notes="""
               The second channel may be specified for frequency domain data sets
               with two array channels; e.g. amplitude and phase, or real and
               imaginary parts. If the second channel is specified, and no
               time or frequncy information is specified in the header (using
               the T= or F= fields) then the import is assumed to be frequency
               domain.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to import to"),
                   Parameter('file', type=Type.STRING,
                             doc="IPDATA file name"),
                   Parameter('chan', type=Type.STRING,
                             doc='Channel to import to (default is ":class:`IP`")'),
                   Parameter('chan2', type=Type.STRING,
                             doc="(optional) Second channel to import to")
               ]),

        Method('ImportIPRED_IP', module='geogxx', version='5.1.0',
               availability=Availability.EXTENSION, 
               doc="Imports data from the Geosoft IPRED format.",
               notes="""
               This import produces a limited :class:`IP` data set with no Current "I",
               Voltage "Vp" or Apparent Resistivity "ResApp" values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to import to"),
                   Parameter('file', type=Type.STRING,
                             doc="File to import from"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to import")
               ]),

        Method('ImportMergeIPRED_IP', module='geogxx', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Imports IPRED data to an existing line.",
               notes="""
               Exits with error if the line does not exist.
               Data is merged on basis of Stn and N value.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to import to"),
                   Parameter('file', type=Type.STRING,
                             doc="File to import from"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to import")
               ]),

        Method('ImportSGDF_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports data from a Scintrex Geophysical Data Format file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to import to"),
                   Parameter('file', type=Type.STRING,
                             doc="SGDF file name")
               ]),

        Method('ImportTopoCSV_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports topography data from a CSV line-station file",
               notes="""
               The elevation of each point in the current database
               is interpolated from the input topography values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to calculate topography for"),
                   Parameter('csv', type=Type.STRING,
                             doc="The name of CSV file")
               ]),

        Method('ImportTopoGrid_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports topography data from a grid",
               notes="""
               The elevation of each point in the current database
               is interpolated from the input topography grid.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to calculate topography for"),
                   Parameter('grid', type=Type.STRING,
                             doc="The name of the grid file, with decorations")
               ]),

        Method('ImportZongeAVG_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports a Zonge AVG format file.",
               notes="See :func:`ImportZongeFLD_IP`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to import to"),
                   Parameter('file', type=Type.STRING,
                             doc="FLD file name"),
                   Parameter('line', type=Type.DOUBLE,
                             doc="Line number (will be scaled if applicable)"),
                   Parameter('scale', type=Type.INT32_T,
                             doc=":def:`IP_STNSCALE`"),
                   Parameter('mult', type=Type.DOUBLE,
                             doc="Line, station multiplier (for :const:`IP_STNSCALE_VALUE`)")
               ]),

        Method('ImportZongeFLD_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports a Zonge FLD format file.",
               notes="""
               The Zonge Line and Station numbers may not be the X or Y position
               values, and a conversion is required.
               The line direction is taken from the :class:`IP` setup values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to import to"),
                   Parameter('file', type=Type.STRING,
                             doc="FLD file name"),
                   Parameter('scale', type=Type.INT32_T,
                             doc=":def:`IP_STNSCALE`"),
                   Parameter('mult', type=Type.DOUBLE,
                             doc="Line, station multiplier (for :const:`IP_STNSCALE_VALUE`)")
               ]),

        Method('NewXYDatabase_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc='Create a subset database using a mask channel, "N" value',
               notes="""
               A mask channel can be used to select a subset of the data.
               A single N value can also be selected (Dummy for all).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('new_db', type="DB",
                             doc="New :class:`DB` object"),
                   Parameter('chan_vv', type="VV",
                             doc="Channel list"),
                   Parameter('mask', type=Type.STRING,
                             doc="Mask channel"),
                   Parameter('pr_n_val', type=Type.DOUBLE,
                             doc='"N" Value')
               ]),

        Method('PseudoPlot_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Create pseudo-sections of a single line using a control file.",
               notes="""
               The control file is created using the IPPLTCON GX. It may then
               be modified by hand as required.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('ini_file', type=Type.STRING,
                             doc='"IPPLOT" INI file name'),
                   Parameter('cur_line', type=Type.STRING,
                             doc="Current line name"),
                   Parameter('map', type=Type.STRING,
                             doc="Map name to create")
               ]),

        Method('PseudoPlot2_IP', module='geogxx', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Same as :func:`PseudoPlot_IP`, but specify a tag for grids created.",
               notes="""
               The control file is created using the IPPLTCON GX. It may then
               be modified by hand as required.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('ini_file', type=Type.STRING,
                             doc='"IPPLOT" INI file name'),
                   Parameter('cur_line', type=Type.STRING,
                             doc="Current line name"),
                   Parameter('tag', type=Type.STRING,
                             doc="Tag for created grids"),
                   Parameter('map', type=Type.STRING,
                             doc="Map name to create")
               ]),

        Method('PseudoPlot2Dir_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Same as :func:`PseudoPlot2_IP`, but with directory specified.",
               notes="""
               The control file is created using the IPPLTCON GX. It may then
               be modified by hand as required.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('ini_file', type=Type.STRING,
                             doc='"IPPLOT" INI file name'),
                   Parameter('cur_line', type=Type.STRING,
                             doc="Current line name"),
                   Parameter('tag', type=Type.STRING,
                             doc="Tag for created grids"),
                   Parameter('map', type=Type.STRING,
                             doc="Map name to create"),
                   Parameter('dir', type=Type.STRING,
                             doc="Directory to create files")
               ]),

        Method('PSStack_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Create a stacked pseudo-section plot using a control file.",
               notes="""
               The control file is created using the IPSTAKCON GX. It may then
               be modified by hand as required.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to plot"),
                   Parameter('con_file', type=Type.STRING,
                             doc='"IPPLOT" INI file name'),
                   Parameter('map', type=Type.STRING,
                             doc="Map name to create")
               ]),

        Method('PSStack2_IP', module='geogxx', version='5.1.0',
               availability=Availability.EXTENSION, 
               doc="As :func:`PSStack_IP`, but select section spacing option.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to plot"),
                   Parameter('con_file', type=Type.STRING,
                             doc='"IPPLOT" INI file name'),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`IP_STACK_TYPE`"),
                   Parameter('map', type=Type.STRING,
                             doc="Map name to create")
               ]),

        Method('PSStack2Dir_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Same as :func:`PseudoPlot2_IP`, but with directory specified.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('chan', type=Type.STRING,
                             doc="Channel to plot"),
                   Parameter('con_file', type=Type.STRING,
                             doc='"IPPLOT" INI file name'),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`IP_STACK_TYPE`"),
                   Parameter('map', type=Type.STRING,
                             doc="Map name to create"),
                   Parameter('dir', type=Type.STRING,
                             doc="Directory to create files")
               ]),

        Method('QCChanLST_IP', module='geogxx', version='7.3.0',
               availability=Availability.EXTENSION, 
               doc="Fill a list with QC channels.",
               notes="""
               Searches for the following QC channels existing in a database:
               QC, QC_RES.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('lst', type="LST",
                             doc=":class:`LST` object")
               ]),

        Method('Recalculate_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Recalculate derived channel values.",
               notes="""
               This function recalculates "derived" channel values from
               "core" data.
               
                   1. Recalculates the "STN" and "N" channels, using the TX1,
                      TX2, RX1 and RX2 channels (depending on the system).
                   2. Recalculates the apparent resistivity "ResCalc",
                      average "IP_Avg" and metal factor "MF" channels
                   3. Recalculates the "X" and "Y" channels. One of these will
                      be equal to "STN", the other to the internally stored
                      line number for the current line.
                   4. Recalculate the "Z" channel, based on the current "Topo"
                      channel, and the "N" values.
               
               Warning: If you make a change to an electrode location, you
               would have to call :func:`Recalculate_IP`, then recalculate "Topo"
               (since the X and Y values would have changed), then call
               :func:`RecalculateZ_IP`, since "Z" values are based on "Topo" values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database")
               ]),

        Method('RecalculateEx_IP', module='geogxx', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Recalculate derived channel values, with option for including/excluding location calculations.",
               notes="""
               See :func:`Recalculate_IP`. This version allows you to suppress the recalculation of the
               current X, Y and Z channel values from the station locations.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('recalculate_xyz', type=Type.INT32_T,
                             doc="Recalculate XYZ locations (TRUE or FALSE)?")
               ]),

        Method('RecalculateZ_IP', module='geogxx', version='5.1.1',
               availability=Availability.EXTENSION, 
               doc="Recalculate Z channel values.",
               notes="""
               The "Z" channel values are calculated as follows:
               If the "Topo" value is defined, then
               Z = Topo - 0.5*N*A, where "N" is the N-spacing, and
               A is the A-spacing. If the Topography is not defined, then
               it is assumed to be equal to 0.
               """,
               see_also=":func:`Recalculate_IP`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database")
               ]),

        Method('RESIX_Zonge_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Runs the Interpex RESIX Zonge inversion on selected lines.",
               notes="""
               The IP2DI program is run in batch mode, and the
               input file is overwritten with the new results, ready to
               be imported using :func:`ImportI2X_IP`.
               The three :class:`IP` channels are required only if joint Res/:class:`IP` inversion
               is selected.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database object"),
                   Parameter('line', type=Type.STRING,
                             doc="Name of the line"),
                   Parameter('res_chan', type=Type.STRING,
                             doc="Apparent resistivity channel"),
                   Parameter('syn_res_chan', type=Type.STRING,
                             doc="Synthetic Apparent resistivity channel"),
                   Parameter('inv_res_chan', type=Type.STRING,
                             doc="Inverted Apparent resistivity channel"),
                   Parameter('ip_too', type=Type.INT32_T,
                             doc="Invert :class:`IP` data too? :def:`IP_I2XINV`"),
                   Parameter('chg_chan', type=Type.STRING,
                             doc=":class:`IP` channel"),
                   Parameter('syn_chg_chan', type=Type.STRING,
                             doc="Synthetic :class:`IP` channel"),
                   Parameter('inv_chg_chan', type=Type.STRING,
                             doc="Inverted :class:`IP` channel")
               ]),

        Method('SetImportLine_IP', module='geogxx', version='9.3.0',
               availability=Availability.EXTENSION, 
               doc="Set the line name for some imports.",
               notes="For some imports, no line name is derivable from the import itself.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('line', type=Type.STRING,
                             doc="Line name")
               ]),

        Method('SetImportMode_IP', module='geogxx', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc="When importing data to a line, set append/overwrite mode.",
               notes="""
               By default, importing data overwrites existing data.
               Call this function before doing the import in order
               to append imported data to existing data.
               "Short" data channels will be dummied to the existing
               data length before the new data is appended.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` Handle"),
                   Parameter('append', type=Type.INT32_T,
                             doc="0: Overwrite, 1: Append")
               ]),

        Method('Window_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Window an :class:`IP` array channel to produce a normal channel.",
               notes="""
               The array channels cannot be used directly to produce sections.
               :func:`Window_IP` allows the user to select one or more of the windows
               and create a new channel. In time domain, if more than one channel
               is selected a weighted sum is performed, according to window widths.
               In frequency domain a simple sum is performed.
               Window List Syntax:
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('va_chan', type=Type.STRING,
                             doc=":class:`VA` channel to use"),
                   Parameter('chan', type=Type.STRING,
                             doc="New channel"),
                   Parameter('windows', type=Type.STRING,
                             doc="Window list")
               ]),

        Method('WinnowChanList_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Removes obviously non-pseudo-section type channels from list.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('lst', type="LST",
                             doc="List of channels")
               ]),

        Method('WinnowChanList2_IP', module='geogxx', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Same as :func:`WinnowChanList_IP`, but removes current X,Y,Z.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('lst', type="LST",
                             doc="List of channels"),
                   Parameter('db', type="DB",
                             doc="Database")
               ]),

        Method('isValidLine_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="See if a given database line is registered for the :class:`IP` system",
               return_type=Type.INT32_T,
               return_doc="1 if the line is a valid :class:`IP` line, 0 if not",
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('line', type=Type.STRING,
                             doc="Line name")
               ]),

        Method('iLineArrayType_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Return the type of :class:`IP` array for the input line. If necessary, first imports the specified line into the :class:`IP` object",
               return_type=Type.INT32_T,
               return_doc=":def:`IP_ARRAY`",
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('line', type=Type.STRING,
                             doc="Line name")
               ]),

        Method('rASpacing_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Return the A-Spacing for the input line. If necessary, first imports the specified line into the :class:`IP` object.",
               return_type=Type.DOUBLE,
               return_doc="""
               The A-Spacing value. If there are multiple A-Spacings, the base or smallest value.
               				 This value could be :const:`rDUMMY` for some arrays (such as 3D) where no A-Spacing is explicitly defined.
               """,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('line', type=Type.STRING,
                             doc="Line name")
               ]),

        Method('iPLDPConvention_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Return the user's plot point convention for pole-dipole arrays.",
               return_type=Type.INT32_T,
               return_doc="The user's PLDP plot point convention :def:`IP_PLDP_CONV`",
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` Object")
               ]),

        Method('GetElectrodeLocationsAndMaskValues_IP', module='geogxx', version='9.0.0',
               availability=Availability.EXTENSION, 
               doc="Get unique electrodes, along with current mask info.",
               notes="""
               The mask values are determined from the first row where a given electrode is found.
               Values returned for all currently selected lines.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('line', type=Type.STRING,
                             doc='Line name ("" for all selected lines)'),
                   Parameter('tx_rx', type=Type.INT32_T,
                             doc="Electrode type. 0:Tx, 1:Rx"),
                   Parameter('v_vx', type="VV",
                             doc="X locations"),
                   Parameter('v_vy', type="VV",
                             doc="Y locations"),
                   Parameter('v_vm1', type="VV",
                             doc=':class:`IP` QC channel values ("QC" or "QC_IP")'),
                   Parameter('v_vm2', type="VV",
                             doc='Resistivity QC channel values ("QC_RES")')
               ]),

        Method('GetElectrodeLocationsAndMaskValues2_IP', module='geogxx', version='9.2.0',
               availability=Availability.EXTENSION, 
               doc="Get unique electrodes, along with current mask info.",
               notes="""
               The mask values are determined from the first row where a given electrode is found.
               Values returned for all currently selected lines.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('line', type=Type.STRING,
                             doc='Line name ("" for all selected lines)'),
                   Parameter('tx_rx', type=Type.INT32_T,
                             doc="Electrode type. 0:Tx, 1:Rx"),
                   Parameter('v_vx', type="VV",
                             doc="X locations"),
                   Parameter('v_vy', type="VV",
                             doc="Y locations"),
                   Parameter('v_vm1', type="VV",
                             doc=':class:`IP` QC channel values ("QC" or "QC_IP")'),
                   Parameter('v_vm2', type="VV",
                             doc='Resistivity QC channel values ("QC_RES")'),
                   Parameter('v_vlines', type="VV",
                             doc="Line symbol values (:const:`GS_INT`)")
               ]),

        Method('SetElectrodeMaskValues_IP', module='geogxx', version='9.0.0',
               availability=Availability.EXTENSION, 
               doc="Set unique electrodes, along with current mask info.",
               notes="Mask values are set for all included electrode locations, currently selected lines.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('line', type=Type.STRING,
                             doc='Line name ("" for all selected lines)'),
                   Parameter('tx_rx', type=Type.INT32_T,
                             doc="Electrode type. 0:Tx, 1:Rx"),
                   Parameter('v_vx', type="VV",
                             doc="X locations"),
                   Parameter('v_vy', type="VV",
                             doc="Y locations"),
                   Parameter('v_vm1', type="VV",
                             doc=':class:`IP` QC channel values ("QC" or "QC_IP")'),
                   Parameter('v_vm2', type="VV",
                             doc='Resistivity QC channel values ("QC_RES")')
               ]),

        Method('SetElectrodeMaskValuesSingleQCChannel_IP', module='geogxx', version='9.2.0',
               availability=Availability.EXTENSION, 
               doc="Set unique electrodes, along with current mask info.",
               notes="Mask values are set for all included electrode locations, currently selected lines.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('line', type=Type.STRING,
                             doc='Line name ("" for all selected lines)'),
                   Parameter('tx_rx', type=Type.INT32_T,
                             doc="Electrode type. 0:Tx, 1:Rx"),
                   Parameter('qc_type', type=Type.INT32_T,
                             doc="QC channel type.  :def:`IP_QCTYPE`"),
                   Parameter('v_vx', type="VV",
                             doc="X locations"),
                   Parameter('v_vy', type="VV",
                             doc="Y locations"),
                   Parameter('v_vm', type="VV",
                             doc='QC channel values ("QC")')
               ]),

        Method('GetQCChannel_IP', module='geogxx', version='9.2.0',
               availability=Availability.EXTENSION, 
               doc="Get the QC channel handle, if it exists.",
               notes="""
               For :class:`IP`, looks for "QC_IP", then "QC_OffTime", then "QC".
               For Resistivity, looks for "QC_Res", then "QC_OnTime" (case insensitive).
               """,
               return_type="DB_SYMB",
               return_doc="Channel handle,  :const:`NULLSYMB` if not found",
               parameters = [
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('qc_type', type=Type.INT32_T,
                             doc="QC channel type.  :def:`IP_QCTYPE`"),
                   Parameter('chan', type=Type.STRING, is_ref=True, size_of_param='size',
                             doc="String to place name into"),
                   Parameter('size', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Maximum length of string, should be :const:`DB_SYMB_NAME_SIZE` to hold all possible channel names.")
               ]),

        Method('LocateContributingElectrodes_IP', module='geogxx', version='9.4.0',
               availability=Availability.EXTENSION, 
               doc="Locate on a map electrodes selected in a database row.",
               notes="""
               Sets up an EXT object in the database that captures row/line change events and plots the
               electrodes for the selected row on an accompanying map.
               The EXT object is removed by running LaunchRemoveContributingElectrodesEXTTool_IPGUI.
               This EXT is not serialized, so it is also removed if the database is closed (since
               this is not the normal behaviour expected from a database).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('map', type=Type.STRING,
                             doc='The current map'),
                   Parameter('rx1x', type=Type.STRING,
                             doc='Rx1 X channel'),
                   Parameter('rx1y', type=Type.STRING,
                             doc='Rx1 Y channel'),
                   Parameter('rx2x', type=Type.STRING,
                             doc='Rx2 X channel'),
                   Parameter('rx2y', type=Type.STRING,
                             doc='Rx2 Y channel'),
                   Parameter('tx1x', type=Type.STRING,
                             doc='Tx1 X channel'),
                   Parameter('tx1y', type=Type.STRING,
                             doc='Tx1 Y channel'),
                   Parameter('tx2x', type=Type.STRING,
                             doc='Tx2 X channel'),
                   Parameter('tx2y', type=Type.STRING,
                             doc='Tx2 Y channel'),
                   Parameter('sym_size', type=Type.DOUBLE,
                             doc='Symbol size (mm)'),
               ])
    ],
    'Obsolete': [

        Method('AverageDuplicates_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Average duplicate samples in a database.",
               notes="""
               Averages all values with shared station and N values,
               as long as the mask channel is defined at that FID.
               Previous averaged values (IP_DATA_AVG) are overwritten according to the
               overwrite flag.
               REPLACED BY: :func:`AverageDuplicatesQC_IP`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('db', type="DB",
                             doc="Database to export from"),
                   Parameter('chan', type=Type.STRING,
                             doc="Mask or reference channel"),
                   Parameter('out', type=Type.INT32_T,
                             doc=":def:`IP_DUPLICATE`")
               ]),

        Method('ExportUBCIP_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Export an :class:`IP` OBS file to use in the UBC IPINV2D program.",
               notes="""
               Outputs a ``*.DAT`` file of the survey data for use in the
               UBC 2D inversion program IPINV2D.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('line', type=Type.STRING,
                             doc="Output line name"),
                   Parameter('chan', type=Type.STRING,
                             doc="Output :class:`IP` channel name"),
                   Parameter('obs', type=Type.STRING,
                             doc="Output OBS file name"),
                   Parameter('topo', type=Type.STRING,
                             doc="Output TOPO file name")
               ]),

        Method('ExportUBCIP2_IP', module='geogxx', version='6.4.2',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Same as :func:`ExportUBCIP_IP`, with error channel output.",
               notes="""
               Outputs a ``*.DAT`` file of the survey data for use in the
               UBC 2D inversion program IPINV2D.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('line', type=Type.STRING,
                             doc="Output line name"),
                   Parameter('chan', type=Type.STRING,
                             doc="Output :class:`IP` channel name"),
                   Parameter('error_chan', type=Type.STRING,
                             doc='Output error channel name ("" for none)'),
                   Parameter('obs', type=Type.STRING,
                             doc="Output OBS file name"),
                   Parameter('topo', type=Type.STRING,
                             doc="Output TOPO file name")
               ]),

        Method('ExportUBCRes_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Export a RES OBS file to use in the UBC DCINV2D program.",
               notes="""
               Outputs a ``*.DAT`` file of the survey data for use in the
               UBC 2D inversion program DCINV2D.
               Voltage and current channels should be in units such that
               V/I gives volts/amp (or mV/mA).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('line', type=Type.STRING,
                             doc="Output line name"),
                   Parameter('voltage_chan', type=Type.STRING,
                             doc="Output voltage channel name"),
                   Parameter('current_chan', type=Type.STRING,
                             doc="Output current channel name"),
                   Parameter('obs', type=Type.STRING,
                             doc="Output OBS file name"),
                   Parameter('topo', type=Type.STRING,
                             doc="Output TOPO file name")
               ]),

        Method('ExportUBCRes2_IP', module='geogxx', version='6.4.2',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Same as :func:`ExportUBCRes_IP`, with error channel output.",
               notes="""
               Outputs a ``*.DAT`` file of the survey data for use in the
               UBC 2D inversion program DCINV2D.
               Voltage and current channels should be in units such that
               V/I gives volts/amp (or mV/mA).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ip', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('db', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('line', type=Type.STRING,
                             doc="Output line name"),
                   Parameter('voltage_chan', type=Type.STRING,
                             doc="Output voltage channel name"),
                   Parameter('current_chan', type=Type.STRING,
                             doc="Output current channel name"),
                   Parameter('error_chan', type=Type.STRING,
                             doc='Output error channel name ("" for none)'),
                   Parameter('obs', type=Type.STRING,
                             doc="Output OBS file name"),
                   Parameter('topo', type=Type.STRING,
                             doc="Output TOPO file name")
               ])
    ]
}

