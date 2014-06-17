import unittest
import networkx as nx
from finder import Finder

class FinderTests(unittest.TestCase):

    def setUp(self):
        g = nx.DiGraph()
        g.add_nodes_from([0, 1, 2, 3, 4])
        g.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4)]) # Can't go from 1 to 3, or 2 to 1
        self.f = Finder(g)
    
    def testFindsAPath(self):
        # should return a new path as long as there are any new paths
        test = sorted(self.f.find_paths_from(0))
        self.assertEqual(test, [[0, 1, 3], [0, 1, 4], [0, 2]])
