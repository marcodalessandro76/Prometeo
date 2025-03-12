"""
This module contains some low-level functions.
"""

from ruamel.yaml import YAML
import numpy as np
import os

def dict_to_yaml_dump(dict, filename):
    """
    Write a dictionary to a yaml file.

    Args:
        dict (:py:class:`dict`): dictionary to be written
        filename (:py:class:`string`): name of the file
    """
    yaml = YAML()
    with open(filename, 'w') as f:
        yaml.dump(dict, f)

def parse_yaml_file(filename):
    """
    Read a yaml file and return the dictionary.

    Args:
        filename (:py:class:`string`): name of the file

    Return:
        :py:class:`dict` : dictionary with the content of the file
    """
    with open(filename, 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)

