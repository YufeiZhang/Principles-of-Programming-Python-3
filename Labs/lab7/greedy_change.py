choice = [100, 50, 20, 10, 5, 2, 1]
data = {}
amount = int(input("Input the desired amount: "))

nowa = 0
while amount:
	#print(amount)
	checking = amount//choice[nowa]
	#print(checking)
	if checking: data[choice[nowa]] = checking; amount -= checking*choice[nowa]
	nowa += 1

data = sorted(data.items(), key=lambda x:x[0], reverse = True)
#print(data)

for ch in data:
	print('${}: {}'.format(ch[0], ch[1]))
