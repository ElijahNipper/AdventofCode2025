#Regex is useful for splitting the string
import re

#Get our input. 
f = open("Days/DaySeven/PuzzleTwo/input.txt")
lines = f.readlines()

#Turns each line into its own array and gets rid of the newline characters at the end
for i in range(len(lines)):
    currLine = lines[i].strip()
    listLine = list(currLine)
    lines[i] = listLine

start = "S"
splitter = "^"

#Get our starting index from the first line
firstLine = lines[0]
startIndex = firstLine.index(start)

#Holds the value of our timelines
timelines = 0

#Holds our timelines. Each number represents the number of paths a beam could take to end up in that column
timelinePaths = [0 for x in range(len(firstLine))]

#Get our starting timeline
timelinePaths[startIndex] = 1

#Updates timelinePaths for each row in our input. On a split, the adjacent indices both get the value of the current column, and the current is set to 0
for line in lines:
    #Gets the index of all the splitters in a row
    splitters = [i for i,x in enumerate(line) if x == splitter]
    
    for split in splitters:
        timelinePaths[split - 1] += timelinePaths[split]
        timelinePaths[split + 1] += timelinePaths[split]
        timelinePaths[split] = 0

#Adds up all our timelines
for timeline in timelinePaths:
    timelines += timeline

#Print out our final timeline
print(timelines)