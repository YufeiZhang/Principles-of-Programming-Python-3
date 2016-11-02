'''
Input the desired amount: 739

12 banknotes are needed
The detail is:
$100: 7
 $20: 1
 $10: 1
  $5: 1
  $2: 2
'''

#amount = int(input('Input the desired amount: '))
amount = 739

order1 = [100, 50, 20, 10, 5, 2, 1]
spaces = {100:'', 50:' ', 20:' ', 10:' ', 5:'  ', 2:'  ', 1:'  '}
order2 = []
record = {}

count = 0
while amount:
    for r in order1:
        if amount // r:
            count += amount//r
            record[r] = amount // r
            order2.append(r)
            amount = amount % r

print('\n{} banknotes are needed\nThe detail is:'.format(count))
for o in order2:
    print('{}${}: {}'.format(spaces[o], o, record[o]))
