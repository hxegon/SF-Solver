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

    for i in range(0, self.SIZE[0] * self.SIZE[1]):
      self.add_node(i, value=attributes[i])
