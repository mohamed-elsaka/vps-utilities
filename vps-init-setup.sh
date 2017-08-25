echo "=================================";
echo "Updating system...";
eval 'apt-get -y update';

echo "=================================";
echo "Upgrading system...";
echo "-------------------";
eval 'apt-get -y upgrade';

echo "=================================";
echo "Installing pip & unzip ...";
echo "-----------------";
eval 'apt-get -y install unzip python-pip';
eval 'pip install -U pip'

echo "=================================";
echo "Installing aria2 ...";
echo "-----------------------------";
eval "apt-get -y install aria2";

echo "=================================";
echo "Installing youtube-dl...";
echo "------------------------";
eval 'curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/bin/youtube-dl';
eval 'chmod a+rx /usr/bin/youtube-dl';

echo "=================================";
echo "Installing rp.py ...";
echo "--------------------";
eval 'curl -L https://github.com/pythonoma/vps-utilities/raw/master/rp.py -o /usr/bin/rp.py';
eval 'chmod a+rx /usr/bin/rp.py';


echo "=================================";
echo "Installing prefix.py ...";
echo "--------------------";
eval 'curl -L https://github.com/pythonoma/vps-utilities/raw/master/prefix.py -o /usr/bin/prefix.py';
eval 'chmod a+rx /usr/bin/prefix.py';

echo "=================================";
echo "Installing youtube-upload ...";
echo "-----------------------------";
eval 'pip install --upgrade google-api-python-client progressbar2';
eval 'wget https://github.com/tokland/youtube-upload/archive/master.zip';
eval 'unzip master.zip';
eval 'cd youtube-upload-master';
eval 'sudo python setup.py install';

eval 'cd ..';
eval 'rm master.zip';
eval 'rm -rf youtube-upload-master';

echo "=================================";
echo "Installing internetarchive...";
echo "-----------------------------";
eval 'pip install internetarchive';
