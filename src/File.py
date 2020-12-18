#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
import hashlib
import shutil

def open_file(folder, filename):
    path = os.path.join(folder, filename)
    _, extension = os.path.splitext(path)

    f = open(path, 'rb').read()
    hash_code = hashlib.md5(f).hexdigest()

    rename_file(path, hash_code, extension, folder)


def retrieve_file(folder=os.getcwd()):
    for filename in os.listdir(folder):
        open_file(folder, filename)


def rename_file(f, new_name, extension, folder):
    new_file = os.path.join(folder, new_name + extension)
    os.rename(f, new_file)
