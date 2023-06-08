#!/usr/bin/python3
from sys import argv

if (len(argv) == 1):
    print("0 arguments.")
elif len(argv) > 1:
    if len(argv) == 2:
        print("{}".format(len(argv) - 1) + " argument")
    else:
        print("{}".format(len(argv) - 1) + " arguments")
    for arg in range(1, len(argv)):
        print("{}: {}".format(arg, argv[arg]))
