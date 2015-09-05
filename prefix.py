#!/usr/bin/env python

# This script batch adds a prefix to multiple files in current directory
# Mainly for 

from os import rename, listdir
import sys

def renameFiles(fname):
    newName = stringPrefix + fname
    rename(fname, newName)
    print "'" + fname+"' => '"+newName+"'"

if( len(sys.argv) < 3 ):
    print "This script batch adds a prefix to multiple files in current directory"
    print "Please pass the args. stringFind stringPrefix"
    print "ex 1: python prefix.py \"intro_to_shoot_house\" \"Panteao-\" "
    print "      converts \"intro_to_shoot_house_01\" to \"Panteao-intro_to_shoot_house_01\" "

    print "ex 2: python prefix.py \"--serial\" \"Panteao-\" "
    print "      adds \"Panteao-\" as a prefix of any file whose name starts with 2 numbers.e.g. \"01-help.mp3\" "

elif(len(sys.argv) == 3):
    stringFind = sys.argv[1]
    stringPrefix = sys.argv[2]

    fnames = listdir('.')
    for fname in fnames:
        if(stringFind == "--serial"):
            if(fname[0].isdigit() and fname[1].isdigit()):
                renameFiles(fname)

        elif( fname.startswith(stringFind) ):
                renameFiles(fname)

else:
    print "unknown error"

