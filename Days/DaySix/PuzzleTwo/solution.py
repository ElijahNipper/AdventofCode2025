#Regex is useful for splitting the string
import re

#Get our input. Uses read().split() instead of readlines() to not have to deal with \n at the end of every string
f = open("Days/DaySix/PuzzleTwo/input.txt")
lines = f.readlines()

#Gets the last line of our input, which contains all the operations (and also holds the secret to correct spacing)
lastLine = lines[-1]

#Hold the indexes to actually split each row on to preserve correct whitespace
splitIndices = []

#Gets the indices for splitIndices
for i in range(0, len(lastLine)):
    if lastLine[i] == "*" or lastLine[i] == "+":
        splitIndices.append(i)

#Holds all of our rows once they have been split on the correct spots
rows = []

#Splits all the data and puts it into rows
for line in lines:
    currRow = []
    for i in range(0, len(splitIndices) - 1):
        startIndex = splitIndices[i]
        nextIndex = splitIndices[i + 1] - 1
        currRow.append(line[startIndex:nextIndex])

    currRow.append(line[splitIndices[-1]:-1])

    rows.append(currRow)

#Uses a fancy python oneliner with zip and the unpacking operator (*) to create a new transposed array, flipping the rows and columns of the original
transposedRows = [list(row) for row in zip(*rows)]

#Replaces the blank spaces with zeros. I might get rid of this later, I don't think its actually necessary. I can do this because the input contains no 0s, but its prob not best practice
for row in transposedRows:
    for i in range(len(row) - 1):
        row[i] = row[i].replace(" ", "0")
    row[-1] = row[-1].strip()

#Holds the actual operations we will need to do once we have converted to cephalapod math
actualOperations = []

#Converts to cephalapod math
for line in transposedRows:
    operator = line[-1]

    lineLen = len(line)
    numLen = len(line[0])
    
    start = 0
    newVals = []

    while (start < numLen):
        newVal = line[0][start]

        for i in range(1, lineLen - 1):
            newVal += line[i][start]
        
        newVals.append(newVal)
        start += 1
    newVals.append(operator)
    
    
    actualOperations.append(newVals)

#Get rid of the zeros now that we have factored in the spacing of the significant digits
for row in actualOperations:
    for i in range(len(row)):
        row[i] = row[i].replace("0", "")

#Holds the running total of every calculation
operationsSum = 0

#Performs the correct operation on the given values based on the operator. Reduces redundant code in the for loop
def performFunction(startVal, nextVal, operator):
    if operator == "*":
        return startVal * nextVal
    if operator == "+":
        return startVal + nextVal

#Calculates the result of each problem and adds it to our running total
for line in actualOperations:
    currentTotal = int(line[0])
    operator = line[-1]

    for i in range(1, len(line) - 1):
        currentTotal = performFunction(currentTotal, int(line[i]), operator)

    operationsSum += currentTotal

#Print out our grand total
print("Grand total: " + str(operationsSum))
