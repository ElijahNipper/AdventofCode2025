import math
import operator

#Get our input. 
f = open("Days/DayEight/PuzzleTwo/input.txt")
lines = f.readlines()

#Strip newlines and blank space
lines = [x.strip() for x in lines]

#Class which holds info about each connection being made - the 2 coordinates being connected and the distance between them
class Connection:
    def __init__(self, coordinates1, coordinates2):
        self.coordinates1 = coordinates1
        self.coordinates2 = coordinates2

        coList1 = self.coordinates1.split(",")
        coList2 = self.coordinates2.split(",")

        self.xCo1 = int(coList1[0])
        self.yCo1 = int(coList1[1])
        self.zCo1 = int(coList1[2])

        self.xCo2 = int(coList2[0])
        self.yCo2 = int(coList2[1])
        self.zCo2 = int(coList2[2])

        #Uses euclidian distance
        self.distance = math.sqrt((self.xCo1 - self.xCo2) ** 2 + (self.yCo1 - self.yCo2) ** 2 + (self.zCo1 - self.zCo2) ** 2)

#Implements union find algorithm for keeping track of circuits
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False

        if self.size[rootA] < self.size[rootB]:
            rootA, rootB = rootB, rootA

        self.parent[rootB] = rootA
        self.size[rootA] += self.size[rootB]
        return True

#Hold all the connection objects we make
connections = []

#Adds every unique connection to connections
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        connections.append(Connection(lines[i], lines[j]))

#Uses operator.attrgetter to sort connections by their distance attribute, so we can select the n shortest connections
connections.sort(key=operator.attrgetter('distance'))

#Instantiates our union find  
uf = UnionFind()

#Add all unique coordinates as disjoint sets
for coord in lines:
    uf.add(coord)

#Keep track of the number of coordinates left
coordinate_count = len(lines)

#Keep track of what the last connection is
last_connection = None

#Loops through connections until everything is connected, then stops
for con in connections:
    merged = uf.union(con.coordinates1, con.coordinates2)

    if merged:
        coordinate_count -= 1
        last_connection = con

        if coordinate_count == 1:
            break

#Gets the x coordinates of the last two coordinates connected
x1 = last_connection.xCo1
x2 = last_connection.xCo2
answer = x1 * x2

#Prints our answer
print("Product of X coordinates of final connection:", answer)