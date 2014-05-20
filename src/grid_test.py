import unittest
from grid import Grid

class GridTests(unittest.TestCase):

    def setUp(self):
        self.g = Grid()

    def testDefaultSizeIs4x4(self):
        self.assertEqual(self.g.SIZE, (4, 4))

    def testHasAppropriateNumberOfNodes(self):
        self.assertEqual(len(self.g.nodes()), 16)

    #def testForGridStyleEdges(self):
