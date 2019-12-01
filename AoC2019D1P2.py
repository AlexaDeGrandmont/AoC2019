#ADVENT OF CODE - DECEMBER 1 - PUZZLE 2
#ALEXADEGRANDMONT

import math

#recursively calculate amount of fuel per module
def fuel2Launch(mass):
    sumFuel = 0
    #recurse until mass is not positive
    while(int(mass)>=0):
        mass = math.floor(int(mass)/3) - 2
        #stop when mass is not positive
        if (mass <= 0):
             return sumFuel
        sumFuel += mass
        fuel2Launch(mass)
    return sumFuel

f = open("AoC2019D1input.txt")
totalFuel = 0
for line in f:
    totalFuel += fuel2Launch(line)

f.close()
print(totalFuel)