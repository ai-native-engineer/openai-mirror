<!-- source: https://spinningup.openai.com/en/latest/utils/logger.html -->

* [Docs](../index.html) »
* Logger
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/utils/logger.rst)

---

# [Logger](#id2)[¶](#logger "Permalink to this headline")

Table of Contents

* [Logger](#logger)
  + [Using a Logger](#using-a-logger)
    - [Examples](#examples)
    - [Logging and PyTorch](#logging-and-pytorch)
    - [Logging and MPI](#logging-and-mpi)
  + [Logger Classes](#logger-classes)
  + [Loading Saved Models (PyTorch Only)](#loading-saved-models-pytorch-only)
  + [Loading Saved Graphs (Tensorflow Only)](#loading-saved-graphs-tensorflow-only)

## [Using a Logger](#id3)[¶](#using-a-logger "Permalink to this headline")

Spinning Up ships with basic logging tools, implemented in the classes [Logger](../utils/logger.html#spinup.utils.logx.Logger) and [EpochLogger](../utils/logger.html#spinup.utils.logx.EpochLogger). The Logger class contains most of the basic functionality for saving diagnostics, hyperparameter configurations, the state of a training run, and the trained model. The EpochLogger class adds a thin layer on top of that to make it easy to track the average, standard deviation, min, and max value of a diagnostic over each epoch and across MPI workers.

You Should Know

All Spinning Up algorithm implementations use an EpochLogger.

### [Examples](#id4)[¶](#examples "Permalink to this headline")

First, let’s look at a simple example of how an EpochLogger keeps track of a diagnostic value:

```
>>> from spinup.utils.logx import EpochLogger
>>> epoch_logger = EpochLogger()
>>> for i in range(10):
        epoch_logger.store(Test=i)
>>> epoch_logger.log_tabular('Test', with_min_and_max=True)
>>> epoch_logger.dump_tabular()
-------------------------------------
|     AverageTest |             4.5 |
|         StdTest |            2.87 |
|         MaxTest |               9 |
|         MinTest |               0 |
-------------------------------------
```

The `store` method is used to save all values of `Test` to the `epoch_logger`‘s internal state. Then, when `log_tabular` is called, it computes the average, standard deviation, min, and max of `Test` over all of the values in the internal state. The internal state is wiped clean after the call to `log_tabular` (to prevent leakage into the statistics at the next epoch). Finally, `dump_tabular` is called to write the diagnostics to file and to stdout.

Next, let’s look at a full training procedure with the logger embedded, to highlight configuration and model saving as well as diagnostic logging:

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 ``` | ```  import numpy as np  import tensorflow as tf  import time  from spinup.utils.logx import EpochLogger    def mlp(x, hidden_sizes=(32,), activation=tf.tanh, output_activation=None):      for h in hidden_sizes[:-1]:          x = tf.layers.dense(x, units=h, activation=activation)      return tf.layers.dense(x, units=hidden_sizes[-1], activation=output_activation)    # Simple script for training an MLP on MNIST.  def train_mnist(steps_per_epoch=100, epochs=5,                  lr=1e-3, layers=2, hidden_size=64,                  logger_kwargs=dict(), save_freq=1):       logger = EpochLogger(**logger_kwargs)      logger.save_config(locals())       # Load and preprocess MNIST data      (x_train, y_train), _ = tf.keras.datasets.mnist.load_data()      x_train = x_train.reshape(-1, 28*28) / 255.0       # Define inputs & main outputs from computation graph      x_ph = tf.placeholder(tf.float32, shape=(None, 28*28))      y_ph = tf.placeholder(tf.int32, shape=(None,))      logits = mlp(x_ph, hidden_sizes=[hidden_size]*layers + [10], activation=tf.nn.relu)      predict = tf.argmax(logits, axis=1, output_type=tf.int32)       # Define loss function, accuracy, and training op      y = tf.one_hot(y_ph, 10)      loss = tf.losses.softmax_cross_entropy(y, logits)      acc = tf.reduce_mean(tf.cast(tf.equal(y_ph, predict), tf.float32))      train_op = tf.train.AdamOptimizer().minimize(loss)       # Prepare session      sess = tf.Session()      sess.run(tf.global_variables_initializer())       # Setup model saving      logger.setup_tf_saver(sess, inputs={'x': x_ph},                                  outputs={'logits': logits, 'predict': predict})       start_time = time.time()       # Run main training loop      for epoch in range(epochs):          for t in range(steps_per_epoch):              idxs = np.random.randint(0, len(x_train), 32)              feed_dict = {x_ph: x_train[idxs],                           y_ph: y_train[idxs]}              outs = sess.run([loss, acc, train_op], feed_dict=feed_dict)              logger.store(Loss=outs[0], Acc=outs[1])           # Save model          if (epoch % save_freq == 0) or (epoch == epochs-1):              logger.save_state(state_dict=dict(), itr=None)           # Log info about epoch          logger.log_tabular('Epoch', epoch)          logger.log_tabular('Acc', with_min_and_max=True)          logger.log_tabular('Loss', average_only=True)          logger.log_tabular('TotalGradientSteps', (epoch+1)*steps_per_epoch)          logger.log_tabular('Time', time.time()-start_time)          logger.dump_tabular()   if __name__ == '__main__':      train_mnist() ``` |

In this example, observe that

* On line 19, [logger.save\_config](../utils/logger.html#spinup.utils.logx.Logger.save_config) is used to save the hyperparameter configuration to a JSON file.
* On lines 42 and 43, [logger.setup\_tf\_saver](../utils/logger.html#spinup.utils.logx.Logger.setup_tf_saver) is used to prepare the logger to save the key elements of the computation graph.
* On line 54, diagnostics are saved to the logger’s internal state via [logger.store](../utils/logger.html#spinup.utils.logx.EpochLogger.store).
* On line 58, the computation graph is saved once per epoch via [logger.save\_state](../utils/logger.html#spinup.utils.logx.Logger.save_state).
* On lines 61-66, [logger.log\_tabular](../utils/logger.html#spinup.utils.logx.EpochLogger.log_tabular) and [logger.dump\_tabular](../utils/logger.html#spinup.utils.logx.Logger.dump_tabular) are used to write the epoch diagnostics to file. Note that the keys passed into [logger.log\_tabular](../utils/logger.html#spinup.utils.logx.EpochLogger.log_tabular) are the same as the keys passed into [logger.store](../utils/logger.html#spinup.utils.logx.EpochLogger.store).

### [Logging and PyTorch](#id5)[¶](#logging-and-pytorch "Permalink to this headline")

The preceding example was given in Tensorflow. For PyTorch, everything is the same except for L42-43: instead of `logger.setup_tf_saver`, you would use `logger.setup_pytorch_saver`, and you would pass it [a PyTorch module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) (the network you are training) as an argument.

The behavior of `logger.save_state` is the same as in the Tensorflow case: each time it is called, it’ll save the latest version of the PyTorch module.

### [Logging and MPI](#id6)[¶](#logging-and-mpi "Permalink to this headline")

You Should Know

Several algorithms in RL are easily parallelized by using MPI to average gradients and/or other key quantities. The Spinning Up loggers are designed to be well-behaved when using MPI: things will only get written to stdout and to file from the process with rank 0. But information from other processes isn’t lost if you use the EpochLogger: everything which is passed into EpochLogger via `store`, regardless of which process it’s stored in, gets used to compute average/std/min/max values for a diagnostic.

## [Logger Classes](#id7)[¶](#logger-classes "Permalink to this headline")

*class* `spinup.utils.logx.``Logger`(*output\_dir=None*, *output\_fname='progress.txt'*, *exp\_name=None*)[[source]](../_modules/spinup/utils/logx.html#Logger)[¶](#spinup.utils.logx.Logger "Permalink to this definition")
:   A general-purpose logger.

    Makes it easy to save diagnostics, hyperparameter configurations, the
    state of a training run, and the trained model.

    `__init__`(*output\_dir=None*, *output\_fname='progress.txt'*, *exp\_name=None*)[[source]](../_modules/spinup/utils/logx.html#Logger.__init__)[¶](#spinup.utils.logx.Logger.__init__ "Permalink to this definition")
    :   Initialize a Logger.

        |  |  |
        | --- | --- |
        | Parameters: | * **output\_dir** (*string*) – A directory for saving results to. If   `None`, defaults to a temp directory of the form   `/tmp/experiments/somerandomnumber`. * **output\_fname** (*string*) – Name for the tab-separated-value file   containing metrics logged throughout a training run.   Defaults to `progress.txt`. * **exp\_name** (*string*) – Experiment name. If you run multiple training   runs and give them all the same `exp_name`, the plotter   will know to group them. (Use case: if you run the same   hyperparameter configuration with multiple random seeds, you   should give them all the same `exp_name`.) |

    `dump_tabular`()[[source]](../_modules/spinup/utils/logx.html#Logger.dump_tabular)[¶](#spinup.utils.logx.Logger.dump_tabular "Permalink to this definition")
    :   Write all of the diagnostics from the current iteration.

        Writes both to stdout, and to the output file.

    `log`(*msg*, *color='green'*)[[source]](../_modules/spinup/utils/logx.html#Logger.log)[¶](#spinup.utils.logx.Logger.log "Permalink to this definition")
    :   Print a colorized message to stdout.

    `log_tabular`(*key*, *val*)[[source]](../_modules/spinup/utils/logx.html#Logger.log_tabular)[¶](#spinup.utils.logx.Logger.log_tabular "Permalink to this definition")
    :   Log a value of some diagnostic.

        Call this only once for each diagnostic quantity, each iteration.
        After using `log_tabular` to store values for each diagnostic,
        make sure to call `dump_tabular` to write them out to file and
        stdout (otherwise they will not get saved anywhere).

    `save_config`(*config*)[[source]](../_modules/spinup/utils/logx.html#Logger.save_config)[¶](#spinup.utils.logx.Logger.save_config "Permalink to this definition")
    :   Log an experiment configuration.

        Call this once at the top of your experiment, passing in all important
        config vars as a dict. This will serialize the config to JSON, while
        handling anything which can’t be serialized in a graceful way (writing
        as informative a string as possible).

        Example use:

        ```
        logger = EpochLogger(**logger_kwargs)
        logger.save_config(locals())
        ```

    `save_state`(*state\_dict*, *itr=None*)[[source]](../_modules/spinup/utils/logx.html#Logger.save_state)[¶](#spinup.utils.logx.Logger.save_state "Permalink to this definition")
    :   Saves the state of an experiment.

        To be clear: this is about saving *state*, not logging diagnostics.
        All diagnostic logging is separate from this function. This function
        will save whatever is in `state_dict`—usually just a copy of the
        environment—and the most recent parameters for the model you
        previously set up saving for with `setup_tf_saver`.

        Call with any frequency you prefer. If you only want to maintain a
        single state and overwrite it at each call with the most recent
        version, leave `itr=None`. If you want to keep all of the states you
        save, provide unique (increasing) values for ‘itr’.

        |  |  |
        | --- | --- |
        | Parameters: | * **state\_dict** (*dict*) – Dictionary containing essential elements to   describe the current state of training. * **itr** – An int, or None. Current iteration of training. |

    `setup_pytorch_saver`(*what\_to\_save*)[[source]](../_modules/spinup/utils/logx.html#Logger.setup_pytorch_saver)[¶](#spinup.utils.logx.Logger.setup_pytorch_saver "Permalink to this definition")
    :   Set up easy model saving for a single PyTorch model.

        Because PyTorch saving and loading is especially painless, this is
        very minimal; we just need references to whatever we would like to
        pickle. This is integrated into the logger because the logger
        knows where the user would like to save information about this
        training run.

        |  |  |
        | --- | --- |
        | Parameters: | **what\_to\_save** – Any PyTorch model or serializable object containing PyTorch models. |

    `setup_tf_saver`(*sess*, *inputs*, *outputs*)[[source]](../_modules/spinup/utils/logx.html#Logger.setup_tf_saver)[¶](#spinup.utils.logx.Logger.setup_tf_saver "Permalink to this definition")
    :   Set up easy model saving for tensorflow.

        Call once, after defining your computation graph but before training.

        |  |  |
        | --- | --- |
        | Parameters: | * **sess** – The Tensorflow session in which you train your computation   graph. * **inputs** (*dict*) – A dictionary that maps from keys of your choice   to the tensorflow placeholders that serve as inputs to the   computation graph. Make sure that *all* of the placeholders   needed for your outputs are included! * **outputs** (*dict*) – A dictionary that maps from keys of your choice   to the outputs from your computation graph. |

*class* `spinup.utils.logx.``EpochLogger`(*\*args*, *\*\*kwargs*)[[source]](../_modules/spinup/utils/logx.html#EpochLogger)[¶](#spinup.utils.logx.EpochLogger "Permalink to this definition")
:   Bases: [`spinup.utils.logx.Logger`](#spinup.utils.logx.Logger "spinup.utils.logx.Logger")

    A variant of Logger tailored for tracking average values over epochs.

    Typical use case: there is some quantity which is calculated many times
    throughout an epoch, and at the end of the epoch, you would like to
    report the average / std / min / max value of that quantity.

    With an EpochLogger, each time the quantity is calculated, you would
    use

    ```
    epoch_logger.store(NameOfQuantity=quantity_value)
    ```

    to load it into the EpochLogger’s state. Then at the end of the epoch, you
    would use

    ```
    epoch_logger.log_tabular(NameOfQuantity, **options)
    ```

    to record the desired values.

    `get_stats`(*key*)[[source]](../_modules/spinup/utils/logx.html#EpochLogger.get_stats)[¶](#spinup.utils.logx.EpochLogger.get_stats "Permalink to this definition")
    :   Lets an algorithm ask the logger for mean/std/min/max of a diagnostic.

    `log_tabular`(*key*, *val=None*, *with\_min\_and\_max=False*, *average\_only=False*)[[source]](../_modules/spinup/utils/logx.html#EpochLogger.log_tabular)[¶](#spinup.utils.logx.EpochLogger.log_tabular "Permalink to this definition")
    :   Log a value or possibly the mean/std/min/max values of a diagnostic.

        |  |  |
        | --- | --- |
        | Parameters: | * **key** (*string*) – The name of the diagnostic. If you are logging a   diagnostic whose state has previously been saved with   `store`, the key here has to match the key you used there. * **val** – A value for the diagnostic. If you have previously saved   values for this key via `store`, do *not* provide a `val`   here. * **with\_min\_and\_max** (*bool*) – If true, log min and max values of the   diagnostic over the epoch. * **average\_only** (*bool*) – If true, do not log the standard deviation   of the diagnostic over the epoch. |

    `store`(*\*\*kwargs*)[[source]](../_modules/spinup/utils/logx.html#EpochLogger.store)[¶](#spinup.utils.logx.EpochLogger.store "Permalink to this definition")
    :   Save something into the epoch\_logger’s current state.

        Provide an arbitrary number of keyword arguments with numerical
        values.

## [Loading Saved Models (PyTorch Only)](#id8)[¶](#loading-saved-models-pytorch-only "Permalink to this headline")

To load an actor-critic model saved by a PyTorch Spinning Up implementation, run:

```
ac = torch.load('path/to/model.pt')
```

When you use this method to load an actor-critic model, you can minimally expect it to have an `act` method that allows you to sample actions from the policy, given observations:

```
actions = ac.act(torch.as_tensor(obs, dtype=torch.float32))
```

## [Loading Saved Graphs (Tensorflow Only)](#id9)[¶](#loading-saved-graphs-tensorflow-only "Permalink to this headline")

`spinup.utils.logx.``restore_tf_graph`(*sess*, *fpath*)[[source]](../_modules/spinup/utils/logx.html#restore_tf_graph)[¶](#spinup.utils.logx.restore_tf_graph "Permalink to this definition")
:   Loads graphs saved by Logger.

    Will output a dictionary whose keys and values are from the ‘inputs’
    and ‘outputs’ dict you specified with logger.setup\_tf\_saver().

    |  |  |
    | --- | --- |
    | Parameters: | * **sess** – A Tensorflow session. * **fpath** – Filepath to save directory. |
    | Returns: | A dictionary mapping from keys to tensors in the computation graph loaded from `fpath`. |

When you use this method to restore a graph saved by a Tensorflow Spinning Up implementation, you can minimally expect it to include the following:

| Key | Value |
| --- | --- |
| `x` | Tensorflow placeholder for state input. |
| `pi` | Samples an action from the agent, conditioned  on states in `x`. |

The relevant value functions for an algorithm are also typically stored. For details of what else gets saved by a given algorithm, see its documentation page.
