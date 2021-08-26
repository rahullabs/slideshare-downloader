import os
import shutil

def imageDirectory(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)

def rmdir(dir):
    shutil.rmtree(dir)
    