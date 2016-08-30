# Write a program characters_triangle.py that gets a strictly positive integer N
# as input and outputs a triangle of height N, following this kind of interaction:

try:
	n = int(input("Enter strictly positive number: "))
	if n < 0:
		raise ValueError

	m = 0
	for i in range(n):
		m += i
		print(" "* (n-i-1), end = "")
		for j in range(2*i + 1):
			if j > i:
				print(chr(((m + i+i - j)%26) + 65), end = "")
			else:
				print(chr(((m + j)%26) + 65), end = "")
		print()

except ValueError:
	print("Value Error: You cannot input a negative int")
