class Finder:
    
    def __init__(self, graph):
        self.graph = graph

    def find_paths_from(self, start_point):
        stack = [[start_point]]
        accumulator = []
        while stack:
            path = stack.pop()
            neighbors = self.graph.neighbors(path[-1])
            neighbors = [ n for n in neighbors if n not in path ] # Don't use the same node twice
            if not neighbors:
                accumulator.append(path)
            else:
                for n in neighbors:
                    stack.append(path + [n])
        return accumulator

    def find_all_paths(self):
        accumulator = [] # possibly not needed?
        for n in self.graph.nodes():
            accumulator += self.find_paths_from(n)
        return accumulator
