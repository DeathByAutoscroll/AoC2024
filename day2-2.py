f = open("input/day2.txt", "r")
inputdata = f.readlines()
f.close()

safecount = 0

for line in inputdata:
	data = line.split(" ")

	for i in range(len(data)):
		data[i] = int(data[i])

	numbers = data
	for j in range(len(data) + 1):
		print(f"{j} of {len(numbers)}: {numbers}")
		safe = True
		if numbers[0] == numbers[1]:
			#print(f"Data failed due to same number")
			safe = False

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
				#print(f"Data failed due to diff of {diff} at index {i}: {numbers}")
				break

		if safe:
			safecount += 1
			break
		else:
			if j == len(data):
				break
			else:
				numbers = data.copy()
				numbers.pop(j)


print(f"Safe count: {safecount}")