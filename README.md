# vps-utilities

Some python and bash scripts I use in my Linux sysadmin

=> VPS initial setup:

```
curl -L https://github.com/pythonoma/vps-utilities/raw/master/vps-init-setup.sh -o /usr/bin/vps-init-setup.sh

chmod a+rx /usr/bin/vps-init-setup.sh 
```

-------------------------------------------------------------
=> To download multiple files at same time:

```aria2c -c -j=10 -i urls.txt```

```-c``` => continue non fininshed files.

```-j``` => max conccurent downloads.

```-i``` => file urls input file


-------------------------------------------------------------
=> Upload to archive.org:

```ia configure```
```
 ia upload <identifier> *.* --metadata="mediatype:movies"
```
