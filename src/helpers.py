import os

def imageDirectory(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)