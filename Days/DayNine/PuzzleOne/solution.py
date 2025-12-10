import operator

#Get our input. 
f = open("Days/DayNine/PuzzleOne/input.txt")
lines = f.readlines()

#Strip newlines and blank space
lines = [x.strip() for x in lines]

#Class which holds info about all possible rectangles
class Rectangle:
    def __init__(self, coordinates1, coordinates2):
        self.coordinates1 = coordinates1
        self.coordinates2 = coordinates2

        coList1 = self.coordinates1.split(",")
        coList2 = self.coordinates2.split(",")

        self.xCo1 = int(coList1[0])
        self.yCo1 = int(coList1[-1])

        self.xCo2 = int(coList2[0])
        self.yCo2 = int(coList2[-1])

        self.area = (abs(self.xCo1 - self.xCo2) + 1) * (abs(self.yCo1 - self.yCo2) + 1)

rectangles = []

#Adds every unique rectangle to rectangles
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        rectangles.append(Rectangle(lines[i], lines[j]))

#Uses operator.attrgetter to sort rectangles by their area attribute, so we can select the biggest rectangle
rectangles.sort(key=operator.attrgetter('area'))

#Print the rectangle with the largest area
print(rectangles[-1].area)