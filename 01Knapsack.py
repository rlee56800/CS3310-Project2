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

capacity = input("Please enter value for capacity: ")

# open input.txt and take items
file = open("input.txt", "r")
print(file.read())
file.close()


