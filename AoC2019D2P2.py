#ADVENT OF CODE - DECEMBER 2 - PUZZLE 2
#ALEXADEGRANDMONT

#get data from file
f = open("AoC2019D2.txt")
intData = f.read()

#get copy of data as list of integers to work with
intList = intData.split(",")
intList = [int(i) for i in intList] 
intListCopy = intList.copy()
f.close()

#set index 1 to 12 and index 2 to 2
intListCopy[1] = 12
intListCopy[2] = 2

#perform operation at index 0 on operands at indices 1 and 2, place result at index 3
def gravityAssist(intList):
    for i in range(0, len(intList)-4, 4):
        if (intList[i] == 99): #return
            return intList[0]
        elif (intList[i] == 1): #sum
            result = intList[intList[i+1]] + intList[intList[i+2]]
        elif (intList[i] == 2): #product
            result = intList[intList[i+1]] * intList[intList[i+2]]
        intList[intList[i+3]] = result

#test all possible values of indices 1 and 2 until the target number 19690720 is found
for j in range(0,100):
    for k in range(0,100):
        intListCopy = intList.copy()
        intListCopy[1] = j
        intListCopy[2] = k
        moonLanding = gravityAssist(intListCopy)
        if (moonLanding == 19690720):
            print('Noun = ' + str(j) + ' and verb = ' + str(k))
            break


    
