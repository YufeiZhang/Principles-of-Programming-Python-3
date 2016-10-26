choice = [100, 50, 20, 10, 5, 2, 1]
data = {}
amount = input("Input the desired amount: ")

nowa = 0
while amount:
	if amount//nowa: data[choice[nowa]] = amount//nowa
	nowa += 1
print(data)
