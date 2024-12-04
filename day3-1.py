f = open("input/day3.txt", "r")
inputdata = f.readlines()
f.close()

import re

total = 0
matches = re.findall("mul\(\d{1,3},\d{1,3}\)", str(inputdata))

for match in matches:
	splitMatch = match.split(",")
	multiply = int(splitMatch[0].strip("mul(")) * int(splitMatch[1].strip(")"))
	total += multiply

print(total)