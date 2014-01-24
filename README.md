A scripting program for eDraw.

INSTALLATION

Until I get around to packaging the module, installation will be a little
amateurish. eDraw requires python > version 3.2 and my strong recommendation
is to use anaconda http://continuum.io/downloads 

Follow the instructions on continuum's page to install anaconda for your
platform. By default, Anaconda comes with python 2.7. We'll need to create
a python 3 environment, but with Anaconda's conda command, this is extremely
easy ( see http://continuum.io/blog/anaconda-python-3 ):

$ conda create -n py3k python=3 anaconda

This creates a virtual environment named py3k, which you can activate with the
source command:

$ source activate py3k

Once you've run this command, you are in the python 3 environment, and you can
install the dependencies for eDraw using pip:

$ pip install svgwrite
$ pip install lxml

FYI, the first (svgwrite) is used for generating svg output, the second (lxml)
is used for high performance XML parsing/serialization.

Now you should have a working environment in which to run eDraw. Download the
github repository and unpack it to the directory of your liking. I strongly
suggest running eDraw out of ipython, which is a glorified python interpreter
with several useful features (it was installed with anaconda).

If we want to import eDraw, we'll need to add the path of the directory where
you've extracted it to our path. I know this is silly, and it will be fixed
soon.

Start ipython, then

import sys
sys.path.append('your-eDraw-directory')

Now statements such as

import eDraw

should not throw an error.

As for actually using the module, see bin/ for example scripts and data/ for 
their output.
