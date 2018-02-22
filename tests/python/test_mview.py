import unittest
import geosoft.gxapi as gxapi
import numpy as np
import geosoft.gxpy.view as gxv
import geosoft.gxpy.group as gxg
import geosoft.gxpy.vv as gxvv

from base import GXAPITest


class Test(GXAPITest):
    
    @classmethod
    def setUpClass(cls):
        cls.setUpGXAPITest()

    @unittest.skip('WIP – see issue #13 https://github.com/GeosoftInc/gxapi/issues/13')
    def test_draw_surface_3d(self):

        verts = np.array([[0, 0, 0],
                          [5, 0, 0],
                          [5, 5, 0],
                          [0, 3, 5],
                          [2.5, 2, 10],
                          [-3, 6, 8],
                          [-4, 0, 12]], dtype=np.float64)
        faces = np.array([[0, 1, 2],
                          [0, 2, 3],
                          [3, 2, 4],
                          [1, 2, 4],
                          [3, 4, 5],
                          [6, 4, 5]], dtype=np.int32)

        with gxv.View_3d.new() as v3d:
            v3d_file = v3d.file_name
            with gxg.Draw_3d(v3d, 'Surface') as g:
                verts = verts[faces].reshape(-1, 3)
                vx, vy, vz = gxvv.vvset_from_np(verts)
                vf1, vf2, vf3 = gxvv.vvset_from_np(faces)
                normals = gxg.vertex_normals_np(faces, verts)
                nx, ny, nz = gxvv.vvset_from_np(normals[faces].reshape(-1, 3))

                # using a constant color does not complain
                v3d.gxview.draw_surface_3d_ex('test',
                                              vx.gxvv, vy.gxvv, vz.gxvv,
                                              nx.gxvv, ny.gxvv, nz.gxvv,
                                              gxapi.GXVV.null(), gxg.C_GREY,
                                              vf1.gxvv, vf2.gxvv, vf3.gxvv,
                                              v3d.coordinate_system.gxipj)

                # using an array color raises invalid number of colour if we pass colours/vertex
                color = np.array([gxg.C_GREY for i in range(vx.length)])
                color_vv = gxvv.GXvv(color, dtype=np.int32)
                try:
                    v3d.gxview.draw_surface_3d_ex('test2',
                                                  vx.gxvv, vy.gxvv, vz.gxvv,
                                                  nx.gxvv, ny.gxvv, nz.gxvv,
                                                  color_vv.gxvv, gxg.C_GREY,
                                                  vf1.gxvv, vf2.gxvv, vf3.gxvv,
                                                  v3d.coordinate_system.gxipj)

                except gxapi.GXAPIError as e:
                    print(str(e))

                    # and if pass colours/face it asserts
                    color = np.array([gxg.C_GREY for i in range(faces.shape[0])])
                    color_vv = gxvv.GXvv(color, dtype=np.int32)
                    v3d.gxview.draw_surface_3d_ex('test2',
                                                  vx.gxvv, vy.gxvv, vz.gxvv,
                                                  nx.gxvv, ny.gxvv, nz.gxvv,
                                                  color_vv.gxvv, gxg.C_GREY,
                                                  vf1.gxvv, vf2.gxvv, vf3.gxvv,
                                                  v3d.coordinate_system.gxipj)


###############################################################################################

if __name__ == '__main__':

    unittest.main()
