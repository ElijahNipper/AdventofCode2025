#Regex is useful for splitting the string
import re

#Get our input. Uses read().split() instead of readlines() to not have to deal with \n at the end of every string
f = open("Days/DayThree/PuzzleOne/input.txt")
lines = f.read().split()

joltageSums = 0

for line in lines:
    maxVoltage = 0

    for i in range(len(line)):
        firstDigit = line[i]

        for j in range(i+1, len(line)):
            secondDigit = line[j]

            totalDigit = int(firstDigit + secondDigit)

            if totalDigit > maxVoltage:
                maxVoltage = totalDigit

    joltageSums += maxVoltage

print("Max sum = " + str(joltageSums))