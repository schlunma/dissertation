#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is used to produce materials for the following work:

# Doctoral Dissertation
# (c) by Manuel Schlund

# This work is licensed under a
# Creative Commons Attribution 4.0 International License.

# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

"""Search regex in ``pdf`` file ignoring whitespace.

Examples
--------
python search_in_pdf.py '.{40}\s+1[^A-Za-z0-9].{40}'

"""


import re
import sys
from pathlib import Path

import pdftotext


PATH = Path(__file__).parents[1].resolve() / 'Dissertation_Manuel_Schlund.pdf'


def search(filename, pattern, replace_whitespace_char=' '):
    """Search for pattern in filename."""
    with open(filename, 'rb') as f_in:
        pdf_pages = pdftotext.PDF(f_in)
    pdf_str = '\n\n'.join(pdf_pages)
    pdf_str = re.sub('\s+', replace_whitespace_char, pdf_str)
    matches = re.findall(pattern, pdf_str)
    if not matches:
        return
    print("Found {len(matches):d} matche(s)")
    for match in matches:
        print(f"    {match}")


def main():
    """Main function."""
    if len(sys.argv) != 2:
        raise ValueError(f"Expected exactly one command line argument for "
                         f"regex pattern, got {len(sys.argv) - 1:d}")
    pattern = sys.argv[1]
    print(f"Searching file '{PATH}'")
    print(f"Using regex pattern '{pattern}'")
    print()

    # Search in file
    search(PATH, pattern)


if __name__ == '__main__':
    main()
