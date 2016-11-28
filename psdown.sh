#!/bin/bash 
ps_username="$1"
ps_password="$2"
course_url="$3"

var1=$1
if [[ $var1 = "-h" || $var1 = "" ]]; then 
        echo "pass username, password & course url as example:"
        echo "psdown.sh username password \"https://app.pluralsight.com/library/courses/django-angularjs-web-development\" "
        exit 0;
fi

command="youtube-dl --username $ps_username --password $ps_password --autonumber-size 2 $course_url -o '%(autonumber)s_%(title)s.%(ext)$
#echo $command
eval $command
echo "------------------Finished Downloading the course-------------------"




