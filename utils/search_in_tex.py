#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is used to produce materials for the following work:

# Doctoral Dissertation
# (c) by Manuel Schlund

# This work is licensed under a
# Creative Commons Attribution 4.0 International License.

# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

"""Search regex in all ``tex`` files ignoring line breaks.

Examples
--------
python search_in_tex.py '(?i).{25}[\.\)]\s*\\.{0,12}cite\{.{25}'
python search_in_tex.py '(?i).{25}[\.\)]\s*\\.{0,12}ac.{0,12}\{.{25}'
python search_in_tex.py '(?i).{25}[\.\)]\s*\\.{0,12}ref.{0,12}\{.{25}'

python search_in_tex.py '(?i)\\caption\[.*?\]\{.*?\\label' | egrep -iC 999 '\\ac\{'
python search_in_tex.py '(?i)\\begin\{tabular.*?\}.*?\\end\{tabular.*?\}' | egrep -iC 999 '\\ac\{'

python search_in_tex.py '.{20}\\[aA]{1}c[fl]?[p]?\{[^\}]+\}[^\s,\.\)\}\:;'']+?.{20}'

python search_in_tex.py '.{20}ly-.{20}'

python search_in_tex.py '.{20}\s+[Aa][n]?\s+\\[Aa]c.{20}'

python search_in_tex.py '\\.{0,7}ref.?\{' | sort -u

python search_in_tex.py '.{50}figure[s]?[^\}A-Za-z]+.{50}'

"""


import re
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1].resolve()


def get_file_as_str(filename):
    """Read file and return ``str``."""
    with open(filename, 'r') as f_in:
        file_contents = f_in.read()
    return file_contents


def search(filename, pattern, replace_linebreak_char=' '):
    """Search for pattern in filename."""
    file_str = get_file_as_str(filename)
    file_str_no_lb = file_str.replace('\n', replace_linebreak_char)
    matches = re.findall(pattern, file_str_no_lb)
    if not matches:
        return
    print(f"In file '{filename}', found {len(matches):d} matche(s)")
    for match in matches:
        print(f"    {match}")
    print()


def main():
    """Main function."""
    if len(sys.argv) != 2:
        raise ValueError(f"Expected exactly one command line argument for "
                         f"regex pattern, got {len(sys.argv) - 1:d}")
    pattern = sys.argv[1]
    print(f"Using root path '{ROOT}'")
    print(f"Using regex pattern '{pattern}'")
    print()

    # Iterate over all tex files
    tex_files = ROOT.rglob('*.tex')
    for filename in tex_files:
        search(filename, pattern)


if __name__ == '__main__':
    main()
