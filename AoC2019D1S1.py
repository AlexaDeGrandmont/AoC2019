#ADVENTOFCODE2019 - DAY1 - STAR1
#ALEXADEGRANDMONT

def fuel2Launch(mass):
    return (mass // 3) - 2

f = open("AoC2019D1.txt", "r")

totalFuel = 0
for line in f:
    totalFuel += fuel2Launch(int(line))

print(totalFuel)
