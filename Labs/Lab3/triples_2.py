from math import sqrt, ceil

def is_aa_plus_bb(n):
	for i in range(ceil(sqrt(n))+1):
		for j in range(ceil(sqrt(n))+1):
			if i*i + j*j == n:
				return True
	return False


for i in range(140, 810):
	if is_aa_plus_bb(i) and is_aa_plus_bb(i+1) and is_aa_plus_bb(i+2):
		print(i, i+1, i+2)

