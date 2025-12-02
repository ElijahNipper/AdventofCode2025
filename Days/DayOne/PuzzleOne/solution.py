
#Regex is useful for splitting the string
import re

#Get our input
f = open("Days/DayOne/PuzzleOne/input.txt")
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

    #Uses the modulo operator to provide circular addition/subtraction. Throws an error if first character isnt right or left
    if (direction == right):
        lockValue = (lockValue + distance) % numDials
    elif ([direction == left]):
        lockValue = (lockValue - distance) % numDials
    else:
         raise ValueError("Invalid Direction!")
    
    if (lockValue == 0):
        numZeroes += 1

f.close()

print("Secret code: " + str(numZeroes))