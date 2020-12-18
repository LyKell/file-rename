#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys

def open_file(filename, folder):
    with open(os.path.join(folder, filename), 'r') as f:
        print(f.name)


def retrieve_file(folder=os.getcwd()):
    for filename in os.listdir(folder):
        open_file(filename, folder)


