from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('SHP',
                 doc="The :class:`SHP` class is used to create ESRI shape files.",
                 notes="""
                 Shape files contain a single "geometry" type, e.g.
                 points, arcs or polygons. They may be accompanied by
                 a DBF file containing attribute data.
                 """)


gx_defines = [
    Define('SHP_GEOM_TYPE',
           doc="Shape file geometry types",
           constants=[
               Constant('SHP_GEOM_TYPE_POINT', value='1', type=Type.INT32_T,
                        doc="Single (X, Y) point"),
               Constant('SHP_GEOM_TYPE_ARC', value='3', type=Type.INT32_T,
                        doc="Arc (polyline) multiple (X, Y) points."),
               Constant('SHP_GEOM_TYPE_POLYGON', value='5', type=Type.INT32_T,
                        doc="Polygon. Multiple (X, Y) points."),
               Constant('SHP_GEOM_TYPE_POINTZ', value='11', type=Type.INT32_T,
                        doc="Single (X, Y, Z) point"),
               Constant('SHP_GEOM_TYPE_ARCZ', value='13', type=Type.INT32_T,
                        doc="Arc (polyline) multiple (X, Y, Z) points."),
               Constant('SHP_GEOM_TYPE_POLYGONZ', value='15', type=Type.INT32_T,
                        doc="Polygon. Multiple (X, Y, Z) points.")
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('AppendItem_SHP', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Append the current item and data to an old :class:`SHP` object.",
               notes="""
               The currently stored :class:`SHP` item and data are written to the
               :class:`SHP` geometry and data files. (If no data fields have been
               defined, then the data file is not written).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object")
               ]),

        Method('Create_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Create a new :class:`SHP` object",
               notes="""
               The file name is used to create the various files. The
               file type and extension are added:
               
               e.g. "filename.shp",
                    "filename.dbf"
               
               The following geometry types are currently supported:
               
               Type                    Required geometry function.
               
               :def_val:`SHP_GEOM_TYPE_POINT`     :func:`SetPoint_SHP`
               :def_val:`SHP_GEOM_TYPE_ARC`       :func:`SetArc_SHP`
               :def_val:`SHP_GEOM_TYPE_POLYGON`   :func:`SetPolygon_SHP`
               
               :def_val:`SHP_GEOM_TYPE_POINTZ`    :func:`SetPointZ_SHP`
               :def_val:`SHP_GEOM_TYPE_ARCZ`      :func:`SetArcZ_SHP`
               :def_val:`SHP_GEOM_TYPE_POLYGONZ`  :func:`SetPolygonZ_SHP`
               """,
               return_type="SHP",
               return_doc=":class:`SHP` object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="File name"),
                   Parameter('type', type=Type.INT32_T,
                             doc=":def:`SHP_GEOM_TYPE`")
               ]),

        Method('Destroy_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`SHP` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object")
               ]),

        Method('iAddIntField_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Add an INT type data field to a shape file",
               notes="""
               The returned field index should be used with the SetXXX_SHP
               functions to set individual data values.
               """,
               return_type=Type.INT32_T,
               return_doc="Index of the new field",
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('field', type=Type.STRING,
                             doc="Field name")
               ]),

        Method('iAddRealField_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Add a REAL type data field to a shape file",
               notes="""
               The returned field index should be used with the SetXXX_SHP
               functions to set individual data values.
               """,
               return_type=Type.INT32_T,
               return_doc="Index of the new field",
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('field', type=Type.STRING,
                             doc="Field name"),
                   Parameter('dec', type=Type.INT32_T,
                             doc="Number of decimal places")
               ]),

        Method('iAddStringField_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Add a string type data field to a shape file",
               notes="""
               The returned field index should be used with the SetXXX_SHP
               functions to set individual data values.
               """,
               return_type=Type.INT32_T,
               return_doc="Index of the new field",
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('field', type=Type.STRING,
                             doc="Field name"),
                   Parameter('width', type=Type.INT32_T,
                             doc="Maximum number of characters in the string")
               ]),

        Method('iFindField_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Find the index for a data field.",
               return_type=Type.INT32_T,
               return_doc="The index, -1 if not found.",
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('field', type=Type.STRING,
                             doc="Field name")
               ]),

        Method('iMaxIDNum_SHP', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the max ID number.",
               return_type=Type.INT32_T,
               return_doc="The max ID number.",
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object")
               ]),

        Method('iNumFields_SHP', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the field number.",
               return_type=Type.INT32_T,
               return_doc="The field number.",
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object")
               ]),

        Method('iNumRecords_SHP', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the record number.",
               return_type=Type.INT32_T,
               return_doc="The record number.",
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object")
               ]),

        Method('iType_SHP', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`SHP` object's geometry type.",
               return_type=Type.INT32_T,
               return_doc="The :class:`SHP` object's geometry type (:def:`SHP_GEOM_TYPE`)",
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object")
               ]),

        Method('Open_SHP', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Open an old :class:`SHP` object",
               return_type="SHP",
               return_doc=":class:`SHP` object",
               parameters = [
                   Parameter('name', type=Type.STRING,
                             doc="File name")
               ]),

        Method('SetArc_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Write an XY arc (polyline) item.",
               notes="Can ONLY be used for :def_val:`SHP_GEOM_TYPE_ARC` files.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('vv_x', type="VV",
                             doc="X locations"),
                   Parameter('vv_y', type="VV",
                             doc="Y locations")
               ]),

        Method('SetArcZ_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Write an XYZ arc (polyline) item.",
               notes="Can ONLY be used for :def_val:`SHP_GEOM_TYPE_ARCZ` files.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('vv_x', type="VV",
                             doc="X locations"),
                   Parameter('vv_y', type="VV",
                             doc="Y locations"),
                   Parameter('vv_z', type="VV",
                             doc="Z locations")
               ]),

        Method('SetInt_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set a data value to a int.",
               notes="The input value is converted to the field's data type.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('index', type=Type.INT32_T,
                             doc="Data field index"),
                   Parameter('val', type=Type.INT32_T,
                             doc="Input int value")
               ]),

        Method('SetIPJ_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set a :class:`SHP` object's projection.",
               notes="""
               If the :class:`SHP` object has a projection, and it
               is not :def_val:`IPJ_TYPE_NONE`, then it will be output
               to a file with the .prj extension when the
               first object is output.
               This function should be called BEFORE the first
               object is written.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('ipj', type="IPJ",
                             doc="Input :class:`IPJ`")
               ]),

        Method('SetPoint_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Write an XY point item.",
               notes="Can ONLY be used for :def_val:`SHP_GEOM_TYPE_POINT` files.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X location"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y location")
               ]),

        Method('SetPointZ_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Write an XYZ point item.",
               notes="Can ONLY be used for :def_val:`SHP_GEOM_TYPE_POINTZ` files.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="X location"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('z', type=Type.DOUBLE,
                             doc="Z location")
               ]),

        Method('SetPolygon_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Write an XY polygon item.",
               notes="Can ONLY be used for :def_val:`SHP_GEOM_TYPE_POLYGON` files.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('vv_x', type="VV",
                             doc="X locations"),
                   Parameter('vv_y', type="VV",
                             doc="Y locations"),
                   Parameter('inclusive', type=Type.BOOL,
                             doc="``True`` for outer ring polygon (inclusive/island), ``False`` for inner ring (exclusive/hole)")
               ]),

        Method('SetPolygonZ_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Write an XYZ polygon item.",
               notes="Can ONLY be used for :def_val:`SHP_GEOM_TYPE_POLYGONZ` files.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('vv_x', type="VV",
                             doc="X locations"),
                   Parameter('vv_y', type="VV",
                             doc="Y locations"),
                   Parameter('vv_z', type="VV",
                             doc="Z locations"),
                   Parameter('inclusive', type=Type.INT32_T,
                             doc="``True`` for outer ring polygon (inclusive/island), ``False`` for inner ring (exclusive/hole)")
               ]),

        Method('SetReal_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set a data value to a real.",
               notes="The input value is converted to the field's data type.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('index', type=Type.INT32_T,
                             doc="Data field index"),
                   Parameter('val', type=Type.DOUBLE,
                             doc="Input real value")
               ]),

        Method('SetString_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set a data value to a string.",
               notes="The input string is converted to the field's data type.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('index', type=Type.INT32_T,
                             doc="Data field index"),
                   Parameter('str_val', type=Type.STRING,
                             doc="Input string value")
               ]),

        Method('WriteItem_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Output the current item and data.",
               notes="""
               The currently stored :class:`SHP` item and data are written to the
               :class:`SHP` geometry and data files. (If no data fields have been
               defined, then the data file is not written).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('shp', type="SHP",
                             doc=":class:`SHP` object")
               ])
    ]
}

