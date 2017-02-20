"""
This module is about how to reuse code using packages

Code can be organised into reusable components using
* Functions
* Classes
* Modules
* Packages

Functions and Classes go into Modules
Modules goes into Packages

This file is module while the folder in which it is saved is called its package.
Packages can be hierarchial in nature based on groups of their features.

To make these folder discoverable in Python as package trees, include a file
called '__init__.py' in each of the folders. Without this file, non-pythonic
code will be accessible in a python program outside of this package structure.

To use code in this module, use the 'import' keyword followed by the path to the
module with each folder being separted by a full stop.
"""
import top.top_module 			as top
import top.sub1.sub1_module 	as sub1

from top.sub1.sub2 	import sub2_module as sub2
from top.sub3 		import sub3_module as sub3

top.print_details()
sub1.print_details()
sub2.print_details()
sub3.print_details()
