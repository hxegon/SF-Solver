import unittest
from grid import Grid

class NodeTests(unittest.TestCase):

    def testSetsNodeAttributes(self):
        test_attrs = [ x for x in range(0, 16) ] # 0 - 15
        self.g = Grid(test_attrs)
        for x in range(0, 16):
            self.assertEqual(self.g.node[x]['value'], x)

    def setUp(self):
        test_attrs = [ x for x in range(0, 16) ] # 0 - 15
        self.g = Grid(test_attrs)

    def testHasAppropriateNumberOfNodes(self):
        self.assertEqual(len(self.g.nodes()), 16)

#class EdgeTests(unittest.TestCase):

    #def testMakesCorrectEdges(self):
