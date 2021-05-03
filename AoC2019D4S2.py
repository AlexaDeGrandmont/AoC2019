#ADVENTOFCODE2019 - DAY4 - STAR2
#ALEXADEGRANDMONT

from itertools import groupby

#get input from file
f = open("AoC2019D4.txt", "r")

#initialize values
nums = []
start = int(f.readline())
end = int(f.readline())

#set up number/bool pairs
for i in range(start,end):
    nums.append([str(i), True])

#filter by double digits
doubles = []
for num in nums:
    for i in range(0,5):
        if num[0][i] == num[0][i+1]:
            doubles.append(num)

#flag non-increasing numbers
for double in doubles:
    for i in range(0,5):
        if double[0][i] > double[0][i+1]:
            double[1] = False

#filter out non-increasing numbers
increasing = []
for double in doubles:
    if double[1] == True:
        increasing.append(double[0])

#eliminate duplicate numbers
increasing = set(increasing)

#chunk numbers into different groups of digits
chunks = []
for num in increasing:
    chunks.append([num, [''.join(chunk) for _, chunk in groupby(num)]])

#filter out groups not containing a chunk of exactly size 2
passwords = []
for num in chunks:
    for chunk in range (len(num[1])):
        if len(num[1][chunk]) == 2:
            passwords.append(num[0])
            break
    
print(len(passwords))

