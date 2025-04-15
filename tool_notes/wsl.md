1. mount to a usb device on windows:
    (https://askubuntu.com/questions/1116200/how-can-i-access-my-usb-drive-from-my-windows-subsystem-for-linux-ubuntu-dist)
    > Create the mount point: mkdir /mnt/g (add whatever word or letter you want, I used the matching letter to the windows drive. You might need to use sudo to create the directory in the /mnt directory.)
    > Mount the drive to the directory using sudo mount -t drvfs G: /mnt/g