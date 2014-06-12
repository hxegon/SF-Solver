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
        self.assertEqual(sorted(self.g.get_candidate_neighbors_for((0,1))['adjacent']), [(0,0), (0,2), (1,1)])
        self.assertEqual(sorted(self.g.get_candidate_neighbors_for((0,1))['diagonal']), [(1,0), (1,2)])

        self.assertEqual(sorted(self.g.get_candidate_neighbors_for((3,3))['adjacent']), [(2,3), (3,2)])
        self.assertEqual(sorted(self.g.get_candidate_neighbors_for((3,3))['diagonal']), [(2,2)])

