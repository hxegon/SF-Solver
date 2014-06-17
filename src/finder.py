import networkx as nx
import pdb

class Finder:
    
    def __init__(self, graph):
        self.graph = graph
        self.paths = []

    #def find_paths_from(self, start_point, history=[], paths=[]):
    #    # NOT MEM SAFE, DON'T USE FOR LARGE GRAPHS ( > O(N^e) where e is > 5 )
    #    history.append(start_point)
    #    #pdb.set_trace()
    #    if self.graph.neighbors(start_point) == []: # and start_point != history[-1]
    #        return history
    #    else:
    #        paths += [ self.find_paths_from(n, history.copy(), paths) for n in self.graph.neighbors(start_point) if n not in history ]
    #        return paths


    def find_paths_from(self, start_point):
        # history really isn't needed
        neighbors = self.graph.neighbors(start_point)
        if neighbors == []:
            return [start_point]
        else:
            return [ [start_point] + self.find_paths_from(n) for n in neighbors ]


#G = nx.DiGraph()
#G.add_nodes_from([0, 1, 2, 3, 4])
#G.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4)]) 
#F = Finder(G)
#paths_final = F.find_paths_from(0)
