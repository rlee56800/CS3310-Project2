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
    print(i)
    while parent[i] != i:
        
        i = parent[i]
    return i

def merge(p, q):
    if p < q:
        parent[q] = p
    else:
        parent[p] = q

def kruskal():
    sorted_arr = sorted(arr, key=lambda x: x[2])
    for i in range(1, nodes+1): # initialize n disjoint subsets
        parent.append(i)
    print(parent)
    
    while len(edgesArr) < len(arr):
        #print("entered while")
        e = min(sorted_arr)
        i = e[0]
        j = e[1]
        p = find(i)
        q = find(j)
        if p != q:
            merge(p, q)
            edgesArr.append(e)
            sorted_arr.remove(e)


arr = []
parent = []
edgesArr = []
with open('kruskal_input.txt') as f:
    nodes = int(next(f)) # first number is amount of nodes
    for line in f: # read rest of lines
        arr.append([int(x) for x in line.split()])

#for i in range(len(arr)):
#    print(arr[i])

kruskal()
print(edgesArr)
mst = 0