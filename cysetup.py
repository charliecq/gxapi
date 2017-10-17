from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        [Extension(
            "gxapi_cy", 
            ['gxapi_cy.pyx'], 
            libraries=['geogx_utf8', 'geodist'],
            library_dirs=['../gxdeveloper/lib'],
            extra_compile_args=["/GF"]
         )])
)