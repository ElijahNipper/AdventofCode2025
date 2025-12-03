#Get our input
f = open("Days/DayTwo/PuzzleTwo/input.txt")
input = f.read()

#Split our input into discrete ranges, and remove the newline character from the end of the final range
ranges = input.split(',')
ranges[-1] = ranges[-1].replace("\n", "") #This is probably unnecessary in python but it doesn't hurt anything

#Hold our invalid IDs
invalidIds = []

#Go over each set of ranges
for el in ranges:
    #Gets the start and end of the current range, and casts them to int so I can iterate over the range
    splitRange = el.split('-')
    start = int(splitRange[0])
    end = int(splitRange[-1])

    #iterates over each value in the range. Just ticks up the value of start since I never need to come back and reference the starting value
    while (start <= end):
        #Get our current value as a string, and the length of that string. This is useful because it lets me do string operations on the current value
        currString = str(start)
        strLen = len(currString)

        #This loop gets slices of the current value for up to half of it using floor division, then checks if the string consists of that slice repeating
        for i in range(strLen // 2):
            #Gets our slice of the current value
            slice = currString[0:i + 1]
            #Replaces all iterations of the given slice, giving us an empty string if our current value is any number of repitions of the same number
            removedSlice = currString.replace(slice, "") 
            #If the length of removedSlice is 0 then we know it was an id consisting of any number of repetitions of the same value
            if len(removedSlice) == 0:
                #Adds our ids to the list of invalid IDs
                invalidIds.append(int(currString))
                #Stops the for loop since we already found a positive match
                break
        start += 1

#Get and print the sum of our invalidIds. Python really does have a billion built in functions
invalidIdSum = sum(invalidIds)
print("Sum of invalid IDs: " + str(invalidIdSum))