# Cooper LeBrun <cooperlebrun@gmail.com>

import networkx as nx

class Grid(nx.DiGraph):
  """
  Wraps nx.DiGraph
  Handles initializing nodes, values and edges in 4x4 grid manner.
  """

  def __init__(self, attributes):
    self.SIZE = (4, 4) # could be any size but doesn't need to
    super().__init__(self)

    # Is it ok to just have 1-16 nodes or are coords needed?
    self.add_nodes_from(zip([x for x in range(0, 16)], attributes))
