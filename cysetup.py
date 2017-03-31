from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([Extension("gxapi_cy", ['gxapi_cy.pyx'], libraries=["geoengine.core.gx_utf8", "geodist"])])
)