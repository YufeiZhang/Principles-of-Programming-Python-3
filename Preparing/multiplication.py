# multiplication.py

for i in range(100,389,2): # 9988 / 22 = 454
	for j in range(22,99, 2): # 9988 / 100 = 99.8
		shiwei = str(j)[0]
		gewei  = str(j)[1]
		#print(shiwei, gewei)
		a = i * int(gewei)
		b = i * int(shiwei)
		c = a + 10*b

		a,b,c = str(a), str(b),str(c)
		if int(c) <= 9988 and int(b) <= 989 and int(a) >= 2122:
			i,j= str(i),str(j)
			if int(a[0])%2==0 and int(a[1])%2 and int(a[2])%2 == 0 and int(a[3])%2 == 0:
				if int(b[0])%2==0 and int(b[1])%2 and int(b[2])%2 == 0:
					if int(c[0])%2 and int(c[1])%2 and int(c[2])%2 == 0 and int(c[3])%2 == 0:
							print("\
  {} {} {}\n\
x   {} {}\n\
  -----\n\
{} {} {} {}\n\
{} {} {}\n\
-------\n\
{} {} {} {}".format(\
i[0], i[1], i[2],\
j[0], j[1],\
a[0], a[1], a[2], a[3],\
b[0], b[1], b[2],\
c[0], c[1], c[2], c[3]))
