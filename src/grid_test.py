import unittest
from grid import Grid

class GridTests(unittest.TestCase):

    def testSetsNodeAttributes(self):
        # not attributes in the networkx sense, just in the sense that the node object itself can store a value.
        test_attrs = [ x for x in range(0, 16) ] # 0 - 15
        should_be = [(0,0), (1,1), (2,2), (3,3), (4,4), (5,5),
                (6,6), (7,7), (8,8), (9,9), (10,10), (11, 11),
                (12, 12), (13, 13), (14, 14), (15, 15)]
        self.g = Grid(test_attrs)
        self.assertEqual(sorted(self.g.nodes()), should_be)

    def setUp(self):
        test_attrs = [ x for x in range(0, 16) ] # 0 - 15
        self.g = Grid(test_attrs)

    def testDefaultSizeIs4x4(self):
        self.assertEqual(self.g.SIZE, (4, 4))

    def testHasAppropriateNumberOfNodes(self):
        self.assertEqual(len(self.g.nodes()), 16)


    # do we need coord style nodes?
    #def testForGridStyleEdges(self):
