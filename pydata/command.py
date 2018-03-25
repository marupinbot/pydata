#!/usr/bin/env python
# coding: utf-8

from argparse import ArgumentParser

parsers = ArgumentParser(
    progress="pydata",
    usage='%(progress)s [-l] [-o] project',
    description="Location list and Organizer List on PyData"
    )

parsers.add_argument(
    "-l",
    action="store_true",
    default=False,
    help="You can see lists of all PyData location."
    )

parsers.add_argument(
    "-o",
    action="store",
    nargs=1,
    help="You can see lists of PyData organizer."
    )



