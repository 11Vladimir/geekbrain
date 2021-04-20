#!/usr/bin/env python3


import os
import sys


files = sys.argv[1]


def find_files(files):
    if files in os.listdir(os.getcwd()):
        dirpath, filename = os.path.split(os.path.abspath(files))
        print(filename.split('.')[0])


find_files(files)