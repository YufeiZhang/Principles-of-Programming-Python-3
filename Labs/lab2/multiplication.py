output = [0,0,0,0]
factor = [10,1]

for m in range(100, 1000):
	m = str(m)
	m1 = '0'  + m
	for n in range(11,100):
		output = [0,0,0,0]
		n = str(n)
		if int(m) * int(n) < 10000:
			n1 = '00' + n
			for i in range(len(n)): a = str(int(m) * int(n[i]) * factor[i])
				for j in range(-1,-len(a)-1,-1): output[j] += int(a[j]) * 2
			for i in range(4): output[i] += int(m1[i]) + int(n1[i])

			if  output[0] == output[1] \
			and output[1] == output[2] \
			and output[2] == output[3]:
				print("{:d} * {:d} = {:d}, all columns adding up to {:d}"\
					.format(int(m), int(n), int(m)*int(n), int(output[0])))

