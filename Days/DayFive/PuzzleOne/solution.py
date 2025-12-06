#Regex is useful for splitting the string
import re

#Get our input. Uses read().split() instead of readlines() to not have to deal with \n at the end of every string
f = open("Days/DayFive/PuzzleOne/input.txt")
lines = f.readlines()

#Find the index of the newline seperating ranges from ids
separatorIndex = lines.index("\n")

#Get rid of all the newLines
lines = [line.strip() for line in lines]

#Get our ranges
ranges = lines[0:separatorIndex]
#Get our ingredient ids and cast them to ints
ingredientIds = lines[separatorIndex + 1:len(lines)]
ingredientIds = [int(ingredient) for ingredient in ingredientIds]

#Get our total number of valid ingredient IDs
validIds = 0

#Checks each ingredient to see if it falls within an applicable range
for ingredient in ingredientIds:
    for rangeString in ranges:
        rangeParams = rangeString.split("-")
        rangeStart = int(rangeParams[0])
        rangeEnd = int(rangeParams[-1])

        if (ingredient >= rangeStart and ingredient <= rangeEnd):
            validIds += 1
            break

#Prints the sum total of fresh ingredients
print("Fresh ingredients: " + str(validIds))