class Path:

    def __init__(self):
        self.current = None
        self.history = []

    def goto(self, node):
        if self.history == []:
            self.last = None
        else:
            self.last = self.history[-1]
        if node in self.history: # if node previously visited
            raise Exception
        self.current = node
        self.history.append(node)
