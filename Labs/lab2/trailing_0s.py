num_of_0s, fact = 0,1

def count_0s(a, num_of_0s):
	print(a)
	if a % 10 == 0:
		num_of_0s += 1
		if a%25 == 0:
			num_of_0s+=1
		if a% 100 == 0:
			num_of_0s += 1
		count_0s(a//10, num_of_0s)
	return num_of_0s


for i in range(1,401):
	fact *= i
	if i%10 == 0:
		num_of_0s = count_0s(i,num_of_0s)
	elif i % 25 == 0:
		num_of_0s += 2
	elif i%10 == 5:
		num_of_0s += 1
num_of_0s = num_of_0s-1

print(fact)
print("There are {:d} trailing 0s in 1000!".format(num_of_0s))

