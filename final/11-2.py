import sys
from random import seed, sample


def main():
    args = input('Enter 2 nonnegative integers: ').split()
    try:
        arg1 = int(args[0])
        arg2 = int(args[1])
    except ValueError:
        print('Incorrect input (not all integers), giving up.')
        sys.exit()


if __name__ == '__main__':
    main()
