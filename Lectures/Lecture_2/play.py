if 1 > 0 and 1 > -1:
	print (111)
if (1 > 0) ^ (1 > 1): # ^ is xor
	print(222)

# ^ is xor
# | is or
# & is and

def gcd(a,b):
	while b: a,b = b, a%b; return a
	
print(gcd(16,24))
print(gcd(34, 12))

def two(a,b):
	return a+b, a*b

def one(a,b):
	return a, b

print(two(*one(1,2)))

a = []
b = [1,2]
for ch in a:
	b.append(ch)
print(b)
