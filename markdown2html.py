#!/usr/bin/env python3

import sys
import os
import markdown

# Check if the number of arguments is less than 2
if len(sys.argv) != 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

# Get the input and output file names from the arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the Markdown file exists
if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# Read the Markdown file and convert it to HTML
try:
    with open(input_file, 'r') as md_file:
        markdown_text = md_file.read()
        html_content = markdown.markdown(markdown_text)

    # Write the HTML content to the output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

    sys.exit(0)  # Success

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)  # Error
