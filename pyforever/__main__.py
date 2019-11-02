#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
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

    proc = subprocess.Popen(args)
    return proc


async def _watch(args, proc=None):
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
    async for _ in watchgod.awatch(path):
        if proc is not None:
            proc.kill()
        proc = _run(args)


def main():
    if len(sys.argv) == 1:
        sys.stderr.write("No arguments supplied.\n")
        sys.stderr.flush()
        exit(1)

    args = [sys.executable] + sys.argv[1:]

    # run once and start watching then
    proc = _run(args, clear=False)
    asyncio.run(_watch(args, proc))


if __name__ == "__main__":
    main()
