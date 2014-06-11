import unittest
from grid import Grid

class GridTests(unittest.TestCase):

    def testSetsNodeAttributes(self):
        # not attributes in the networkx sense, just in the sense that the node object itself can store a value.
        test_attrs = [ x for x in range(0, 16) ] # 0 - 15
        should_be = list(zip(test_attrs, test_attrs))
        self.g = Grid(test_attrs)
        self.assertEqual(sorted(self.g.nodes()), should_be)

    #def testRejectsWrongLengthAttributes(self):

    def setUp(self):
        test_attrs = [ x for x in range(0, 16) ] # 0 - 15
        self.g = Grid(test_attrs)

    def testDefaultSizeIs4x4(self):
        self.assertEqual(self.g.SIZE, (4, 4))

    def testHasAppropriateNumberOfNodes(self):
        self.assertEqual(len(self.g.nodes()), 16)

    #def testForGridStyleEdges(self):
