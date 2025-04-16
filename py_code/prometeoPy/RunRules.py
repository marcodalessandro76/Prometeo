"""
This module manages the parameters used to define the OMP parellelization strategy.
"""
import os


class RunRules(dict):
    """
    Defines and manage a dictionary with all the parameters needed to set up the rules
    for parallel computing.

    Parameters:
        scheduler (:py:class:`string`) : choose the scheduler used to submit the job
        omp_num_threads (:py:class:`int`) : used to set the value of the environment variable OMP_NUM_THREADS

    """

    def __init__(self,scheduler='direct',omp_num_threads=os.environ.get('OMP_NUM_THREADS', 1)):
        if scheduler == 'direct':
            rules = dict(omp_num_threads=omp_num_threads)
            dict.__init__(self,scheduler=scheduler,**rules)
        if scheduler == 'slurm':
            print('Slurm scheduler yet to be implemented')

    
