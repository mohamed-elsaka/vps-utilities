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

```aria2c -c -j10 -i urls.txt```

```-c``` => continue non fininshed files.

```-j``` => max conccurent downloads.

```-i``` => file urls input file


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
