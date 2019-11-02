#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys

import watchgod


def _run(args, clear=True):
    """
    Run the executable
    :param args: The full path and arguments to be run
    :param clear: Whether to clear the console or not (default: True)
    """

    if clear:
        os.system("cls") if os.name == "nt" else os.system("clear")

    p = subprocess.Popen(args)
    p.wait()


def _watch(args):
    """
    Run the executable on changes
    :param args: The full path and arguments to be run
    """

    path = os.getcwd()
    if os.path.isfile(sys.argv[1]):
        path = os.path.dirname(os.path.abspath(sys.argv[1]))
    print("Watching for changes in", path, "...")
    print()

    # re-run the script if the current directory changes
    for _ in watchgod.watch(path):
        _run(args)


def main():
    if len(sys.argv) == 1:
        sys.stderr.write("No arguments supplied.\n")
        sys.stderr.flush()
        exit(1)

    args = [sys.executable] + sys.argv[1:]

    # run once and start watching then
    _run(args, clear=False)
    _watch(args)


if __name__ == "__main__":
    main()
