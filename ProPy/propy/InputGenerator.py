
"""
This module creates and manages the input file used by the main program.
The input can be created from scratch or can be initialized from an existing input file.
"""
import os
from copy import deepcopy
from propy import Utilities as U

# Define the default input dictionary and the associated one with the comments for each key
default = {
    'iteration': 1000,
    'io_step': 100,      
}
comments = {
    'iteration': 'Number of iterations of the simulation',
    'io_step': 'Number of iterations between two I/O operations',      
}
# Define the header of the input file
branch,commit = U.get_git_info()
header =  f"""Input file for the main program
Branch: '{branch}'
Commit: '{commit}'

"""
class InputGenerator(dict):
    """
    Class to generate an manipulate the input file used by the main program.
    The input can be created from scratch or can be initialized from an existing input file.
    
    Attributes:
        default (:py:class:`dict`): default input dictionary
        comments (:py:class:`dict`): dictionary with the comments for each key in the input dictionary
    
    Args:
        filename (:py:class:`string`) : name of an exsistent input file, used to
            initialize the dictionaries of the object
        **kwargs : keyword arguments used to initialize the keys of the object

    Methods:
        parseInputFile : Build the input dictionary from a YAML file.
        write : Write the input object to a YAML file, preserving comments.     
    """

    def __init__(self,filename=None,**kwargs):
        """
        Initialize the default keys and values. 
        Default can be updated the dictionaries with the kwargs passed as input parameters.
        If an input file is provided it is parsed and the dictionary is updated.

        Args:
            filename (:py:class:`string`) : name of an exsistent input file, used to
                initialize the dictionaries of the object
            **kwargs : keyword arguments used to initialize the keys of the
                object

        """
        dict.__init__(self)

        self.update(deepcopy(default))

        if filename is not None:
            self.parseInputFile(filename)
        self.update(kwargs)


    def parseInputFile(self,filename):
        """
        Build the input dictionary from a YAML file.

        Args:
            filename (:py:class:`string`) : name of an exsistent input file, used
                initialize the dictionaries of the object

        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Input file '{filename}' not found")
        self.update(U.parse_yaml_file(filename))


    def write(self, filename,column=30,verbose=True):
        """
        Write the input object to a YAML file, preserving comments.

        Args:
            filename (:py:class:`string`): name of the file including the path
            column (:py:class:`int`): column where the comments start
            verbose (:py:class:`bool`): if True, print a message to the standard output
        """
        yaml_data = U.create_commented_yaml(self,comments,header=header,column=column)  
        U.dict_to_yaml_dump(yaml_data,filename,verbose=verbose)


   