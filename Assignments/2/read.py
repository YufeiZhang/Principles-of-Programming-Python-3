import sys

try:
	command = sys.argv
	if len(command) != 4:
		if len(command) != 3:
			raise OSError

	filename,print_maze = '', False
	if '--file' in command:
		f_index = command.index('--file') + 1
		if f_index < len(command):
			filename = command[f_index]
	if '-print' in command:
		print_maze = True
	print(filename)
	print(print_maze)


	file = open(filename)

except OSError:
	print('I expect --file followed by filename and possibly -print as command line arguments.')


