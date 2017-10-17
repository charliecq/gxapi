import geosoft.gxapi_cy as g_cy
import numpy as np

class ref_value:
    def __init__(self, value=None):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

class int_ref(ref_value):
    def __init__(self, value=0):
        self._value = value
    
class float_ref(ref_value):
    def __init__(self, value=0.0):
        self._value = value

class str_ref(ref_value):
    def __init__(self, value=""):
        self._value = value

class GX3DN:
    """
    This class manages the rendering of a 3D view. It allows
    the positioning of the camera, specification of the zoom
    as well as some rendering controls for the axis. It is
    directly related to the MVIEW class.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else g_cy.Wrap3DN(0)

    @classmethod
    def null(cls):
        """
        null() -> GX3DN:
        
        A null (undefined) instance of :class:`GX3DN`
        
        :returns: A null :class:`GX3DN`
        :rtype: :class:`GX3DN`
        """
        return GX3DN()

    def is_null(self):
        """
        is_null() -> bool:
        
        Check if the instance of :class:`GX3DN is null (undefined)`
        
        :returns: True if this is a null instance of :class:`GX3DN`, False otherwise.
        :rtype: bool
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle

    @classmethod
    def create(cls):
        """
        create() -> GX3DN:

        Creates a 3DN.

        :returns: 3DN Object
        :rtype: :class:`GX3DN`

        versionadded:: 5.1.2
        """
        return GX3DN(g_cy.Wrap3DN.create())

    def get_render_controls(self, p2, p3, p4, p6, p8):
        """
        get_render_controls((int_ref)p2, (int_ref)p3, (str_ref)p4, (str_ref)p6, (str_ref)p8) -> None:

        Get the rendering controls

        :param p2: Render Bounding Box (0 or 1)
        :type p2: :class:`int_ref`
        :param p3: Render Axis (0 or 1)
        :type p3: :class:`int_ref`
        :param p4: Label for X axis
        :type p4: :class:`str_ref`
        :param p6: Label for Y axis
        :type p6: :class:`str_ref`
        :param p8: Label for Z axis
        :type p8: :class:`str_ref`
        :returns: Nothing
        :rtype: None


        versionadded:: 6.3.0
        """
        p2.value, p3.value, p4.value, p6.value, p8.value = self._wrapper.get_render_controls(p2.value, p3.value, p4.value.encode(), p6.value.encode(), p8.value.encode())

    def set_render_controls(self, p2, p3, p4, p6, p8):
        """
        set_render_controls((int)p2, (int)p3, (str)p4, (str)p6, (str)p8) -> None:

        Get the rendering controls

        :param p2: Render Bounding Box (0 or 1)
        :type p2: int
        :param p3: Render Axis (0 or 1)
        :type p3: int
        :param p4: Label for X axis
        :type p4: str
        :param p6: Label for Y axis
        :type p6: str
        :param p8: Label for Z axis
        :type p8: str
        :returns: Nothing
        :rtype: None


        versionadded:: 6.3.0
        """
        self._wrapper.set_render_controls(p2, p3, p4.encode(), p6.encode(), p8.encode())

    


class GXVV:
    """
    This class manages the rendering of a 3D view. It allows
    the positioning of the camera, specification of the zoom
    as well as some rendering controls for the axis. It is
    directly related to the MVIEW class.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else g_cy.WrapVV(0)

    @classmethod
    def create(cls, type, elements):
        return GXVV(g_cy.WrapVV.create(type, elements))


    def fill_double(self, value):
        self._wrapper.fill_double(value)

    def get_data(self, start, num_elements, b, type):
        self._wrapper.get_data(start, num_elements, b, 5)

    def get_data_array(self, start, num_elements, dtype):
        return self._wrapper.get_data_array(start, num_elements, 5)

    def get_data_np(self, start, num_elements, dtype):
        r, a = self._wrapper.get_data_array(start, num_elements, 5)
        return (r, np.asarray(a))

c = g_cy.WrapPGeo("a", "1.0", 0, 0)
try:
#    print("Hit Enter to continue")
#    input()

    with GXVV.create(1, 5) as vv:
        b = bytearray(5*8)
        vv.get_data(0, 5, b, float)
        print(b)
        r, a = vv.get_data_array(0, 5, float)
        na = np.asarray(a)
        print(na)
        vv.fill_double(13.2345)
        vv.get_data(0, 5, b, float)
        print(b)
        r, a = vv.get_data_array(0, 5, float)
        nb = np.asarray(a)
        print(nb)
        print('dealloc na')
        na = None
        print('dealloc nb')
        nb = None

        r, npa = vv.get_data_np(0, 5, float)
        print(npa)
        print(npa.dtype)
        print('dealloc npa')
        npa = None
        print('end width')
        


    #dn = g_cy.Wrap3DN.create()
    #try:
    #    print(dn)
    #
    #    print(dn.get_render_controls(9,9,"".encode(),"".encode(),"".encode()))
    #    print(dn.set_render_controls(0,0,"a".encode(),"v".encode(),"x".encode()))
    #    print(dn.get_render_controls(9,9,"".encode(),"".encode(),"".encode()))
    #finally:
    #    del dn
    #
    #with GX3DN.create() as dn:
    #    print(dn)
    #
    #    box = int_ref()
    #    axis = int_ref()
    #    xl = str_ref()
    #    yl = str_ref()
    #    zl = str_ref()
    #    dn.get_render_controls(box,axis,xl,yl,zl)
    #    print("box: {}, axis: {}, xl: {}, yl: {}, zl: {}".format(box.value,axis.value,xl.value,yl.value,zl.value))
    #    dn.set_render_controls(0,0,"a","v","x")
    #    dn.get_render_controls(box,axis,xl,yl,zl)
    #    print("box: {}, axis: {}, xl: {}, yl: {}, zl: {}".format(box.value,axis.value,xl.value,yl.value,zl.value))
    print('final end')

finally:
    del c