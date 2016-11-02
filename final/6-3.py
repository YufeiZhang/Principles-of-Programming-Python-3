'''
Please input a string of lowercase letters: abefcgd
The solution is: abcd
'''

string = list(input('Please input a string of lowercase letters: '))
#string = list('abcpqrstuvwxbcbcddddeffghijklrst')

coms = []

while string:
    add = 1
    s = string.pop(0)
    for i in range(len(coms)):
        #print(ord(coms[i][-1]))
        if (ord(s)-97)%26 - (ord(coms[i][-1])-97)%26 == 1:
            coms[i] = coms[i] + s
            add = 0
    if add:
        coms.append(s)
#print(coms)

if coms:
    length = []
    for c in coms:
        length.append(len(c))
    max_one = coms[length.index(max(length))]
    
    print('The solution is: {}'.format(max_one))
else:
    print('There is no solution.')

