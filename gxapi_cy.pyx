
#cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8

from libc.stdint cimport int32_t, int16_t
from libc.stdlib cimport malloc, free
from libc.string cimport strcpy, strcat, strncat, memset, memchr, memcmp, memcpy, memmove

import threading
from threading import current_thread

thread_local = threading.local()

from geosoft.gxapi import GXCancel, GXExit, GXAPIError, GXError

ctypedef Py_UNICODE WCHAR
ctypedef const WCHAR* LPCWSTR
ctypedef void* HWND
ctypedef void* HDC
cdef extern void Destr_SYS(void*, const int32_t* p1);
cdef extern int32_t iCheckTerminate_SYS(void*, int32_t* p1);
cdef extern int16_t sGetError_GEO(void*, char*, int32_t, char*, int32_t, int32_t*);



# Class GEOSOFT



# Class 3DN


cdef extern void Copy_3DN(void*, const int32_t* p1, const int32_t* p2);


cdef extern int32_t Create_3DN(void*);


cdef extern void Destroy_3DN(void*, const int32_t* p1);


cdef extern void GetPointOfView_3DN(void*, const int32_t* p1, double* p2, double* p3, double* p4);


cdef extern void GetScale_3DN(void*, const int32_t* p1, double* p2, double* p3, double* p4);


cdef extern int32_t iGetAxisColor_3DN(void*, const int32_t* p1);


cdef extern void IGetAxisFont_3DN(void*, const int32_t* p1, char* p2, const int32_t* p3);


cdef extern int32_t iGetBackgroundColor_3DN(void*, const int32_t* p1);


cdef extern void IGetRenderControls_3DN(void*, const int32_t* p1, int32_t* p2, int32_t* p3, char* p4, const int32_t* p5, char* p6, const int32_t* p7, char* p8, const int32_t* p9);


cdef extern int32_t iGetShading_3DN(void*, const int32_t* p1);


cdef extern void SetAxisColor_3DN(void*, const int32_t* p1, const int32_t* p2);


cdef extern void SetAxisFont_3DN(void*, const int32_t* p1, const char* p2);


cdef extern void SetBackgroundColor_3DN(void*, const int32_t* p1, const int32_t* p2);


cdef extern void SetPointOfView_3DN(void*, const int32_t* p1, const double* p2, const double* p3, const double* p4);


cdef extern void SetRenderControls_3DN(void*, const int32_t* p1, const int32_t* p2, const int32_t* p3, const char* p4, const char* p5, const char* p6);


cdef extern void SetScale_3DN(void*, const int32_t* p1, const double* p2, const double* p3, const double* p4);


cdef extern void SetShading_3DN(void*, const int32_t* p1, const int32_t* p2);



cdef extern void* pCreate_GEO(const char*, const char*, int32_t, void*, int32_t, char*, int32_t);
cdef extern void Destroy_GEO(void *);

cdef unicode _tounicode(char* s):
    return s.decode('UTF-8', 'backslashreplace')

ctypedef unsigned char char_type

cdef char_type[:] _chars(s):
    if isinstance(s, unicode):
        # encode to the specific encoding used inside of the module
        s = (<unicode>s).encode('utf8')
    else:
        unicode(s).encode('utf8')
    return s

cdef class WrapPGeo:
    cdef void* p_geo
    
    def __cinit__(self, application, version, wind_id, flags):
        app = (<unicode>application).encode('utf8')
        ver = (<unicode>version).encode('utf8')
        cdef size_t wind_handle = wind_id
        cdef void* hParentWnd = <void *>wind_handle
        cdef char* err = <char*>malloc(4096)
        try:
            tls_geo = getattr(thread_local, 'gxapi_cy_geo', None)
            if not tls_geo is None:
                raise GXAPIError("Only one gxapi_cy.WrapPGeo instance per thread allowed.");
            self.p_geo = pCreate_GEO(app, ver, 0, hParentWnd, flags, err, 4096)
            if self.p_geo == NULL:
                raise GXAPIError(_tounicode(err))
            thread_local.gxapi_cy_geo = <size_t>self.p_geo
        finally:
            free(err)
        
    def __dealloc__(self):
        if self.p_geo != NULL:
            Destroy_GEO(self.p_geo)
        thread_local.gxapi_cy_geo = None

    cdef _raise_on_gx_errors(self, void* p_geo):
        cdef int32_t term
        cdef char* module
        cdef char* err
        cdef int32_t error_number
        if iCheckTerminate_SYS(p_geo, &term) > 0:
            if term == 0:
                raise GXExit()
            elif term == -1:
                raise GXCancel()
            else:
                module = <char*>malloc(1024)
                err = <char*>malloc(4096)
                try:
                    sGetError_GEO(p_geo, module, 1024, err, 4096, &error_number)
                    if (error_number == 21023 or error_number == 21031 or # These two due to GXX asserts, Abort_SYS etc
                        error_number == 31009 or error_number == 31011):  # wrapper bind errors
                        raise GXAPIError(_tounicode(err));
                    else:
                        raise GXError(_tounicode(err), _tounicode(module), error_number)
                finally:
                    if module != NULL:
                        free(module)
                    if err != NULL:
                        free(err)
    
cdef void* get_p_geo():
    tls_geo = getattr(thread_local, 'gxapi_cy_geo', None)
    if tls_geo is None:
        raise GXAPIError("A gxapi_cy.WrapPGeo instance has not been instantiated on current thread yet.");
    return <void*><size_t>tls_geo






