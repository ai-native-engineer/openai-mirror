<!-- source: https://spinningup.openai.com/en/latest/utils/run_utils.html -->

* [Docs](../index.html) »
* Run Utils
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/utils/run_utils.rst)

---

# [Run Utils](#id1)[¶](#run-utils "Permalink to this headline")

Table of Contents

* [Run Utils](#run-utils)
  + [ExperimentGrid](#experimentgrid)
  + [Calling Experiments](#calling-experiments)

## [ExperimentGrid](#id2)[¶](#experimentgrid "Permalink to this headline")

Spinning Up ships with a tool called ExperimentGrid for making hyperparameter ablations easier. This is based on (but simpler than) [the rllab tool](https://github.com/rll/rllab/blob/master/rllab/misc/instrument.py#L173) called VariantGenerator.

*class* `spinup.utils.run_utils.``ExperimentGrid`(*name=''*)[[source]](../_modules/spinup/utils/run_utils.html#ExperimentGrid)[¶](#spinup.utils.run_utils.ExperimentGrid "Permalink to this definition")
:   Tool for running many experiments given hyperparameter ranges.

    `add`(*key*, *vals*, *shorthand=None*, *in\_name=False*)[[source]](../_modules/spinup/utils/run_utils.html#ExperimentGrid.add)[¶](#spinup.utils.run_utils.ExperimentGrid.add "Permalink to this definition")
    :   Add a parameter (key) to the grid config, with potential values (vals).

        By default, if a shorthand isn’t given, one is automatically generated
        from the key using the first three letters of each colon-separated
        term. To disable this behavior, change `DEFAULT_SHORTHAND` in the
        `spinup/user_config.py` file to `False`.

        |  |  |
        | --- | --- |
        | Parameters: | * **key** (*string*) – Name of parameter. * **vals** (*value* *or* *list of values*) – Allowed values of parameter. * **shorthand** (*string*) – Optional, shortened name of parameter. For   example, maybe the parameter `steps_per_epoch` is shortened   to `steps`. * **in\_name** (*bool*) – When constructing variant names, force the   inclusion of this parameter into the name. |

    `print`()[[source]](../_modules/spinup/utils/run_utils.html#ExperimentGrid.print)[¶](#spinup.utils.run_utils.ExperimentGrid.print "Permalink to this definition")
    :   Print a helpful report about the experiment grid.

    `run`(*thunk*, *num\_cpu=1*, *data\_dir=None*, *datestamp=False*)[[source]](../_modules/spinup/utils/run_utils.html#ExperimentGrid.run)[¶](#spinup.utils.run_utils.ExperimentGrid.run "Permalink to this definition")
    :   Run each variant in the grid with function ‘thunk’.

        Note: ‘thunk’ must be either a callable function, or a string. If it is
        a string, it must be the name of a parameter whose values are all
        callable functions.

        Uses `call_experiment` to actually launch each experiment, and gives
        each variant a name using `self.variant_name()`.

        Maintenance note: the args for ExperimentGrid.run should track closely
        to the args for call\_experiment. However, `seed` is omitted because
        we presume the user may add it as a parameter in the grid.

    `variant_name`(*variant*)[[source]](../_modules/spinup/utils/run_utils.html#ExperimentGrid.variant_name)[¶](#spinup.utils.run_utils.ExperimentGrid.variant_name "Permalink to this definition")
    :   Given a variant (dict of valid param/value pairs), make an exp\_name.

        A variant’s name is constructed as the grid name (if you’ve given it
        one), plus param names (or shorthands if available) and values
        separated by underscores.

        Note: if `seed` is a parameter, it is not included in the name.

    `variants`()[[source]](../_modules/spinup/utils/run_utils.html#ExperimentGrid.variants)[¶](#spinup.utils.run_utils.ExperimentGrid.variants "Permalink to this definition")
    :   Makes a list of dicts, where each dict is a valid config in the grid.

        There is special handling for variant parameters whose names take
        the form

        > `'full:param:name'`.

        The colons are taken to indicate that these parameters should
        have a nested dict structure. eg, if there are two params,

        > | Key | Val |
        > | --- | --- |
        > | `'base:param:a'` | 1 |
        > | `'base:param:b'` | 2 |

        the variant dict will have the structure

        ```
        variant = {
            base: {
                param : {
                    a : 1,
                    b : 2
                    }
                }
            }
        ```

## [Calling Experiments](#id3)[¶](#calling-experiments "Permalink to this headline")

`spinup.utils.run_utils.``call_experiment`(*exp\_name*, *thunk*, *seed=0*, *num\_cpu=1*, *data\_dir=None*, *datestamp=False*, *\*\*kwargs*)[[source]](../_modules/spinup/utils/run_utils.html#call_experiment)[¶](#spinup.utils.run_utils.call_experiment "Permalink to this definition")
:   Run a function (thunk) with hyperparameters (kwargs), plus configuration.

    This wraps a few pieces of functionality which are useful when you want
    to run many experiments in sequence, including logger configuration and
    splitting into multiple processes for MPI.

    There’s also a SpinningUp-specific convenience added into executing the
    thunk: if `env_name` is one of the kwargs passed to call\_experiment, it’s
    assumed that the thunk accepts an argument called `env_fn`, and that
    the `env_fn` should make a gym environment with the given `env_name`.

    The way the experiment is actually executed is slightly complicated: the
    function is serialized to a string, and then `run_entrypoint.py` is
    executed in a subprocess call with the serialized string as an argument.
    `run_entrypoint.py` unserializes the function call and executes it.
    We choose to do it this way—instead of just calling the function
    directly here—to avoid leaking state between successive experiments.

    |  |  |
    | --- | --- |
    | Parameters: | * **exp\_name** (*string*) – Name for experiment. * **thunk** (*callable*) – A python function. * **seed** (*int*) – Seed for random number generators. * **num\_cpu** (*int*) – Number of MPI processes to split into. Also accepts   ‘auto’, which will set up as many procs as there are cpus on   the machine. * **data\_dir** (*string*) – Used in configuring the logger, to decide where   to store experiment results. Note: if left as None, data\_dir will   default to `DEFAULT_DATA_DIR` from `spinup/user_config.py`. * **\*\*kwargs** – All kwargs to pass to thunk. |

`spinup.utils.run_utils.``setup_logger_kwargs`(*exp\_name*, *seed=None*, *data\_dir=None*, *datestamp=False*)[[source]](../_modules/spinup/utils/run_utils.html#setup_logger_kwargs)[¶](#spinup.utils.run_utils.setup_logger_kwargs "Permalink to this definition")
:   Sets up the output\_dir for a logger and returns a dict for logger kwargs.

    If no seed is given and datestamp is false,

    ```
    output_dir = data_dir/exp_name
    ```

    If a seed is given and datestamp is false,

    ```
    output_dir = data_dir/exp_name/exp_name_s[seed]
    ```

    If datestamp is true, amend to

    ```
    output_dir = data_dir/YY-MM-DD_exp_name/YY-MM-DD_HH-MM-SS_exp_name_s[seed]
    ```

    You can force datestamp=True by setting `FORCE_DATESTAMP=True` in
    `spinup/user_config.py`.

    |  |  |
    | --- | --- |
    | Parameters: | * **exp\_name** (*string*) – Name for experiment. * **seed** (*int*) – Seed for random number generators used by experiment. * **data\_dir** (*string*) – Path to folder where results should be saved.   Default is the `DEFAULT_DATA_DIR` in `spinup/user_config.py`. * **datestamp** (*bool*) – Whether to include a date and timestamp in the   name of the save directory. |
    | Returns: | logger\_kwargs, a dict containing output\_dir and exp\_name. |
