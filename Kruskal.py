'''
Task #3 – Kruskal’s Algorithm (40 Pts)
Use greedy approach to find the MST of a graph using Kruskal’s algorithm .

Please make sure to use the disjoint set method explained in the class.
For more information on this method please check Appendix C of the course textbook.

INPUT:
    Read the weights of all the edges on the graph (adjacency matrix) from an input.txt file.
        You can use the following adjacency matrix as your reference; however, your program
        should be able to work with any graph size.

OUTPUT: 
    Print the list of all the edges in MST and the total cost of MST.
'''

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add(self, arr):
        self.edges.append(arr)

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal(self):
        result = []
        i, e = 0, 0
        self.edges = sorted(self.edges, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        while e < self.vertices - 1:
            u, v, w = self.edges[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        for u, v, weight in result:
            print(str(u) + " - " + str(v) + ": " + str(weight))


with open('kruskal_input.txt') as f:
    curGraph = Graph(int(next(f)))
    for line in f: # read rest of lines
        arr = []
        for x in range(10):# next(f).split():
            arr.append(int(x))
        curGraph.add(arr)

curGraph.kruskal()
