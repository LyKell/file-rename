#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import File

def main():
    if (len(sys.argv) != 2):
        File.retrieve_file()

    else:
        File.retrieve_file(sys.argv[1])


if __name__ == "__main__":
    main()

