"""
Question 1: Route Between Nodes

Given a directed graph and two nodes (S and E), design an algorithm to find
out whether there is a route from S to E.

customDict = {
    "a" : ["c","d", "b"],
    "b" : ["j"],
    "c" : ["g"],
    "d" : [],
    "e" : ["f", "a"],
    "f" : ["i"],
    "g" : ["d", "h"],
    "h" : [],
    "i" : [],
    "j" : []
}

g = Graph(customDict)
g.checkRoute("a", "j") #True
"""


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def checkRoute(self, startNode, endNode):
        visited = [startNode]
        queue = [startNode]
        while queue:
            deVertex = queue.pop(0)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    if adjacentVertex == endNode:
                        return True
                        break
                    else:
                        visited.append(adjacentVertex)
                        queue.append(adjacentVertex)
        return False


customDict = {
    "a": ["c", "d", "b"],
    "b": ["j"],
    "c": ["g"],
    "d": [],
    "e": ["f", "a"],
    "f": ["i"],
    "g": ["d", "h"],
    "h": [],
    "i": [],
    "j": [],
}


g = Graph(customDict)
print(g.checkRoute("a", "e"))
