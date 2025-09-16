# System and configuration
1.	add PATH: 
```vim ~/.bashrc``` or ```~/.profile```
write: ```export PATH="/path/to/your/directory:$PATH"```
apply ```change: source ~```
verify: 

1. find the path of a command：
    ```which pip```
    ```where pip```  
    使用特定的pip： 
    1. cd到这个虚拟环境所在的pip.exe的目录下然后用pip install
    1. 或者：/mnt/t9/mqyu/.conda/envs/RNA-FM/bin/pip install rna-fm  

# Conda 

## conda basics

    1. create environment
        ```
        conda create -n <env_name> [python=3.6]
        ```

    1.	conda install 
        specify version:
        ```conda install <pkg>=<version>```

    1.	delete: 
        ```conda remove --name ENV_NAME --all```
        all means all the packages

    1. list info
        list environments: ```conda env list```
        list packages: ```conda list```

    1. search version
    ```conda search```	
    check all versions: 
        ```conda search -f```

    1. conda storage management
    
        conda environment some times take up very big spaces. To clean the environment, first remove environments no longer wanted; then clean the cache by: `conda clean --all`

    1. clone: 
    ```
    conda create --name venv2 --clone venv1 
    ```

    1. add/remove channels: 
    ```
    conda config –add / --remove channels <name>
    ```

    or to directly `vim vim ~/.condarc`

## Install conda w/o sudo

1. install 
    ```
    wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh
    bash Anaconda3-2024.02-1-Linux-x86_64.sh
    source anaconda3/bin/activate
    conda init
    ```
    The `wget` file can be fund at https://repo.continuum.io/archive  

1. manually activate conda

    ```
    cd ~
    eval "$( path_to_anaconda3/anaconda3/bin/conda shell.bash hook )"
    # then should see `(base)`
    conda activate base
    ```

## conda channel / mirror related

1. show all sources: 
```
conda config --show channels
```

2. 查看channel名字：
   cat ~/.condarc
	或 conda config --show channels

3. 删除 
   conda config --remove channels CHANNEL_NAME

4. 添加镜像：
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro 
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
conda install -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ r-essentials
pip install -i https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ package
```

# Yaml or requirements.txt

## 1. requirments.txt

```pip install requirements.txt```
or
```conda install --yes --file requirements.txt``` 

note: `--yes` or `-y` means don't need to type `y`.

## 2. yml

1. create env
```
conda env export > env.yml
conda env create  -f env.yml
```


# pytorch, cuda

**have version matching, careful**


## check version

1. check cuda version: 
   ```conda list cuda-toolkit```
1. check pytorch version: 
   ```python, import torch, print(torch.cuda.is_available())```
1. check torch’s certain cuda version: 
  ```print(torch.version.cuda)```

## Install 

1. Check cuda driver version: 
    cuda driver is usually installed in the server, 
    use `nvidia-smi` to check, right top will be a line called `cuda version`, which is the cuda driver version
1. determine the cuda toolkit version and install
    1. Cuda toolkit version not higher than cuda driver version is OK
    1. ~~Find cuda toolkit download script at https://developer.nvidia.com/cuda-toolkit-archive~~
        If without sudo, install cuda toolkit via conda: https://anaconda.org/nvidia/cuda-toolkit 
    1. Check cuda version and verify
    - Note: to check Linux version, architecture, and distribution, see `Useful-Notes-and-Logs/code_n_commands/tool_notes/linux/general_linux.md`
1. find compatible pytroch version and install
   on https://pytorch.org/ 

**Available:**

```
# cuda=11.8
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
conda install nvidia/label/cuda-11.8.0::cuda

# cuda=12.1
conda create -n cuda121 python=3.10
conda install nvidia/label/cuda-12.1.1::cuda-toolkit
pip install torch==2.3.1 torchvision==0.18.1 --index-url https://download.pytorch.org/whl/cu121
pip install timm==0.6.12
pip install mmengine==0.2.0
``` 

## check if successfully installed

```
python
>>> import torch                    # to check if torch installed
>>> torch.cuda.is_available()       # to check if cuda installed
True
>>> torch.cuda.device_count()
2
```

# TensoFlow

1. Install
    ```Conda install tensorflow-gpu```

**Available:**
(just create new env and just `conda install tensorflow-gpu`, let it choose for you)
or: install tensorflow with indicated version first
```
conda install tensorflow=2.1    # then python=3.7 is automatically installed
```

1. Check:
```tf.test.is_gpu_available()```
```tf.config.list_physical_devices('GPU')```


 

