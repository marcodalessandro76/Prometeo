
"""
This module creates and manages the run_options file used by the main program to define the run options such as the run directory.
The module could for instance implement a method that scan a list of folder and seek for results of previous runs, like netdcdf files, 
and check if the some parts of run can be skipped.
The instance of the class is not thought to be used directly, but instead it is used by the Calculator class.
"""

from copy import deepcopy
from prometeoPy import Utilities as U
default = {
     
}
comments = {
    'run_dir': 'Folder in which the simulation is performed'
}
header =  f"""Run options for the main program
"""

class RunOptions(dict):
    """
    Class to generate the `run_options` file used by the main program to define the run options such as the run directory.
    
    
    Args:
        **kwargs : keyword arguments used to initialize the keys of the object

    Methods:
        write : Write the runOptions object to a YAML file.     
    """

    def __init__(self,**kwargs):
        """
        Initialize the default keys and values. 

        Args:
            **kwargs : keyword arguments used to initialize the keys of the object

        """
        dict.__init__(self)
        #self.update(deepcopy(default))
        self.update(kwargs)


    def write(self, filename,column=30,verbose=True):
        """
        Write the runOptions object to a YAML file, preserving comments.

        Args:
            filename (:py:class:`string`): name of the file including the path
            column (:py:class:`int`): column where the comments start
            verbose (:py:class:`bool`): if True, print a message to the standard output
        """
        yaml_data = U.create_commented_yaml(self,comments,header=header,column=column)  
        U.dict_to_yaml_dump(yaml_data,filename,verbose=verbose)
