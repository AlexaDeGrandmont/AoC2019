#ADVENTOFCODE2019 - DAY5 - STAR2
#ALEXADEGRANDMONT

#get input from file
f = open("AoC2019D5.txt", "r")
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
def intcode(code):
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
                code[i+1] = int(input("Enter a value: "))
            else:
                code[code[i+1]] = int(input("Enter a value: "))
            i+=2
        elif opcode[0] == '04':
            if opcode[1] == '1':
                print(code[i+1])
            else:
                print(code[code[i+1]])
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

intcode(code)