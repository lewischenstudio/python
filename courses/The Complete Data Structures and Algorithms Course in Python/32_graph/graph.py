"""
Graph
   A --- D
  / \   /
 /   \ /
B --- C
"""


class Graph:
    def __init__(self, adjacency_list=None):
        self.adjacency_list = adjacency_list or {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        print(vertex, " is not added")
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        if (
            vertex1 in self.adjacency_list.keys()
            and vertex2 in self.adjacency_list.keys()
        ):
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        print(vertex2, " is not added")
        return False

    def remove_edge(self, vertex1, vertex2):
        if (
            vertex1 in self.adjacency_list.keys()
            and vertex2 in self.adjacency_list.keys()
        ):
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        print(vertex2, " is not removed")
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        print(vertex, " is not removed")
        return False


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "D")
my_graph.print_graph()
my_graph.remove_vertex("A")
print("After remove..")
my_graph.print_graph()


customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["b", "c", "d", "f"],
    "f": ["d", "e"],
}

graph = Graph(customDict)
graph.print_graph()
