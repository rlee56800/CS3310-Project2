'''
Task #2 – 0/1 Knapsack                                                                                        (40 Pts)

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
    i, j = 0
    

capacity = int(input("Please enter value for capacity (for this data set, optimally under 24): "))
#capacity = 20
total = 0

with open('input.txt') as f:
    items = int(next(f)) # read first line
    profit = []
    for x in next(f).split():
        profit.append(int(x))
    weight = []
    for x in next(f).split():
        weight.append(int(x))




print("Total: " + str(total))


