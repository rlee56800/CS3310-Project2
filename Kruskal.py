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

def kruskal():
    sorted_arr = sorted(arr, key=lambda x: x[2])
    F = []
    while len(F) > len(arr):
        print()


arr = []
with open('kruskal_input.txt') as f:
    for line in f: # read rest of lines
        arr.append([int(x) for x in line.split()])

for i in range(len(arr)):
    print(arr[i])




#print(sorted_arr)