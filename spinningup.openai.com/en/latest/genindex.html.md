<!-- source: https://spinningup.openai.com/en/latest/genindex.html -->

* [Docs](index.html) »
* Index
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/genindex.rst)

---

# Index

[**Symbols**](#Symbols)
| [**\_**](#_)
| [**A**](#A)
| [**C**](#C)
| [**D**](#D)
| [**E**](#E)
| [**G**](#G)
| [**L**](#L)
| [**M**](#M)
| [**N**](#N)
| [**P**](#P)
| [**R**](#R)
| [**S**](#S)
| [**T**](#T)
| [**V**](#V)

## Symbols

|  |  |
| --- | --- |
| * --act, --ac\_kwargs:activation   + [command line option](user/running.html#cmdoption-act) * --count   + [command line option](user/plotting.html#cmdoption-count) * --cpu, --num\_cpu   + [command line option](user/running.html#cmdoption-cpu) * --data\_dir   + [command line option](user/running.html#cmdoption-data-dir) * --datestamp   + [command line option](user/running.html#cmdoption-datestamp) * --env, --env\_name   + [command line option](user/running.html#cmdoption-env) * --exclude=[EXC ...]   + [command line option](user/plotting.html#cmdoption-exclude) * --exp\_name   + [command line option](user/running.html#cmdoption-exp-name) * --hid, --ac\_kwargs:hidden\_sizes   + [command line option](user/running.html#cmdoption-hid) * --select=[SEL ...]   + [command line option](user/plotting.html#cmdoption-select) | * -d, --deterministic   + [command line option](user/saving_and_loading.html#cmdoption-d) * -i I, --itr=I, default=-1   + [command line option](user/saving_and_loading.html#cmdoption-i) * -l L, --len=L, default=0   + [command line option](user/saving_and_loading.html#cmdoption-l) * -l, --legend=[LEGEND ...]   + [command line option](user/plotting.html#cmdoption-l) * -n N, --episodes=N, default=100   + [command line option](user/saving_and_loading.html#cmdoption-n) * -nr, --norender   + [command line option](user/saving_and_loading.html#cmdoption-nr) * -s, --smooth=S, default=1   + [command line option](user/plotting.html#cmdoption-s) * -x, --xaxis=XAXIS, default='TotalEnvInteracts'   + [command line option](user/plotting.html#cmdoption-x) * -y, --value=[VALUE ...], default='Performance'   + [command line option](user/plotting.html#cmdoption-y) |

## \_

|  |
| --- |
| * [\_\_init\_\_() (spinup.utils.logx.Logger method)](utils/logger.html#spinup.utils.logx.Logger.__init__) |

## A

|  |  |
| --- | --- |
| * [add() (spinup.utils.run\_utils.ExperimentGrid method)](utils/run_utils.html#spinup.utils.run_utils.ExperimentGrid.add) | * [apply\_gradients() (spinup.utils.mpi\_tf.MpiAdamOptimizer method)](utils/mpi.html#spinup.utils.mpi_tf.MpiAdamOptimizer.apply_gradients) |

## C

|  |  |
| --- | --- |
| * [call\_experiment() (in module spinup.utils.run\_utils)](utils/run_utils.html#spinup.utils.run_utils.call_experiment) * command line option   + [--act, --ac\_kwargs:activation](user/running.html#cmdoption-act)   + [--count](user/plotting.html#cmdoption-count)   + [--cpu, --num\_cpu](user/running.html#cmdoption-cpu)   + [--data\_dir](user/running.html#cmdoption-data-dir)   + [--datestamp](user/running.html#cmdoption-datestamp)   + [--env, --env\_name](user/running.html#cmdoption-env)   + [--exclude=[EXC ...]](user/plotting.html#cmdoption-exclude)   + [--exp\_name](user/running.html#cmdoption-exp-name)   + [--hid, --ac\_kwargs:hidden\_sizes](user/running.html#cmdoption-hid)   + [--select=[SEL ...]](user/plotting.html#cmdoption-select)   + [-d, --deterministic](user/saving_and_loading.html#cmdoption-d)   + [-i I, --itr=I, default=-1](user/saving_and_loading.html#cmdoption-i)   + [-l L, --len=L, default=0](user/saving_and_loading.html#cmdoption-l)   + [-l, --legend=[LEGEND ...]](user/plotting.html#cmdoption-l)   + [-n N, --episodes=N, default=100](user/saving_and_loading.html#cmdoption-n)   + [-nr, --norender](user/saving_and_loading.html#cmdoption-nr)   + [-s, --smooth=S, default=1](user/plotting.html#cmdoption-s)   + [-x, --xaxis=XAXIS, default='TotalEnvInteracts'](user/plotting.html#cmdoption-x)   + [-y, --value=[VALUE ...], default='Performance'](user/plotting.html#cmdoption-y)   + [logdir](user/plotting.html#cmdoption-arg-logdir) | * [compute\_gradients() (spinup.utils.mpi\_tf.MpiAdamOptimizer method)](utils/mpi.html#spinup.utils.mpi_tf.MpiAdamOptimizer.compute_gradients) |

## D

|  |  |
| --- | --- |
| * [ddpg\_pytorch() (in module spinup)](algorithms/ddpg.html#spinup.ddpg_pytorch) | * [ddpg\_tf1() (in module spinup)](algorithms/ddpg.html#spinup.ddpg_tf1) * [dump\_tabular() (spinup.utils.logx.Logger method)](utils/logger.html#spinup.utils.logx.Logger.dump_tabular) |

## E

|  |  |
| --- | --- |
| * [EpochLogger (class in spinup.utils.logx)](utils/logger.html#spinup.utils.logx.EpochLogger) | * [ExperimentGrid (class in spinup.utils.run\_utils)](utils/run_utils.html#spinup.utils.run_utils.ExperimentGrid) |

## G

|  |
| --- |
| * [get\_stats() (spinup.utils.logx.EpochLogger method)](utils/logger.html#spinup.utils.logx.EpochLogger.get_stats) |

## L

|  |  |
| --- | --- |
| * [log() (spinup.utils.logx.Logger method)](utils/logger.html#spinup.utils.logx.Logger.log) * [log\_tabular() (spinup.utils.logx.EpochLogger method)](utils/logger.html#spinup.utils.logx.EpochLogger.log_tabular)   + [(spinup.utils.logx.Logger method)](utils/logger.html#spinup.utils.logx.Logger.log_tabular) | * logdir   + [command line option](user/plotting.html#cmdoption-arg-logdir) * [Logger (class in spinup.utils.logx)](utils/logger.html#spinup.utils.logx.Logger) |

## M

|  |  |
| --- | --- |
| * [mpi\_avg() (in module spinup.utils.mpi\_tools)](utils/mpi.html#spinup.utils.mpi_tools.mpi_avg) * [mpi\_avg\_grads() (in module spinup.utils.mpi\_pytorch)](utils/mpi.html#spinup.utils.mpi_pytorch.mpi_avg_grads) | * [mpi\_fork() (in module spinup.utils.mpi\_tools)](utils/mpi.html#spinup.utils.mpi_tools.mpi_fork) * [mpi\_statistics\_scalar() (in module spinup.utils.mpi\_tools)](utils/mpi.html#spinup.utils.mpi_tools.mpi_statistics_scalar) * [MpiAdamOptimizer (class in spinup.utils.mpi\_tf)](utils/mpi.html#spinup.utils.mpi_tf.MpiAdamOptimizer) |

## N

|  |
| --- |
| * [num\_procs() (in module spinup.utils.mpi\_tools)](utils/mpi.html#spinup.utils.mpi_tools.num_procs) |

## P

|  |  |
| --- | --- |
| * [ppo\_pytorch() (in module spinup)](algorithms/ppo.html#spinup.ppo_pytorch) * [ppo\_tf1() (in module spinup)](algorithms/ppo.html#spinup.ppo_tf1) | * [print() (spinup.utils.run\_utils.ExperimentGrid method)](utils/run_utils.html#spinup.utils.run_utils.ExperimentGrid.print) * [proc\_id() (in module spinup.utils.mpi\_tools)](utils/mpi.html#spinup.utils.mpi_tools.proc_id) |

## R

|  |  |
| --- | --- |
| * [restore\_tf\_graph() (in module spinup.utils.logx)](utils/logger.html#spinup.utils.logx.restore_tf_graph) | * [run() (spinup.utils.run\_utils.ExperimentGrid method)](utils/run_utils.html#spinup.utils.run_utils.ExperimentGrid.run) |

## S

|  |  |
| --- | --- |
| * [sac\_pytorch() (in module spinup)](algorithms/sac.html#spinup.sac_pytorch) * [sac\_tf1() (in module spinup)](algorithms/sac.html#spinup.sac_tf1) * [save\_config() (spinup.utils.logx.Logger method)](utils/logger.html#spinup.utils.logx.Logger.save_config) * [save\_state() (spinup.utils.logx.Logger method)](utils/logger.html#spinup.utils.logx.Logger.save_state) * [setup\_logger\_kwargs() (in module spinup.utils.run\_utils)](utils/run_utils.html#spinup.utils.run_utils.setup_logger_kwargs) * [setup\_pytorch\_for\_mpi() (in module spinup.utils.mpi\_pytorch)](utils/mpi.html#spinup.utils.mpi_pytorch.setup_pytorch_for_mpi) * [setup\_pytorch\_saver() (spinup.utils.logx.Logger method)](utils/logger.html#spinup.utils.logx.Logger.setup_pytorch_saver) | * [setup\_tf\_saver() (spinup.utils.logx.Logger method)](utils/logger.html#spinup.utils.logx.Logger.setup_tf_saver) * [spinup.utils.mpi\_pytorch (module)](utils/mpi.html#module-spinup.utils.mpi_pytorch) * [spinup.utils.mpi\_tf (module)](utils/mpi.html#module-spinup.utils.mpi_tf) * [spinup.utils.mpi\_tools (module)](utils/mpi.html#module-spinup.utils.mpi_tools) * [store() (spinup.utils.logx.EpochLogger method)](utils/logger.html#spinup.utils.logx.EpochLogger.store) * [sync\_all\_params() (in module spinup.utils.mpi\_tf)](utils/mpi.html#spinup.utils.mpi_tf.sync_all_params) * [sync\_params() (in module spinup.utils.mpi\_pytorch)](utils/mpi.html#spinup.utils.mpi_pytorch.sync_params) |

## T

|  |  |
| --- | --- |
| * [td3\_pytorch() (in module spinup)](algorithms/td3.html#spinup.td3_pytorch) | * [td3\_tf1() (in module spinup)](algorithms/td3.html#spinup.td3_tf1) * [trpo\_tf1() (in module spinup)](algorithms/trpo.html#spinup.trpo_tf1) |

## V

|  |  |
| --- | --- |
| * [variant\_name() (spinup.utils.run\_utils.ExperimentGrid method)](utils/run_utils.html#spinup.utils.run_utils.ExperimentGrid.variant_name) * [variants() (spinup.utils.run\_utils.ExperimentGrid method)](utils/run_utils.html#spinup.utils.run_utils.ExperimentGrid.variants) | * [vpg\_pytorch() (in module spinup)](algorithms/vpg.html#spinup.vpg_pytorch) * [vpg\_tf1() (in module spinup)](algorithms/vpg.html#spinup.vpg_tf1) |
