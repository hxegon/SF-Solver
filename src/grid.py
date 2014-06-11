# Cooper LeBrun <cooperlebrun@gmail.com>

import networkx as nx

class Grid(nx.DiGraph):
    # responsible for making a graph in the structure of a grid and filling it with values, but not enforcing rules.

    def __init__(self, attributes):
        """
        1. Checks input
        2. Makes Graph from input
        """
        self.SIZE = (4, 4) # could be any size but doesn't need to
        super().__init__(self)

        # Is it ok to just have 1-16 nodes or are coords needed?
        self.add_nodes_from(zip([x for x in range(0, 16)], attributes))
