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

def knapsack():
    i, j = 0

capacity = input("Please enter value for capacity: ")

# open input.txt and take items
file = open("input.txt", "r")
print(file.read())
file.close()


