<!-- source: https://spinningup.openai.com/en/latest/utils/mpi.html -->

* [Docs](../index.html) »
* MPI Tools
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/utils/mpi.rst)

---

# [MPI Tools](#id1)[¶](#mpi-tools "Permalink to this headline")

Table of Contents

* [MPI Tools](#mpi-tools)
  + [Core MPI Utilities](#module-spinup.utils.mpi_tools)
  + [MPI + PyTorch Utilities](#mpi-pytorch-utilities)
  + [MPI + Tensorflow Utilities](#mpi-tensorflow-utilities)

## [Core MPI Utilities](#id2)[¶](#module-spinup.utils.mpi_tools "Permalink to this headline")

`spinup.utils.mpi_tools.``mpi_avg`(*x*)[[source]](../_modules/spinup/utils/mpi_tools.html#mpi_avg)[¶](#spinup.utils.mpi_tools.mpi_avg "Permalink to this definition")
:   Average a scalar or vector over MPI processes.

`spinup.utils.mpi_tools.``mpi_fork`(*n*, *bind\_to\_core=False*)[[source]](../_modules/spinup/utils/mpi_tools.html#mpi_fork)[¶](#spinup.utils.mpi_tools.mpi_fork "Permalink to this definition")
:   Re-launches the current script with workers linked by MPI.

    Also, terminates the original process that launched it.

    Taken almost without modification from the Baselines function of the
    [same name](https://github.com/openai/baselines/blob/master/baselines/common/mpi_fork.py).

    |  |  |
    | --- | --- |
    | Parameters: | * **n** (*int*) – Number of process to split into. * **bind\_to\_core** (*bool*) – Bind each MPI process to a core. |

`spinup.utils.mpi_tools.``mpi_statistics_scalar`(*x*, *with\_min\_and\_max=False*)[[source]](../_modules/spinup/utils/mpi_tools.html#mpi_statistics_scalar)[¶](#spinup.utils.mpi_tools.mpi_statistics_scalar "Permalink to this definition")
:   Get mean/std and optional min/max of scalar x across MPI processes.

    |  |  |
    | --- | --- |
    | Parameters: | * **x** – An array containing samples of the scalar to produce statistics   for. * **with\_min\_and\_max** (*bool*) – If true, return min and max of x in   addition to mean and std. |

`spinup.utils.mpi_tools.``num_procs`()[[source]](../_modules/spinup/utils/mpi_tools.html#num_procs)[¶](#spinup.utils.mpi_tools.num_procs "Permalink to this definition")
:   Count active MPI processes.

`spinup.utils.mpi_tools.``proc_id`()[[source]](../_modules/spinup/utils/mpi_tools.html#proc_id)[¶](#spinup.utils.mpi_tools.proc_id "Permalink to this definition")
:   Get rank of calling process.

## [MPI + PyTorch Utilities](#id3)[¶](#mpi-pytorch-utilities "Permalink to this headline")

`spinup.utils.mpi_pytorch` contains a few tools to make it easy to do data-parallel PyTorch optimization across MPI processes. The two main ingredients are syncing parameters and averaging gradients before they are used by the adaptive optimizer. Also there’s a hacky fix for a problem where the PyTorch instance in each separate process tries to get too many threads, and they start to clobber each other.

The pattern for using these tools looks something like this:

1. At the beginning of the training script, call `setup_pytorch_for_mpi()`. (Avoids clobbering problem.)
2. After you’ve constructed a PyTorch module, call `sync_params(module)`.
3. Then, during gradient descent, call `mpi_avg_grads` after the backward pass, like so:

```
optimizer.zero_grad()
loss = compute_loss(module)
loss.backward()
mpi_avg_grads(module)   # averages gradient buffers across MPI processes!
optimizer.step()
```

`spinup.utils.mpi_pytorch.``mpi_avg_grads`(*module*)[[source]](../_modules/spinup/utils/mpi_pytorch.html#mpi_avg_grads)[¶](#spinup.utils.mpi_pytorch.mpi_avg_grads "Permalink to this definition")
:   Average contents of gradient buffers across MPI processes.

`spinup.utils.mpi_pytorch.``setup_pytorch_for_mpi`()[[source]](../_modules/spinup/utils/mpi_pytorch.html#setup_pytorch_for_mpi)[¶](#spinup.utils.mpi_pytorch.setup_pytorch_for_mpi "Permalink to this definition")
:   Avoid slowdowns caused by each separate process’s PyTorch using
    more than its fair share of CPU resources.

`spinup.utils.mpi_pytorch.``sync_params`(*module*)[[source]](../_modules/spinup/utils/mpi_pytorch.html#sync_params)[¶](#spinup.utils.mpi_pytorch.sync_params "Permalink to this definition")
:   Sync all parameters of module across all MPI processes.

## [MPI + Tensorflow Utilities](#id4)[¶](#mpi-tensorflow-utilities "Permalink to this headline")

The `spinup.utils.mpi_tf` contains a a few tools to make it easy to use the AdamOptimizer across many MPI processes. This is a bit hacky—if you’re looking for something more sophisticated and general-purpose, consider [horovod](https://github.com/uber/horovod).

*class* `spinup.utils.mpi_tf.``MpiAdamOptimizer`(*\*\*kwargs*)[[source]](../_modules/spinup/utils/mpi_tf.html#MpiAdamOptimizer)[¶](#spinup.utils.mpi_tf.MpiAdamOptimizer "Permalink to this definition")
:   Adam optimizer that averages gradients across MPI processes.

    The compute\_gradients method is taken from Baselines [MpiAdamOptimizer](https://github.com/openai/baselines/blob/master/baselines/common/mpi_adam_optimizer.py).
    For documentation on method arguments, see the Tensorflow docs page for
    the base [AdamOptimizer](https://www.tensorflow.org/api_docs/python/tf/train/AdamOptimizer).

    `apply_gradients`(*grads\_and\_vars*, *global\_step=None*, *name=None*)[[source]](../_modules/spinup/utils/mpi_tf.html#MpiAdamOptimizer.apply_gradients)[¶](#spinup.utils.mpi_tf.MpiAdamOptimizer.apply_gradients "Permalink to this definition")
    :   Same as normal apply\_gradients, except sync params after update.

    `compute_gradients`(*loss*, *var\_list*, *\*\*kwargs*)[[source]](../_modules/spinup/utils/mpi_tf.html#MpiAdamOptimizer.compute_gradients)[¶](#spinup.utils.mpi_tf.MpiAdamOptimizer.compute_gradients "Permalink to this definition")
    :   Same as normal compute\_gradients, except average grads over processes.

`spinup.utils.mpi_tf.``sync_all_params`()[[source]](../_modules/spinup/utils/mpi_tf.html#sync_all_params)[¶](#spinup.utils.mpi_tf.sync_all_params "Permalink to this definition")
:   Sync all tf variables across MPI processes.
