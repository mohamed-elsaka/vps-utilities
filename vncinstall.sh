eval "sudo apt-get -y update";
eval "sudo apt install -y xfce4 xfce4-goodies tightvncserver midori filezilla deluge unrar unzip"; 
eval "vncserver";
eval "vncserver -kill :1";
eval "sleep 4s";
eval "mv ~/.vnc/xstartup ~/.vnc/xstartup.bak";
echo -e "#!/bin/bash \nxrdb $HOME/.Xresources \nstartxfce4 &" > ~/.vnc/xstartup ;
eval "sudo chmod +x ~/.vnc/xstartup";
eval "vncserver";
