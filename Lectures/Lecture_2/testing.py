# This is a useful line:
# [x for x in dir(set) if not x.startswith"__"]

from random import choice, randint

def gogogo():
	while 1:
		try:
			iteration = int(input("input a number: "))
			if iteration <= 0:
				raise ValueError		 
			break
		except:
			print("Not happy, try again.") 
	while True:
		switch = input("Do you want to switch? ")
		if switch in (["Yes", "yes", "Y","y"]):
			switch = True
			break
		elif switch in (["No", "no", "N","n"]):
			switch = False
			break
		print("Not happy, try again. with y/n.")
	return iteration, switch


def simulate():
	(iteration, switch) = gogogo()
	num_of_wins = 0
	for _ in range(iteration):
		doors = ['A','B','C']
		winning_door = choice(doors)
		first_choice = choice(doors)
		print(winning_door, first_choice)

		if first_choice == winning_door:
			if switch:
				second_choice = doors[0]
			else:
				second_choice = first_choice
				num_of_wins +=1 
		else:
			
			if :
				pass
			else:
				pass
	print()



if __name__ == '__main__':
	simulate()

