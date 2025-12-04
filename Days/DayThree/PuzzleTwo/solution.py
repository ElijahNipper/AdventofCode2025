#Regex is useful for splitting the string
import re

#Get our input. Uses read().split() instead of readlines() to not have to deal with \n at the end of every string
f = open("Days/DayThree/PuzzleTwo/input.txt")
lines = f.read().split()

joltageLen = 12

joltageSums = 0

for line in lines:
    print(line)
    lineLen = len(line)
    zeroLine = "0" * lineLen

    charsFound = 0
    indices = []

    for i in range(9, 0, -1):
        if charsFound >= joltageLen - 1:
            break
        values = [index for index, number in enumerate(line) if number == str(i)]
        
        if (len(values) != 0):
            indices.append(values)

        charsFound += len(values)

    zeroList = list(zeroLine)

    charsPlaced = 0

    for indexArray in indices:
        if (charsPlaced == joltageLen):
            break
        indexArray.reverse()
        
        for index in indexArray:
            if (charsPlaced == joltageLen):
                break
            zeroList[index] = line[index]
            charsPlaced += 1

    zeroList = [number for number in zeroList if number != "0"]

    maxNum = ""

    for number in zeroList:
        maxNum += number

    maxNum = int(maxNum)
    print(maxNum)
    exit()

print("Max sum = " + str(joltageSums))