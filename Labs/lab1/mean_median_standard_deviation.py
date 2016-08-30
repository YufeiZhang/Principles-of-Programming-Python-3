from random import randint
import sys
import numpy as np
import statistics


nb_of_elements = input('How many elements do you want to generate? ')
try:
    nb_of_elements = int(nb_of_elements)
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()

L = [randint(-50, 50) for _ in range(nb_of_elements)]
print('The list is:' , L)


mean = sum(L)/nb_of_elements
print(' The mean is {:2.2f}'.format(mean))
sl = sorted(L)
if len(sl) % 2:
	print(' The median is {:2.2f}'.format(sl[len(sl)//2]))
else:
	print(' The median is {:2.2f}'.format((sl[len(sl)//2-1]+sl[len(sl)//2])/2))
sumsq = 0
for ch in L:
	sumsq += (ch-mean)**2
print(' The standard deviation is {:2.2f}'.format(np.sqrt(sumsq/nb_of_elements)))


print(' The mean is {:2.2f}'.format(np.mean(L)))
print(' The median is {:2.2f}'.format(np.median(L)))
print(' The standard deviation is {:2.2f}'.format(np.std(L)))

