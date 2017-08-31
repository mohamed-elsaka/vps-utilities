#!/usr/bin/env python
# This script batch renames multiple files in a directory
# Mainly for
from os import rename, listdir
import sys
import argparse

def renameFiles(stringToBeReplaced, stringToReplaceOld, isPreview, renameDir='.'):
    if(not renameDir.endswith('/')):
        renameDir += '/'

    fnames = listdir(renameDir)

    for fname in fnames:
        if(fname.find(stringToBeReplaced) > -1):
            newName = fname.replace(stringToBeReplaced, stringToReplaceOld)
            if(isPreview == False):
                rename(renameDir + fname, renameDir + newName)
                # print renameDir+fname
            else:
                print("  '" + fname + "' => '" + newName + "'")


ar2en = {
	'ﻻ': 'la',
	'ﻷ': 'la2',
	'ﻵ': 'l2a',
    'د': 'd',
    'ج': 'g',
    'ح': '7',
    'خ': 'kh',
    'ه': 'h',
    'ع': '3',
    'غ': 'gh',
    'ف': 'f',
    'ق': 'q',
    'ث': 'th',
    'ص': 's',
    'ض': 'd',
    'ذ': 'z',
    'ط': 't',
    'ك': 'k',
    'م': 'm',
    'ن': 'n',
    'ت': 't',
    'ا': 'a',
    'أ': 'a',
    'إ': 'e',
    'آ': 'a',
    'ل': 'l',
    'ب': 'b',
    'ي': 'e',
    'س': 's',
    'ش': 'sh',
    'ظ': 'z',
    'ز': 'z',
    'و': 'o',
    'ة': 'h',
    'ى': 'a',
    'ر': 'r',
    'ؤ': '2o',
    'ء': '2a',
    'ئ': '2e',
    '١': '1',
    '٢': '2',
    '٣': '3',
    '٤': '4',
    '٥': '5',
    '٦': '6',
    '٧': '7',
    '٨': '8',
    '٩': '9',
    '٠': '0'
}

parser = argparse.ArgumentParser(
    description='Converts Arabic file names to English (Franco)')
parser.add_argument('-d', '--directory',
                    help='Directory containing files to be converted.', default='.')

args = vars(parser.parse_args())
arg_directory = args['directory']

for key, value in ar2en.items():
    renameFiles(key, value, False, arg_directory)
