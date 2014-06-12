# Cooper LeBrun <cooperlebrun@gmail.com>

import networkx as nx

class Grid(nx.DiGraph):
  """
  Nodes take the form of coordinate tuples ((0,1)), using nx's node attributes (dicts) to store their value

  Initializes:
  [x] Nodes
  [x] Values
  [ ] Edges
  """

  def __init__(self, attributes):
    self.SIZE = (4, 4) # could be any size but doesn't need to
    super().__init__(self)

    # Initalize nodes
    for x in range(0, self.SIZE[0]):
      for y in range(0, self.SIZE[1]):
        self.add_node((x, y))

    # Initialize values
    for node, val in zip(sorted(self.nodes()), attributes):
      self.node[node]['value'] = val
