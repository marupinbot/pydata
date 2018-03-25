#!/usr/bin/env python
# coding: utf-8

import sys
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
            print(list)

    except Exception as e:
        error_type = type(e).__name__
        sys.stderr.write("{0}: {1}\n".format(error_type, e.message))
        sys.exit(1)

if __name__ == "__main__":
    main()