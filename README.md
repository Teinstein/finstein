# Welcome to Finstein Library!

This Guide will help you set up the library.

**Directory tree:**
 - setup.py
 - Tests
 - Finstein
 - DOCS
 - README.md
 

## Running Tests
- All test modules can be run at a time by simply opening a shell/cmd terminal in the **Tests** directory and typing -``python -m unittest``
- To run a particular test type :``python -m unittest test_1.py `` 


## Installing and Uninstalling the Library

- The Finstein Library can be installed be running the following command in the root directory of the library folder : ``pip install .``
- Dependencies : **Scipy** (will be automatically installed during pip installation of Library)
- Also the library can be easily uninstalled using the following pip command : ``pip uninstall Finstein``

## Accessing & Generating Docs

- To access the docs in HTML version, a shortcut to index.html is provided in DOCS folder.
- To generate the new docs file enter the following commands in  shell/cmd terminal : (**Note** - Generate docs everytime the code is updated )
 ``sphinx autodoc -o . ../Finstein``
 ``make html``