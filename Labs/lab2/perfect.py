n = 1

while n < 1000:
    if sum([i for i in range(1,n+1) if n%i == 0]) == 2*n:
    	print("{:d} is a 3-digit perfect number.".format(n))
    n += 1
