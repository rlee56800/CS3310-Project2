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

def find(i):
    while parent[i] != i:
        
        i = parent[i]
    return i

def merge(p, q):
    a = find(p)
    b = find(q)
    parent[a] = b

def kruskal():
    for i in range(1, nodes): # initialize n disjoint subsets
        parent[i] = i
    
    while len(edgesArr) < nodes - 1:
        min = 1000 # initialize number
        a = -1
        b = -1
        for i in range(nodes):
            for j in range(nodes):
                if find(i) != find(j) and arr[i][j] < min:
                    min = arr[i][j]
                    a = i
                    b =j
        merge(a, b)
        edgesArr.append([a, b, min])
        


arr = []
parent = []
edgesArr = []
with open('kruskal_input.txt') as f:
    nodes = int(next(f)) # first number is amount of nodes
    for line in f: # read rest of lines
        arr.append([int(x) for x in line.split()])


for i in range(nodes): # initialize n disjoint subsets
    parent.append(i)

#for i in range(len(arr)):
#    print(arr[i])

kruskal()

mst = 0
print("Edges: ")
for i in range(len(edgesArr)):
    print("(" + str(edgesArr[i][0]) + ", " + str(edgesArr[i][1]) + ")")
    mst += edgesArr[i][2]
print("MST total cost: " + str(mst))