f = open("input/day2.txt", "r")
inputdata = f.readlines()
f.close()

safecount = 0

for line in inputdata:
	numbers = line.split(" ")
	safe = True

	for i in range(len(numbers)):
		numbers[i] = int(numbers[i])

	if numbers[0] == numbers[1]:
		#print(f"Data failed due to same number")
		continue

	# Increasing numbers [1,2,3,4]
	if numbers[0] < numbers[1]:
		inc = True
	else:
		inc = False

	for i in range(len(numbers) - 1):
		if inc:
			diff = numbers[i+1] - numbers[i]
		else:
			diff = numbers[i] - numbers[i+1]

		if diff < 1 or diff > 3:
			safe = False
			#print(f"Data failed due to diff of {diff) - int(numbers[i])} at index {i}: {numbers}")
			break

	if safe:
		safecount += 1

print(f"Safe count: {safecount}")