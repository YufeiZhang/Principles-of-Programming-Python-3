'''
$ python3 sum_of_digits.py
Input a number that we will use as available digits: 12234
Input a number that represents the desired sum: 5
There are 4 solutions.

$ python3 sum_of_digits.py
Input a number that we will use as available digits: 11111
Input a number that represents the desired sum: 5
There is a unique solution
'''

from itertools import combinations as cb 

try:
	a = input("Input a number that we will use as available digits: ")
	b = input("Input a number that represents the desired sum: ")
	if int(a) < 0 or int(b) < 0: raise ValueError

	a_list = list(a)
	sums = []

	for i in range(len(a_list)):
		combies = list(cb(a_list,i+1))

		for ch in combies:
			_sum = 0
			ch = list(ch)
			for c in ch:
				_sum += int(c)
			sums.append(_sum)

	count = 0
	for ch in sums:
		if ch == int(b):
			count+=1

	if count > 1:
		print("There are {:d} solutions.".format(count))
	elif count == 1:
		print("There is a unique solution")
	else:
		print("There is no solution.")



except ValueError:
	print("Both inputs cannot be negative.")