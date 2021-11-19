'''
Task #2 – 0/1 Knapsack (40 Pts)

Use Dynamic programming approach to implement 0/1 knapsack problem.

INPUT:
    Ask user for knapsack capacity.
    Ask user for n objects’ weights and profits or read an input.txt that
    contains n objects’ weights and profits.

OUTPUT:

    List objects that maximize the profit and show the maximum profit as
    output considering knapsack capacity.
'''

def fill():
    '''for i in range(items+1):
        arr.append([0])
    for j in range(capacity):
        arr[0].append(0)'''
    for i in range(items):
        print("i: " + str(i))
        for j in range(capacity):
            print("j: " + str(j))
            if weight[i] > j:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = max(arr[i - 1][j], (profit[i] + arr[i-1][j - weight[i]]))
    
'''#capacity = int(input("Please enter value for capacity (for this data set, optimally under 24): "))
capacity = 5 # testing
total = 0
profit = []
weight = []
arr = []


with open('input.txt') as f:
    items = int(next(f)) # first number is amount of items
    for x in next(f).split(): # first row is profit
        profit.append(int(x))
    for x in next(f).split(): # second row is weights
        weight.append(int(x))
#print(profit)
#print(weight)
'''
capacity = 6
total = 0
items = 4
profit = [3, 4, 8, 5]
weight = [3, 1, 4, 3]
arr = []
for i in range(items + 1):
    arr1 = []
    for j in range(capacity):
        arr1.append(0)
    arr.append(arr1)

fill()

for i in range(len(arr)):
    print(arr[i])

#print("Total: " + str(arr[items][capacity]))


