def width():
	a = input("width:  ")
	try:
		if int(a) < 0:
			raise ValueError
		return int(a)
	except ValueError:
		print("Incorrect input, try again.")
		width()


def height():
	a = input("height: ")
	try:
		if int(a) < 0:
			raise ValueError
		return int(a)
	except ValueError:
		print("Incorrect input, try again.")
		height()


def main():
	w = width()
	h = height()

	m = 0
	for i in range(h):
		for j in range(w):
			if i%2:
				print(chr((m+w-j-1)%26+65), end = '')
			else:
				print(chr((m+j)%26+65),     end = '')
		print()
		m += w


main()

