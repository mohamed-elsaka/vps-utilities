echo "=================================";
echo "Updating system...";
eval 'apt-get -y update';

echo "=================================";
echo "Upgrading system...";
echo "-------------------";
eval 'apt-get -y upgrade';

echo "=================================";
echo "Installing tree ...";
echo "-----------------";
eval "apt-get -y install tree";

echo "=================================";
echo "Installing pip, npm & unzip ...";
echo "-----------------";
eval 'apt-get -y install unzip npm python-pip';
eval "ln -s /usr/bin/nodejs /usr/bin/node";
eval 'pip install -U pip'

echo "=================================";
echo "Installing aria2 ...";
echo "-----------------------------";
eval "apt-get -y install aria2";

echo "=================================";
echo "Installing renamer ...";
echo "-----------------";
eval 'sudo npm install -g renamer';

echo "=================================";
echo "Installing sanitize-filenames ...";
echo "------------------------";
eval 'curl -L https://raw.githubusercontent.com/pythonoma/vps-utilities/master/sanitize-filenames.sh -o /usr/bin/sanitize-filenames';
eval 'chmod a+rx /usr/bin/sanitize-filenames';

echo "=================================";
echo "Installing youtube-dl...";
echo "------------------------";
eval 'curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/bin/youtube-dl';
eval 'chmod a+rx /usr/bin/youtube-dl';
eval 'pip install -U youtube_dl'

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
echo "Installing youtube-batch_up...";
echo "------------------------";
eval "curl -L https://github.com/pythonoma/vps-utilities/raw/master/youtube-batch_up.sh -o /usr/bin/youtube-batch_up.sh"
eval "chmod a+rx /usr/bin/youtube-batch_up.sh"
 
echo "=================================";
echo "Installing internetarchive...";
echo "-----------------------------";
eval 'pip install internetarchive';
