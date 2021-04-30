#ADVENTOFCODE2019 - DAY1 - STAR2
#ALEXADEGRANDMONT

def fuel2Launch(mass):
    return (mass // 3) - 2

f = open("AoC2019D1.txt", "r")

def fuelRecursion(mass):
    fuel = 0
    while fuel2Launch(mass) >= 0:
        mass = fuel2Launch(mass)
        fuel += mass
    return fuel

totalFuel = 0
for line in f:
    totalFuel += fuelRecursion(int(line))

print(totalFuel)

