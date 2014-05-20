# Cooper LeBrun <cooperlebrun@gmail.com>

import networkx as nx

class Grid(nx.DiGraph):
    # responsible for making a graph in the structure of a grid and filling it with values, but not enforcing rules.

    def __init__(self):
        """
        Could be modified to take any size Grid?
        1. Checks input
        2. Makes Graph from input
        """
        self.SIZE = (4, 4)
        super().__init__(self)

        for i in range (0, self.SIZE[0] * self.SIZE[1]):
            self.add_node(i)    
