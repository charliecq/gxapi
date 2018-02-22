import os
import shutil
import unittest
import inspect
import subprocess
from tkinter import Tk, messagebox
import win32con
import win32gui

os.environ['GEOSOFT_FORCE_MESA_3D'] = '1'
os.environ['GEOSOFT_TEST_MODE'] = '1'
os.environ['GEOSOFT_TESTSYSTEM_MODE'] = '1'

def set_geosoft_bin_path():
    if 'GX_GEOSOFT_BIN_PATH_TESTING' in os.environ:
        os.environ['GX_GEOSOFT_BIN_PATH'] = os.environ['GX_GEOSOFT_BIN_PATH_TESTING']

import geosoft
import geosoft.gxapi as gxapi

_prevent_interactive = os.environ.get('GEOSOFT_PREVENT_INTERACTIVE', 0) == '1'
if _prevent_interactive:
    UPDATE_RESULTS = False
    UPDATE_RESULTS_DONT_ASK = False
    SHOW_TEST_VIEWERS = False

win32gui.SystemParametersInfo(win32con.SPI_SETFONTSMOOTHING, True)

def _t(s):
    return s

def _verify_no_gx_context():
    try:
        loc_gx = gxapi.GXContext.current()
    except:
        loc_gx = None
    if loc_gx is not None:
        raise Exception(_t("We have a GXContext but should not!"))


class GXAPITest(unittest.TestCase):
    _test_case_py = None
    _test_case_filename = None
    _result_base_dir = None
    _cls_unique_id_count = 0
    _gx = None

    @classmethod
    def _cls_uuid(cls):
        cls._cls_unique_id_count = cls._cls_unique_id_count + 1
        return 'uuid_{}_{}'.format(cls._test_case_filename, cls._cls_unique_id_count)

    @classmethod
    def setUpGXAPITest(cls, version=geosoft.__version__):
        _verify_no_gx_context()

        cls._cls_unique_id_count = 0
        cls._test_case_py = os.path.join(os.getcwd(), inspect.getfile(cls))
        cls._test_case_filename = os.path.split(cls._test_case_py)[1]
        if cls._test_case_filename == os.path.split(__file__)[1]:
            raise Exception(_t("GXAPITest base class incorrectly detected as test case!"))

        cur_dir = os.path.dirname(cls._test_case_py)
        cls._result_base_dir = os.path.join(cur_dir, 'results', cls._test_case_filename)
        os.makedirs(cls._result_base_dir, exist_ok=True)
        os.chdir(cls._result_base_dir)

        cls._temp_folder_override = os.path.join(cls._result_base_dir, '__tmp__')
        if os.path.exists(cls._temp_folder_override):
            shutil.rmtree(cls._temp_folder_override)
        os.makedirs(cls._temp_folder_override, exist_ok=True)

        set_geosoft_bin_path()
        cls._gx = gxapi.GXContext.create('GXAPI test', version, 0, 0)
        pass

    @classmethod
    def tearDownGXAPITest(cls):
        cls._gx = None
        cls._test_case_py = None
        cls._test_case_filename = None
        cls._result_base_dir = None
        cls._cls_unique_id_count = 0
        _verify_no_gx_context()

    @property
    def gx(self):
        return self.__class__._gx

    @property
    def gid(self):
        user = gxapi.str_ref()
        company = gxapi.str_ref()
        gxapi.GXSYS.get_licensed_user(user, company)
        return user.value

    @classmethod
    def setUpClass(cls):
        if cls is GXAPITest:
            raise unittest.SkipTest("Skip GXAPITest tests, it's a base class")
        cls.setUpGXAPITest()

    @classmethod
    def tearDownClass(cls):
        cls.tearDownGXAPITest()

    def _uuid(self):
        self._unique_id_count = self._unique_id_count + 1
        return 'uuid_{}_{}'.format(self._func, self._unique_id_count)

    def start(self):
        self._func = self.id().split('.')[-1]
        self._result_dir = os.path.join(self._result_base_dir, self._func)
        result_run_dir = os.path.join(self._result_dir, 'result')
        if os.path.exists(result_run_dir):
            shutil.rmtree(result_run_dir)

        self._uuid_callable = self._uuid
        self._unique_id_count = 0

    @property
    def result_dir(self):
        return self._result_dir

    @result_dir.setter
    def result_dir(self, value):
        self._result_dir = value

    @classmethod
    def pause(cls):
        if not _prevent_interactive:
            print("\n\nHit Return key to continue...")
            input()