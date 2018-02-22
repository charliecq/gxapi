import unittest
import geosoft.gxapi as gxapi
from base import GXAPITest


class Test(GXAPITest):

    @classmethod
    def setUpClass(cls):
        cls.setUpGXAPITest()
        pass

    def test_context(self):
        self.start()

        self.assertTrue(len(self.gid) > 0)

    def test_version(self):
        self.start()

        i = gxapi.str_ref()
        gxapi.GXSYS.get_sys_info(gxapi.SYS_INFO_VERSION_MAJOR, i)
        self.assertEqual('9', i.value)

        gxapi.GXSYS.get_sys_info(gxapi.SYS_INFO_VERSION_MINOR, i)
        try:
            self.assertEqual('3', i.value)
        except AssertionError:
            self.assertEqual('4', i.value)

###############################################################################################

if __name__ == '__main__':

    unittest.main()
