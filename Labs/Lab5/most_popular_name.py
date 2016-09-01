import os.path
import sys
import io

for filename in os.listdir('names/'):
	#print(filename)
	with io.open('names/' + filename, encoding='utf-8') as ori_txt:
		#print(ori_txt)
		#print(ori_txt)
		for line in ori_txt:
			print(line)
	#txt = open('names/' + filename)
	#print(txt)