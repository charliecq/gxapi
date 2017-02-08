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
                        doc="Single (X, Y) point")                        ,
               Constant('SHP_GEOM_TYPE_ARC', value='3', type=Type.INT32_T,
                        doc="Arc (polyline) multiple (X, Y) points.")                        ,
               Constant('SHP_GEOM_TYPE_POLYGON', value='5', type=Type.INT32_T,
                        doc="Polygon. Multiple (X, Y) points.")                        ,
               Constant('SHP_GEOM_TYPE_POINTZ', value='11', type=Type.INT32_T,
                        doc="Single (X, Y, Z) point")                        ,
               Constant('SHP_GEOM_TYPE_ARCZ', value='13', type=Type.INT32_T,
                        doc="Arc (polyline) multiple (X, Y, Z) points.")                        ,
               Constant('SHP_GEOM_TYPE_POLYGONZ', value='15', type=Type.INT32_T,
                        doc="Polygon. Multiple (X, Y, Z) points.")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('AppendItem_SHP', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Append the current item and data to an old :class:`SHP` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object")
               ]),

        Method('Create_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Create a new :class:`SHP` object",
               return_type="SHP",
               return_doc=":class:`SHP` object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`SHP_GEOM_TYPE`")
               ]),

        Method('Destroy_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`SHP` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object")
               ]),

        Method('iAddIntField_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Add an INT type data field to a shape file",
               return_type=Type.INT32_T,
               return_doc="Index of the new field",
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="field name")
               ]),

        Method('iAddRealField_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Add a REAL type data field to a shape file",
               return_type=Type.INT32_T,
               return_doc="Index of the new field",
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="field name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="number of decimal places")
               ]),

        Method('iAddStringField_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Add a string type data field to a shape file",
               return_type=Type.INT32_T,
               return_doc="Index of the new field",
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="field name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Maximum number of characters in the string")
               ]),

        Method('iFindField_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Find the index for a data field.",
               return_type=Type.INT32_T,
               return_doc="The index, -1 if not found.",
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="field name")
               ]),

        Method('iMaxIDNum_SHP', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the max ID number.",
               return_type=Type.INT32_T,
               return_doc="The max ID number.",
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object")
               ]),

        Method('iNumFields_SHP', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the field number.",
               return_type=Type.INT32_T,
               return_doc="The field number.",
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object")
               ]),

        Method('iNumRecords_SHP', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the record number.",
               return_type=Type.INT32_T,
               return_doc="The record number.",
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object")
               ]),

        Method('iType_SHP', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`SHP` object's geometry type.",
               return_type=Type.INT32_T,
               return_doc="the :class:`SHP` object's geometry type (:def:`SHP_GEOM_TYPE`)",
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object")
               ]),

        Method('Open_SHP', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Open an old :class:`SHP` object",
               return_type="SHP",
               return_doc=":class:`SHP` object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File name")
               ]),

        Method('SetArc_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Write an XY arc (polyline) item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type="VV",
                             doc="X locations"),
                   Parameter('p3', type="VV",
                             doc="Y locations")
               ]),

        Method('SetArcZ_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Write an XYZ arc (polyline) item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type="VV",
                             doc="X locations"),
                   Parameter('p3', type="VV",
                             doc="Y locations"),
                   Parameter('p4', type="VV",
                             doc="Z locations")
               ]),

        Method('SetInt_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set a data value to a int.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="data field index"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="input int value")
               ]),

        Method('SetIPJ_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set a :class:`SHP` object's projection.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type="IPJ",
                             doc="input :class:`IPJ`")
               ]),

        Method('SetPoint_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Write an XY point item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y location")
               ]),

        Method('SetPointZ_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Write an XYZ point item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z location")
               ]),

        Method('SetPolygon_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Write an XY polygon item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type="VV",
                             doc="X locations"),
                   Parameter('p3', type="VV",
                             doc="Y locations"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`GEO_BOOL` :def_val:`GS_TRUE` for outer ring polygon (inclusive/island), :def_val:`GS_FALSE` for inner ring (exclusive/hole)")
               ]),

        Method('SetPolygonZ_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Write an XYZ polygon item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type="VV",
                             doc="X locations"),
                   Parameter('p3', type="VV",
                             doc="Y locations"),
                   Parameter('p4', type="VV",
                             doc="Z locations"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`GEO_BOOL` :def_val:`GS_TRUE` for outer ring polygon (inclusive/island), :def_val:`GS_FALSE` for inner ring (exclusive/hole)")
               ]),

        Method('SetReal_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set a data value to a real.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="data field index"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="input real value")
               ]),

        Method('SetString_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set a data value to a string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="data field index"),
                   Parameter('p3', type=Type.STRING,
                             doc="input string value")
               ]),

        Method('WriteItem_SHP', module='geogxx', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Output the current item and data.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SHP",
                             doc=":class:`SHP` object")
               ])
    ]
}

