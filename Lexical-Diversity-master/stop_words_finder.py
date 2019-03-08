import os
import sys
import re

target = 'tagged'

pathstump = "/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Analysis/"

d = {}

for dirname, dirs, files in os.walk('.'):
    if target in dirname:
        #author = re.findall("..(.*?)\\\\tagged", dirname)[0]
        author = dirname.split(os.sep)[1]
        #print author
        # .\James\tagged\..\James_MAT_50.txt
        for filename in files:
            if 'tagged.txt' in filename: 
                book = filename.replace('_tagged.txt', '')
                data = open(pathstump + author + "/" + "tagged/" + filename, 'r')
                for line in data:
                    line = line.rstrip('\n')
                    line = line.split('\t')
                    lemma = line[2]
                    if lemma in d:
                        d[lemma] += 1			#add lemma to dictionary or increase value
                    else:
                        d[lemma] = 1
for entry in sorted(d.items(), key=lambda x: (-x[1],x[0]))[:5]:
	print entry[0], entry[1]