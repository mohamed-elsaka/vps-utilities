#!/usr/bin/env python
from os import rename, listdir
import sys

if(len(sys.argv) < 2):
    print "Please pass the args. stringToBeReplaced stringToReplaceOld"
elif(len(sys.argv) == 2):
    #if(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print "Please pass the args. stringToBeReplaced stringToReplaceOld"
elif(len(sys.argv) == 3):
    stringToBeReplaced = sys.argv[1]
    stringToReplaceOld = sys.argv[2]

    fnames = listdir('.')
    for fname in fnames:
        if( fname.find(stringToBeReplaced) > -1 ):
            newName = fname.replace(stringToBeReplaced, stringToReplaceOld, 1)
            rename(fname, newName)
            print "'" + fname + "' is'" + newName + "' \n"

else:
    print "unknown error"



