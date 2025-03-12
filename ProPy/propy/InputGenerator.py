
"""
This module creates and manages the input file used by the main program.
The input can be created from scratch or can be initialized from an existing input file.
"""
import os
from copy import deepcopy
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap
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

yaml = YAML()  
yaml.preserve_quotes = True

def create_commented_yaml(data):
    """
    Convert a dictionary into a CommentedMap and add comments.
    The comments start at the same column for each key. 
    """
    yaml_data = CommentedMap()
    
    for key, value in data.items():
        yaml_data[key] = value
        if key in comments:
            yaml_data.yaml_add_eol_comment(comments[key], key,column=30)

    return yaml_data

class InputGenerator(dict):
    """
    Class to generate an manipulate the input file used by the main program.

    """

    def __init__(self,filename=None,**kwargs):
        """
        Initialize the default keys and values. 
        Default can be updated the dictionaries with the kwargs passed as input parameters.
        If an input file is provided it is parsed and the 'file' key is added to the object dictionary.

        Args:
            filename (:py:class:`string`) : name of an exsistent input file, used to
                initialize the dictionaries of the object
            **kwargs : keyword arguments used to initialize the keys of the
                object

        """
        dict.__init__(self)

        self.update(deepcopy(default))

        if filename is not None:
            self['filename'] = filename
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

    def write(self, filename,verbose=True):
        """
        Write the input object to a YAML file, preserving comments.

        Args:
            filename (:py:class:`string`): name of the file including the path
            verbose (:py:class:`bool`): if True, print a message to the standard output
        """
        yaml_data = create_commented_yaml(self)  # Ensure comments are added
        with open(filename, "w", encoding="utf-8") as f:
            yaml.dump(yaml_data, f)
        if verbose : print(f"File YAML '{filename}' written on disk")



   