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

leftlist.sort()
rightlist.sort()

finalnumber = 0

length = range(len(leftlist))

for i in length:
	number = leftlist[i] - rightlist[i]
	if number < 0:
		number = number * -1

	finalnumber = finalnumber + number

print(finalnumber)