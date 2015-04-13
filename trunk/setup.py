# -*- coding: latin-1 -*-
"""
Notes:

- use setup.py develop when tracking in-development code
- when removing modules or data files from the project, run setup.py clean --all and delete any obsolete .pyc or .pyo.

"""

"""
    Information about this versioned file:
        $LastChangedBy$
        $LastChangedDate$
        $LastChangedRevision$
        $URL$
        $Id$
"""

import ez_setup
ez_setup.use_setuptools()

import sys
from setuptools import setup, find_packages

import respiwheat

if sys.version_info < (2, 7):
    print('ERROR: Respi-Wheat requires at least Python 2.7 to run.')
    sys.exit(1)

if sys.version_info >= (3, 0):
    print('WARNING: Respi-Wheat has not been tested with Python 3.')

setup(
    name = "Respi-Wheat",
    version=respiwheat.__version__,
    packages = find_packages(),

    include_package_data = True,

    # metadata for upload to PyPI
    author = "C.Chambon, R.Barillot",
    author_email = "camille.chambon@grignon.inra.fr, romain.barillot@grignon.inra.fr",
    description = "Model of respiration adapted to wheat ",
    long_description = "Modèle de respiration associée aux principales fonctions physiologiques végétales. Inspiré des travaux de Cannell et Thornley (2000).",
    license = "", # TODO
    keywords = "", # TODO
    url = "https://sourcesup.renater.fr/projects/respi-wheat/",
    download_url = "", # TODO
)
