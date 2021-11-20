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
    for i in range(items+1):
        arr[i][0] = 0
    for j in range(capacity):
        arr[0][j] = 0
    for i in range(1, items+1):
        #print("i: " + str(i))
        for j in range(1, capacity+1):
            #print("j: " + str(j))
            if weight[i-1] > j:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = max(arr[i - 1][j], (profit[i-1] + arr[i-1][j - weight[i-1]]))
    
    
    finTotal = arr[items][capacity]
    w = capacity
    for i in range(len(profit), 0, -1):
        if finTotal <= 0:
            break
        if finTotal == arr[i - 1][w]:
            continue
        else:
            usedProfit.append(profit[i - 1])
            usedWeight.append(weight[i-1])
            finTotal = finTotal - profit[i - 1]
            w = w - weight[i - 1]

capacity = int(input("Please enter value for capacity: "))
#capacity = 20#7 # testing
total = 0
profit = []
weight = []
arr = []
usedProfit = []
usedWeight = []

with open('input.txt') as f:
    items = int(next(f)) # first number is amount of items
    for x in next(f).split(): # first row is profit
        profit.append(int(x))
    for x in next(f).split(): # second row is weights
        weight.append(int(x))
#print(profit)
#print(weight)
'''
capacity = 7
total = 0
items = 4
profit = [1,4,5,7]
weight = [1,3,4,5]
arr = []'''

for i in range(items + 1):
    arr1 = []
    for j in range(capacity+1):
        arr1.append(0)
    arr.append(arr1)


fill()

#for i in range(len(arr)):
#    print(arr[i])

print("Max Profit: " + str(arr[items][capacity]))
print("Items used (profit, then weight):")
print(usedProfit)
print(usedWeight)
