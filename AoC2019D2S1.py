#ADVENTOFCODE2019 - DAY2 - STAR1
#ALEXADEGRANDMONT

#get input from file
f = open("AoC2019D2.txt", "r")
code = f.read().split(',')

#convert input to integers
for i in range(0,len(code)):
    code[i] = int(code[i])

#initialize program with values given in the problem
code[1] = 12
code[2] = 2

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

intcode(code)
print(code[0])


