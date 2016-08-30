from random import randint as ri

L = [ri(-50, 50) for _ in range(10)]

print("The list is:", L)

max_element = 0
mim_element = 0

for i in range(10):
    if L[i] > max_element:
        max_element = L[i]
    if L[i] < mim_element:
        mim_element = L[i]
print('  The maximum number in this list is:', max_element-mim_element)
# Of course there is an easier way;
# as so often, python just makes it too easy!
print('Confirming with builtin operation:', max(L)-min(L))


