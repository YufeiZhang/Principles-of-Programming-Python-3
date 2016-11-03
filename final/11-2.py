import sys
from random import seed, sample
from priority_queue import *

def preferred_sequence(pq,l):
    output = []
    target = pq._data[:l+1]
    print(target)

    while l-1:
        pre = l // 2
        print(target[pre], target[l])
        if target[pre] > target[l]:
            output.insert(0, target[pre])
            target[pre] = target[l]
            target.pop()
        else:
            output.insert(0, target.pop())
        l -= 1
    output.insert(0, target[1])
    
    return output

def main():
    #args = input('Enter 2 nonnegative integers: ').split()
    try:
        #if len(args) != 2: raise ValueError
        #_seed  = int(args[0])
        #length = int(args[1])
        _seed = 0; length = 10
        
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
    print(preferred_sequence(pq,length))

if __name__ == '__main__':
    main()
