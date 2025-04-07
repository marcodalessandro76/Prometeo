class Runner():
    """
    This object is associated with the concept of execution of an action.
    It may be customized to be used inside workflows and datasets.
    The central functionality is the `run` method that can be customized on
    subclasses of `Runner`. This object manages both global and local options
    for its run method. Global options are set during instantiation, while
    local options can be provided each time the `run` method is called,
    temporarily updating the global options for that specific execution.

    Args:
        **kwargs: Global options for the runner. These keyword arguments are
            deep-copied and stored as the initial global options. See
            :meth:`global_options` for retrieving these options.

    Example:
        >>> torun = Runner(args1='one', args2='two')
        >>> print(torun.global_options())
        {'args1': 'one', 'args2': 'two'}
        >>> print(torun.get_global_option('args1'))
        'one'
    """

    def __init__(self, **kwargs):
        import copy
        self._global_options = copy.deepcopy(kwargs)

    def global_options(self):
        """
        Get all global options as a dictionary.

        Returns:
            dict: A dictionary containing the current global options.
        """
        return self._global_options

    def get_global_option(self, key):
        """
        Get the value of a specific global option.

        Args:
            key (str): The key of the global option to retrieve.

        Returns:
            The value associated with the given `key` in the global options.

        Raises:
            KeyError: If the provided `key` is not found in the global options.
        """
        if key not in self._global_options:
            raise KeyError(f"Global option '{key}' not found.")
        return self._global_options[key]

    def update_global_options(self, **kwargs):
        """
        Update the global options with new keyword arguments.

        Any keys provided in `kwargs` will be added to or update the existing
        global options.

        Args:
            **kwargs: Keyword arguments representing the options to update.
        """
        self._global_options.update(kwargs)

    def pop_global_option(self, key):
        """
        Remove a specific global option from the global option dictionary.

        Args:
            key (str): The key of the global option to remove.

        Returns:
            The value of the global option that was removed.

        Raises:
            KeyError: If the provided `key` is not found in the global options.
        """
        if key not in self._global_options:
            raise KeyError(f"Global option '{key}' not found.")
        return self._global_options.pop(key)

    def _run_options(self, **kwargs):
        """
        Create a local dictionary for a specific run.

        This internal method combines the current global options with any local
        options provided to the `run` method to create the `run_options`
        dictionary. This dictionary is accessible within the `process_run`
        method and contains all relevant configuration for the current run.
        """
        import copy
        self.run_options = copy.deepcopy(self._global_options)
        self.run_options.update(kwargs)

    def run(self, **kwargs):
        """
        Run method of the class.

        This is the central method for executing an action. It orchestrates the
        following steps:

        1.  Constructs the local `run_options` dictionary by combining global
            options with the `kwargs` provided to this method.
        2.  Calls the :meth:`pre_processing` method to prepare any necessary
            arguments for the main processing step.
        3.  Calls the abstract :meth:`process_run` method with the arguments
            returned by :meth:`pre_processing`.
        4.  Merges the results returned by :meth:`process_run` back into the
            arguments.
        5.  Calls the :meth:`post_processing` method to perform any final
            operations on the results.
        6.  Returns the object returned by the :meth:`post_processing` method.

        Subclasses are expected to override the :meth:`pre_processing`,
        :meth:`process_run`, and :meth:`post_processing` methods to implement
        specific execution logic.

        Args:
            **kwargs: Local options specific to this run. These keyword
                arguments will temporarily update the global options for this
                particular execution.

        Returns:
            Any: The object returned by the :meth:`post_processing` method,
                representing the result of the run.
        """
        from mppi.Utilities import Utils as f
        self._run_options(**kwargs)
        run_args = self.pre_processing()
        run_results = self.process_run(**run_args)
        f.dict_merge(dest=run_args, src=run_results)
        return self.post_processing(**run_args)

    def pre_processing(self):
        """
        Pre-treat the keyword arguments and the options, if needed.

        This method is intended to be overridden by subclasses to perform
        any necessary setup or preparation before the main :meth:`process_run`
        method is called. It has access to both global and local run options
        through the `self.run_options` attribute.

        Returns:
            dict: A dictionary of pre-treated keyword arguments that will be
            passed to the :meth:`process_run` method. The default implementation
            returns an empty dictionary.
        """
        return {}

    def process_run(self, **kwargs):
        """
        Main item of the runner, defines the information that have to be
        post-processed by :meth:`post_processing`.

        This method contains the core logic of the action performed by the
        runner. Subclasses **must** override this method to implement their
        specific functionality. It receives the pre-processed arguments from
        :meth:`pre_processing`, potentially updated with local options from
        the :meth:`run` call.

        Args:
            **kwargs (dict): Keyword arguments as returned from the
             :meth:`pre_processing` method, potentially updated with local
             options from the :meth:`run` call.

        Returns:
            dict: A dictionary of results to be passed to
            :meth:`post_processing`. These results will be merged into the
            `kwargs` passed to `post_processing`. The default implementation
            returns the `kwargs` it receives.
        """
        return kwargs

    def post_processing(self, **kwargs):
        """
        Post-processing, take the arguments as they are provided by the update
        of :meth:`process_run` and :meth:`pre_processing` methods.

        This method is called after :meth:`process_run` has completed. Subclasses
        can override this method to perform any necessary cleanup or final
        operations on the results contained in `kwargs`.

        Args:
            **kwargs (dict): Keyword arguments containing the results from
                :meth:`pre_processing` and :meth:`process_run`.

        Returns:
            Any: The final object that each call to the :meth:`run` method is
            supposed to provide. The default implementation returns `None`.
        """
        return None