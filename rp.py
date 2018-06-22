#!/usr/bin/python2
# This script batch renames multiple files in a directory
# Mainly for 
from os import rename, listdir
import sys

global renameDir 
renameDir = "."

def matching_files_exist_in_dir(stringToBeReplaced, dir):
    if( not dir.endswith('/') ):
        dir += '/'

    fnames = listdir(dir)

    for fname in fnames:
        if( fname.find(stringToBeReplaced) > -1 ):
          return True
    return False


def renameFiles(stringToBeReplaced, stringToReplaceOld, isPreview):

    global renameDir

    if( not renameDir.endswith('/') ):
        renameDir += '/'

    fnames = listdir(renameDir)

    for fname in fnames:
        if( fname.find(stringToBeReplaced) > -1 ):
            newName = fname.replace(stringToBeReplaced, stringToReplaceOld)
            if( isPreview == False ): 
                rename( renameDir + fname, renameDir + newName)
                #print renameDir+fname
            else:
                print "  '" + fname+"' => '"+newName+"'"

if( len(sys.argv) < 3 ):
    print "This script batch renames multiple files in a directory"
    print "Please pass the args. stringToBeReplaced stringToReplaceOld  [renameDir='/var/www/rl/files']"
    print "ex 1: python rp.py \"--\" \"-\" "
    print "      converts \"name1--name2\" to \"name1-name2\" "
    print "ex 2: python rp.py \"--\" \"-\" \"/var/www/rl/files/\" "
    print "      converts \"name1--name2\" to \"name1-name2\" in directory \"/var/www/rl/files/\" "


elif(len(sys.argv) >= 3):
    stringToBeReplaced = sys.argv[1]
    stringToReplaceOld = sys.argv[2]

    if(len(sys.argv) == 4):
        print "args = 4"
        renameDir = sys.argv[3]
    
    if matching_files_exist_in_dir(stringToBeReplaced, renameDir):
      print "Will be renaming these files:"
      renameFiles(stringToBeReplaced, stringToReplaceOld, True ) #isPreview = True

      print "Are you sure u want to rename?[Y]/n"
      reponseY = raw_input()
      
      if(reponseY == "y" or reponseY == ""):
          renameFiles(stringToBeReplaced, stringToReplaceOld, False) #isPreview = False
          print "All files renamed!"
      else:
          print "Canceled by user!"

else:
    print "unknown error"





