'''
$ python3 longest_sequence.py
Please input a string of lowercase letters: abcefgh
The solution is: efgh

$ python3 longest_sequence.py
Please input a string of lowercase letters: abcefg
The solution is: abc

$ python3 longest_sequence.py
Please input a string of lowercase letters: ablccmdnneofffpg
The solution is: abcdefg
'''

letters = str(input("Please input a string of lowercase letters: "))

solutions = [[letters[0]]]


for ch in letters[1:]:
	flag = 1
	for i in range(len(solutions)):
		if (ord(ch.lower())-97)%26 - 1 == (ord(solutions[i][-1].lower())-97)%26:
			solutions[i].append(ch)
			flag = 0
			break
	if flag:
		solutions.append([ch])


max_len = 0
max_idx = 0
for i in range(len(solutions)):
	if len(solutions[i]) > max_len:
		max_len = len(solutions[i])
		max_idx = i

out = ''
for ch in solutions[max_idx]:
	out += ch

print("The solution is:", out)



