#ADVENTOFCODE2019 - DAY3 - STAR1
#ALEXADEGRANDMONT

#get input from file
f = open("AoC2019D3.txt", "r")
path1 = f.readline().split(',')
path2 = f.readline().split(',')

#set up initial values
crossings = []
m = 8192
n = 8192
origin = [n//2, m//2]
matrix = [['.'] * m for i in range(n)]

#check where path2 intersects path1
def checkIntersection(vpos, hpos, pathNum):
    if matrix[vpos][hpos] == '-' and pathNum == 2:
        crossings.append([vpos, hpos])
        return True

#draw paths on grid
def drawPath(path, pathNum):
    matrix[n//2][m//2] = 'o'
    hpos = n//2
    vpos = m//2
    if pathNum == 1:
        char = '-'
    elif pathNum == 2:
        char = '+'
    for item in path:
        count = int(item[1:])
        if item[0] == 'R':
            for i in range(1, count+1):
                if(checkIntersection(vpos, hpos+i, pathNum)):
                    matrix[vpos][hpos+i] = 'x'
                else: matrix[vpos][hpos+i] = char
            hpos = hpos + count
        elif item[0] == 'L':
            for i in range(1, count+1):
                if (checkIntersection(vpos, hpos-i, pathNum)):
                    matrix[vpos][hpos-i] = 'x'
                else: matrix[vpos][hpos-i] = char
            hpos = hpos - count
        elif item[0] == 'U':
            for i in range(1, count+1):
                if(checkIntersection(vpos-i, hpos, pathNum)):
                    matrix[vpos-i][hpos] = 'x'
                else: matrix[vpos-i][hpos] = char
            vpos = vpos - count
        elif item[0] == 'D':
            for i in range(1, count+1):
                if(checkIntersection(vpos+i, hpos, pathNum)):
                    matrix[vpos+i][hpos] = 'x'
                else: matrix[vpos+i][hpos] = char
            vpos = vpos + count
    return

#draw paths
drawPath(path1, 1)
drawPath(path2, 2)

#calculate manhattan distances and find the min
manDist = []
for crossing in crossings:
    manDist.append(abs(crossing[1] - origin[1]) + abs(crossing[0] - origin[0]))
print(min(manDist))