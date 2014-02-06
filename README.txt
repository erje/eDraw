A scripting program for eDraw. License is LGPL3+. Requires lxml and svgwrite.

INSTALLATION

eDraw requires python 3+. 

I strongly recommend using Anaconda from Continuum:

http://continuum.io/downloads

By default, Anaconda comes with python 2.7. You will need to create a python 3 environment using the conda command ( see http://continuum.io/blog/anaconda-python-3 ):

    conda create -py3k python=3 anaconda

Running this command will install a python 3 environment "py3k". Once installed, you need to install eDraw's dependencies:

$ pip install svgwrite
$ pip install lxml

svgwrite is used for generating svg output, and lxml is used for high performance XML parsing/serialization.

Now install eDraw:

$ pip install eDraw

The best eDraw tutorial is installed in the docs/examples directory (see docs/examples/output for reference). Syntax is designed to be similar to matplotlib's pyplot.

Don't forget that when you want to work with eDraw, you need to activate the py3k environment:

$ activate py3k

Contact me with problems: http://www.github.com/erje/eDraw
