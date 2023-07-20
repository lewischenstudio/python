"""
Disjoint Set in Python

Time complexity: O(N)
"""


class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:  # O(N)
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item
        return self.find(self.parent[item])  # O(N)

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1


vertices = ["A", "B", "C", "D", "E"]

ds = DisjointSet(vertices)
ds.union("A", "B")
ds.union("A", "C")
print(ds.find("A"))
print(ds.find("B"))
print(ds.find("C"))
