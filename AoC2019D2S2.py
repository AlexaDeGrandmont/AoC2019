#ADVENTOFCODE2019 - DAY2 - STAR2
#ALEXADEGRANDMONT

#get input from file
f = open("AoC2019D2.txt", "r")
code = f.read().split(',')

#convert input to integers
for i in range(0,len(code)):
    code[i] = int(code[i])

#define and execute operations
def intcode(code):
    for i in range (0, len(code), 4):
        opcode = code[i]
        if opcode == 99:
            return
        elif opcode == 1:
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
        elif opcode == 2:
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
    return 

#test all possible combinations of initial values for indices 1 and 2
for j in range(0,100):
    for k in range(0,100):
        codeCopy = code.copy() 
        codeCopy[1] = j
        codeCopy[2] = k
        intcode(codeCopy)
        if codeCopy[0] == 19690720:
            print(100 * j + k)


        

