#!/bin/bash 
cred="leech1"
playlist="$2"

echo "videos to upload:"
var1=$1
if [[ $var1 = "-h" || $var1 = "" ]]; then 
	echo "pass args as follow in quotes \"*.*\" then playlist "
	echo "ex 1: ./youtube-batch_up.sh \"1*\" \"ttc playlist\" "
	echo "ex 2: ./youtube-batch_up.sh \"1* 2*\" \"ttc playlist\" "
	exit 0;
fi

numOfVidToUp=0
for f in $var1; do
	if [[ -e f ]]; then
		echo $f
		((numOfVidToUp++))
	fi
done

if [[ $numOfVidToUp -gt 0 ]]; then
	echo "will upload $numOfVidToUp videos."
else
	echo "No files found mactching your filter!"
	exit 1;
fi

read -p "do you want to upload them?y/n: " response
if [[ ! $response = "y" ]]; then
	exit 1;
fi

numOfVidUploaded=0
for f in $var1; do
	#echo $f
	command="youtube-upload --privacy=\"unlisted\" --playlist=\"$playlist\" --credentials-file=leech1  -t $f $f"
	#echo $command
	eval $command
	((numOfVidUploaded++))
	sleep 5
done 
echo "Uploaded $numOfVidUploaded/$numOfVidToUp"
