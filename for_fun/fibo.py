from datetime import datetime as dt

def fibo_iter(n, t1 = 0, t2 = 1):
	if   n == 0: return t1
	elif n == 1: return t2
	else:
		for i in range(n-1): t1, t2 = t2, t1 + t2
		return t2


def fibo_rcsn(n):
	pass



def fibo_re_2(n):
	pass



n = 10

a = td.now()
print(fibo_iter(n))
b = td.now()
print(b-a)


a = td.now()
print(fibo_rcsn(n))
b = td.now()
print(b-a)


a = td.now()
print(fibo_re_2(n))
b = td.now()
print(b-a)