#Regex is useful for splitting the string
import re

#Get our input. Uses read().split() instead of readlines() to not have to deal with \n at the end of every string
f = open("Days/DayThree/PuzzleTwo/input.txt")
lines = f.read().split()

joltageLen = 12

joltageSums = 0

for line in lines:
    lineLen = len(line)

    maxJoltage = ["0"]

    for i in range(lineLen):
        intsLeft = lineLen - i
        startIndex = joltageLen - intsLeft
        if startIndex < 0:
            startIndex = 0

        currInt = int(line[i])

        appended = False

        for j in range(startIndex, len(maxJoltage)):
            currIntTwo = int(maxJoltage[j])
            
            if (currInt > currIntTwo):
                for k in range(len(maxJoltage) - j):
                    maxJoltage.pop()
                maxJoltage.append(str(currInt))
                appended = True
                break
            
        if (appended == False and len(maxJoltage) < joltageLen):
            maxJoltage.append(str(currInt))

    finalStringValue = ""

    for voltage in maxJoltage:
        finalStringValue += voltage

    maxJoltageInt = int(finalStringValue)
    joltageSums += maxJoltageInt

print("Max sum = " + str(joltageSums))