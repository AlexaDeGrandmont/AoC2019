#ADVENTOFCODE2019 - DAY7 - STAR1
#ALEXADEGRANDMONT

import itertools

#get input from file
f = open("AoC2019D7.txt", "r")
code = f.read().split(",")


#convert input to integers
for i in range(0,len(code)):
    code[i] = int(code[i])

#helper function to determine opcodes and modes
def parseOpcode(opcode):
    opcode = str(str(opcode).zfill(5))
    parsed = [opcode[3:], opcode[2], opcode[1], opcode[0]]
    return parsed 

#helper function to implement different modes
def getMode(opcode, i):
    operand1 = 0
    operand2 = 0
    if opcode[1] == '1':
        operand1 = code[i+1]
    else:
        operand1 = code[code[i+1]]
    if opcode[2] == '1':
        operand2 = code[i+2]
    else:
        operand2 = code[code[i+2]]
    return [operand1, operand2]

#define and execute operations
def intcode(code, inputs):
    i = 0
    while i < len(code):
        opcode = parseOpcode(code[i])
        if opcode[0] == '99':
            return
        elif opcode[0] == '01':
            operands = getMode(opcode, i)
            if opcode[3] == '1':
                code[i+3] = operands[0] + operands[1]
            else:
                code[code[i+3]] = operands[0] + operands[1]
            i+=4
        elif opcode[0] == '02':
            operands = getMode(opcode, i)
            if opcode[3] == '1':
                code[i+3] = operands[0] * operands[1]
            else:
                code[code[i+3]] = operands[0] * operands[1]
            i+=4
        elif opcode[0] == '03':
            if opcode[1] == '1':
                code[i+1] = inputs[0]
                del inputs[0]
            else:
                code[code[i+1]] = inputs[0]
                del inputs[0]
            i+=2
        elif opcode[0] == '04':
            if opcode[1] == '1':
                return code[i+1]
            else:
                return code[code[i+1]]
            i+=2
        elif opcode[0] == '05':
            operands = getMode(opcode, i)
            if operands[0] != 0:
                i = operands[1]
            else:
                i+=3
        elif opcode[0] == '06':
            operands = getMode(opcode, i)
            if operands[0] == 0:
                i = operands[1]
            else:
                i+=3
        elif opcode[0] == '07':
            operands = getMode(opcode, i)
            if opcode[3] == '1':
                if operands[0] < operands[1]:
                    code[i+3] = 1
                else:
                    code[i+3] = 0
            else:
                if operands[0] < operands[1]:
                    code[code[i+3]] = 1
                else:
                    code[code[i+3]] = 0
            i+=4
        elif opcode[0] == '08':
            operands = getMode(opcode, i)
            if opcode[3] == '1':
                if operands[0] == operands[1]:
                    code[i+3] = 1
                else:
                    code[i+3] = 0
            else:
                if operands[0] == operands[1]:
                    code[code[i+3]] = 1
                else:
                    code[code[i+3]] = 0
            i+=4
    return 

#generate all permutations
nums = [0,1,2,3,4]
permutations = list(itertools.permutations(nums))

#run intcode loop on the 5 amplifiers
inputs = []
thrusters = []
result = 0
for perm in permutations:
    for i in range(0,5):
        inputs.append(perm[i])
        inputs.append(result)
        result = intcode(code, inputs)
    thrusters.append(result)
    result = 0

print(max(thrusters))
    



