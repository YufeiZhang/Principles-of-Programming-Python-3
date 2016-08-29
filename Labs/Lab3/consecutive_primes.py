from math import ceil, sqrt

def is_prime(n):
	for i in range(2, ceil(sqrt(n))):
		if n % i == 0: return False
	return True

for i in range(10001, 100000, 2):
	if is_prime(i):
		if is_prime(i+2):
			if is_prime(i+6):
				if is_prime(i+12):
					if is_prime(i+20):
						if is_prime(i+30):
							if not is_prime(i+14) and not is_prime(i+18) and not is_prime(i+24):
								print(i, i+2, i+6, i+12, i+20, i+30)