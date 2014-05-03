# Cooper LeBrun <cooperlebrun@gmail.com>

# 1. Generate a directional Graph with 4x4 coordinates and no edges
# 2. Add coordinate values from given grid
# 3. Determine edges and add to graph
# 4. Find all Hamiltonian Paths in graph.
# 4a. If no Hamiltonian paths, find all Hamiltonian^-1 paths
# 5. Calculate scores and compare for highest

import networkx as nx

class Grid(nx.Graph):

    def __init__(self):
        """
        Could be modified to take any size Grid.
        """
    
    def set_grid(self, numbers):
        """
        Numbers should be an array of numbers
        rename?
        """

    #def find_paths(self):

    def find_edges(self):
        """
        Internal?
        """


class Solver:
    #def __init__(self, start_point):
    pass
        


# 1. Generate a directional Graph with 4x4 coordinates and no edges
# 2. Add coordinate values from given grid
# 3. Determine edges and add to graph
# 4. Find all Hamiltonian Paths in graph.
# 4a. If no Hamiltonian paths, find all Hamiltonian^-1 paths
# 5. Calculate scores and compare for highest
