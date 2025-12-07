#Regex is useful for splitting the string
import re

#Get our input. 
f = open("Days/DaySeven/PuzzleOne/input.txt")
lines = f.readlines()

#Turns each line into its own array and gets rid of the newline characters at the end
for i in range(len(lines)):
    currLine = lines[i].strip()
    listLine = list(currLine)
    lines[i] = listLine

start = "S"
empty = "."
beam = "|"
splitter = "^"

#Keeps track of how many times we have split our beam
timesSplit = 0

#Get our starting index
firstLine = lines[0]
startIndex = firstLine.index(start)

#Keeps track of all indices that have a beam. Uses a set to automatically filter out duplicates 
beamIndices = {startIndex}

#For each line, either extends our beam or splits it
for i in range(1, len(lines)):
    currLine = lines[i]
    
    iterIndices = list(beamIndices)

    for index in iterIndices:
        considering = currLine[index]

        #This first if statement is only for visualization purposes, it's not actually necessary
        if (considering == empty):
            currLine[index] = beam
        if (considering == splitter):
            former = index - 1
            latter = index + 1

            currLine[former] = beam
            currLine[latter] = beam

            beamIndices.add(former)
            beamIndices.add(latter)
            beamIndices.remove(index)

            timesSplit += 1

#Prints out the number of times we split the beam
print(timesSplit)