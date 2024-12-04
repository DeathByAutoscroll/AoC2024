f = open("input/day4.txt", "r")
inputdata = f.readlines()
f.close()

xmasFound = 0

def probe(x, y):
	if x < 0 or x > len(inputdata[0])-1:
		return False
	if y < 0 or y > len(inputdata)-1:
		return False
	return inputdata[y][x]

for y in range(len(inputdata)):
	for x in range(len(inputdata[0])):
		if inputdata[y][x] == 'A': # Checks to see if M clockwise from position.
			if probe(x-1, y-1) == 'M': #TL
					if probe(x+1, y-1) == 'M': #TR
						if probe(x-1, y+1) == 'S' and probe(x+1, y+1) == 'S':
							xmasFound += 1

			if probe(x+1, y-1) == 'M': #TR
					if probe(x+1, y+1) == 'M': #BR
						if probe(x-1, y-1) == 'S' and probe(x-1, y+1) == 'S':
							xmasFound += 1

			if probe(x+1, y+1) == 'M': #BR
					if probe(x-1, y+1) == 'M': #BL
						if probe(x-1, y-1) == 'S' and probe(x+1, y-1) == 'S':
							xmasFound += 1

			if probe(x-1, y+1) == 'M': #BL
					if probe(x-1, y-1) == 'M':#TL
						if probe(x+1, y-1) == 'S' and probe(x+1, y+1) == 'S':
							xmasFound += 1

print(xmasFound)
