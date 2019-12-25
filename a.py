import re

with open('c:/temp/test.txt') as f:
	str=f.read()
	pat = re.compile(r'https://ss2.meipian.me/users/5968647/.*?src="(.*?.jpg)-mobile')
	urls = pat.findall(str)
	for url in urls:
		print(url)
