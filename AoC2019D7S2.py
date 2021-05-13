#ADVENTOFCODE2019 - DAY7 - STAR2
#ALEXADEGRANDMONT

import itertools
import copy

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
def getMode(code, opcode, i):
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
def intcode(code, i, inputs):
    while i < len(code):
        opcode = parseOpcode(code[i])
        if opcode[0] == '99':
            return
        elif opcode[0] == '01':
            operands = getMode(code, opcode, i)
            if opcode[3] == '1':
                code[i+3] = operands[0] + operands[1]
            else:
                code[code[i+3]] = operands[0] + operands[1]
            i+=4
        elif opcode[0] == '02':
            operands = getMode(code, opcode, i)
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
                return [code, i, code[i+1]]
            else:
                return [code, i, code[code[i+1]]]
            i+=2
        elif opcode[0] == '05':
            operands = getMode(code, opcode, i)
            if operands[0] != 0:
                i = operands[1]
            else:
                i+=3
        elif opcode[0] == '06':
            operands = getMode(code, opcode, i)
            if operands[0] == 0:
                i = operands[1]
            else:
                i+=3
        elif opcode[0] == '07':
            operands = getMode(code, opcode, i)
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
            operands = getMode(code, opcode, i)
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
nums = [5,6,7,8,9]
permutations = list(itertools.permutations(nums))

#run intcode loop on the 5 amplifiers
inputs = []
thrusters = []
result = 0
#try each permutation of phase settings
for perm in permutations:
    #create new code copies for each permutation
    codeA = copy.deepcopy(code)
    codeB = copy.deepcopy(code)
    codeC = copy.deepcopy(code)
    codeD = copy.deepcopy(code)
    codeE = copy.deepcopy(code)
    #start up each amplifier with their phase settings 
    inputs.append(perm[0])
    inputs.append(result)
    ampA = intcode(codeA, 0, inputs)
    inputs.append(perm[1])
    inputs.append(ampA[2])
    ampB = intcode(codeB, 0, inputs)
    inputs.append(perm[2])
    inputs.append(ampB[2])
    ampC = intcode(codeC, 0, inputs)
    inputs.append(perm[3])
    inputs.append(ampC[2])
    ampD = intcode(codeD, 0, inputs)
    inputs.append(perm[4])
    inputs.append(ampD[2])
    ampE = intcode(codeE, 0, inputs)
    #loop until all amps are done
    while 1:
        inputs.append(ampE[2])
        ampA = intcode(ampA[0], ampA[1]+2, inputs)
        if ampA == None:
            thrusters.append(inputs[0])
            inputs.clear()
            break
        inputs.append(ampA[2])
        ampB = intcode(ampB[0], ampB[1]+2, inputs)
        inputs.append(ampB[2])
        ampC = intcode(ampC[0], ampC[1]+2, inputs)
        inputs.append(ampC[2])
        ampD = intcode(ampD[0], ampD[1]+2, inputs)
        inputs.append(ampD[2])
        ampE = intcode(ampE[0], ampE[1]+2, inputs)
print(max(thrusters))



