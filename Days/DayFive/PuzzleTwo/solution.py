#Regex is useful for splitting the string
import re

#Get our input. Uses read().split() instead of readlines() to not have to deal with \n at the end of every string
f = open("Days/DayFive/PuzzleTwo/input.txt")
lines = f.readlines()

#Find the index of the newline seperating ranges from ids
separatorIndex = lines.index("\n")

#Get rid of all the newLines
lines = [line.strip() for line in lines]

#Get our ranges
ranges = lines[0:separatorIndex]

#Object class that lets me quickly access the values for ranges without casting every time, as well as keep track of if a range has been weeded out in sorting
class rangeObject:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.skipped = False

#Holds our rangeObjects
objectRanges = []

#Creates rangeObjects for each range in the input and adds them to objectRanges
for rangeString in ranges:
    rangeParams = rangeString.split("-")
    rangeStart = int(rangeParams[0])
    rangeEnd = int(rangeParams[-1])
    rangeObj = rangeObject(rangeStart, rangeEnd)
    objectRanges.append(rangeObj)

#Keeps track of if our list of ranges was changed at all
changed = True

#Performs a left to right absorption algorithm of ranges in the list. Once it finishes, it repeats these left-to-right passes until no more range optimization is possible
while (changed):

    changed = False

    #Gets our first range, which will be compared with every range to the right of it
    for i in range(0, len(objectRanges) - 1):
            currObj = objectRanges[i]
            currStart = currObj.start
            currEnd = currObj.end 

            if (currObj.skipped):
                    continue
            
            #Goes through each range to the right of our currObj. If there is any crossover in the two ranges, set the vals of our first range to include all vals, and set our second range to be skipped.
            for j in range(i + 1, len(objectRanges)):
                currObj2 = objectRanges[j]
                currStart2 = currObj2.start
                currEnd2 = currObj2.end

                if (currObj2.skipped):
                    continue

                if currStart >= currStart2 and currEnd <= currEnd2:
                    currObj.start =  min(currObj.start, currObj2.start)
                    currObj.end =  max(currObj.end, currObj2.end)
                    currObj2.skipped = True
                    changed = True
                elif currStart >= currStart2 and currEnd >= currEnd2:
                    if currStart <= currEnd2:
                        currObj.start =  min(currObj.start, currObj2.start)
                        currObj.end =  max(currObj.end, currObj2.end)
                        currObj2.skipped = True
                        changed = True
                elif currStart <= currStart2 and currEnd <= currEnd2:
                    if currEnd >= currStart2:
                        currObj.start =  min(currObj.start, currObj2.start)
                        currObj.end =  max(currObj.end, currObj2.end)
                        currObj2.skipped = True
                        changed = True
                elif currStart <= currStart2 and currEnd >= currEnd2:
                    currObj.start =  min(currObj.start, currObj2.start)
                    currObj.end =  max(currObj.end, currObj2.end)
                    currObj2.skipped = True
                    changed = True

#Creates a new list only consisting of ranges that survived our sorting algorithm
objectRanges = [x for x in objectRanges if x.skipped == False]

#Get our total number of valid ingredient IDs
validIds = 0

#Adds the total numbers in each range to validIds
for obj in objectRanges:
    rangeIncl = (obj.end + 1) - obj.start
    validIds += rangeIncl

#Prints the sum total of fresh ingredients
print("Fresh ingredients: " + str(validIds))