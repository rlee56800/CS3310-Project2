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
        print("weight > cap HHHH")
        return tot + (profitperunit[index] * cap), 0
    else:
        print("cap < weight item:" + str(index))
        profitperunit[index] = -1
        return tot + (profit[index]), cap - weight[index]
    

#capacity = input("Please enter value for capacity: ")
# optimally between 2 and 24, exclusive
capacity = 20
total = 0

'''
# open input.txt and take items
file = open("input.txt", "r")
print(file.read())
file.close()
'''

# Until I figure out how to read from txt file
items = 3#5
profit = [25, 24, 15]#[16, 10, 18, 10, 6]
weight = [18, 15, 10]#[2, 5, 6, 10, 1]

profitperunit = []
for i in range(items):
    profitperunit.append(profit[i]/weight[i])
total = 0
print(profitperunit)

while capacity != 0 and max(profitperunit) != -1:
    #temp = fill(total, capacity, profitperunit.index(max(profitperunit)))
    #total = total + temp[0]
    #capacity = temp[1]
    total, capacity = fill(total, capacity, profitperunit.index(max(profitperunit)))
    print(total)
    print(capacity)

print("Total: " + str(total))