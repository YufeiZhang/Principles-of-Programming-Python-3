'''
$ python3 merging_strings.py
Please input the first string: ab
Please input the second string: cd
Please input the third string: abcd
The third string can be obtained by merging the other two.

$ python3 merging_strings.py
Please input the first string: ab
Please input the second string: cdab
Please input the third string: cd
The second string can be obtained by merging the other two.

$ python3 merging_strings.py
Please input the first string: abcd
Please input the second string: cd
Please input the third string: ab
The first string can be obtained by merging the other two.

$ python3 merging_strings.py
Please input the first string: ab
Please input the second string: cd
Please input the third string: adcb
No solution
'''

str1 = str(input("Please input the first string: "))
str2 = str(input("Please input the second string: "))
str3 = str(input("Please input the third string: "))

if   len(str1) > len(str2) and len(str1) > len(str3):
	if str2+str3 == str1 or str3+str2 == str1:
		print("The first string can be obtained by merging the other two.")
	else:
		print("No solution")
elif len(str2) > len(str1) and len(str2) > len(str3):
	if str1+str3 == str2 or str3+str1 == str2:
		print("The second string can be obtained by merging the other two.")
	else:
		print("No solution")
elif len(str3) > len(str1) and len(str3) > len(str2):
	if str1+str2 == str3 or str2+str1 == str3:
		print("The third string can be obtained by merging the other two.")
	else:
		print("No solution")

