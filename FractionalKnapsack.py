'''
Task #1 – Fractional Knapsack (20 Pts)

Use greedy approach to implement fractional knapsack problem.

INPUT:
    Ask user for knapsack capacity.
    Ask user for n objects’ weights and profits or read an input.txt that
    contains n objects’ weights and profits.

OUTPUT:
    List objects that maximize the profit and show the maximum profit as
    output considering knapsack capacity.
'''

# fills knapsack; enter index of largest p/w ratio
# returns total profit of items in knapsack and remaining capacity of bag
def fill(tot, cap, index):
    if weight[index] > cap: # if there's no more room in the knapsack (split an item)
        #print("weight > cap")
        return tot + (profitperunit[index] * cap), 0
    else: # if a whole item can fit in the knapsack
        #print("cap < weight item:" + str(index))
        profitperunit[index] = -1 # item is used up
        return tot + (profit[index]), cap - weight[index]
    

capacity = int(input("Please enter value for capacity (for this data set, optimally under 24): "))
#capacity = 20 # testing; should be 56
total = 0
profit = []
weight = []
profitperunit = []

with open('input.txt') as f:
    items = int(next(f)) # first number is amount of items
    for x in next(f).split(): # first row is profit
        profit.append(int(x))
    for x in next(f).split(): # second row is weights
        weight.append(int(x))
#print(profit)
#print(weight)

'''
# Until I figure out how to read from txt file
items = 5
profit = [16, 10, 18, 10, 6]
weight = [2, 5, 6, 10, 1]
'''


for i in range(items):
    profitperunit.append(profit[i]/weight[i])
#print(profitperunit)

while capacity != 0 and max(profitperunit) != -1: # while bag has space and there are items left
    total, capacity = fill(total, capacity, profitperunit.index(max(profitperunit)))
    #print(total)
    #print(capacity)

print("Total: " + str(total))