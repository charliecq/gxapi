from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import Cython.Compiler.Options

compile_args = ["/GF", "/Gy"]
link_args = ["/OPT:ICF", "/OPT:REF"]

setup(
    ext_modules=cythonize(
        [Extension(
            "gxapi_cy", 
            ['gxapi_cy.pyx'], 
            libraries=['geogx_utf8', 'geodist'],
            library_dirs=['../gxdeveloper/lib'],
            include_dirs = ['../gxdeveloper/include'],
            extra_compile_args=compile_args,
            extra_link_args=link_args
         ),
         Extension(
            "gxapi_cy_extend", 
            ['gxapi_cy_extend.pyx'], 
            libraries=['geogx_utf8', 'geodist'],
            library_dirs=['../gxdeveloper/lib'],
            include_dirs = ['../gxdeveloper/include'],
            extra_compile_args=compile_args,
            extra_link_args=link_args
         )])
)