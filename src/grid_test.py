import unittest
from grid import Grid

class GridTests(unittest.TestCase):

    def testSetsNodeAttributes(self):
        test_attrs = [ x for x in range(0, 16) ] # 0 - 15
        self.g = Grid(test_attrs)

    def setUp(self):
        self.g = Grid()

    def testDefaultSizeIs4x4(self):
        self.assertEqual(self.g.SIZE, (4, 4))

    def testHasAppropriateNumberOfNodes(self):
        self.assertEqual(len(self.g.nodes()), 16)


    # do we need coord style nodes?
    #def testForGridStyleEdges(self):
