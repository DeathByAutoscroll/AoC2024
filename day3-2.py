f = open("input/day3.txt", "r")
inputdata = f.readlines()
f.close()

inputdata = str(inputdata)

doEnabled = True
wordsearch = 0
num1 = "" 
num2 = ""
finalTotal = 0

for char in inputdata:
	#print(wordsearch)
	# Start
	if wordsearch == 0:
		if doEnabled and char == 'm':
			wordsearch = 1
		elif char == 'd':
			wordsearch = 11
		else:
			continue
	# mul()
	elif wordsearch == 1:
		if char == 'u':
			wordsearch = 3
		elif char == 'o':
			wordsearch = 12
		else:
			wordsearch = 0
	elif wordsearch == 3:
		if char == 'l':
			wordsearch = 4
		else:
			wordsearch = 0
	elif wordsearch == 4:
		if char == '(':
			wordsearch = 5
		else:
			wordsearch = 0
	elif wordsearch == 5:
		if char.isnumeric():
			wordsearch = 6
			num1 = num1 + str(char)
		else:
			wordsearch = 0
	elif wordsearch == 6: # Num1 adder
		if char.isnumeric():
			num1 = num1 + str(char)
			if len(num1) > 3:
				num1 = ""
				wordsearch = 0
		elif char == ',':
			wordsearch = 7
		else: # Restart search
			num1 = ""
			wordsearch = 0
	elif wordsearch == 7:
		if char.isnumeric():
			num2 = num2 + str(char)
			if len(num2) > 3:
				num1 = ""
				num2 = ""
				wordsearch = 0
		elif char == ')':
			finalTotal += int(num1) * int(num2)
			wordsearch = 0
			num1 = ""
			num2 = ""
		else: # Restart search
			num1 = ""
			num2 = ""
			wordsearch = 0

	#do??
	elif wordsearch == 11:
		if char == 'o':
			wordsearch = 12
		else:
			wordsearch = 0
	elif wordsearch == 12:
		if char == '(':
			wordsearch = 13
		elif char == 'n':
			wordsearch = 14
		else:
			wordsearch = 0

	#do()
	elif wordsearch == 13:
		if char == ')':
			doEnabled = True
			#print(f"enabled")
			wordsearch = 0
		else:
			wordsearch = 0	

	#don't()
	elif wordsearch == 14:
		if char == "'":
			wordsearch = 16
		else:
			wordsearch = 0
	elif wordsearch == 16:
		if char == 't':
			wordsearch = 17
		else:
			wordsearch = 0
	elif wordsearch == 17:
		if char == '(':
			wordsearch = 18
		else:
			wordsearch = 0
	elif wordsearch == 18:
		if char == ')':
			doEnabled = False
			#print(f"disabled")
			wordsearch = 0
		else:
			wordsearch = 0

print(f"The final total is {finalTotal}")