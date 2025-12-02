#Regex is useful for splitting the string
import re

#Get our input
f = open("Days/DayOne/PuzzleTwo/input.txt")
lines = f.readlines()

numZeroes = 0 #Number of times the lock has stopped on zero
lockValue = 50 #Where the lock currently sits. Initially its at 50
numDials = 100 #number of 'clicks'
right = "R"
left = "L"

for line in lines:
    parts = re.split('(\\d+)', line) #Splits on Number, so we get an Array that looks like [Direction (String), Distance (int), newline character (Char)]
    parts = parts[:-1] #Remove the newline character. Not really necessary but it makes it cleaner

    direction = parts[0] #Get the direction
    distance = int(parts[1]) #Get the distance

    if (direction == right):
        #Uses floor int division to figure out how many times the lock has gone past 0
        tempVal = lockValue + distance
        if (tempVal > 99):
            numZeroes += tempVal // 100

        lockValue = (lockValue + distance) % numDials #Updates lock value
    elif (direction == left):
        #My clever solution was no match for the annoyance of off by one incidents 
        #tempVal = lockValue - distance
        #if (tempVal < 1):
            #numZeroes -= tempVal // 100
        
        startVal = lockValue

        #Just brute forces this part because I'm tired and I have work in the morning. Might clean this up later
        for i in range(distance):
            if (startVal == 0):
                startVal = 99
            else:
                startVal -= 1
            if (startVal == 0):
                numZeroes += 1

        lockValue = (lockValue - distance) % numDials #Updates lock value
    else:
         raise ValueError("Invalid Direction!") #Throws an error if we get an improper first character. That won't happen but it's good practice
    
f.close() #Close file

#Print out our code
print("Secret code: " + str(numZeroes))