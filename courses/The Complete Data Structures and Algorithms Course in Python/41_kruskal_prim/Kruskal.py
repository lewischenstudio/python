"""
Kruskal Algorithm  in Python

Graph 1
              5
       A ----------- B
     / |            /|
15 /   |          /  |
 /     |         /   |
E   13 |    10 /     | 8
 \     |     /       |
20 \   |   /         |
     \ | /           |
       C ----------- D
              6

Graph 2
              5
       A ----------- B
     / |            /|
15 /   |          /  |
 /     |         /   |
E   13 |    10 /     | 8
 \     |     /       |
20 \   |   /         |
     \ | /           |
       C ----------- D
       |      6 
    11 | 
       |  
       F  


Graph 2
              5
       A ----------- B
     / |            /|
15 /   |          /  |
 /     |         /   |
E   13 |    10 /     | 8
 \     |     /       |
20 \   |   /         |
     \ | /           |
       C ----------- D
       |      6      |
    11 |             | 16
       |             |
       F ----------- G
              13
"""

import disjointSet as dst


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, start, end, weight):
        self.graph.append([start, end, weight])

    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, start, end, weight):
        path = self.MST[0][0]
        for start, end, weight in self.MST:
            print("%s - %s: %s" % (start, end, weight))
            if end not in path:
                if len(path) == 1:
                    path += end
                elif start == path[0]:
                    path = end + path
                else:
                    path += end
                if start not in path:
                    path += start
        print("path: ", path)
        return path

    def kruskal(self):
        index, edge = 0, 0
        ds = dst.DisjointSet(self.nodes)
        # sort the graph based on weights
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while edge < self.vertices - 1:
            start, end, weight = self.graph[index]
            index += 1
            x = ds.find(start)
            y = ds.find(end)
            if x != y:
                edge += 1
                self.MST.append([start, end, weight])
                ds.union(x, y)
        self.printSolution(start, end, weight)


def graph_1():
    g = Graph(5)
    g.addNode("A")
    g.addNode("B")
    g.addNode("C")
    g.addNode("D")
    g.addNode("E")
    g.addEdge("A", "B", 5)
    g.addEdge("A", "C", 13)
    g.addEdge("A", "E", 15)
    g.addEdge("B", "A", 5)
    g.addEdge("B", "C", 10)
    g.addEdge("B", "D", 8)
    g.addEdge("C", "A", 13)
    g.addEdge("C", "B", 10)
    g.addEdge("C", "E", 20)
    g.addEdge("C", "D", 6)
    g.addEdge("D", "B", 8)
    g.addEdge("D", "C", 6)
    g.addEdge("E", "A", 15)
    g.addEdge("E", "C", 20)
    g.kruskal()


def graph_2():
    g = Graph(6)
    g.addNode("A")
    g.addNode("B")
    g.addNode("C")
    g.addNode("D")
    g.addNode("E")
    g.addNode("F")
    g.addEdge("A", "B", 5)
    g.addEdge("A", "C", 13)
    g.addEdge("A", "E", 15)
    g.addEdge("B", "A", 5)
    g.addEdge("B", "C", 10)
    g.addEdge("B", "D", 8)
    g.addEdge("C", "A", 13)
    g.addEdge("C", "B", 10)
    g.addEdge("C", "E", 20)
    g.addEdge("C", "D", 6)
    g.addEdge("D", "B", 8)
    g.addEdge("D", "C", 6)
    g.addEdge("E", "A", 15)
    g.addEdge("E", "C", 20)
    g.addEdge("C", "F", 11)
    g.kruskal()


def graph_3():
    g = Graph(7)
    g.addNode("A")
    g.addNode("B")
    g.addNode("C")
    g.addNode("D")
    g.addNode("E")
    g.addNode("F")
    g.addNode("G")
    g.addEdge("A", "B", 5)
    g.addEdge("A", "C", 13)
    g.addEdge("A", "E", 15)
    g.addEdge("B", "A", 5)
    g.addEdge("B", "C", 10)
    g.addEdge("B", "D", 8)
    g.addEdge("C", "A", 13)
    g.addEdge("C", "B", 10)
    g.addEdge("C", "E", 20)
    g.addEdge("C", "D", 6)
    g.addEdge("D", "B", 8)
    g.addEdge("D", "C", 6)
    g.addEdge("E", "A", 15)
    g.addEdge("E", "C", 20)
    g.addEdge("C", "F", 11)
    g.addEdge("D", "G", 16)
    g.addEdge("F", "G", 14)
    g.kruskal()


# The added path depends heavily on the situation where
# 1. the weights on edges increase over time,
# i.e., AB = 5, CF = 11 and FG = 4 gives path = FGBADCE,
# but AB = 5 and CF = 11 and FG = 14 gives EABDCFG
# 2. the direction in addEdge() such that it doesn't close the cycle,
# i.e., g.addEdge("G", "F", 13) closes the cycle -> path: EABDCF
graph_3()
