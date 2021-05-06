#ADVENTOFCODE2019 - DAY6 - STAR1
#ALEXADEGRANDMONT

#get input from file
f = open("AoC2019D6.txt", "r")
orbits = []
for line in f:
    orbits.append([line.rstrip().split(')'), True])

#sort the orbits
sortedOrbits = []
def topologicalSort(orbits, planets):
    for orbit in orbits:
        for planet in planets:
            if orbit[1] == True:
                if orbit[0][0] == planet:
                    sortedOrbits.append(orbit[0])
                    planets.append(orbit[0][1])
                    orbit[1] = False
        if len(planets) == len(orbits)+1:
            return sortedOrbits
    return topologicalSort(orbits, planets)
    
topologicalSort(orbits, ['COM'])

#create tree node class
class Node(object):
    def __init__(self, name, value, parent):
        self.name = name
        self.value = value
        self.children = []
        self.parent = parent
    def add_child(self, child):
        self.children.append(child)

#initialize tree root
tree = [Node('COM', 0, None)]

#populate tree, values are the heights of the nodes
for orbit in sortedOrbits:
    for node in tree:
        if node.name == orbit[0]:
            child = Node(orbit[1], node.value+1, node)
            node.add_child(child)
            tree.append(child)

#sum up the height values
heightSum = 0
for node in tree:
    heightSum += node.value

print(heightSum)


