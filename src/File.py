# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import hashlib


def open_file(folder, filename, extension):
    """Opens a file and calculates its hashcode.

    Args:
        folder (str): the source folder of the files to rename.
        filename (str): the file name.
        extension (str): the current file extension (.png, .jpg, .gif, .jpeg)

    Returns:
        0 if the file has already been renamed (file name = hashcode).
        rename_file if the file can be renamed.
    """
    path = os.path.join(folder, filename)

    f = open(path, 'rb')
    name = os.path.basename(f.name)
    name = os.path.splitext(name)

    file = f.read()
    f.close()

    hash_code = hashlib.md5(file).hexdigest()

    if name[0] == hash_code:
        return 0, 0

    return rename_file(path, hash_code, extension, folder)


def retrieve_file(folder=os.getcwd()):
    """Runs through all files from specified folder and displays
    the number of file renamed.

    Args:
        folder (str, optional): the source folder of the files to rename.
                                Defaults to current dir.
    """
    # Add extension to rename here
    extensions = {".jpg", ".png", ".gif", ".jpeg"}
    count = 0
    removed = 0

    folder = folder.replace("\"", "")

    for subdir, _, files in os.walk(folder):
        for f in files:
            _, extension = os.path.splitext(f)
            if extension in extensions:
                c, r = open_file(subdir, f, extension)
                count += c
                removed += r

    print("Number of files renamed: {0}".format(count))
    print("Number of files removed: {0}".format(removed))


def rename_file(f, name, extension, folder):
    """Renames files and removes it if duplicate.

    Args:
        f (str): the file path
        name (str): the name to rename to
        extension (str): the original file extension
        folder (str): the destination folder of the new file
                        (same as source folder)

    Returns:
        1
    """
    removed = 0
    new_file = os.path.join(folder, name + extension)
    try:
        os.rename(f, new_file)
    except FileExistsError:
        os.remove(f)
        removed += 1

    return 1, removed
