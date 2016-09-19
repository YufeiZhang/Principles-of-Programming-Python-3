import sys

try:
	command = sys.argv
	filename = ''
	print_it = False
	print(command)

	if len(command) != 4:
		if len(command) != 3:
			raise OSError

	if command[0] == 'read.py' and '--file' in command:
		f_index = command.index('--file') + 1
		if f_index < len(command):
			filename = command[f_index]
	print(filename)
	print(print_it)


	file = open(filename)

except OSError:
	print('I expect --file followed by filename and possibly -print as command line arguments.')


