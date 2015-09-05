#!/usr/bin/env python

# This script batch adds a prefix to multiple files in a directory
# Mainly for 

from os import rename, listdir
import sys

global renameDir 
renameDir = "/var/www/rl/files/"

def renameFiles(fname, isPreview):
    global renameDir 

    newName = stringPrefix + fname
    if( isPreview == False ):
        rename( renameDir+fname, renameDir+newName)
    else:
        print "  '" + fname+"' => '"+newName+"'"

def do_renameFiles(isPreview):
    global renameDir 
    
    if( not renameDir.endswith('/') ):
        renameDir += '/'

    fnames = listdir(renameDir)
    for fname in fnames:
        if(stringFind == "--serial"):
            if(fname[0].isdigit() and fname[1].isdigit()):
                renameFiles(fname, isPreview)

        elif( fname.startswith(stringFind) ):
                renameFiles(fname, isPreview)

if( len(sys.argv) < 3 ):
    print "This script batch adds a prefix to multiple files in a directory"
    print "Please pass the args. stringFind stringPrefix [renameDir='/var/www/rl/files']"
    print "ex 1: python prefix.py \"intro_to_shoot_house\" \"Panteao-\" "
    print "      converts \"intro_to_shoot_house_01\" to \"Panteao-intro_to_shoot_house_01\" "

    print "ex 2: python prefix.py \"--serial\" \"Panteao-\" "
    print "      adds \"Panteao-\" as a prefix of any file whose name starts with 2 numbers.e.g. \"01-help.mp3\" "

elif(len(sys.argv) >= 3):
    stringFind = sys.argv[1]
    stringPrefix = sys.argv[2]

    if(len(sys.argv) == 4):
        renameDir = sys.argv[3]
    
    print "Will be renaming these files:"
    do_renameFiles(True)

    print "Are you sure u want to rename?y/n"
    reponseY = raw_input()
    
    if(reponseY == "y"):
       do_renameFiles(False)
       print "All files renamed!"
    else:
        print "Canceled by user!"

else:
    print "unknown error"




