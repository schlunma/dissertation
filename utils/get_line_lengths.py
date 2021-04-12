#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is used to produce materials for the following work:

# Doctoral Dissertation
# (c) by Manuel Schlund

# This work is licensed under a
# Creative Commons Attribution 4.0 International License.

# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

"""Get maximum line length of all ``tex`` files."""

from pathlib import Path


ROOT = Path(__file__).parents[1].resolve()


def get_file_as_str(filename):
    """Read file and return ``str``."""
    with open(filename, 'r') as f_in:
        file_contents = f_in.read()
    return file_contents


def check_file(filename):
    """Check single file."""
    with open(filename, 'r') as f_in:
        lines = f_in.readlines()
    max_length = 0
    max_length_idx = 0
    for (idx, line) in enumerate(lines):
        idx += 1
        if len(line) > max_length:
            max_length = len(line)
            max_length_idx = idx
    print(f"File '{filename}':")
    print(f"    Maximum line length is {max_length:4d}, first appearance in "
          f"line {max_length_idx:5d}")
    print()


def main():
    """Main function."""
    print(f"Using root path '{ROOT}'")
    print()

    # Iterate over all tex files
    tex_files = ROOT.rglob('*.tex')
    for filename in tex_files:
        check_file(filename)


if __name__ == '__main__':
    main()
