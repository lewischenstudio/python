"""
Breadth First Search
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

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:  # O(V)
            print("queue: ", queue)
            deVertex = queue.pop(0)
            print("deVertex: ", deVertex)
            for adjacentVertex in self.gdict[deVertex]:  # O(E)
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)


customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "e"],
}
graph = Graph(customDict)
graph.bfs("a")
