from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages, Extension
import numpy as np

ext_modules = []

setup(
    name = "chemlab",
    version = "0.4.1",
    packages = find_packages(),
    ext_modules = ext_modules,
    include_dirs = [np.get_include()],
    package_data = {'': ['distribute_setup.py', '*.rst', '*.txt'],
                    'chemlab.graphics.renderers.shaders': ['*.vert', '*.frag'],
                    'chemlab.graphics.postprocessing.shaders': ['*.vert', '*.frag'],
                    'chemlab.resources' : ["*"],
                    'chemlab.db.localdb.data' : ['*'],
                    'chemlab.db.localdb.molecule' : ['*'],
                    'chemlab.core.spacegroup': ['*']},
    
    author = "Gabriele Lanaro",
    scripts = ['scripts/chemlab'],
    zip_safe = False,
    
    
    author_email = "gabriele.lanaro@gmail.com",
    description = "The python chemistry library you were waiting for",
    long_description = '''
    chemlab is a python library and a set of utilities built to ease the
    life of the computational chemist. It takes inspiration from other
    python scientific library such as numpy scipy and matplotlib, and aims
    to bring a consistent and simple API by following the python
    guidelines.

    Computational and theoretical chemistry is a huge
    field, and providing a program that encompasses all aspects of it is an
    impossible task. The spirit of chemlab is to provide a common ground
    from where you can build specific programs. For this reason it
    includes an easily extendable molecular viewer and flexible data
    structures field-independent.
    ''',
    classifiers = ['Intended Audience :: Science/Research',
                   'Topic :: Scientific/Engineering :: Chemistry',
                   'Topic :: Scientific/Engineering :: Visualization',
                   'Topic :: Scientific/Engineering :: Physics',
                   'Topic :: Multimedia :: Graphics :: Viewers',
                   'Programming Language :: Python :: 2.7'],
    license = "LGPL if parts using PyQt (chemlab.graphics and chemlab.mviewer packages), GPL3 if the PyQt parts are included.",
    keywords = "chemistry molecular_viewer",
    url = "https://chemlab.github.com/chemlab"
)
