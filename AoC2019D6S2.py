#ADVENTOFCODE2019 - DAY6 - STAR2
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

#creates a list showing the path from one node up to another
def getPath(ancestor, node):
    path = []
    while node.parent.name != ancestor:
        path.append(node.name)
        node = node.parent
    path.append(node.name)
    path.append(ancestor)
    return path

#creates paths from YOU and SAN up to COM
for node in tree:
    if node.name == 'YOU':
        nodeYou = node
        you = getPath('COM', node)
    elif node.name == 'SAN':
        nodeSan = node
        san = getPath('COM',node)

#reverse paths so that they start at COM
you.reverse()
san.reverse()

#find the most recent common ancestor
commonAncestor = 'COM'
for i in range(min(len(you), len(san))):
    if you[i] != san[i]:
        commonAncestor = you[i-1]
        break

#get path lengths, -4 to account for com/you and com/san respecitvely, since they are not to be included
you2Ancestor = getPath(commonAncestor, nodeYou)
san2Ancestor = getPath(commonAncestor, nodeSan)
print(len(you2Ancestor)+len(san2Ancestor)-4)


