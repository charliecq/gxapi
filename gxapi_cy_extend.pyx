#cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8

from cython.view cimport array

from libc.stdint cimport uintptr_t, int32_t, int16_t
from libc.stdlib cimport malloc, free

cdef extern int32_t iCheckError_SYS(void*)
cdef extern int32_t iCheckTerminate_SYS(void*, int32_t* p1);
cdef extern int16_t sGetError_GEO(void*, char*, int32_t, char*, int32_t, int32_t*);

from geosoft.gxapi import GXCancel, GXExit, GXAPIError, GXError

cdef void callback_free_data(void *p):
    print("In callback_free_data")
    free(p)

cdef _raise_on_gx_errors(void* p_geo):
    cdef int32_t term
    cdef char* module
    cdef char* err
    cdef int32_t error_number
    cdef int32_t check_err
    if iCheckTerminate_SYS(p_geo, &term) > 0:
        check_err = iCheckError_SYS(p_geo)
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
                    raise GXAPIError(err);
                else:
                    raise GXError(err, module, error_number)
            finally:
                if module != NULL:
                    free(module)
                if err != NULL:
                    free(err)


cdef extern int32_t iGetData_VV(void*, const int32_t* p1, int32_t p2, int32_t p3, void* p4, int32_t p5);


cdef class WrapVVExtra:
    @classmethod
    def get_data_array_vv(cls, uintptr_t p_geo, int32_t vv_handle, int32_t p2, int32_t p3, int32_t p5):
        """
        Type code	C Type	Python Type	Minimum size in bytes	Notes
        'b'	signed char	int	1	 
        'B'	unsigned char	int	1	 
        'u'	Py_UNICODE	Unicode character	2	(1)
        'h'	signed short	int	2	 
        'H'	unsigned short	int	2	 
        'i'	signed int	int	2	 
        'I'	unsigned int	int	2	 
        'l'	signed long	int	4	 
        'L'	unsigned long	int	4	 
        'q'	signed long long	int	8	(2)
        'Q'	unsigned long long	int	8	(2)
        'f'	float	float	4	 
        'd'	double	float	8	 
        Notes:
        """
    
        cdef void* ap4 = NULL
        cdef array arrp4
        cdef size_t itemsize
        try:
            itemsize=sizeof(double)
            ap4 = malloc(p3*itemsize)
            arrp4 = array(shape=(p3,), itemsize=itemsize, format="d", mode="c", allocate_buffer=False)
            arrp4.data = <char*>ap4
            arrp4.callback_free_data = callback_free_data
            ap4 = NULL
            _return_val = iGetData_VV(<void*>p_geo, &vv_handle, p2, 5, <void*>arrp4.data, p5)
            _raise_on_gx_errors(<void*>p_geo)
            return (_return_val, arrp4)
        finally:
            if (ap4): free(ap4)

        



