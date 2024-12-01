from collections import Counter

f = open("input/day1.txt", "r")

inputdata = f.readlines()

f.close()

leftlist = []
rightlist = []

leftslice = slice(5)
rightslice = slice(8, 13)

for line in inputdata:
	leftlist.append(int(line[leftslice]))
	rightlist.append(int(line[rightslice]))

rightcount = Counter()
for data in rightlist:
	rightcount[data] += 1

finalnumber = 0
length = range(len(leftlist))
for i in length:
	number = leftlist[i] * rightcount[leftlist[i]]
	finalnumber = finalnumber + number

print(finalnumber)
