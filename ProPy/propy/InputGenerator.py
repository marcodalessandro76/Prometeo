
"""
This module creates and manages the input file used by the main program.
The input can be created from scratch or can be initialized from an existing input file.
"""
import os
from copy import deepcopy
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap
from propy import Utilities as U

# Define the default input dictionary and the corresponding yaml object with the
# comments for each key  
default = {
    'iteration': 1000,
    'io_step': 100,      
}

yaml = YAML()  
yaml.preserve_quotes = True

def create_commented_yaml(data):
    """
    Convert a dictionary into a CommentedMap and add comments.
    """
    yaml_data = CommentedMap()
    
    for key, value in data.items():
        yaml_data[key] = value
    
    # Aggiunta dei commenti
    yaml_data.yaml_set_comment_before_after_key('iteration', inline='Number of iterations of the simulation')
    yaml_data.yaml_set_comment_before_after_key('io_step', inline='Number of iterations between two I/O operations')
    
    return yaml_data

class InputGenerator(dict):
    """
    Class to generate an manipulate the input file used by the main program.

    """

    def __init__(self,file=None,**kwargs):
        """
        Initialize the default keys and values. 
        Default can be updated the dictionaries with the kwargs passed as input parameters.
        If an input file is provided it is parsed and the 'file' key is added to the object dictionary.

        Args:
            file (:py:class:`string`) : name of an exsistent input file, used to
                initialize the dictionaries of the object
            **kwargs : keyword arguments used to initialize the keys of the
                object

        """
        dict.__init__(self)

        self.update(deepcopy(default))

        if file is not None:
            self['file'] = file
            self.parseInputFile(file)
        self.update(kwargs)


    # def parseInputFile(self,file):
    #     """
    #     Read the arguments and variables from the input file.
    #     All the elements that belong to the possible namelist of pw are parsed.
    #     Instead, among the possible pw cards the actual implementation considers
    #     only : ATOMIC_SPECIES, ATOMIC_POSITIONS, K_POINTS, CELL_PARAMETERS

    #     Args:
    #         file (:py:class:`string`) : name of an exsistent input file, used
    #             initialize the dictionaries of the object

    #     """
        
    def write(self, file):
        """
        Write the input object to a YAML file, preserving comments.

        Args:
            file (:py:class:`string`): name of the file including the path
        """
        yaml_data = create_commented_yaml(self)  # Ensure comments are added
        print(yaml_data)
        with open(file, "w", encoding="utf-8") as f:
            yaml.dump(yaml_data, f)
        print(f"File YAML '{file}' scritto con commenti!")



   