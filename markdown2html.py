#!/usr/bin/python3
"""
Write a script markdown2html.py that takes two string arguments:

    First argument is the name of the Markdown file
    Second argument is the output file name
"""

import sys
import os


def parse_heading(line):
    """Parse and convert Markdown headings to HTML."""
    # Strip the leading spaces and count the number of '#' characters
    stripped_line = line.lstrip()
    heading_num = len(stripped_line) - len(stripped_line.lstrip('#'))

    # Check if the line is a valid Markdown heading
    if 1 <= heading_num <= 6:
        # Remove '#' characters and any leading/trailing spaces from the text
        content = stripped_line[heading_num:].strip()
        return f"<h{heading_num}>{content}</h{heading_num}>\n"
    return line


def check_arg():
    """ Check if the number of arguments is correct"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)






if __name__ == '__main__':
    check_arg()
    sys.exit(0)

