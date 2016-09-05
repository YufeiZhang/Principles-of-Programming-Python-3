# decoding.py
def find_upper(m, n, upper_bound = 0):
	while m**upper_bound <= n:
		upper_bound += 1
	return upper_bound-1


# n = 2^0 + 2^1 + 2^2 + 2^3
def  decode(m, n):
	codes = []

	while n > 0:
		upper_bound = find_upper(m,n)
		for j in range(1,11):
			if n - j * (m**upper_bound) < 0:
				break
		n -= (j-1) * (m**upper_bound)
		codes.append(upper_bound)

	out = "{"
	for ch in codes:
		if ch != codes[-1]:
			out += str(ch)+", "
		else:
			out += str(ch)+'}'
	
	return out

if __name__ == '__main__':
	print(decode(8,4223296))


