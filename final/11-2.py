import sys
from random import seed, sample
from priority_queue import *

def main():
    #args = input('Enter 2 nonnegative integers: ').split()
    try:
        #if len(args) != 2: raise ValueError
        #_seed  = int(args[0])
        #length = int(args[1])
        _seed = 0; length = 5
        
        if length < 0 or length > 100:
            print('Incorrect input (2nd integer not between 1~99), give up')
            sys.exit()        
    except ValueError:
        print('Incorrect input (not all integers or not exactly two integers), giving up.')
        sys.exit()

    seed(_seed)
    L = sample(range(length * 10), length)
    #print(L)
    pq = PriorityQueue()
    for e in L:
        pq.insert(e)
    print('The heap that has been generated is: ')
    print(pq._data[ : len(pq) + 1])
    print('The preferred ordering of data to generate this heap by successive insertions is:')
    

if __name__ == '__main__':
    main()
