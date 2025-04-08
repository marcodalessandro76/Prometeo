
from setuptools import setup, find_packages
from os import path

# Package meta-data.
NAME = 'prometeoPy'
DESCRIPTION = 'Python Interface for the Prometero template project'
URL = 'https://github.com/marcodalessandro76/Prometeo'
EMAIL = 'marco.dalessandro@ism.cnr.it'
AUTHOR = "Marco D'Alessandro"
REQUIRES_PYTHON = '>=3.6'
VERSION = '1.0'
REQUIRED = ['numpy','matplotlib','ruamel.yaml','nbsphinx'] #,'scipy','nbsphinx','netCDF4'
#-----------------------------------------------

here = path.abspath(path.dirname(__file__))

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    keywords='python system-interface post-processing',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED
)
