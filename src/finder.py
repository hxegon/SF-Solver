class Finder:
    
    def __init__(self, graph):
        self.graph = graph

    def find_paths_from(self, start_point):

        def recursive_search(stack, accumulator):
            if not stack:
                return accumulator
            path = stack.pop()
            neighbors = self.graph.neighbors(path[-1])
            neighbors = [ n for n in neighbors if n not in path ] # Don't use the same node twice
            if not neighbors:
                accumulator.append(path)
            else:
                for n in neighbors:
                    stack.append(path + [n])
            return recursive_search(stack, accumulator)
        return recursive_search([[start_point]], [])
