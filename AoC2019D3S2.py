#ADVENTOFCODE2019 - DAY3 - STAR1
#ALEXADEGRANDMONT

#get input from file
f = open("AoC2019D3.txt", "r")
path1 = f.readline().split(',')
path2 = f.readline().split(',')

#set up initial values
crossings = []
m = 16000
n = 16000
origin = [n//2, m//2]
matrix = [['.'] * m for i in range(n)]

#check if paths intersect at a location, mark this the first time
def checkIntersection(vpos, hpos, pathNum):
    if matrix[vpos][hpos] == '-' and pathNum == 2:
        matrix[vpos][hpos] = 'x'
        crossings.append([vpos, hpos])
        return True
    elif matrix[vpos][hpos] == 'x':
        return True
    else: return False

#draw paths on grid
def drawPath(path, pathNum, crossing):
    #set up grid
    matrix[n//2][m//2] = 'o'
    hpos = n//2
    vpos = m//2
    totalCount = 0
    #set up path drawing
    if pathNum == 1: char = '-'
    elif pathNum == 2: char = '+'
    else: char = '*'
    for item in path:
        direction = item[0]
        count = int(item[1:])
        #right moves
        if direction == 'R':
            for i in range(1, count+1):
                if(checkIntersection(vpos, hpos+i, pathNum)):
                    if pathNum < 1 and vpos == crossing[0] and hpos+i == crossing[1]:
                        totalCount += i
                        return totalCount
                else: matrix[vpos][hpos+i] = char
            hpos = hpos + count
            totalCount += count
        #left moves
        elif direction == 'L':
            for i in range(1, count+1):
                if (checkIntersection(vpos, hpos-i, pathNum)):
                    if pathNum < 1 and vpos == crossing[0] and hpos-i == crossing[1]: 
                        totalCount += i
                        return totalCount
                else: matrix[vpos][hpos-i] = char
            hpos = hpos - count
            totalCount += count
        #up moves
        elif direction == 'U':
            for i in range(1, count+1):
                if(checkIntersection(vpos-i, hpos, pathNum)):
                    if pathNum < 1 and vpos-i == crossing[0] and hpos == crossing[1]: 
                        totalCount += i
                        return totalCount
                else: matrix[vpos-i][hpos] = char
            vpos = vpos - count
            totalCount += count
        #down moves
        elif direction == 'D':
            for i in range(1, count+1):
                if(checkIntersection(vpos+i, hpos, pathNum)):
                    if pathNum < 1 and vpos+i == crossing[0] and hpos == crossing[1]: 
                        totalCount += i
                        return totalCount
                else: matrix[vpos+i][hpos] = char
            vpos = vpos + count
            totalCount += count

#draw paths
drawPath(path1, 1, [n//2, m//2])
drawPath(path2, 2, [n//2, m//2])

#sum distances and find the min
distances = []
for crossing in crossings:
    distances.append(drawPath(path1, 0, crossing) + drawPath(path2, 0, crossing))
print(min(distances))
