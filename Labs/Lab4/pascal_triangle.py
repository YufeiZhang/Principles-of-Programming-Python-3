'''
Write a program pascal_triangle.py that prompts the user for a number N and
prints out the first N + 1 lines of Pascal triangle, making sure the numbers
are nicely aligned, following this kind of interaction.
'''

try:
	n = int(input("Enter a nonnegative integer: "))
	if n < 0:
		raise ValueError

	pre = [0, 1, 0]
	for i in range(n):
		row = [0] 
		print(" "* (n-i-1), end = "")

		for j in range(i+1):
			row.append(pre[j] + pre[j+1])
			print(row[j+1], end = " ")

		pre = row; pre.append(0)
		print()

except ValueError:
	print("Value Error: You should enter a nonnegative integer")


