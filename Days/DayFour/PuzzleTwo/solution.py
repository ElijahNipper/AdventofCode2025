#Regex is useful for splitting the string
import re

#Get our input. Uses read().split() instead of readlines() to not have to deal with \n at the end of every string
f = open("Days/DayFour/PuzzleTwo/input.txt")
lines = f.read().split()

#The values representing an empty spot or a spot with a roll. Defined to prevent hardcoding
empty = "."
roll = "@"

#Get a bunch of length values about our input. I definitely don't need all these but they're just here for legibility
lineW = len(lines[0])
lineH = len(lines)
newLineW = lineW + 2
newLineH = lineH + 2
actualStart = 1
actualEnd = newLineW - 1

#Total sum of accessible rolls
accessibleRolls = 0
#Any number of adjacent rolls less than this value is considered accessible
accessMax = 4

#I make a grid surrounded by a "moat" of empty spaces to be able to check all adjacent spots
tpGrid = [[empty for x in range(newLineW)] for y in range(newLineH)]

#Put our original values into our "moat" array
for i in range(0, lineW):
    for j in range(0, lineH):
        tpGrid[i+1][j+1] = lines[i][j]

#Return a list of the adjacent values of a given coordinate
def getAdjacent(i, j):
    adjacentVals = []
    upLeft = tpGrid[i - 1][j - 1]
    upStraight = tpGrid[i - 1][j]
    upRight = tpGrid[i - 1][j + 1]
    left = tpGrid[i][j -1]
    right = tpGrid[i][j + 1]
    downLeft = tpGrid[i + 1][j - 1]
    downStraight = tpGrid[i + 1][j]
    downRight = tpGrid[i + 1][j + 1]
    adjacentVals.append(upLeft)
    adjacentVals.append(upStraight)
    adjacentVals.append(upRight)
    adjacentVals.append(left)
    adjacentVals.append(right)
    adjacentVals.append(downLeft)
    adjacentVals.append(downStraight)
    adjacentVals.append(downRight)
    return adjacentVals

#Returns the total number of rolls in tpGrid. I use this to see if any rolls were removed.
def getRollCount():
    rollCount = 0
    for i in range(1, lineW + 1):
        for j in range(1, lineH + 1):
            if tpGrid[i][j] == roll:
                rollCount += 1
    return rollCount

#Gets the initial number of rolls at the start of the while function
initialCount = getRollCount()
#Use this for the number of rolls at the end of the while function
newCount = 0

#I might come back and do this with recursion but I'm tired right now
#Check each roll to see if its accessible. Remove roll if it is accessible. Loops until no more rolls accessible.  Doesn't check accessibility for coordinates which don't contain a roll.
while (newCount != initialCount):
    initialCount = getRollCount()
    for i in range(1, lineW + 1):
        for j in range(1, lineH + 1):
            if tpGrid[i][j] == roll:
                adjacentVals = getAdjacent(i, j)
                if adjacentVals.count(roll) < accessMax:
                    accessibleRolls += 1
                    tpGrid[i][j] = empty
    newCount = getRollCount()

#Prints our total accessible rolls
print("Accessible Rolls: " + str(accessibleRolls))