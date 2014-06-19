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

    def testGetCandidateNeghborsFor(self):
        fixture = self.g.get_candidate_neighbors((0,1))
        self.assertEqual(sorted(fixture['adjacent']), [(0,0), (0,2), (1,1)])
        self.assertEqual(sorted(fixture['diagonal']), [(1,0), (1,2)])

        fixture = self.g.get_candidate_neighbors((3,3))
        self.assertEqual(sorted(fixture['adjacent']), [(2,3), (3,2)])
        self.assertEqual(sorted(fixture['diagonal']), [(2,2)])

class ValueTests(unittest.TestCase):

    def setUp(self):
        self.g = Grid([ i for i in range(0, 16) ])

    def testAssignsValues(self):
        self.assertEqual(self.g.node[(0,0)]['value'], 0)

    def testPathValues(self):
        self.assertEqual(self.g.path_values([(0, 1), (0, 2), (0, 3)]), [1, 2, 3])

class EdgeTests(unittest.TestCase):

    def testMakesCorrectEdges(self):
        g = Grid([x for x in range(0, 16)])
        self.assertEqual(sorted(g.out_edges((1,2))),
                sorted([((1,2), (0,1)), ((1,2), (0,2)), ((1,2), (0,3)),
                 ((1,2), (2,1)), ((1,2), (2,2)), ((1,2), (2,3))]))
