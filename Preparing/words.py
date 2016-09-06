# words.py



def main():
	try:
		txt = open("text_file.txt")
		target = input("Enter characters (spaces will be ignored): ")
	except OSError:
		print("OSError: Cannot find the file.")

	string = ''
	for ch in target: string += ch.lower()

	words = []
	for line in txt: line = line.strip(); words.append(line)

	
	is_in = {}
	for word in words:
		flag = 1
		for char in word:
			if char in string:
				pass
			else:
				flag = 0
				break
		if flag:
			if len(word) not in is_in:
				is_in[len(word)] = [word]
			else:
				is_in[len(word)].append(word)

	
	is_in = sorted(is_in.items(), key = lambda x:x[0])

	for key in is_in:
		print("Words of length {:d} built from these characters, in lexicographic order:".format(key[0]))
		for ch in key[1]:
			print('\t', ch)



if __name__ == '__main__':
	main()