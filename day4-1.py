f = open("input/day4.txt", "r")
inputdata = f.readlines()
f.close()

xmasFound = 0
offset = 1

print(f"Data: {len(inputdata)}, line: {len(inputdata[0])}")

def probe(j, i, x, y, offset):
	if i+(x*offset) < 0 or i+(x*offset) > len(inputdata[0])-1:
		return False
	if j+(y*offset) < 0 or j+(y*offset) > len(inputdata)-1:
		return False
	return inputdata[j+(y*offset)][i+(x*offset)]

for j in range(len(inputdata)):
	for i in range(len(inputdata[0])):
		if inputdata[j][i] == 'X':
			#print(f" X: {i}, Y: {j}")
			for y in range(3):
				for x in range(3):
					#print(f"{probe(j, i, x-1, y-1, offset)} found at position {j+((y-1)*offset)},{i+((x-1)*offset)}")
					if probe(j, i, x-1, y-1, offset) == 'M':
						if probe(j, i, x-1, y-1, offset*2) == 'A':
							if probe(j, i, x-1, y-1, offset*3) == 'S':
								#print(f"Found xmas!")
								xmasFound += 1


print(xmasFound)
