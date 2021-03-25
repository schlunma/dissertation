#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is used to produce materials for the following work:

# Doctoral Dissertation
# (c) by Manuel Schlund

# This work is licensed under a
# Creative Commons Attribution 4.0 International License.

# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

from pathlib import Path


ROOT = Path(__file__).parents[1].resolve()


def add_header(filename, header):
    """Add header to a single file."""
    with open(header, 'r') as f_in:
        header_str = f_in.read()
    with open(filename, 'r+') as f_out:
        file_contents = f_out.read()
        if file_contents.startswith(header_str):
            print(f"    Skipping {filename} which alread contains header "
                  f"{header}")
            return
        f_out.seek(0, 0)
        f_out.write(header_str)
        f_out.write(file_contents)
    print(f"    Wrote header {header} to file {filename}")


def add_headers(pattern, header):
    """Add header to all files that match a pattern."""
    print(f"Writing header {header} to all files matching {ROOT / pattern}")
    files = ROOT.rglob(pattern)
    for filename in files:
        add_header(filename, header)
    print()


def main():
    """Main function."""
    print(f"Using root path {ROOT}")
    print()
    add_headers('*.py', 'HEADER_PY')
    add_headers('*.tex', 'HEADER_TEX')
    add_headers('*.yml', 'HEADER_YML')


if __name__ == '__main__':
    main()
