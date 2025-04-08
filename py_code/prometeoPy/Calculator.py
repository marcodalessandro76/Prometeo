"""
This module manages the execution of a calculation. The run of the computation is performed by the python 
subprocess package (direct scheduler) or by an external scheduler like slurm (to be implemented).
"""

from .Runner import Runner
import os

class Calculator(Runner):
    """
    Perform a calculation. The parameters used to define the parellelization strategy are provided in the `runRules` object.

    Parameters:
       runRulues (:class:`RunRules`) : instance of the :class:`RunRules` class
       skip (:py:class:`bool`) : if True evaluate if the computation can be skipped. This is done by checking if the log
            file of the run contains the string `job_done`, defined as a data member of this class (to be implemented).
       dry_run (:py:class:`bool`) : with this option enabled the calculator setup the calculations and write the script
            for submitting the job, but the computations are not run
       verbose (:py:class:`bool`) : set the amount of information provided on terminal
       kwargs : other parameters that are stored in the _global_options dictionary

    Computations are performed in the folder specified by the ``run_dir`` parameter. The input and
    the log files are written in the run_dir. Instead, the $prefix.xml file and the $prefix.save
    folders are written in the ``out_dir`` path. The values of the prefix and out_dir variables
    are read from the input file. If the ``out_dir`` path is a relative path its root is located
    in the ``run_dir`` folder.

    Example:
     >>> rr = RunRules(scheduler='direct',omp_num_threads=4,memory='124GB')
     >>> code = calculator(rr,skip=True,verbose=True)
     >>> code.run(input = ..., run_dir = ...,name = ..., source_dir = ..., **kwargs)

     When the run method is called the class runs the command:
         cd run_dir ; `mpirun command` executable_name -inp name.in > name.log

     where the arguments of the run method are:

    Args:
        run_dir (:py:class:`string`) : the folder in which the simulation is performed
        input (:py:class:`string`) : instance of the :class:`InputGenerator` class
            that define the input object
        name (:py:class:`string`) : string with the name associated to the input file xxxxxxxx
        source_dir (:py:class:`string`) : xxxxxxxxxxxxxxxxxxxxx
        kwargs : other parameters that are stored in the run_options dictionary

    """

    def __init__(self, runRules, skip =  True, dry_run = False, verbose = True, **kwargs):
        # Use the initialization from the Runner class (all options inside _global_options)
        Runner.__init__(self,**runRules,skip=skip,dry_run=dry_run,verbose=verbose,**kwargs)
        print('Initialize a calculator with scheduler %s' %self._global_options['scheduler'])