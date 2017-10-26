from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('PDF3D',
                 doc="The :class:`PDF3D` class provides the ability to create 3D PDFs.")





gx_methods = {
    'Miscellaneous': [

        Method('Render_PDF3D', module='geopdf3d', version='6.4.2',
               availability=Availability.PUBLIC, 
               doc="Render a voxel, voxsurf and/or gensurf to pdf",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('file_name', type=Type.STRING,
                             doc="Filename"),
                   Parameter('resolution', type=Type.INT32_T,
                             doc="Resolution"),
                   Parameter('no_clipping', type=Type.INT32_T,
                             doc="Noclipping")
               ]),

        Method('RenderToPage_PDF3D', module='geopdf3d', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Render a voxel, voxsurf and/or gensurf to a specified page on a pdf",
               return_type=Type.VOID,
               parameters = [
                   Parameter('mview', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('file_name', type=Type.STRING,
                             doc="Filename"),
                   Parameter('page_number', type=Type.INT32_T,
                             doc="Page number"),
                   Parameter('resolution', type=Type.INT32_T,
                             doc="Resolution"),
                   Parameter('no_clip', type=Type.INT32_T,
                             doc="Noclipping")
               ]),

        Method('Export2D_PDF3D', module='geopdf3d', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Export a 2D map to a PDF file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('input_map', type=Type.STRING,
                             doc="Input map file"),
                   Parameter('output_file', type=Type.STRING,
                             doc="Output PDF file"),
                   Parameter('create_layersin_pdf', type=Type.INT32_T,
                             doc="Create layers in PDF"),
                   Parameter('geospatial_pdf', type=Type.INT32_T,
                             doc="Geospatial PDF"),
                   Parameter('open_pdf', type=Type.INT32_T,
                             doc="Open PDF after export")
               ])
    ]
}

