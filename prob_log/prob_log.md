# <span style="color:blue">sample template</span>
## <span style="color:green">24-10-03 sample prob</span>

### error message 
```
Can't find nvmlDeviceGetNvLinkRemoteDeviceType: /lib64/libnvidia-ml.so.1: undefined symbol: nvmlDeviceGetNvLinkRemoteDeviceType
```
### brief analysis

Did what on what causes the problem 

### full trace back

```the full error message```

### solution

did what to solve

### takeaway

how to avoid this next time

---


# <span style="color:blue"> linux related </span>

## <span style="color:green">25-01-17 version `GLIBCXX_3.4.29' not found </span>

### error message 
```
ImportError: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /share/home/Andrew/anaconda3/envs/torch251/lib/python3.12/site-packages/PIL/../../.././libLerc.so.4)
```
### brief analysis

When importing some packages, has this problem. eg `from PIL import Image`

### full trace back

```
>>> from PIL import Image
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/share/home/Andrew/anaconda3/envs/torch251/lib/python3.12/site-packages/PIL/Image.py", line 97, in <module>
    from . import _imaging as core
ImportError: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /share/home/Andrew/anaconda3/envs/torch251/lib/python3.12/site-packages/PIL/../../.././libLerc.so.4)
```

### solution

refer to  this [link](https://stackoverflow.com/questions/58424974/anaconda-importerror-usr-lib64-libstdc-so-6-version-glibcxx-3-4-21-not-fo)
Did: `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/share/home/Andrew/anaconda3/lib/`

## <span style="color:green">24-10-07 server no connection</span>

### error message 

eg when downloading conda or conda install, says cannot connect, http error

### brief analysis

Didn't add proxy. Add proxy to the `~/.bashrc`. 

### solution

For cu cse server, can just use the proxy on cse177 

---

## <span style="color:green">24-10-08 cannot find a specific gcc </span>

### error message 

```
The Open MPI wrapper compiler was unable to find the specified compiler
x86_64-conda_cos6-linux-gnu-cc in your PATH.

Note that this compiler was either specified at configure time or in
one of several possible environment variables.
```

### brief analysis

This is due to version problem. Cannot find the specific compiler `x86_64-conda_cos6-linux-gnu-cc`

### solution

If no `sudo` rights, a workaround is to wrap the normal gcc in a file named `x86_64-conda_cos6-linux-gnu-cc` and add it to `$PATH`.

1. Create a file named `x86_64-conda_cos6-linux-gnu-cc` with the following content: 
```bash
#!/bin/bash
exec gcc "$@"
```
2. then:
```
chmod +x x86_64-conda_cos6-linux-gnu-cc
export PATH="${PATH}:/path/to/directory/containing/wrapper"
```
---

# <span style="color:blue"> anaconda install related (including pip)  </span>

---

## <span style="color:green">24-10-07 tensor flow cannot find gpu</span>

### error message 
```
W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudnn.so.8'; dlerror: libcudnn.so.8: cannot open shared object file: No such file or directory
```

### full trace back

```
>>> tf.test.is_gpu_available()
2024-10-07 21:30:01.364600: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 AVX512F FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2024-10-07 21:30:01.700437: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudnn.so.8'; dlerror: libcudnn.so.8: cannot open shared object file: No such file or directory
2024-10-07 21:30:01.700476: W tensorflow/core/common_runtime/gpu/gpu_device.cc:1835] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
False
```

### solution

This happens when directly copying an environment to another machine. And when the cuda version of 2 machines diff, cannot work. Normally just need to upgrade cuda, but cannot do without sudo. So maybe should try reinstall tensorflow and find suitable version

---

## <span style="color:green">24-10-08 tensor flow cannot find certain function or module </span>

### error message 
```
AttributeError: module 'tensorflow.compat.v2.__internal__' has no attribute 'dispatch'
```
### brief analysis

Diff tensor flow has really different implementation and it often occurs that cannot find some package or module.

### solution

No very good way. just paste the problem to google and some might answer you which version would solve this problem.  
For this certain error, should not install tensorflow\==2.6 but tensorflow==2.1 works.

---

## <span style="color:green"> 24-10-5 dependency issue with pin-1 </span>

### error message 

```
pin-1 is not installable because it requires
  └─ python 3.12.* , which conflicts with any installable versions previously reported;
```
But the version of python is just 3.12

### brief analysis

If this happens the python version in the error will be exactly your python version.

### full trace back

```
LibMambaUnsatisfiableError: Encountered problems while solving:
  - nothing provides cudatoolkit 8.0.* needed by py-xgboost-0.72-py27h83be7fe_0

Could not solve for environment specs
The following packages are incompatible
├─ __cuda is requested and can be installed;
├─ libstdcxx-ng 11.2.0.*  is requested and can be installed;
├─ numpy-base 2.0.1.*  is installable with the potential options
│  ├─ numpy-base 2.0.1 would require
│  │  └─ numpy 2.0.1 py312hc5e2394_1, which can be installed;
│  ├─ numpy-base 2.0.1 would require
│  │  └─ python >=3.10,<3.11.0a0 , which can be installed;
│  ├─ numpy-base 2.0.1 would require
│  │  └─ python >=3.11,<3.12.0a0 , which can be installed;
│  ├─ numpy-base 2.0.1 would require
│  │  └─ numpy 2.0.1 py312h2809609_1, which can be installed;
│  └─ numpy-base 2.0.1 would require
│     └─ python >=3.9,<3.10.0a0 , which can be installed;
├─ pin-1 is not installable because it requires
│  └─ python 3.12.* , which conflicts with any installable versions previously reported;
```

### solution

Currently not solved. 
Workarounds such as using pip install

---

## <span style="color:green">24-10-08 cannot find a specific gcc </span>

### error message 

```
The Open MPI wrapper compiler was unable to find the specified compiler
x86_64-conda_cos6-linux-gnu-cc in your PATH.

Note that this compiler was either specified at configure time or in
one of several possible environment variables.
```

### brief analysis

This is due to version problem. Cannot find the specific compiler `x86_64-conda_cos6-linux-gnu-cc`

### solution

If no `sudo` rights, a workaround is to wrap the normal gcc in a file named `x86_64-conda_cos6-linux-gnu-cc` and add it to `$PATH`.

1. Create a file named `x86_64-conda_cos6-linux-gnu-cc` with the following content: 
```bash
#!/bin/bash
exec gcc "$@"
```
2. then:
```
chmod +x x86_64-conda_cos6-linux-gnu-cc
export PATH="${PATH}:/path/to/directory/containing/wrapper"
```
---

# <span style="color:blue"> general python packages </span>

---

## <span style="color:green">25-01-17 In VScode ipynb cannot find kernel in when selecting kernel</span>

### error message 
When clicking Select Kernel, can't find the conda environment

### solution

Install the Jupyter extension, and `pip install jupyterlab`. Then reload window and try again

---

## <span style="color:green">24-11-30 Rectangle.set() got an unexpected keyword argument 'normed'</span>

### error message 
```
Traceback (most recent call last):
  File "/data2/mqyu/work/ynu/beam/post_analysis.py", line 324, in <module>
    plotScoresDistributions(file, motpath)
  File "/data2/mqyu/work/ynu/beam/post_analysis.py", line 202, in plotScoresDistributions
    plt.hist(scores,normed=True, alpha=0.5, label="input", bins=np.arange(minmin, maxmax + binwidth, binwidth))
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/matplotlib/pyplot.py", line 3440, in hist
    return gca().hist(
           ^^^^^^^^^^^
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/matplotlib/__init__.py", line 1473, in inner
    return func(
           ^^^^^
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/matplotlib/axes/_axes.py", line 7154, in hist
    p._internal_update(kwargs)
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/matplotlib/artist.py", line 1216, in _internal_update
    return self._update_props(
           ^^^^^^^^^^^^^^^^^^^
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/matplotlib/artist.py", line 1190, in _update_props
    raise AttributeError(
AttributeError: Rectangle.set() got an unexpected keyword argument 'normed'
```

### brief analysis

Because the updated version of plt.hist, no more keyword `normed`. `normed=True` changed to `density=True`

### solution

Change all the `normed=True` to `density=True` in `plt.hist()`


---

#  <span style="color:blue"> Pytorch / cuda </span>

---

## <span style="color:green"> 24-10-03 Lightning unable to import </span>

### error message 

```
When importing lightning on python, error and report "max recursion depth reached"
```
### brief analysis

It's a version conflict problem. Just recreate an env following the .md


---

## <span style="color:green"> 24-10-03 pl Lightning problem </span>

### error message 
Can't find nvmlDeviceGetNvLinkRemoteDeviceType: /lib64/libnvidia-ml.so.1: undefined symbol: nvmlDeviceGetNvLinkRemoteDeviceType

### brief analysis

Running a lightning module with multi-thread one thread not working and had time out.

### full trace back
```
  File "/data2/mqyu/work/ablation/wb_no_fm/train_mul_gpu.py", line 101, in <module>
    main()
  File "/data2/mqyu/work/ablation/wb_no_fm/train_mul_gpu.py", line 94, in main
    trainer.fit(model=model, train_dataloaders=data_module)
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/lightning/pytorch/trainer/trainer.py", line 538, in fit
    call._call_and_handle_interrupt(
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/lightning/pytorch/trainer/call.py", line 46, in _call_and_handle_interrupt
    return trainer.strategy.launcher.launch(trainer_fn, *args, trainer=trainer, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/lightning/pytorch/strategies/launchers/subprocess_script.py", line 105, in launch
    return function(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/lightning/pytorch/trainer/trainer.py", line 574, in _fit_impl
    self._run(model, ckpt_path=ckpt_path)
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/lightning/pytorch/trainer/trainer.py", line 981, in _run
    results = self._run_stage()
              ^^^^^^^^^^^^^^^^^
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/lightning/pytorch/trainer/trainer.py", line 1025, in _run_stage
    self.fit_loop.run()
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/lightning/pytorch/loops/fit_loop.py", line 206, in run
    self.on_advance_end()
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/lightning/pytorch/loops/fit_loop.py", line 377, in on_advance_end
    call._call_lightning_module_hook(trainer, "on_train_epoch_end")
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/lightning/pytorch/trainer/call.py", line 167, in _call_lightning_module_hook
    output = fn(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^
  File "/data2/mqyu/work/ablation/wb_no_fm/model.py", line 167, in on_train_epoch_end
    auroc_scores = self.train_auroc_metric.compute()
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torchmetrics/metric.py", line 633, in wrapped_func
    value = _squeeze_if_scalar(compute(*args, **kwargs))
                               ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torchmetrics/classification/auroc.py", line 124, in compute
    return _binary_auroc_compute(state, self.thresholds, self.max_fpr)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torchmetrics/functional/classification/auroc.py", line 89, in _binary_auroc_compute
    fpr, tpr, _ = _binary_roc_compute(state, thresholds, pos_label)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torchmetrics/functional/classification/roc.py", line 54, in _binary_roc_compute
    fps, tps, thres = _binary_clf_curve(preds=state[0], target=state[1], pos_label=pos_label)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[rank1]:[E1003 18:37:01.832146912 ProcessGroupNCCL.cpp:607] [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=6463, OpType=ALLREDUCE, NumelIn=1, NumelOut=1, Timeout(ms)=1800000) ran for 1800017 milliseconds before timing out.
[rank1]:[E1003 18:37:01.833575187 ProcessGroupNCCL.cpp:1664] [PG 0 (default_pg) Rank 1] Exception (either an error or timeout) detected by watchdog at work: 6463, last enqueued NCCL work: 6463, last completed NCCL work: 6462.
[rank1]:[E1003 18:37:01.833621509 ProcessGroupNCCL.cpp:1709] [PG 0 (default_pg) Rank 1] Timeout at NCCL work: 6463, last enqueued NCCL work: 6463, last completed NCCL work: 6462.
[rank1]:[E1003 18:37:01.833637681 ProcessGroupNCCL.cpp:621] [Rank 1] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank1]:[E1003 18:37:01.833650825 ProcessGroupNCCL.cpp:627] [Rank 1] To avoid data inconsistency, we are taking the entire process down.
[rank1]:[E1003 18:37:01.838048403 ProcessGroupNCCL.cpp:1515] [PG 0 (default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=6463, OpType=ALLREDUCE, NumelIn=1, NumelOut=1, Timeout(ms)=1800000) ran for 1800017 milliseconds before timing out.
Exception raised from checkTimeout at /opt/conda/conda-bld/pytorch_1724789560443/work/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:609 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x96 (0x7fbeb989ef86 in /data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1d2 (0x7fbebab8bf22 in /data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x233 (0x7fbebab92963 in /data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10c (0x7fbebab94d4c in /data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xd3b75 (0x7fbf1d214b75 in /data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torch/lib/../../../.././libstdc++.so.6)
frame #5: <unknown function> + 0x7ea5 (0x7fbf2c4b0ea5 in /lib64/libpthread.so.0)
frame #6: clone + 0x6d (0x7fbf2bad0b0d in /lib64/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG 0 (default_pg) Rank 1] Process group watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=6463, OpType=ALLREDUCE, NumelIn=1, NumelOut=1, Timeout(ms)=1800000) ran for 1800017 milliseconds before timing out.
Exception raised from checkTimeout at /opt/conda/conda-bld/pytorch_1724789560443/work/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:609 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x96 (0x7fbeb989ef86 in /data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1d2 (0x7fbebab8bf22 in /data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x233 (0x7fbebab92963 in /data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10c (0x7fbebab94d4c in /data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xd3b75 (0x7fbf1d214b75 in /data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torch/lib/../../../.././libstdc++.so.6)
frame #5: <unknown function> + 0x7ea5 (0x7fbf2c4b0ea5 in /lib64/libpthread.so.0)
frame #6: clone + 0x6d (0x7fbf2bad0b0d in /lib64/libc.so.6)

Exception raised from ncclCommWatchdog at /opt/conda/conda-bld/pytorch_1724789560443/work/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1521 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x96 (0x7fbeb989ef86 in /data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0xe52446 (0x7fbeba81e446 in /data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xd3b75 (0x7fbf1d214b75 in /data2/mqyu/anaconda3/envs/rnafm/lib/python3.12/site-packages/torch/lib/../../../.././libstdc++.so.6)
frame #3: <unknown function> + 0x7ea5 (0x7fbf2c4b0ea5 in /lib64/libpthread.so.0)
frame #4: clone + 0x6d (0x7fbf2bad0b0d in /lib64/libc.so.6)

pi.cpp":27, please report a bug to PyTorch. Can't find nvmlDeviceGetNvLinkRemoteDeviceType: /lib64/libnvidia-ml.so.1: undefined symbol: nvmlDeviceGetNvLinkRemoteDeviceType
[1;34mwandb[0m: 🚀 View run [33mlaced-salad-1[0m at: [34mhttps://wandb.ai/leoyu20220822-the-chinese-university-of-hong-kong/ablation_oh_only_train_10-03-17-59/runs/a7a503n3[0m
```

### solution

Just waited for one night and becomes OK


---

#  <span style="color:blue"> Others </span>

---

## <span style="color:green"> 24-11-11 markdone print unable to print latex </span>

### solution

add below to the .md file

```
    <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
    </script>
```


---