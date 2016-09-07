from csv import reader as cread

#filename = "HNP_Data.csv"
filename = "testing.csv"

try:
	file = cread(open(filename))
	next(file) # I do not need to see the first line of the csv file
	for line in file:
		print(line)
	#print(file)

except OSError:
	print('There is no file named {} in the working directory, giving up...'.format(filename))