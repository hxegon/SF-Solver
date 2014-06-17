# Cooper LeBrun <cooperlebrun@gmail.com>

import networkx as nx

class Grid(nx.DiGraph):
  """
  Nodes take the form of coordinate tuples ((0,1)), using nx's node attributes (dicts) to store their value

  Initializes:
  [x] Nodes
  [x] Values
  [x] Edges
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

    # Initialize edges
    for node in self.nodes():
      self.add_edges_from(self.find_edges_of(node))


  def get_candidate_neighbors(self, node):
    x, y, n = node[0], node[1], self.nodes()
    adjacent = [ x for x in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if x in n ]
    diagonal = [ x for x in [(x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)] if x in n ]
    return { 'adjacent': adjacent, 'diagonal': diagonal }

  def find_edges_of(self, node):
    candidates = self.get_candidate_neighbors(node)
    edges = []
    edges += [ x for x in candidates['adjacent'] if self.node[x]['value'] % 2 == 0 ]
    edges += [ x for x in candidates['diagonal'] if self.node[x]['value'] % 2 == 1 ]
    return [ (node, x) for x in edges ]
