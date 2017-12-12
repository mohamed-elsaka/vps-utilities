# vps-utilities

Some python and bash scripts I use in my Linux sysadmin

=> VPS initial setup:

```
curl -L https://github.com/pythonoma/vps-utilities/raw/master/vps-init-setup.sh -o /usr/bin/vps-init-setup.sh

chmod a+rx /usr/bin/vps-init-setup.sh 

vps-init-setup.sh
```

-------------------------------------------------------------
=> VNC install:

```
curl -L https://github.com/pythonoma/vps-utilities/raw/master/vncinstall.sh -o /usr/bin/vncinstall.sh

chmod a+rx /usr/bin/vncinstall.sh 

vncinstall.sh
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


Youtube-dl:
--------------------------------------------------------------

Download Pluralsight course:
```
youtube-dl -u USERNAME -p PASSWORD -o "%(playlist)s/%(chapter_number)s. %(chapter)s/%(playlist_index)s. %(title)s.%(ext)s" --sleep-interval 40 COURSE_URL
```

Download Udemy course:
```
youtube-dl -u USERNAME -p PASSWORD -o '%(playlist)s/%(chapter_number)s.%(chapter)s-%(autonumber)s_%(title)s.%(ext)s' COURSE_URL
```


FFMPEG4
--------------------------------------------------------------

Compress all videos using FFMPEG4
```
for i in *.*; do eval "ffmpeg -i '${i}' -c:v libx264 -preset slow -crf 28 -c:a copy '$(echo ${i} | cut -f 1 -d '.').mp4'"; done
```

Compress all WAV audio files to M4A 
```
for i in *.wav; do eval "ffmpeg -i '${i}'  -c:a aac -strict -2 -vbr 5 '$(echo ${i} | cut -f 1 -d '.').m4a'"; done
 ```
 


Create 1G Swap memory file:
---------------------------------------------------------------

```
sudo fallocate -l 1G /mnt/1GB.swap
sudo mkswap /mnt/1GB.swap
sudo swapon /mnt/1GB.swap
sudo echo '/mnt/1GB.swap  none  swap  sw 0  0' >> /etc/fstab
sudo swapon -s
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

Delete all ``*.ext`` files in subfolders:
```
find . - name *.ext -type f -delete
```
