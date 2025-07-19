# want a full environemt with cuda, pytorch, tensorflow


####### issues met
# 1. I ask for cuda=11.8, by `conda install nvidia/label/cuda-11.8.0::cuda-toolkit -y`
#    but when checking by `nvcc --version` it installed cuda=12.2


# 1. first decide which version of cuda to use.
# cuda=11.8 usually most compatible, but can also refer to the GPU version
# then can check the pytorch website: https://pytorch.org/get-started/locally/
# which tells you that 1. there is a pytorch choice for cuda=11.8, and 2. python must 3.9 or later

# 2. so install python
conda create -n cuda118 python=3.9 -y

# 3. then install cudatoolkit 11.8, 
# ❌ from this website: https://anaconda.org/nvidia/cuda-toolkit, find the command
# ❌ conda install nvidia/label/cuda-11.8.0::cuda-toolkit -y
# not the above command, but:
conda install conda-forge::cudatoolkit=11.8.0  -y

# to check for successful installation, can run:
nvcc --version
nvidia-smi

# 4. then can install pytorch. from the pytorch website, find the command
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# to check for successful installation, can run:
python -c "import torch; print(torch.__version__)"
python -c "import torch; print(torch.cuda.is_available())"
python -c "import torchvision; print(torchvision.__version__)"
python -c "import torchaudio; print(torchaudio.__version__)"

# 5. then can install tensorflow. from the tensorflow website, find the command
# note: `pip install tensorflow` is for cpu not gpu!!
# check this website for compatible tensorflow version: https://www.tensorflow.org/install/source#gpu
pip install tensorflow[and-cuda]==2.14.0

# to check for successful installation, can run:
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"