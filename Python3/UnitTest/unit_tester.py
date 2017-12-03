"""
This illustrates the basic use of the unittest module to automate unit tests of
a simple class.  There are many more options in the documentation, but this is
what I would consider a minimum example for testing any custom class.

This also serves as a good example of how to set up your own modules to be
importable.  Installing them to be available anywhere is out of scope, but this
will work for portable modules that you wish to include as part of a software package.

Note the empty __init__.py file to indicate that the module is exportable.  When in
doubt, use the "tree" command and inspect the directory tree as seen by Python.
"""
import unittest

# Use the local version of BSTree.py in the folder this is run from
import sys
CLASSPATH = "."
sys.path.insert(0, CLASSPATH)

from BSTree.BSTree import *

TESTVALS_int = [5,6,10,3,2,1,8,7,9,4]

# To provide a regular test framework, define a
# derived testcase class
class simpleBST(unittest.TestCase):

    # Setup is called before every test case
    def setUp(self):
        self.BSTree = BSTree()
        assert self.BSTree is not None
        assert self.BSTree.size == 0

    # Tear down is called after every test case
    def tearDown(self):
        self.BSTree = None



class TestingBSTree(simpleBST):

    def test_empty(self):
        self.assertTrue(self.BSTree.size == 0)

    def test_insert(self):
        self.BSTree.insert(99)
        self.assertTrue(self.BSTree.contains(99))

    def test_remove(self):
        self.BSTree.insert(88)
        self.BSTree.remove(88)
        self.assertFalse(self.BSTree.contains(88))

    def test_size(self):
        self.assertTrue(self.BSTree.size == 0)
        self.BSTree.insert(88)
        self.assertTrue(self.BSTree.size == 1)
        self.BSTree.remove(88)
        self.assertTrue(self.BSTree.size == 0)

    def test_pre_order(self):
        for val in TESTVALS_int:
            self.BSTree.insert(val)
        expected = [5, 3, 2, 1, 4, 6, 10, 8, 7, 9]
        self.assertTrue(expected == [x for x in self.BSTree.pre_order_traversal()])

    def test_post_order(self):
        for val in TESTVALS_int:
            self.BSTree.insert(val)
        expected = [1,2,4,3,7,9,8,10,6,5]
        self.assertTrue(expected == [x for x in self.BSTree.post_order_traversal()])

    def test_in_order(self):
        for val in TESTVALS_int:
            self.BSTree.insert(val)
        expected = [1,2,3,4,5,6,7,8,9,10]
        self.assertTrue(expected == [x for x in self.BSTree.in_order_traversal()])


# Run the tests
if __name__ == "__main__":
    # Simplest way to run
    #unittest.main()

    # More options
    mySuite = unittest.TestLoader().loadTestsFromTestCase(TestingBSTree)
    unittest.TextTestRunner(verbosity=2).run(mySuite)
