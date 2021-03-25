# Dissertation

[![CC BY 4.0][cc-by-shield]][cc-by]

This repository contains my doctoral dissertation.


# Compilation From Source

To compile the document from source, use the following commands:

    pdflatex -synctex=1 -interaction=nonstopmode Dissertation_Manuel_Schlund.tex
    biber Dissertation_Manuel_Schlund.tex
    pdflatex -synctex=1 -interaction=nonstopmode Dissertation_Manuel_Schlund.tex
    pdflatex -synctex=1 -interaction=nonstopmode Dissertation_Manuel_Schlund.tex


# License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
