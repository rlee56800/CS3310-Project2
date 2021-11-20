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
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = []
 
    def add(self, u, v, w):
        self.graph.append([u, v, w])
 
 
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
  
    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.vertex):
            parent.append(node)
            rank.append(0)
        while e < self.vertex - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        
        print("Edges:")
        mst = 0
        for u, v, weight in result:
            print("  (" + str(u) + ", " + str(v) + ") = " + str(weight))
            mst += weight
        print("MST total cost: " + str(mst))        

'''
with open('kruskal_input.txt') as f:
    g = Graph(int(next(f)))
    for line in f: # read rest of lines
        arr = []
        arr = [int(x) for x in line.split()]
        g.add(arr[0], arr[1], arr[2])

g.kruskal()'''


g = Graph(5)
arr = [0, 1, 8]
g.add(arr[0], arr[1], arr[2])
g.add(0, 2, 5)
g.add(1, 2, 9)
g.add(1, 3, 11)
g.add(2, 3, 15)
g.add(2, 4, 10)
g.add(3, 4, 7)
g.kruskal()