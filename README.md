# Prometeo
Prometeo is a template project. The aim of its development is to built a C++ based program with a native python interface. 
As an example the project implements the coding of a simple MonteCarlo simulation for the computation of pi.
Input, logs and report files are written in Yaml.

## Installation of the C++ code
To install the c++ code you need to have a working installation of cmake and a C++ compiler with the OMP and Yaml support.
The package is designed to be installed in a local folder, e.g. /home/username/Applications/Prometeo/cxx_code.
The installation is done using the standard cmake tools. For instance, from the folder where you cloned the repository,
you can run the following commands:

    mkdir build && cd build

    cmake ..

    cmake -build .

## Installation of the python interface 
The python interface of the package is the main tool to interact with the code.
To install the package you can clone this repository in a local folder, e.g. /home/username/Applications/Prometeo/py_code
and install the package using the standard python tools. For instance using the pip tools,

    pip3 install -e .

Note that the _editable_ -e option creates a link from the location of the package to local python repository folder.
In this way you do not need to recompile the package if you make some modifications, useful for coding.

## Usage of the code
The package is mainly designed to be managed using its python interface inside a jupyter notebook but it can also be extecuted from the command line. First set the OMP_NUM_THREADS environment variable to the number of threads you want to use. Then you can run the code using the following command:

    ./program_name -i input.yaml -r run_options.yaml

where input.yaml is the input file, that contains the parameters of the simulation, and run_options.yaml wich is a file that 
contains information about the run, such as the name of folder where the output files are written. 


## Build of the documentation
The C++ documentation is built using the Doxygen tools. To build the documentation you need to have a working installation of Doxygen. To build the documentation move to the folder /home/username/Applications/Prometeo/cxx_code and use the following command:

    doxygen Doxyfile


The Python documentation is built using the Sphinx tools. To build the documentation you need to have a working installation of Sphinx. To build the documentation move to the folder /home/username/Applications/Prometeo/docs and use the following command:

    make html

The breathe plugin is used to integrate the C++ documentation in the Sphinx documentation. 

## Tutorial and examples
We provide many jupyter notebooks that explain the usage of the code.

## Authors
- [Marco D'Alessandro](https://github.com/marcodalessandro76/)

The code is at an early stage of development, help us by sending bug reports and suggestions!

