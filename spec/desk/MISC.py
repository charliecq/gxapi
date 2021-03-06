from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MISC',
                 doc="""
                 Not a class. A catch-all for miscellaneous geophysical
                 methods, primarily file conversions.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('ConvertCG3toRAW_MISC', module='geogxx', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Convert a CG3 dump to RAW format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('cg3', type=Type.STRING,
                             doc="Name of the CG3 file"),
                   Parameter('raw', type=Type.STRING,
                             doc="Name of the RAW file"),
                   Parameter('tide_corr_opt', type=Type.INT32_T,
                             doc="TideCorr Option: 1 - use geosoft, 0 - use CG3/CG5")
               ]),

        Method('ConvertCG5toRAW_MISC', module='geogxx', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Convert a CG5 dump to RAW format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('cg5', type=Type.STRING,
                             doc="Name of the CG5 file"),
                   Parameter('raw', type=Type.STRING,
                             doc="Name of the RAW file"),
                   Parameter('tide_corr_opt', type=Type.INT32_T,
                             doc="TideCorr Option: 1 - use geosoft, 0 - use CG3/CG5")
               ]),

        Method('Ukoa2Tbl_MISC', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Convert a UKOA file to a location TBL file.",
               notes="""
               The TBL file will contain the following fields:
               
               = Line:string16
               = Station:long
               = Latitude:double
               = Longitude:double
               = X:double
               = Y:double
               = Elevation:double
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('ukoa', type=Type.STRING,
                             doc="Name of the UKOA file"),
                   Parameter('alias', type=Type.STRING,
                             doc="Line name alias table"),
                   Parameter('tbl', type=Type.STRING,
                             doc="Name of the output table")
               ])
    ],
    'Obsolete': [

        Method('CG3toRAW_MISC', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Convert a CG3 dump to RAW format.",
               notes="""
               REPLACED BY: :func:`ConvertCG3toRAW_MISC`.
               or supporting tide correction info in the CG3 file.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('cg3', type=Type.STRING,
                             doc="Name of the CG3 file"),
                   Parameter('raw', type=Type.STRING,
                             doc="Name of the RAW file")
               ]),

        Method('CG5toRAW_MISC', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Convert a CG5 dump to RAW format.",
               notes="""
               REPLACED BY: :func:`ConvertCG5toRAW_MISC`.
               for supporting tide correction info in the CG5 file.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('cg5', type=Type.STRING,
                             doc="Name of the CG5 file"),
                   Parameter('raw', type=Type.STRING,
                             doc="Name of the RAW file")
               ])
    ]
}

