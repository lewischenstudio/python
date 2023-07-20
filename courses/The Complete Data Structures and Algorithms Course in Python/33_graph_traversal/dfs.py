"""
Depth First Search
Time complexity: O(V+E)
Space complexity: O(V+E)
   A
  / \ 
 /   \ 
B     C
| \   |
|  \  |  
|   \ |  
|    \|  
D --- E 
 \   /
  \ /
   F
"""  # noqa


class Graph:
    def __init__(self, gdict=None) -> None:
        self.gdict = gdict or {}

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:  # O(V)
            print("queue: ", stack)
            popVertex = stack.pop()
            print("popVertex: ", popVertex)
            for adjacentVertex in self.gdict[popVertex]:  # O(E)
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)


customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f", "c"],
    "f": ["d", "e"],
}
graph = Graph(customDict)
graph.dfs("a")
