import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxapi as gxapi
import geosoft.gxpy.grid as gxgrid

gxc = gx.GXpy()
memory_grid_1 = gxgrid.Grid.new(properties={'nx': 100, 'ny':100})
memory_grid_2 = gxgrid.Grid.new(properties=memory_grid_1.properties())
gxapi.GXIMU.grid_vd(memory_grid_1.gximg, memory_grid_2.gximg)
