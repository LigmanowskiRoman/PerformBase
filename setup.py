from __future__ import print_function
from setuptools import setup, find_packages
import codecs
import os
import re


here = os.path.abspath(os.path.dirname(__file__))
def read(file_paths, default=""):
    # intentionally *not* adding an encoding option to open
    try:
        return codecs.open(os.path.join(here, *file_paths), 'r').read()
    except:
        return default

def find_version(file_paths):
    version_file = read(file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

description='Reusable Base Test Case Module',
long_description=read('README.md', default=description)

setup(
    name='performbase',
    version=find_version(['performbase', '__init__.py']),
    url='https://stash.performgroup.com/projects/QA/repos/performbase/browse',
    author='PERFORM',
    license='Proprietary',
    keywords='selenium testing development',
    packages=find_packages(),
    install_requires=['selenium>=2.46.0', 'elementium>=1.1.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: Proprietary',
        'Programming Language :: Python :: 2.7',
        ],
)
