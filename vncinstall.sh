eval "sudo apt-get -y update";
eval "sudo apt install -y xfce4 xfce4-goodies tightvncserver firefox handbrake filezilla deluge unrar unzip p7zip"; 
eval "vncserver";
eval "vncserver -kill :1";
eval "sleep 4s";
eval "mv ~/.vnc/xstartup ~/.vnc/xstartup.bak";
echo -e "#!/bin/bash \nxrdb $HOME/.Xresources \nstartxfce4 &" > ~/.vnc/xstartup ;
eval "sudo chmod +x ~/.vnc/xstartup";
eval "vncserver";
eval "sudo fallocate -l 1G /mnt/1GB.swap && sudo mkswap /mnt/1GB.swap && sudo swapon /mnt/1GB.swap && sudo echo '/mnt/1GB.swap none swap sw 0 0' >> /etc/fstab && sudo swapon -s";
