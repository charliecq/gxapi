from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import Cython.Compiler.Options

setup(
    ext_modules=cythonize(
        [Extension(
            "gxapi_cy", 
            ['gxapi_cy.pyx'], 
            libraries=['geogx_utf8', 'geodist'],
            library_dirs=['../gxdeveloper/lib'],
            include_dirs = ['../gxdeveloper/include'],
            extra_compile_args=["/GF"]
         ),
         Extension(
            "gxapi_cy_extend", 
            ['gxapi_cy_extend.pyx'], 
            libraries=['geogx_utf8', 'geodist'],
            library_dirs=['../gxdeveloper/lib'],
            include_dirs = ['../gxdeveloper/include'],
            extra_compile_args=["/GF"]
         )])
)