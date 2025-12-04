#Regex is useful for splitting the string
import re

#Get our input. Uses read().split() instead of readlines() to not have to deal with \n at the end of every string
f = open("Days/DayThree/PuzzleOne/input.txt")
lines = f.read().split()

#Hold our running sum of the max joltages
joltageSums = 0

#Go over each input
for line in lines:
    #Holds the current maximum found voltage
    maxJoltage = 0

    #Uses nested for loops to try every combination of two digits in our input to find the max joltage
    for i in range(len(line)):
        firstDigit = line[i]

        for j in range(i+1, len(line)):
            secondDigit = line[j]

            #Thank you python, so easy to combine the digits and turn them into an integer
            totalDigit = int(firstDigit + secondDigit)

            #Updates our maxJoltage if we found a new max
            if totalDigit > maxJoltage:
                maxJoltage = totalDigit

    #Update our running sum
    joltageSums += maxJoltage

#Prints the sum of all max joltages
print("Max sum = " + str(joltageSums))