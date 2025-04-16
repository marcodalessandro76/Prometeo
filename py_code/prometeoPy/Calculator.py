"""
This module manages the execution of a calculation. The run of the computation is performed by the python 
subprocess package (direct scheduler) or by an external scheduler like slurm (to be implemented).
"""

from .Runner import Runner
from .RunOptions import RunOptions
from prometeoPy import Utilities as U  
import os

class Calculator(Runner):
    """
    Perform a calculation. The parameters used to define the parellelization strategy are provided in the `runRules` object.

    Parameters:
        runRulues (:class:`RunRules`) : instance of the :class:`RunRules` class.

        skip (:py:class:`bool`) : if True evaluate if the computation can be skipped. This is done by checking if the log 
        file of the run contains the string `job_done`, defined as a data member of this class (to be implemented).

        dry_run (:py:class:`bool`) : with this option enabled the calculator setup the calculations and write the script 
        for submitting the job, but the computations are not run  (to be implemented).

        verbose (:py:class:`bool`) : set the amount of information provided on terminal.

        kwargs : other parameters that are stored in the _global_options dictionary.

    Computations are performed in the folder specified by the ``run_dir`` parameter provided in the call of the 
    :meth:`run`. The class creates the run directory if it does not exist and write the `input` and the `run_options` 
    files in the run directory. The input file is created by the :class:`InputGenerator` class while the run_options file 
    is written directly by the :class:`Calculator`.

    Example:
     >>> rr = RunRules(scheduler='direct',omp_num_threads=4)
     >>> code = calculator(rr,skip=True,verbose=True)
     >>> code.run(input = ..., run_dir = ...,name = ..., **kwargs)

    When the run method is called the class runs the command:
        
    cd run_dir ; executable_name -inp input_file.in -r run_options_file.yaml

    where the arguments of the run method are:

    Args:
        run_dir (:py:class:`string`) : the folder in which the simulation is performed.

        input (:py:class:`string`) : instance of the :class:`InputGenerator` class that define the input object.

        input_name (:py:class:`string`) : string with the name associated to the input file. If no value is provided the
        name is set to the one of the run directory.

        run_options_name (:py:class:`string`) : string with the name associated to the run_options file. If no value is provided the
        file is called `run_options.yaml`.

        kwargs : other parameters that are stored in the run_options dictionary.

    """

    def __init__(self, runRules, skip =  True, dry_run = False, verbose = True, **kwargs):
        # Use the initialization from the Runner class (all options inside _global_options)
        Runner.__init__(self,**runRules,skip=skip,dry_run=dry_run,verbose=verbose,**kwargs)
        print('Initialize a calculator with scheduler %s' %self._global_options['scheduler'])

    def pre_processing(self):
        """
        Process local run dictionary to create the run directory and input file.

        """
        run_dir = self.run_options.get('run_dir', '.')
        input= self.run_options.get('input')
        input_name = self.run_options.get('input_name',run_dir)
        run_options_name = self.run_options.get('run_options_name','run_options.yaml')
        verbose = self.run_options.get('verbose')

        # Create the run_dir and write the input file
        U.build_folder_path(run_dir,label='run_dir',verbose=verbose) 
        if input is not None:
            input.write(os.path.join(run_dir,input_name)+'.yaml')
        else:
            raise ValueError('Input file not provided.')
        
        # Create the runOptions object and write the run_options file
        runOptions = RunOptions(run_dir=run_dir,omp_num_threads=self.run_options.get('omp_num_threads'))
        # runOptions can perform some check, for instance it can search if some database with compatible results is available
        # and set the skip option (of a part of the run) to True or False. To be implemented.
        runOptions.write(os.path.join(run_dir,run_options_name),verbose=verbose)
        return {}

    def process_run(self):
        """
        Method associated to the running of the executable. The method runs the computation
        and wait the end of the computation before passing to the :meth:`post_processing` method.

        """
        #is_to_run = self.run_options.get('is_to_run')

        #if is_to_run:
        #    job = self.run_job()
        #    self.wait(job)
        return {}