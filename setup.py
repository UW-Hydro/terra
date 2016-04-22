#! /usr/bin/env python
#
# Copyright (C) 2012-2014 Michael Waskom <mwaskom@stanford.edu>
import os
# temporarily redirect config directory to prevent matplotlib importing
# testing that for writeable directory which results in sandbox error in
# certain easy_install versions
os.environ["MPLCONFIGDIR"] = "."

DESCRIPTION = "terra: geospatial data visualization"
LONG_DESCRIPTION = """\
terra is a library for making attractive and informative geospatial graphics
in Python. It is built on top of seaborn and matplotlib, and tightly integrated
with the PyData stack, including support for numpy, pandas, and xarray data
structures and statistical routines from scipy and statsmodels.
"""

DISTNAME = 'terra'
MAINTAINER = 'Joe Hamman'
MAINTAINER_EMAIL = 'jhamman1@uw.edu'
URL = 'unknown'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/jhamman/terra/'
VERSION = '0.0.0'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup


def check_dependencies():
    install_requires = []

    # Just make sure dependencies exist, I haven't rigorously
    # tested what the minimal versions that will work are
    # (help on that would be awesome)
    try:
        import numpy
    except ImportError:
        install_requires.append('numpy')
    try:
        import scipy
    except ImportError:
        install_requires.append('scipy')
    try:
        import matplotlib
    except ImportError:
        install_requires.append('matplotlib')
    try:
        import pandas
    except ImportError:
        install_requires.append('pandas')
    try:
        import xarray
    except ImportError:
        install_requires.append('xarray')
    try:
        import cartopy
    except ImportError:
        install_requires.append('cartopy')

    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          packages=['terra', 'terra.tests'],
          classifiers=['Intended Audience :: Science/Research',
                       'Programming Language :: Python :: 2.7',
                       'Programming Language :: Python :: 3.4',
                       'Programming Language :: Python :: 3.5',
                       'License :: OSI Approved :: BSD License',
                       'Topic :: Scientific/Engineering :: Visualization',
                       'Topic :: Multimedia :: Graphics',
                       'Operating System :: POSIX',
                       'Operating System :: Unix',
                       'Operating System :: MacOS'])
