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
    for i in range(items):
        arr.append([0])
    for j in range(capacity):
        arr[0].append(0)

    
#capacity = int(input("Please enter value for capacity (for this data set, optimally under 24): "))
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

fill()

for i in range(len(arr)):
    print(arr[i])

#print("Total: " + str(total))


