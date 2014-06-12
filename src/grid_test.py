import unittest
from grid import Grid

class NodeTests(unittest.TestCase):

    def testSetsNodeAttributes(self):
        self.g = Grid([ x for x in range(0, 16) ])
        for x, y in zip(sorted(self.g.nodes()), range(0, 16)):
            self.assertEqual(self.g.node[x]['value'], y)

    def setUp(self):
        self.g = Grid([ x for x in range(0, 16) ])

    def testHasAppropriateNumberOfNodes(self):
        self.assertEqual(len(self.g.nodes()), 16)

#class EdgeTests(unittest.TestCase):

    #def testMakesCorrectEdges(self):
