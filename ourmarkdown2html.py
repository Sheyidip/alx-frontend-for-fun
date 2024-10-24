#!/usr/bin/python3
"""
    Markdown to Html
    a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file
    Second argument is the output file name
"""
import sys
import os
""" sys for args and os to check file"""

def check_markdown(markdownFile, htmlFile):
    """ markdown to html"""
    if len(sys.argv) != 3:
        """ check the arg len """
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        sys.exit(1)

    markdownFile = sys.argv[1]
    htmlFile = sys.argv[2]


    if not os.path.isfile(markdownFile):
        """check markdown if it is a markdownfile"""
        sys.stderr.write(f'Missing {markdownFile}\n')
        sys.exit(1)

sys.exit(0)
