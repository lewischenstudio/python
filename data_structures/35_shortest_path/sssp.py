"""
Single Source Shortest Path
Time complexity: O(V+E)
Space complexity: O(V+E)
A -- B # noqa
|    |\ 
|    | \ 
|    |  \ 
C -- D   G
|    |  /
|    | /
|    |/
E -- F
"""


class Graph:
    def __init__(self, gdict=None):
        self.gdict = gdict or {}

    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                print("queue: ", queue)
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return queue


customDict = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"],
}


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
print(g.bfs("a", "e"))
