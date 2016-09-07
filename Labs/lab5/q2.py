from csv import reader as cread

filename = "HNP_Data.csv"
#filename = "testing.csv"

try:
	file = cread(open(filename))

	#indicator = str(input("Enter an indicator Name: "))
	#indicator = "Literacy rate, youth total (% of people ages 15-24)"
	#indicator = "Age population, age 12, female, interpolated"
	#indicator = "Newborns protected against tetanus (%)"
	#indicator = "Number of neonatal deaths"
	indicator = "Female headed households (% of households with a female head)"


	next(file) # I do not need to see the first line of the csv file

	max_value = 0
	countries = []

	for line in file:
		if line[2] == indicator:
			#print(line)
			for i in range(56):
				if line[i+4] == '': num = 0
				else:             num = float(line[i+4])

				if num >= max_value:
					if num == max_value:
						countries.append(line[0])
						countries.append(1960+i)
					else:
						countries = [line[0]]
						countries.append(1960+i)
					max_value = num

	#print(countries)
	#print(max_value)

	wat = {}
	for i in range(1, len(countries), 2):
		if int(countries[i]) not in wat:
			wat[int(countries[i])] = [countries[i-1]]
		else:
			wat[int(countries[i])].append(countries[i-1])
	#print(wat)

	print('''The maximum value is: {}\nIt was reached in these years, for these countries or categories:'''.format(round(max_value,1)))
	for ch in wat:
		print("\t{}: {}".format(ch, wat[ch]))



	#print(file)

except OSError:
	print('There is no file named {} in the working directory, giving up...'.format(filename))


