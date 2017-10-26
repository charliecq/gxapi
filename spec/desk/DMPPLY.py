from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DMPPLY',
                 doc="Datamine Multiple polygon object")





gx_methods = {
    'Miscellaneous': [

        Method('_Clear_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Clear/remove all polygons from the :class:`DMPPLY`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY")
               ]),

        Method('Copy_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Copy",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dest', type="DMPPLY",
                             doc="Destination"),
                   Parameter('source', type="DMPPLY",
                             doc="Source")
               ]),

        Method('Create_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Creates a :class:`DMPPLY` object.",
               return_type="DMPPLY",
               return_doc="DMPLY Object"),

        Method('Destroy_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys the :class:`DMPPLY` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` Object")
               ]),

        Method('GetAzimuth_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the azimuth of a given polygon.",
               notes="""
               The azimuth is the equivalent section azimuth,
               equal to the azimuth of the normal vector plus
               90 degrees.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p', type=Type.INT32_T,
                             doc="Polygon number (1 to NP)"),
                   Parameter('az', type=Type.DOUBLE, is_ref=True,
                             doc="Azimuth (degrees) (o)")
               ]),

        Method('GetExtents_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the center, width and height of a given polygon.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p', type=Type.INT32_T,
                             doc="Polygon number (1 to NP)"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="Center point X (o)"),
                   Parameter('y', type=Type.DOUBLE, is_ref=True,
                             doc="Center point Y (o)"),
                   Parameter('z', type=Type.DOUBLE, is_ref=True,
                             doc="Center point Z (o)"),
                   Parameter('w', type=Type.DOUBLE, is_ref=True,
                             doc="Width of polygon (in its plane) (o)"),
                   Parameter('h', type=Type.DOUBLE, is_ref=True,
                             doc="Height of polygon (Z extent) (o)")
               ]),

        Method('GetJoins_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get join lines for each vertex in a specific polygon.",
               notes="""
               If a specific vertex is not joined, the returned value is 0.
               If the vertex is joined, then the index of the join line (1 to NJoins)
               is returned.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc="Datamine polygon Object"),
                   Parameter('p', type=Type.INT32_T,
                             doc="Polygon number (1 to N)"),
                   Parameter('vv', type="VV",
                             doc="INT :class:`VV` of join indices (1 to NJoins).")
               ]),

        Method('GetNormalVectors_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the normal vectors of a given polygon.",
               notes="""
               Three normalized vectors are returned.
               The first is horizontal, in the plane of the polygon.
               The second is in the vertical plane, corresponding to the
               "down-dip" direction.
               The third is the normal vector to the polygon plane.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p', type=Type.INT32_T,
                             doc="Polygon number (1 to NP)"),
                   Parameter('x1', type=Type.DOUBLE, is_ref=True,
                             doc="X component (o) (Horizontal azimuth vector)"),
                   Parameter('y1', type=Type.DOUBLE, is_ref=True,
                             doc="Y component (o)"),
                   Parameter('z1', type=Type.DOUBLE, is_ref=True,
                             doc="Z component (o)"),
                   Parameter('x2', type=Type.DOUBLE, is_ref=True,
                             doc="X component (o) (Down-dip, in the vertical plane)"),
                   Parameter('y2', type=Type.DOUBLE, is_ref=True,
                             doc="Y component (o)"),
                   Parameter('z2', type=Type.DOUBLE, is_ref=True,
                             doc="Z component (o)"),
                   Parameter('x3', type=Type.DOUBLE, is_ref=True,
                             doc="X component (o) (Normal vector)"),
                   Parameter('y3', type=Type.DOUBLE, is_ref=True,
                             doc="Y component (o)"),
                   Parameter('z3', type=Type.DOUBLE, is_ref=True,
                             doc="Z component (o)")
               ]),

        Method('GetPoly_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get a specific polygon from a :class:`DMPPLY` object.",
               notes="Get the number of points from the :class:`VV` length.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p', type=Type.INT32_T,
                             doc="Polygon number (1 to NP) (i)"),
                   Parameter('v_vx', type="VV",
                             doc="X Locations (o)"),
                   Parameter('v_vy', type="VV",
                             doc="Y Locations (o)"),
                   Parameter('v_vz', type="VV",
                             doc="Z Locations (o)")
               ]),

        Method('GetSwing_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the swing of a given polygon.",
               notes="""
               The swing is the equivalent section swing,
               equal to zero for vertical plates, and increasing
               as the normal vector goes from horizontal upward.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p', type=Type.INT32_T,
                             doc="Polygon number (1 to NP)"),
                   Parameter('az', type=Type.DOUBLE, is_ref=True,
                             doc="Swing (degrees) (o)")
               ]),

        Method('GetVertex_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get a vertex location from a :class:`DMPPLY` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p', type=Type.INT32_T,
                             doc="Polygon number (1 to NP)"),
                   Parameter('v', type=Type.INT32_T,
                             doc="Vertex number (1 to NV)"),
                   Parameter('x', type=Type.DOUBLE, is_ref=True,
                             doc="X Location (o)"),
                   Parameter('y', type=Type.DOUBLE, is_ref=True,
                             doc="Y Location (o)"),
                   Parameter('z', type=Type.DOUBLE, is_ref=True,
                             doc="Z Location (o)")
               ]),

        Method('iNumJoins_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the number of joining lines in a :class:`DMPPLY` object.",
               return_type=Type.INT32_T,
               return_doc="Number of joining lines",
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` object")
               ]),

        Method('iNumPolys_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the number of polygons in a :class:`DMPPLY` object.",
               notes="""
               The value returned is the "NP" used in function descriptions
               below.
               """,
               return_type=Type.INT32_T,
               return_doc="Number of polygons",
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` object")
               ]),

        Method('iNumVertices_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the number of vertices in a polygon.",
               notes="""
               The value returned is the "NV" used in function descriptions
               below.
               """,
               return_type=Type.INT32_T,
               return_doc="Number of vertices in a polygon",
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p', type=Type.INT32_T,
                             doc="Polygon number (1 to NP)")
               ]),

        Method('Load_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Loads a Datamine polygon file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` Object"),
                   Parameter('file', type=Type.STRING,
                             doc="Name of the file to load")
               ]),

        Method('MoveVertex_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Moves a vertex and any associated lines.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p', type=Type.INT32_T,
                             doc="Polygon number (1 to NP)"),
                   Parameter('v', type=Type.INT32_T,
                             doc="Vertex number (1 to NV)"),
                   Parameter('x', type=Type.DOUBLE,
                             doc="New location X"),
                   Parameter('y', type=Type.DOUBLE,
                             doc="New location Y"),
                   Parameter('z', type=Type.DOUBLE,
                             doc="New location Z")
               ]),

        Method('ProjectPoly_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Project a polygon onto a vertical plane.",
               notes="""
               Gives the location in plane coordinates of a selected polygon,
               after it has been projected perpendicularly onto the plane.
               
               Plane coodinates: X - horizontal in plane
                                 Y - "vertical" in plane (can be a swing)
                                 Z - horizontal, "perpendicular" to plane (RH)
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p', type=Type.INT32_T,
                             doc="Polygon number (1 to NP)"),
                   Parameter('xp', type=Type.DOUBLE,
                             doc="X location of plane origin in 3D"),
                   Parameter('yp', type=Type.DOUBLE,
                             doc="Y location of plane origin in 3D"),
                   Parameter('zp', type=Type.DOUBLE,
                             doc="Z location of plane origin in 3D"),
                   Parameter('az', type=Type.DOUBLE,
                             doc="Azimuth of the plane in degrees"),
                   Parameter('swing', type=Type.DOUBLE,
                             doc="Swing of the plane in degrees"),
                   Parameter('v_vx', type="VV",
                             doc="X (horizontal along-section locations on vertical plane  (o)"),
                   Parameter('v_vy', type="VV",
                             doc="Y (vertical locations on vertical plane  (o)"),
                   Parameter('v_vz', type="VV",
                             doc="Z (horizontal distances perpendicular to the plane  (o)")
               ]),

        Method('ReProjectPoly_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Recover polygon locations from 2D locations on vertical plane.",
               notes="""
               This is the inverse operation of :func:`ProjectPoly_DMPPLY`.
               
               Input the 2D locations on the projected vertical plane. These locations
               are projected back onto the original polygon plane.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p', type=Type.INT32_T,
                             doc="Polygon number (1 to lNP) (i)"),
                   Parameter('xp', type=Type.DOUBLE,
                             doc="X location of plane origin in 3D (i)"),
                   Parameter('yp', type=Type.DOUBLE,
                             doc="Y location of plane origin in 3D (i)"),
                   Parameter('zp', type=Type.DOUBLE,
                             doc="Z location of plane origin in 3D (i)"),
                   Parameter('az', type=Type.DOUBLE,
                             doc="Azimuth of the plane in degrees (i)"),
                   Parameter('v_vx', type="VV",
                             doc="X locations on vertical plane  (i)"),
                   Parameter('v_vy', type="VV",
                             doc="Y (actually Z) locations on vertical plane  (i)"),
                   Parameter('v_vx3', type="VV",
                             doc="X Locations of polygon (o)"),
                   Parameter('v_vy3', type="VV",
                             doc="Y Locations of polygon (o)"),
                   Parameter('v_vz3', type="VV",
                             doc="Z Locations of polygon (o)")
               ]),

        Method('Save_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Save to a Datamine polygon file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` Object"),
                   Parameter('file', type=Type.STRING,
                             doc="Name of the file to save to")
               ]),

        Method('SetPoly_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Set a specific polygon into a :class:`DMPPLY` object.",
               notes="Get the number of points from the :class:`VV` length.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('dmpply', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p', type=Type.INT32_T,
                             doc="Polygon number (1 to NP) (i)"),
                   Parameter('v_vx', type="VV",
                             doc="X Locations (i)"),
                   Parameter('v_vy', type="VV",
                             doc="Y Locations (i)"),
                   Parameter('v_vz', type="VV",
                             doc="Z Locations (i)")
               ])
    ]
}

