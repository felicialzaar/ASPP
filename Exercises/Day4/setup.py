from setuptools import Extension
from distutils.core	import setup
from Cython.Build import cythonize
import numpy

#extensions = [
#    Extension("fastloop", ["fastloop.pyx"],
#        include_dirs=[numpy.get_include()],
#        define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION'), ('CYTHON_TRACE', '1')],
#        ),
#    #Extension("*", ["*.pyx"])
#]

setup(
	ext_modules	= cythonize(["fastloop.pyx"]), #, compiler_directives={'linetrace': True}),
    include_dirs=[numpy.get_include()],
)
