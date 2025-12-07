#Regex is useful for splitting the string
import re

#Get our input. Uses read().split() instead of readlines() to not have to deal with \n at the end of every string
f = open("Days/DaySix/PuzzleTwo/input.txt")
lines = f.readlines()

lastLine = lines[-1]

splitIndices = []

for i in range(0, len(lastLine)):
    if lastLine[i] == "*" or lastLine[i] == "+":
        splitIndices.append(i)

rows = []

for line in lines:
    currRow = []
    for i in range(0, len(splitIndices) - 1):
        startIndex = splitIndices[i]
        nextIndex = splitIndices[i + 1] - 1
        currRow.append(line[startIndex:nextIndex])

    currRow.append(line[splitIndices[-1]:-1])

    rows.append(currRow)

transposedRows = [list(row) for row in zip(*rows)]

for row in transposedRows:
    for i in range(len(row) - 1):
        row[i] = row[i].replace(" ", "0")
    row[-1] = row[-1].strip()

actualOperations = []

#Calculates the result of each problem and adds it to our running total
for line in transposedRows:
    #print(line)
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
