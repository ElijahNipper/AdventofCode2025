#Regex is useful for splitting the string
import re

#Get our input. Uses read().split() instead of readlines() to not have to deal with \n at the end of every string
f = open("Days/DaySix/PuzzleOne/input.txt")
lines = f.readlines()

#Splits each line into an array of its numbers
for i in range(len(lines)):
    lines[i] = lines[i].split()

#Uses a fancy python oneliner with zip and the unpacking operator (*) to create a new transposed array, flipping the rows and columns of the original
transposedLines = [list(row) for row in zip(*lines)]

#Holds the running total of every calculation
operationsSum = 0

#Performs the correct operation on the given values based on the operator. Reduces redundant code in the for loop
def performFunction(startVal, nextVal, operator):
    if operator == "*":
        return startVal * nextVal
    if operator == "+":
        return startVal + nextVal

#Calculates the result of each problem and adds it to our running total
for line in transposedLines:

    currentTotal = int(line[0])
    operator = line[-1]

    for i in range(1, len(line) - 1):
        currentTotal = performFunction(currentTotal, int(line[i]), operator)

    operationsSum += currentTotal

#Print out our grand total
print("Grand total: " + str(operationsSum))