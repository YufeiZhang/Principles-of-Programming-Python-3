# 9988 / 100 = 99.88
# 9988 /  22 = 454

for i in range(100, 455, 2):
	for j in range(22, 99, 2):
		c = i*j
		if int(c) <= 9988:
			c = str(c); j = str(j)

			a = str(i * int(j[1]))
			b = str(i * int(j[0]))

			if int(c[0])%2 and int(c[1])%2 and int(c[2])%2 == 0 and int(c[3])%2 == 0 and len(a) == 4 and len(b) ==3:
				if int(a[0])%2 == 0 and int(a[1])%2 and int(a[2])%2 == 0 and int(a[3])%2 == 0:
					if int(b[0])%2 == 0 and int(b[1])%2 and int(b[2])%2 == 0:
						#print(i,j,a,b,c)
						i = str(i)
						print("\
  {} {} {}\n\
x   {} {}\n\
  -----\n\
{} {} {} {}\n\
{} {} {}\n\
-------\n\
{} {} {} {}".format(\
i[0],i[1],i[2],\
j[0],j[1],\
a[0],a[1],a[2],a[3],\
b[0],b[1],b[2],\
c[0],c[1],c[2],c[3]))


