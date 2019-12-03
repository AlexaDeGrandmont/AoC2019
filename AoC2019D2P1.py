#ADVENT OF CODE - DECEMBER 2 - PUZZLE 1
#ALEXADEGRANDMONT

#get data from file
f = open("AoC2019D2.txt")
intData = f.read()

#get data as list of integers to work with
intList = intData.split(",")
intList = [int(i) for i in intList] 
f.close()

#set index 1 to 12 and index 2 to 2
intList[1] = 12
intList[2] = 2

#perform operation at index 0 on operands at indices 1 and 2, place result at index 3
for i in range(0, len(intList)-4, 4):
    if (intList[i] == 99): #return
        break
    elif (intList[i] == 1): #sum
        result = intList[intList[i+1]] + intList[intList[i+2]]
    elif (intList[i] == 2): #product
        result = intList[intList[i+1]] * intList[intList[i+2]]
    intList[intList[i+3]] = result

print(intList[0])
    
