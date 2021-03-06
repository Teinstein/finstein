# Welcome to Finstein Library!

Finstein is a Library for performing various financial calculation tasks. Check DOCS for more info.

This Guide will help you set up the library.

**Project Report** - *https://docs.google.com/document/d/1LR-W4EDnaMJOEfQIT7pVvhHi-7t5b51rz76mmLPxPdg/edit?usp=sharing*

**Directory tree:**
 - setup.py
 - Tests
 - Finstein
 - DOCS
 - README.md
 

## Running Tests
- All test modules can be run at a time by simply opening a shell/cmd terminal in the **Tests** directory and typing -``python -m unittest``
- To run a particular test type :``python -m unittest test_1.py `` 
**Note: unittest should be installed on your system.**


## Installing and Uninstalling the Library
- Finstein Library can be directly installed by typing ``pip install Finstein`` in the terminal.
- The Finstein Library can be installed be running the following command in the root directory of the library folder as well after cloning the repo  : ``pip install .``
- Dependencies : **Scipy, Numpy** (will be automatically installed during pip installation of Library)
- Also the library can be easily uninstalled using the following pip command : ``pip uninstall Finstein``

## Accessing & Generating Docs

- To access the docs in HTML version, a shortcut to index.html is provided in DOCS folder.
- To generate the new docs, first delete the Finstein.rst file present in the folder to generate a new one. Then enter the following commands in  shell/cmd terminal in the DOCS folder : (**Note** - Generate docs everytime the code is updated )

 ``sphinx-apidoc -o . ../Finstein/``

 ``make html``
