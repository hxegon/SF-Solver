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

  def get_candidate_neighbors_for(self, node):
    x, y = node[0], node[1] 
    xp, xm, yp, ym = x+1, x-1, y+1, y-1
    adjacent = [(xp, y), (xm, y), (x, yp), (x, ym)]
    adjacent = [ x for x in adjacent if -1 not in x ]
    adjacent = [ x for x in adjacent if 4 not in x ]

    diagonal = [(xp, yp), (xm, ym), (xm, yp), (xp, ym)]
    diagonal = [ x for x in diagonal if -1 not in x ]
    diagonal = [ x for x in diagonal if 4 not in x ]
    return { 'adjacent': adjacent, 'diagonal': diagonal }
