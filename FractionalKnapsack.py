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
        return tot + profit[index] * cap, 0
    else:
        profitperunit[index] = -1
        return cap - weight[index], tot + (profit[index] * weight[index])
    

#capacity = input("Please enter value for capacity: ")
# optimally between 2 and 24, exclusive
capacity = 4
total = 0

'''
# open input.txt and take items
file = open("input.txt", "r")
print(file.read())
file.close()
'''

# Until I figure out how to read from txt file
items = 5
profit = [16, 10, 18, 10, 6]
weight = [2, 5, 6, 10, 1]

profitperunit = []
for i in range(items):
    profitperunit.append(profit[i]/weight[i])

total = 0
print(profitperunit)

while capacity != 0 and max(profitperunit) != -1:
    total, capacity = fill(total, capacity, profitperunit.index(max(profitperunit)))