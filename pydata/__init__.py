#!/usr/bin/env python
# coding: utf-8

import sys
import logging
import traceback
import pydata
from command import parsers

def main():

    argv = sys.argv
    argv = argv[1:]

    if len(argv) == 0:
        parsers.parse_args(["-h"])
        sys.exit(0)

    args = parsers.parse_args(argv)

    try:
        if args.l:
            pydata.PyData.scraping()

    except Exception as e:
        logging.error(traceback.format_exc())

if __name__ == "__main__":
    main()