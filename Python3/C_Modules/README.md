This outlines the basic process for defining and installing C methods for access by a
Python installation (AKA C extensions).  This was reworked from a tutorial posted here:
https://tutorialedge.net/python/python-c-extensions-tutorial/

The basic premise is to define a number of handles that Python.h can use to interact with
the Python interpreter.  After completing this, you should be able to import your extension and
use it in Python3.*

Setup instructions:
The files herein should be placed in their final resting place, look to your Python installation
to determine where installed modules should live.  You will need sudo privileges.

 ```bash
 python3 setup.py build
 python3 setup.py install
 ```
