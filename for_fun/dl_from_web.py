'''
This is a function that reads an instagram only webpage and download all of 
the pictures on someone's main page.
'''

import urllib.request, urllib.parse, urllib.error

# set an instagram website as page_sourse and the iteration starting from 1
page_sourse = 'https://www.instagram.com/ryiiiann/?hl=en'
i = 1

# open the pase_source and read the page
with urllib.request.urlopen(page_sourse) as response:
   html = str(response.read())

# split a page sourse and store it into a list
html_list = html.split(',')
for ch in html_list:
	# all pictures are following the str "display_src"
	if "display_src" in ch:
		# get the index of where the souce start and end
		start = ch.find("https://")
		end = ch.find("}")
		# download the picture and store it as .png file
		urllib.request.urlretrieve(ch[start:end-1], str(i)+".png")
		i+=1






