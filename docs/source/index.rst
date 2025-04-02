.. Prometeo documentation master file, created by
   sphinx-quickstart on Mon Mar 31 13:09:30 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Prometeo's documentation!
====================================

Prometeo is a template project. The aim of its development is to built a C++ based program with a native python interface. 
As an example the project implements the coding of a simple MonteCarlo simulation for the computation of pi.
Input, logs and report files are written in Yaml.

Installation of the C++ code
----------------------------

To install the c++ code you need to have a working installation of cmake and a C++ compiler with the OMP and Yaml support.
The package is designed to be installed in a local folder, e.g. /home/username/Applications/Prometeo/prometeoMain.
The installation is done using the standard cmake tools. For instance, from the folder where you cloned the repository,
you can run the following commands:

    mkdir build && cd build

    cmake ..

    cmake -build .
    

Installation of the python interface
------------------------------------

The python interface of the package is the main tool to interact with the code.
To install the package you can clone this repository in a local folder, e.g. /home/username/Applications/Prometeo/PrometeoPy
and install the package using the standard python tools. For instance using the pip tools,

    pip3 install -e .

Note that the _editable_ -e option creates a link from the location of the package to local python repository folder.
In this way you do not need to recompile the package if you make some modifications, useful for coding.

Build of the documentation
--------------------------

The C++ documentation is built using the Doxygen tools. To build the documentation you need to have a working installation of Doxygen.
To build the documentation move to the folder /home/username/Applications/Prometeo/PrometeoMain and use the following command:

    doxygen Doxyfile


The Python documentation is built using the Sphinx tools. To build the documentation you need to have a working installation of Sphinx.
To build the documentation move to the folder /home/username/Applications/Prometeo/PrometeoPy/docs and use the following command:

    make html

The breathe plugin is used to integrate the C++ documentation in the Sphinx documentation. 

.. toctree::
    :maxdepth: 2
    :caption: Contents:


PrometeoPy documentation
------------------------

The classes of the PrometeoPy module are

.. toctree:: inputGenerator

PrometeoMain C++ documentation
------------------------------

.. doxygenfunction:: Simulation::Simulation 



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
