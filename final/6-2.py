'''
Please input the first string: ??got
Please input the second string: ?it?go#t##
Please input the third string: it###
The second string can be obtained by merging the other two.
'''

str1 = str(input('Please input the first string: '))
str2 = str(input('Please input the second string: '))
str3 = str(input('Please input the third string: '))

#str1 = '??got'
#str2 = '?it?go#t##'
#str3 = 'it###'
#str1 = 'aaab'
#str2 = 'abcab'
#str3 = 'aaabcaabb'

string = [str1, str2, str3]
length = [len(str1),len(str2),len(str3)]
target = list(string.pop(length.index(max(length))))

#print(target)
#print(string)

a = 0
b = 0
fs = 0
bad = 0
while target:
    t = target.pop(0)
    good = 0
    for i in range(2):
        if (fs+i)%2:
            if b < len(string[(fs+i)%2]) and string[(fs+i)%2][b] == t:
                b += 1
                good = 1
                fs += 1
                fs = fs%2
                break
        else:
            if a < len(string[(fs+i)%2]) and string[(fs+i)%2][a] == t:
                a += 1
                good = 1
                fs += 1
                fs = fs%2
                break
    if good:
        #print(t)
        bad = 0
    else:
        bad = 1

    if bad:
        print('There is no solution.')
        break

if good:
    if   length.index(max(length)) == 0:
        print('The first string can be obtained by merging the other two.')
    elif length.index(max(length)) == 1:
        print('The second string can be obtained by merging the other two.')
    elif length.index(max(length)) == 2:
        print('The third string can be obtained by merging the other two.')
    
