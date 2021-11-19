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
def fill(tot, cap, index):
    if weight[index] > cap:
        #print("weight > cap HHHH")
        return tot + (profitperunit[index] * cap), 0
    else:
        #print("cap < weight item:" + str(index))
        profitperunit[index] = -1
        return tot + (profit[index]), cap - weight[index]
    

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
#print(profit)
#print(weight)

'''
# Until I figure out how to read from txt file
items = 5
profit = [16, 10, 18, 10, 6]
weight = [2, 5, 6, 10, 1]
'''


profitperunit = []
for i in range(items):
    profitperunit.append(profit[i]/weight[i])
total = 0
#print(profitperunit)

while capacity != 0 and max(profitperunit) != -1:
    total, capacity = fill(total, capacity, profitperunit.index(max(profitperunit)))
    #print(total)
    #print(capacity)

print("Total: " + str(total))