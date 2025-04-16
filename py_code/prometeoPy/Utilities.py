"""
This module contains some low-level functions.
"""

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap
import numpy as np
import os
import subprocess

def dict_to_yaml_dump(dict, filename,verbose=True):
    """
    Write a dictionary to a yaml file.

    Args:
        dict (:py:class:`dict`): dictionary to be written. Also works with CommentedMap
        filename (:py:class:`string`): name of the file
        verbose (:py:class:`bool`): if True, print a message to the standard output
    """
    yaml = YAML()
    yaml.preserve_quotes = True # Preserve quotes in the output
    with open(filename, 'w') as f:
        yaml.dump(dict, f)
    if verbose : print(f"File YAML '{filename}' written on disk")

def parse_yaml_file(filename):
    """
    Read a yaml file and return the dictionary.

    Args:
        filename (:py:class:`string`): name of the file

    Return:
        :py:class:`dict` : dictionary with the content of the file
    """
    yaml = YAML()  
    with open(filename, 'r') as f:
        return yaml.load(f)

def create_commented_yaml(data,comments,header=None,column=30):
    """
    Convert a dictionary into a CommentedMap and add comments.
    The comments start at the same column for each key. 
    Args:
        data (:py:class:`dict`): dictionary to be converted
        comments (:py:class:`dict`): dictionary with the comments for each key
        column (:py:class:`int`): column where the comments start
    Return:
        :py:class:`ruamel.yaml.comments.CommentedMap` : dictionary with the content of
            the input dictionary and the comments for each key
    """
    yaml_data = CommentedMap()
    
    if header:
        yaml_data.yaml_set_start_comment(header)
    for key, value in data.items():
        yaml_data[key] = value
        if key in comments:
            yaml_data.yaml_add_eol_comment(comments[key], key,column=column)

    return yaml_data

def get_git_info():
    """Obtain the current branch and commit hash of the git repository."""
    try:
        branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')
        commit = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')
        return branch, commit
    except subprocess.CalledProcessError:
        return None, None

def build_folder_path(dir, label = 'Directory', verbose = True):     
    """
    Create a folder path if it does not exist. 

    Args:
        dir (:py:class:`string`): folder path to be created
        label (:py:class:`string`): label of the folder
        verbose (:py:class:`bool`): if True, print a message to the standard output
    """

    if not os.path.exists(dir):
        os.makedirs(dir)
        if verbose: print('create the %s folder : %s' %(label,dir))
    else:
        if verbose: print('The %s folder %s already exists' %(label,dir))  

def dict_merge(dest, src):
    """
    Recursive dict merge. Inspired by :meth:`dict.update`, instead of
    updating only top-level keys, dict_merge recurses down into dicts nested
    to an arbitrary depth, updating keys. The ``src`` is merged into
    ``dest``.  From :ref:`angstwad/dict-merge.py`

    Args:   
       dest (dict): dict onto which the merge is executed
       src (dict): dict merged into dest

    """
    import collections
    for k, v in src.items():
        if (k in dest and isinstance(dest[k], dict)
                and isinstance(src[k], collections.Mapping)):
            dict_merge(dest[k], src[k])
        else:
            dest[k] = src[k]

    


