# written by yufei

def is_deficient(n):
	devisors = []
	for i in range(1, n):
		if n % i == 0:
			devisors.append(i)

	if sum(devisors) <= n:
		return True
	else:
		return False

def main():
	try:
		a,b = input("Enter two strictly positive numbers: ").split()
		if a.isnumeric() and b.isnumeric():
			pass
		else:
			raise ValueError
		a,b = int(a),int(b)

		if a <= b:
			out = []
			current = []
			for i in range(a, b+1):
				if is_deficient(i):
					current.append(i)
				else:
					out.append(current)
					current = []
			out.append(current)

		max_length = 0
		max_index = -1
		for ch in out:
			if len(ch) > max_length:
				max_length = len(ch)
				max_index += 1

		print("The longest sequence of deficient numbers between {:d} and {:d} ranges between {:d} and {:d}.".format(a,b,out[max_index][0],out[max_index][-1]))
	except ValueError:
		print("Incorrect input, giving up.")



if __name__ == '__main__':
	main()