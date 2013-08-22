#!/usr/bin/env python
#usage: example-create-wordlist.py <file(s)> > wordlist.js
import sys

srcfiles = ['/usr/share/common-licenses/GPL', '/usr/share/common-licenses/BSD']
if len(sys.argv) > 1:
	srcfiles = sys.argv[1:]

words = {}
total = 0
for f in srcfiles:
	for line in open(f):
		for word in line.split():
			word = ''.join(filter(str.isalnum,word))
			if not word:
				continue
			total += 1
			if word in words:
				words[word] += 1
			else:
				words[word] = 1

print ('var wordlist = ')
print (list(sorted([[word, float(count) / float(total)] for (word,count) in words.items()], key=lambda entry: entry[1], reverse=True)))
print (';')
