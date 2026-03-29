# general notes on how to run

Choose the type and num of GPU, and deploy. Then either use the terminal / jupyter notebook provided by runpod. Or connect to it with vscode.

1. Deploy a pod:
   homepage -> (left side bar) Pods -> choose and deploy

   NOTE: set the disk size larger to 400GB is OK

2. Running notes:
   1. Note: store all files under the `/workspace` dir! otherwise after stop everything will be lost

# Network Volume

For storing large, permanent files (eg dataset). When deploying a GPU pod, select the network volume want to mount, and the data will be mounted to /workspace.

Find network volume at "Storage" section.

- can only increase size, not decrease


# Run runpod on vscode

1. On windows cmd
   1. ```ssh-keygen -t ed25519```
   2. ```type %USERPROFILE%\.ssh\id_ed25519.pub``` for windows, ```cat``` for mac to get ssh publich keys
   3. go to run pod home page, `settings` -> `SSH Public Keys` to get key -> update the key
   4. Get a pod (note when newing this pod, must click allow SSH (is allowed by default))
   5. On the pod page, click connect and can see `SSH over-exposed TCP`, use the ssh command and just connect it in VSCode.
   <!-- 6. When connect to VS code, will let you to choose an IP address, choose the same seen in step 5 -->

   6. to scp: `eg scp -r -P 24413 -i ~/.ssh/id_ed25519 Desktop/fk73k_nonoi_pretrain root@195.26.233.54:/root`
   7. if env installed in network volume, everytime need to `source anaconda3/bin/activate`
