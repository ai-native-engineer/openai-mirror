<!-- source: https://spinningup.openai.com/en/latest/user/plotting.html -->

* [Docs](../index.html) »
* Plotting Results
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/user/plotting.rst)

---

# Plotting Results[¶](#plotting-results "Permalink to this headline")

Spinning Up ships with a simple plotting utility for interpreting results. Run it with:

```
python -m spinup.run plot [path/to/output_directory ...] [--legend [LEGEND ...]]
    [--xaxis XAXIS] [--value [VALUE ...]] [--count] [--smooth S]
    [--select [SEL ...]] [--exclude [EXC ...]]
```

**Positional Arguments:**

`logdir`[¶](#cmdoption-arg-logdir "Permalink to this definition")
:   *strings*. As many log directories (or prefixes to log directories, which the plotter will autocomplete internally) as you’d like to plot from. Logdirs will be searched recursively for experiment outputs.

    You Should Know

    The internal autocompleting is really handy! Suppose you have run several experiments, with the aim of comparing performance between different algorithms, resulting in a log directory structure of:

    ```
    data/
        bench_algo1/
            bench_algo1-seed0/
            bench_algo1-seed10/
        bench_algo2/
            bench_algo2-seed0/
            bench_algo2-seed10/
    ```

    You can easily produce a graph comparing algo1 and algo2 with:

    ```
    python spinup/utils/plot.py data/bench_algo
    ```

    relying on the autocomplete to find both `data/bench_algo1` and `data/bench_algo2`.

**Optional Arguments:**

`-l``,` `--legend``=[LEGEND ...]`[¶](#cmdoption-l "Permalink to this definition")
:   *strings*. Optional way to specify legend for the plot. The plotter legend will automatically use the `exp_name` from the `config.json` file, unless you tell it otherwise through this flag. This only works if you provide a name for each directory that will get plotted. (Note: this may not be the same as the number of logdir args you provide! Recall that the plotter looks for autocompletes of the logdir args: there may be more than one match for a given logdir prefix, and you will need to provide a legend string for each one of those matches—unless you have removed some of them as candidates via selection or exclusion rules (below).)

`-x``,` `--xaxis``=XAXIS``,` `default``='TotalEnvInteracts'`[¶](#cmdoption-x "Permalink to this definition")
:   *string*. Pick what column from data is used for the x-axis.

`-y``,` `--value``=[VALUE ...]``,` `default``='Performance'`[¶](#cmdoption-y "Permalink to this definition")
:   *strings*. Pick what columns from data to graph on the y-axis. Submitting multiple values will produce multiple graphs. Defaults to `Performance`, which is not an actual output of any algorithm. Instead, `Performance` refers to either `AverageEpRet`, the correct performance measure for the on-policy algorithms, or `AverageTestEpRet`, the correct performance measure for the off-policy algorithms. The plotter will automatically figure out which of `AverageEpRet` or `AverageTestEpRet` to report for each separate logdir.

`--count`[¶](#cmdoption-count "Permalink to this definition")
:   Optional flag. By default, the plotter shows y-values which are averaged across all results that share an `exp_name`, which is typically a set of identical experiments that only vary in random seed. But if you’d like to see all of those curves separately, use the `--count` flag.

`-s``,` `--smooth``=S``,` `default``=1`[¶](#cmdoption-s "Permalink to this definition")
:   *int*. Smooth data by averaging it over a fixed window. This parameter says how wide the averaging window will be.

`--select``=[SEL ...]`[¶](#cmdoption-select "Permalink to this definition")
:   *strings*. Optional selection rule: the plotter will only show curves from logdirs that contain all of these substrings.

`--exclude``=[EXC ...]`[¶](#cmdoption-exclude "Permalink to this definition")
:   *strings*. Optional exclusion rule: plotter will only show curves from logdirs that do not contain these substrings.
