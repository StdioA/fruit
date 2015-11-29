# coding: utf-8

from distutils.core import setup
import py2exe
import sys
 
#this allows to run it with a simple double click.
sys.argv.append('py2exe')
 
py2exe_options = {
        "includes": ["sip", 'zmq.backend.cython'],
        "dll_excludes": [
            "MSVCP90.dll", 
            'libzmq.pyd',
        ],
        'excludes': ['zmq.libzmq'],
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        "bundle_files": 1,
        }
 
setup(
      name = 'PyQt Demo',
      version = '1.0',
      windows = ['recDemo.py',], 
      zipfile = None,
      options = {'py2exe': py2exe_options},
      data_files=[
        (".", ["data3.dat"]),
        # ('lib', (zmq.libzmq.__file__,))
    ]
)
