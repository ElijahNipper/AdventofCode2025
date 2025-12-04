#Regex is useful for splitting the string
import re

#Get our input. Uses read().split() instead of readlines() to not have to deal with \n at the end of every string
f = open("Days/DayThree/PuzzleTwo/input.txt")
lines = f.read().split()

#The amount of batteries we "turn on" in each row
joltageLen = 12

#The running sum of all of our max joltages
joltageSums = 0

#Go over each input
for line in lines:
    #Get the length of the current input
    lineLen = len(line)

    #An array which I use to keep track of the max voltage. I use this array as a makeshift stack in my algorithm
    maxJoltage = ["0"]

    #Go over each digit in our current input. Algorithm keeps a running stack and pops/appends based on how many digits are left in our input
    for i in range(lineLen):
        #Get the amount of digits left in the current input
        intsLeft = lineLen - i
        #Tells us the index where we can start comparing ints at in maxJoltage. It is 0 at minumum and joltageLen - 1 at maximum
        startIndex = joltageLen - intsLeft
        if startIndex < 0:
            startIndex = 0

        #Get the current integer we're considering from our input
        currInt = int(line[i])

        #Tells us if we found a suitable digit to replace one in our stack
        appended = False

        #Compares currInt to digits in maxJoltage from our startIndex to the end of maxJoltage. If we find a suitable digit, call pop k times and then append that digit
        for j in range(startIndex, len(maxJoltage)):
            currIntTwo = int(maxJoltage[j])
            
            if (currInt > currIntTwo):
                for k in range(len(maxJoltage) - j):
                    maxJoltage.pop()
                maxJoltage.append(str(currInt))
                appended = True
                break
        
        #If our currInt isn't larger than any of the digits in maxJoltage, and maxJoltage hasn't hit length yet, append our currInt to maxJoltage
        if (appended == False and len(maxJoltage) < joltageLen):
            maxJoltage.append(str(currInt))

    finalStringValue = ""

    #Convert our maxJoltage stack to a string
    for voltage in maxJoltage:
        finalStringValue += voltage

    #Convert our string to its int value
    maxJoltageInt = int(finalStringValue)
    #Update our running sum
    joltageSums += maxJoltageInt

#Print out the sum of all maximum joltages
print("Max sum = " + str(joltageSums))