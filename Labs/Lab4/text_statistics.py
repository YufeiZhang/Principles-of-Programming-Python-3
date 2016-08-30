'''
Write a program text_statistics.py that prompts the user for the name of a file
and outputs how many times each digit occurs in this file, provided it does 
occur, following this kind of interaction:
'''

try:
	filename = str(input("Enter the name of a file: text_"))
	txt = open("test_"+filename+".txt", 'r')
	digits = {}

	for line in txt:
		for char in line:
			if char.isnumeric():
				if char not in digits:
					digits[char] = 1
				else:
					digits[char] += 1

	digits = sorted(digits.items(), key = lambda x:x[0])

	if len(digits):
		print("Digits:", end = " ")
		for i in digits:
			print(i[0], end = " ")

		print("\nCount: ", end = " ")
		for j in digits:
			print(j[1], end = " ")
		print()
	else:
		print("There is no digit in this file.")

except OSError as ose:
	print("OSError: {0}".format(ose)) 

