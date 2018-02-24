import unittest
import geosoft.gxapi as gxapi
import geosoft.gxpy.grid as gxgrid
import geosoft.gxpy.vv as gxvv

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

    @unittest.skip('WIP – see issue #17 https://github.com/GeosoftInc/gxapi/issues/17')
    def test_issue_17(self):
        self.start()

        def make_int32_grid():

            # create an int32 grid
            img = gxapi.GXIMG.create_new_file(3, 1, 50, 20, 'test.grd')

            # read 10 row, test that it is dummy
            vv = gxvv.GXvv(dtype=int)
            img.read_v(10, 0, 0, vv.gxvv)
            self.assertEqual(vv[10][0], gxapi.GS_S4DM)

            # fill 10'th row with 1, test that it is 1.
            vv.fill(1)
            img.write_v(10, 0, 0, vv.gxvv)
            img.read_v(10, 0, 0, vv.gxvv)
            self.assertEqual(vv[10][0], 1)

            # OK, grid is as expected, close
            img = None

        def read_grid_we_just_made_as_default():

            # open the grid with default type, which I expect will be GS_LONG
            img = gxapi.GXIMG.create_file(gxapi.GS_TYPE_DEFAULT, 'test.grd', gxapi.IMG_FILE_READORWRITE)

            # !!!! - the grid is GS_FLOAT, but I expected GS_LONG
            self.assertTrue(img.e_type() == gxapi.GS_LONG)

            # read the 10'th row as int, we get the right data
            vv = gxvv.GXvv(dtype=int)
            img.read_v(10, 0, 0, vv.gxvv)
            self.assertEqual(vv[10][0], 1)

            # try as float, also correct
            vv = gxvv.GXvv(dtype=float)
            img.read_v(10, 0, 0, vv.gxvv)
            self.assertEqual(vv[10][0], 1.)

        def read_grid_we_just_made_as_type(gstype):

            # open the grid with specified type
            img = gxapi.GXIMG.create_file(gstype, 'test.grd', gxapi.IMG_FILE_READORWRITE)
            self.assertTrue(img.e_type() == gstype)

            # read the 10'th row as int
            vv = gxvv.GXvv(dtype=int)
            img.read_v(10, 0, 0, vv.gxvv)
            self.assertEqual(vv[10][0], 1)

            # read as float
            vv = gxvv.GXvv(dtype=float)
            img.read_v(10, 0, 0, vv.gxvv)
            self.assertEqual(vv[10][0], 1.)

        try:

            make_int32_grid()
            read_grid_we_just_made_as_type(gxapi.GS_FLOAT)
            read_grid_we_just_made_as_type(gxapi.GS_DOUBLE)
            read_grid_we_just_made_as_type(gxapi.GS_LONG)   # FAILS
            read_grid_we_just_made_as_default()             # FAILS


        finally:
            gxgrid.delete_files('test.grd')

###############################################################################################

if __name__ == '__main__':

    unittest.main()
