#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
import hashlib
import shutil
import re

def open_file(folder, filename):
    """Opens a file and calculates its hashcode.

    Args:
        folder (str): the source folder of the files to rename.
        filename (str): the file name.
    """
    path = os.path.join(folder, filename)
    _, extension = os.path.splitext(path)

    f = open(path, 'rb')
    name = os.path.basename(f.name)
    name = os.path.splitext(name)
    
    fichier = f.read()
    f.close()

    hash_code = hashlib.md5(fichier).hexdigest()

    if name[0] == hash_code:
        return

    rename_file(path, hash_code, extension, folder)


def retrieve_file(folder=os.getcwd()):
    """Runs through all files from specified folder.

    Args:
        folder (str, optional): the source folder of the files to rename. Defaults to current dir.
    """
    reg = re.compile('[.]')

    folder = folder.replace("\"", "")
    
    for subdir, _, files in os.walk(folder):
        if not re.search(reg, subdir):
            for f in files:
                if not re.match(reg, f):
                    open_file(subdir, f)
            


def rename_file(f, name, extension, folder):
    """Renames files and removes it if duplicate.

    Args:
        f (str): the file path
        name (str): the name to rename to
        extension (str): the original file extension
        folder (str): the destination folder of the new file (same as source folder)
    """
    new_file = os.path.join(folder, name + extension)
    try:
        os.rename(f, new_file)
    except FileExistsError:
        os.remove(f)
