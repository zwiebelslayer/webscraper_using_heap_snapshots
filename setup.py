"""
Install libaray
This will call the other setup.py file which then builds the c into a python lib
"""

from distutils.core import setup
import subprocess


#TODO: Support pip install by implementing this file :)
setup(name='webscraper_heap_snapshot',
      version='0.0.1',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='',
      url='',
      packages=['distutils', 'distutils.command', 'playwright'],
     )