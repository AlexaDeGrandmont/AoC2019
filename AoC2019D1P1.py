#ADVENT OF CODE - DECEMBER 1 - PUZZLE 1
#ALEXADEGRANDMONT

import math

#calculate amount of fuel for each module in .txt file
def fuel2Launch(mass):
    #fuel calcuation
    fuel = math.floor(int(mass)/3) - 2
    return fuel

f = open("AoC2019D1input.txt")
sumFuel = 0
#sum up all fuel amounts
for line in f:
    sumFuel += fuel2Launch(line)

f.close()
print(sumFuel)