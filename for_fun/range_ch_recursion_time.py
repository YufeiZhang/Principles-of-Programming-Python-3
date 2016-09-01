from datetime import datetime as dt

def for_i_in_range(L, sumision = 0):
	for i in range(len(L)):
		sumision += L[i]
	return sumision


def for_ch_in_list(L, sumision = 0):
	for ch in L:
		sumision += ch
	return sumision


def recursion(L):
	if L == []:
		return 0
	return recursion(L[1:]) + L[0]

def recursion2(L):
	if len(L) == 1: return L[0]
	return recursion2(L[:len(L) // 2]) + recursion2(L[len(L) // 2:])




L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
	,31,32,33,34,35,36,37,38,39,40, 41,42,43,44,45,46,47,48,49,50,51,52,53,54,55]

start = dt.now()
print(for_i_in_range(L))
end   = dt.now()
print(end - start)


start = dt.now()
print(for_ch_in_list(L))
end   = dt.now()
print(end - start)


start = dt.now()
print(recursion(L))
end   = dt.now()
print(end - start)



start = dt.now()
print(recursion2(L))
end   = dt.now()
print(end - start)













