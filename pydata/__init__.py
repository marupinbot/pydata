#!/usr/bin/env python
# coding: utf-8

import sys
import traceback
from pydata.list import PyData
from pydata.command import parsers

def main():

    argv = sys.argv
    argv = argv[1:]

    if len(argv) == 0:
        parsers.parse_args(["-h"])
        sys.exit(0)

    args = parsers.parse_args(argv)

    try:
        if args.l:
            PyData.scraping()

        if args.o:
            print('test')

    except Exception as e:
        t, v, tb = sys.exc_info()
        error = traceback.format_exception(t, v, tb)
        print(error[0])
        print(error[1])
        print(error[2])

if __name__ == "__main__":
    main()