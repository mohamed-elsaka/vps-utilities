#!/bin/bash 
ps_username="$1"
ps_password="$2"

first_course_url=$3
if [[ $first_course_url = "-h" || $first_course_url = "" ]]; then 
        echo "pass username, password & course urls as example:"
        echo "psdown.sh username password \"https://app.pluralsight.com/library/courses/django-angularjs-web-development\" "
        exit 0;

elif [[ $first_course_url = "-f" ]]; then
        ps_links_file=$4
        while IFS= read -r course_url; do
                command="youtube-dl --username $ps_username --password $ps_password --autonumber-size 2 $course_url -o './%(playlist)s/%(autonumber)s_%(title)s.%(ext)s'"
                #echo $command
                eval $command
                echo "------------------Finished Downloading the course-------------------"

        done < "$ps_links_file"

else
        for course_url in "${@:3}"; do
                command="youtube-dl --username $ps_username --password $ps_password --autonumber-size 2 $course_url -o './%(playlist)s/%(autonumber)s_%(title)s.%(ext)s'"
                #echo $command
                eval $command
                echo "------------------Finished Downloading the course-------------------"
        done
fi

