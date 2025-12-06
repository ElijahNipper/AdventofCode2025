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

class rangeObject:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.skipped = False

objectRanges = []

for rangeString in ranges:
    rangeParams = rangeString.split("-")
    rangeStart = int(rangeParams[0])
    rangeEnd = int(rangeParams[-1])
    rangeObj = rangeObject(rangeStart, rangeEnd)
    objectRanges.append(rangeObj)

# changed = False
# while (changed != True):
#     changed = False
    
#     for i in range(len(objectRanges)):
#         currObj = objectRanges[i]
#         currStart = currObj.start
#         currEnd = currObj.end 

#         for j in range(i + 1, len(objectRanges)):
#             currObj2 = objectRanges[j]
#             currStart2 = currObj2.start
#             currEnd2 = currObj2.end

            

#     changed = True

for obj in objectRanges:
    print("Start: " + str(obj.start) + " End: " + str(obj.end))

lowest = objectRanges[0].start
highest = objectRanges[0].start

for obj in objectRanges:
    if obj.start < lowest:
         lowest = obj.start
    if obj.end > highest:
         highest = obj.end

changed = True

#Figure out why some strings have zero in them. Also when to use or not use the >= or <= signs. Thanks future me!
#Are strings still getting used after being skipped? weird
while (changed):

    changed = False

    #CHANGE THIS BACK FROM -1 IF ITS CAUSING ERRORS
    for i in range(0, len(objectRanges)):
            print(i)
            currObj = objectRanges[i]
            currStart = currObj.start
            currEnd = currObj.end 

            if (currObj.skipped):
                    continue

            #print(str(currStart) + " - " + str(currEnd) + " comparing against: ")

            for j in range(i + 1, len(objectRanges)):
                currObj2 = objectRanges[j]
                currStart2 = currObj2.start
                currEnd2 = currObj2.end

                #print(str(currStart2) + " - " + str(currEnd2))

                if (currObj2.skipped):
                    continue

                # if currStart == currStart2 and currEnd == currEnd2:
                #     currObj2.start = 0
                #     currObj2.end = 0
                #     changed = True

                if currStart >= currStart2 and currEnd <= currEnd2:
                    #currObj.start = currObj2.start
                    #currObj.end = currObj2.end
                    currObj.start =  min(currObj.start, currObj2.start)
                    currObj.end =  max(currObj.end, currObj2.end)
                    #currObj2.start = 0
                    #currObj2.end = 0
                    currObj2.skipped = True
                    changed = True
                    #print(1)
                elif currStart >= currStart2 and currEnd >= currEnd2:
                    if currStart <= currEnd2:
                        #currObj.start = currObj2.start
                        currObj.start =  min(currObj.start, currObj2.start)
                        currObj.end =  max(currObj.end, currObj2.end)
                        #currObj2.start = 0
                        #currObj2.end = 0
                        currObj2.skipped = True
                        changed = True
                        #print(2)
                    #print(5)
                elif currStart <= currStart2 and currEnd <= currEnd2:
                    if currEnd >= currStart2:
                        #currObj.end = currObj2.end
                        currObj.start =  min(currObj.start, currObj2.start)
                        currObj.end =  max(currObj.end, currObj2.end)
                        #currObj2.start = 0
                        #currObj2.end = 0
                        currObj2.skipped = True
                        changed = True
                        #print(3)
                    #print(6)
                elif currStart <= currStart2 and currEnd >= currEnd2:
                    #currObj2.start = 0
                    #currObj2.end = 0
                    currObj.start =  min(currObj.start, currObj2.start)
                    currObj.end =  max(currObj.end, currObj2.end)
                    currObj2.skipped = True
                    changed = True
                    #print(4)
            #print("-------")

#THIS STOPS FROM SEEING IF WE HAVE ANY VALUES WEIRDLY ONLY GETTING ONE ZERO. REVERT IF CAUSING ERRORS
objectRanges = [x for x in objectRanges if x.skipped == False]

#Get our total number of valid ingredient IDs
validIds = 0

for obj in objectRanges:
    rangeIncl = (obj.end + 1) - obj.start
    validIds += rangeIncl
    print("Start: " + str(obj.start) + " End: " + str(obj.end))

#NOTHING IS REPEATING?
for i in range(0, len(objectRanges)):
    currObj = objectRanges[i]
    for j in range(i + 1, len(objectRanges)):
        currObj2 = objectRanges[j]

        if currObj.start == currObj2.start or currObj.end == currObj2.end:
                print("Problem!")
        
print("Lowest: " + str(lowest) + " Highest: " + str(highest))
print("Max number ids: " + str((highest + 1) - lowest))

#Prints the sum total of fresh ingredients
print("Fresh ingredients: " + str(validIds))