import unittest
import geosoft.gxapi as gxapi
import geosoft.gxpy.grid as gxgrid

from base import GXAPITest


class Test(GXAPITest):
    
    @classmethod
    def setUpClass(cls):
        cls.setUpGXAPITest()

    @unittest.skip('WIP – see issue #16 https://github.com/GeosoftInc/gxapi/issues/16')
    def test_gximu_grid_vd_from_memory_grid(self):
        self.start()

        memory_grid_1 = gxgrid.Grid.new(properties={'nx': 100, 'ny': 80})
        memory_grid_2 = gxgrid.Grid.new(properties=memory_grid_1.properties())
        gxapi.GXIMU.grid_vd(memory_grid_1.gximg, memory_grid_2.gximg)
        self.assertEqual(memory_grid_2.nx, 100)
        self.assertEqual(memory_grid_2.ny, 80)


###############################################################################################

if __name__ == '__main__':

    unittest.main()
