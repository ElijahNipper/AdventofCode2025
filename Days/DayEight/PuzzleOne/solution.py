import math
import operator

#Get our input. 
f = open("Days/DayEight/PuzzleOne/input.txt")
lines = f.readlines()

#Strip newlines and blank space
lines = [x.strip() for x in lines]

#The number of n shortest connection the elves want me to wire up
numberConnections = 1000

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
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False  # same circuit, ignore

        # attach smaller to larger
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

#Performs union operation for our n shortest connections
for con in connections[:numberConnections]:
    uf.union(con.coordinates1, con.coordinates2)

#Holds the final length of each circuit we've made (each disjoint set)   
final_sizes = []

#Only saves the root nodes as each root node represents a disjoint set
for node in uf.parent:
    if uf.parent[node] == node:  # root only
        final_sizes.append(uf.size[node])

final_sizes.sort()
answer = final_sizes[-3] * final_sizes[-2] * final_sizes[-1]

#Print our answer
print("Length of our three largest circuits mulitplied together: " + str(answer))