# vps-utilities

Some python and bash scripts I use in my Linux sysadmin

=> VPS initial setup:

```
curl -L https://github.com/pythonoma/vps-utilities/raw/master/vps-init-setup.sh -o /usr/bin/vps-init-setup.sh

chmod a+rx /usr/bin/vps-init-setup.sh 

vps-init-setup.sh
```

-------------------------------------------------------------
=> To download multiple files at same time:

```aria2c -c -x10 -j10 -i urls.txt```

```-c``` => continue non fininshed files.

```-j``` => max conccurent downloads.

```-i``` => file urls input file

Or to batch download:

```
aria2c -c -x10 -j10 -Z -P 'http://example.com/[0-100].mp3'
```

-------------------------------------------------------------
=> Unzip multiple zip files at once:

```unzip '*.zip'```

```rm *.zip```

-------------------------------------------------------------
=> Save folder structre to files-tree.txt:

```tree . >> files-tree.txt```

-------------------------------------------------------------
=> Move all files in subfolders to main folder:

```for d in */; do mv  "$d"* "$d"../;done```

-------------------------------------------------------------
=> (Optional) Remove all folders

```rm -rf */```

-------------------------------------------------------------
=> Upload to archive.org:

```ia configure```
```
 ia upload <identifier> *.* --metadata="mediatype:movies"
```

youtube-dl:
--------------------------------------------------------------

Download Pluralsight course:
```
youtube-dl -u USERNAME -p PASSWORD -o "%(playlist)s/%(chapter_number)s. %(chapter)s/%(playlist_index)s. %(title)s.%(ext)s" --sleep-interval 40 COURSE_URL
```

Download Udemy course:
```
youtube-dl -u USERNAME -p PASSWORD -o '%(playlist)s/%(chapter_number)s.%(chapter)s-%(autonumber)s_%(title)s.%(ext)s' COURSE_URL
```


Misc:
---------------------------------------------------------------

Repeat command every X seconds:
```
while clear; do date; command;sleep 5; done
```

Monitor disk space:
```
while clear; do date; df -h;sleep 5; done
```

Monitor directory files count:
```
while clear; do date; find . -type f | wc -l ;sleep 5; done
```
