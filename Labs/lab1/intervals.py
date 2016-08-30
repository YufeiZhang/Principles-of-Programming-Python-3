from random import randint
import sys


nb_of_elements = input('How many elements do you want to generate? ')
try:
    nb_of_elements = int(nb_of_elements)
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()

L = [randint(0, 19) for _ in range(nb_of_elements)]
print('The list is:' , L)



remainders_intervals = [0] * 4

for i in range(nb_of_elements):
    if 0 <= L[i] and L[i] <= 4:
    	remainders_intervals[0] += 1
    elif 5 <= L[i] and L[i] <= 9:
    	remainders_intervals[1] += 1
    elif 10 <= L[i] and L[i] <= 14:
    	remainders_intervals[2] += 1
    elif 15 <= L[i] and L[i] <= 19:
    	remainders_intervals[3] += 1

for i in range(4):
    if remainders_intervals[i] < 2:
        print(' There is {} elements between {} and {}.'.format(remainders_intervals[i], i*5, i*5+4))
    else:
        print(' There are {} elements between {} and {}.'.format(remainders_intervals[i], i*5, i*5+4))

