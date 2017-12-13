from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('ARCDB',
                 doc="""
                 The :class:`ARCDB` class is used in ArcGIS to access table contents from
                 data sources and layers.
                 """)


gx_defines = [
    Define('ARC_SELTBL_TYPE',
           doc="Describes what kind of table was selected",
           constants=[
               Constant('ARC_SELTBL_STANDALONE', value='0', type=Type.INT32_T,
                        doc="Standalone Table"),
               Constant('ARC_SELTBL_FEATURELAYER', value='1', type=Type.INT32_T,
                        doc="Feature Layer"),
               Constant('ARC_SELTBL_CANCELED', value='-1', type=Type.INT32_T,
                        doc="User Canceled")
           ]),

    Define('ARCDB_NULL',
           is_null_handle=True,
           doc="Database Null")]


gx_methods = {
    'Miscellaneous': [

        Method('CreateDAT_ARCDB', module='geoarcgis', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Create a handle to a ARCGIS table :class:`DAT` 2D object",
               return_type="DAT",
               return_doc=":class:`DAT`, terminates if creation fails",
               parameters = [
                   Parameter('arcdb', type="ARCDB",
                             doc="Handle to table"),
                   Parameter('x_field', type=Type.STRING,
                             doc="Name of X field in table"),
                   Parameter('y_field', type=Type.STRING,
                             doc="Name of Y field in table"),
                   Parameter('d_field', type=Type.STRING,
                             doc="Name of Data field in table")
               ]),

        Method('CreateDAT3D_ARCDB', module='geoarcgis', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Create a handle to a ARCGIS table :class:`DAT` 3D object",
               return_type="DAT",
               return_doc=":class:`DAT`, terminates if creation fails",
               parameters = [
                   Parameter('arcdb', type="ARCDB",
                             doc="Handle to table"),
                   Parameter('x_field', type=Type.STRING,
                             doc="Name of X field in table"),
                   Parameter('y_field', type=Type.STRING,
                             doc="Name of Y field in table"),
                   Parameter('z_field', type=Type.STRING,
                             doc="Name of Z field in table"),
                   Parameter('d_field', type=Type.STRING,
                             doc="Name of Data field in table")
               ]),

        Method('Current_ARCDB', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="This method return a handle to the current table",
               return_type="ARCDB",
               return_doc=":class:`ARCDB` Handle, :const:`ARCDB_NULL` if no table selected"),

        Method('ExportToDB_ARCDB', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Export data from an :class:`ARCDB` table into a group in a Geosoft GDB using a template.",
               notes="""
               1. The import template can be in the local directory or the GEOSOFT
                  directory.
               
               3. If the line already exists, the data will overwrite the existing data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('arcdb', type="ARCDB",
                             doc="Handle to table"),
                   Parameter('db', type="DB",
                             doc="Database"),
                   Parameter('temp', type=Type.STRING,
                             doc="Import template name"),
                   Parameter('line', type=Type.STRING,
                             doc="Oasis montaj line name to create (overrides template value)")
               ]),

        Method('FieldLST_ARCDB', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Place the list of field names in a :class:`LST`.",
               notes="""
               If Z or M values are supported by the table geometry the strings
               "<Z Values>" and "<M Values>" will be added accordingly.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('arcdb', type="ARCDB",
                             doc="Table"),
                   Parameter('lst', type="LST")
               ]),

        Method('FromIUnknown_ARCDB', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method attempts to make a table handle from an IUnknown pointer
               
               Returns				 :class:`ARCDB` Handle, :const:`ARCDB_NULL` if not successful
               """,
               return_type="ARCDB",
               parameters = [
                   Parameter('unknown', type=Type.INT32_T,
                             doc="IUnknown pointer")
               ]),

        Method('GetIPJ_ARCDB', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Get georeference information from a table.",
               notes="""
               If the table does not have an :class:`IPJ`, the :class:`IPJ` that is
               returned will have an unknown projection.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('arcdb', type="ARCDB",
                             doc="Table"),
                   Parameter('ipj', type="IPJ",
                             doc=":class:`IPJ` to fill in")
               ]),

        Method('iExistField_ARCDB', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method checks to see if the specified field exists
               in the table.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Field does not exist
               1 - Field Exists
               """,
               parameters = [
                   Parameter('arcdb', type="ARCDB",
                             doc="Table"),
                   Parameter('field', type=Type.STRING,
                             doc="Name of Field")
               ]),

        Method('iGetIUnknown_ARCDB', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="This method gets the IUnknown pointer",
               return_type=Type.INT32_T,
               return_doc="IUnknown pointer",
               parameters = [
                   Parameter('arcdb', type="ARCDB",
                             doc="Table")
               ]),

        Method('iImportChemDatabaseWizard_ARCDB', module='geoarcgis', version='8.0.0',
               availability=Availability.EXTENSION, is_gui=True, 
               doc="Template creation for importing geochem data.",
               return_type=Type.INT32_T,
               return_doc="0-OK 1-Cancel",
               parameters = [
                   Parameter('arcdb', type="ARCDB",
                             doc="Handle to table"),
                   Parameter('temp', type=Type.STRING,
                             doc="Template to make"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`IMPCH_TYPE`")
               ]),

        Method('SelTblExGUI_ARCDB', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Select table :class:`GUI` with table type.",
               return_type="ARCDB",
               return_doc="Handle to the table (Terminate on Error)",
               parameters = [
                   Parameter('table_type', type=Type.INT32_T, is_ref=True,
                             doc=":def:`ARC_SELTBL_TYPE`")
               ]),

        Method('SelTblGUI_ARCDB', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Select table :class:`GUI`.",
               notes="Terminates with Cancel on cancel, returns :const:`ARCDB_NULL` if there are no valid tables in current document.",
               return_type="ARCDB",
               return_doc="Handle to the table")
    ]
}

