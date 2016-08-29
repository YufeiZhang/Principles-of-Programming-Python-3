
for i in range(12, 77):
	for j in range(10, 88):
		for k in range(10, 99): 
			num_str = str(i*j*k)

			if str(i)[0] in num_str and str(i)[1] in num_str and str(i)[0] != str(i)[1]:
				a = num_str.find(str(i)[0])
				b = num_str.find(str(i)[1])
				num_str = num_str.replace(str(i)[0], "")
				num_str = num_str.replace(str(i)[1], "")

				if str(j)[0] in num_str and str(j)[1] in num_str and str(j)[0] != str(j)[1]:
					a = num_str.find(str(j)[0])
					b = num_str.find(str(j)[1])
					num_str = num_str.replace(str(j)[0], "")
					num_str = num_str.replace(str(j)[1], "")

					if str(k)[0] in num_str and str(k)[1] in num_str and str(k)[0] != str(k)[1]:
						if i < j and j < k:
							print(i, "x", j, "x", k, "=", str(i*j*k))

