from itertools import combinations as cb

try:
    digits = list(input('Input a number that we will use as available digits: '))
    target = int(input('Input a number that represents the desired sum: '))

    #print(digits)
    solutions = []
    for i in range(len(digits)):
        combine = list(cb(digits, i+1))
        for cm in combine:
            _sum = 0
            cm = list(cm)
            #print(cm)
            for c in cm:
                _sum += int(c)
            if _sum == target:
                solutions.append(cm)
    #print(solutions)

    num = len(solutions)
    if num:
        if num == 1:
            print('There is a unique solution.')
        else:
            print('There are {} solutions.'.format(num))
    else:
        print('There is no solution.')

except ValueError:
    print('Value Error.')
