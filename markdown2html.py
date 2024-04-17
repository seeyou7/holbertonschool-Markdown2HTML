#!/usr/bin/python3

import sys
import os

def check_arguments():
    """ Check if the number of arguments is correct"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

# Check if the input file exists
    if not os.path.exists(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)





if __name__ == '__main__':
    check_arguments()