cdef class Wrap3DN:
    


    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            Destroy_3DN(get_p_geo(), &self.handle)





    def copy(self, p2):
        cdef int32_t cp2

        try:


            cp2 = p2

            Copy_3DN(get_p_geo(), &self.handle, &cp2)
            
        finally:
            pass

    @classmethod
    def create(cls):

        try:



            _return_val = Wrap3DN(Create_3DN(get_p_geo()))
            return _return_val
        finally:
            pass




    def get_point_of_view(self, p2, p3, p4):
        cdef double cp2
        cdef double cp3
        cdef double cp4

        try:


            cp2 = p2
            cp3 = p3
            cp4 = p4

            GetPointOfView_3DN(get_p_geo(), &self.handle, &cp2, &cp3, &cp4)
            return (cp2, cp3, cp4)
        finally:
            pass


    def get_scale(self, p2, p3, p4):
        cdef double cp2
        cdef double cp3
        cdef double cp4

        try:


            cp2 = p2
            cp3 = p3
            cp4 = p4

            GetScale_3DN(get_p_geo(), &self.handle, &cp2, &cp3, &cp4)
            return (cp2, cp3, cp4)
        finally:
            pass


    def get_axis_color(self):

        try:



            _return_val = iGetAxisColor_3DN(get_p_geo(), &self.handle)
            return _return_val
        finally:
            pass


    def get_axis_font(self, p2):
        cdef char* cp2 = NULL
        cdef int32_t cp3

        try:
            cencp2 = (<unicode>p2).encode('utf8')

            cp2 = <char*>malloc(4*1024)

            strcpy(cp2, cencp2)
            cp3 = 4*1024

            IGetAxisFont_3DN(get_p_geo(), &self.handle, cp2, &cp3)
            return cp2
        finally:
            if cp2: free(cp2)



    def get_background_color(self):

        try:



            _return_val = iGetBackgroundColor_3DN(get_p_geo(), &self.handle)
            return _return_val
        finally:
            pass


    def get_render_controls(self, p2, p3, p4, p6, p8):
        cdef int32_t cp2
        cdef int32_t cp3
        cdef char* cp4 = NULL
        cdef int32_t cp5
        cdef char* cp6 = NULL
        cdef int32_t cp7
        cdef char* cp8 = NULL
        cdef int32_t cp9

        try:
            cencp4 = (<unicode>p4).encode('utf8')
            cencp6 = (<unicode>p6).encode('utf8')
            cencp8 = (<unicode>p8).encode('utf8')

            cp4 = <char*>malloc(4*1024)
            cp6 = <char*>malloc(4*1024)
            cp8 = <char*>malloc(4*1024)

            cp2 = p2
            cp3 = p3
            strcpy(cp4, cencp4)
            cp5 = 4*1024
            strcpy(cp6, cencp6)
            cp7 = 4*1024
            strcpy(cp8, cencp8)
            cp9 = 4*1024

            IGetRenderControls_3DN(get_p_geo(), &self.handle, &cp2, &cp3, cp4, &cp5, cp6, &cp7, cp8, &cp9)
            return (cp2, cp3, cp4, cp6, cp8)
        finally:
            if cp4: free(cp4)
            if cp6: free(cp6)
            if cp8: free(cp8)



    def get_shading(self):

        try:



            _return_val = iGetShading_3DN(get_p_geo(), &self.handle)
            return _return_val
        finally:
            pass


    def set_axis_color(self, p2):
        cdef int32_t cp2

        try:


            cp2 = p2

            SetAxisColor_3DN(get_p_geo(), &self.handle, &cp2)
            
        finally:
            pass


    def set_axis_font(self, p2):
        

        try:
            cencp2 = (<unicode>p2).encode('utf8')


            cp2 = cencp2

            SetAxisFont_3DN(get_p_geo(), &self.handle, cp2)
            
        finally:
            pass


    def set_background_color(self, p2):
        cdef int32_t cp2

        try:


            cp2 = p2

            SetBackgroundColor_3DN(get_p_geo(), &self.handle, &cp2)
            
        finally:
            pass


    def set_point_of_view(self, p2, p3, p4):
        cdef double cp2
        cdef double cp3
        cdef double cp4

        try:


            cp2 = p2
            cp3 = p3
            cp4 = p4

            SetPointOfView_3DN(get_p_geo(), &self.handle, &cp2, &cp3, &cp4)
            
        finally:
            pass


    def set_render_controls(self, p2, p3, p4, p5, p6):
        cdef int32_t cp2
        cdef int32_t cp3
        
        
        

        try:
            cencp4 = (<unicode>p4).encode('utf8')
            cencp5 = (<unicode>p5).encode('utf8')
            cencp6 = (<unicode>p6).encode('utf8')


            cp2 = p2
            cp3 = p3
            cp4 = cencp4
            cp5 = cencp5
            cp6 = cencp6

            SetRenderControls_3DN(get_p_geo(), &self.handle, &cp2, &cp3, cp4, cp5, cp6)
            
        finally:
            pass


    def set_scale(self, p2, p3, p4):
        cdef double cp2
        cdef double cp3
        cdef double cp4

        try:


            cp2 = p2
            cp3 = p3
            cp4 = p4

            SetScale_3DN(get_p_geo(), &self.handle, &cp2, &cp3, &cp4)
            
        finally:
            pass


    def set_shading(self, p2):
        cdef int32_t cp2

        try:


            cp2 = p2

            SetShading_3DN(get_p_geo(), &self.handle, &cp2)
            
        finally:
            pass

    pass

