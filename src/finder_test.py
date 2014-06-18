import unittest
import networkx as nx
from finder import Finder

class FinderTests(unittest.TestCase):

    def setUp(self):
        self.g = nx.DiGraph()
        self.f = Finder(self.g)
    
    def testFindsAPath(self):
        self.g.add_nodes_from([0, 1, 2, 3, 4])
        self.g.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4)]) # Can't go from 1 to 3, or 2 to 1

        test = sorted(self.f.find_paths_from(0))
        self.assertEqual(test, [[0, 1, 3], [0, 1, 4], [0, 2]])

    def testHandlesCyclicGraphs(self):
        self.g.add_nodes_from([0, 1, 2])
        self.g.add_edges_from([(0, 1), (1, 2), (2, 0)])

        test = sorted(self.f.find_paths_from(0))
        self.assertEqual(sorted(self.f.find_paths_from(0)), [[0, 1, 2]])
