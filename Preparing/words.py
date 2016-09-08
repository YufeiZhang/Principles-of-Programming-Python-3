# words.py



def main():
	try:
		#txt = open("test_1.txt")
		#txt = open("test_2.txt")
		#txt = open("test_3.txt")
		txt = open("test_4.txt")
		#target = input("Enter characters (spaces will be ignored): ")
		#target = "cluuud IN    DeD 23*"
		target = "NSCRT - oooe+*"
	except OSError:
		print("OSError: Cannot find the file.")

	string = ''
	for ch in target: string += ch.lower()

	lines = []
	for line in txt: line = line.strip(); lines.append(line)
	
	all_words = []
	for line in lines:
		words = line.split()
		for word in words:
			if not word[-1].isalpha(): word = word[:-1]
			if word.lower() not in all_words:
				all_words.append(word.lower())
	all_words = sorted(all_words)
	#print(all_words)

	
	is_in = {}
	for word in all_words:
		flag = 1
		for char in word:
			if char == '.':
				pass
			else:
				if char in string and char:
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