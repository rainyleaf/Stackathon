import os
import sys
import re

def calculate_mattr50():		#moving average type token ratio for 50 words)
	if tokens < (int(window_size) - 1):				#this won't happen? also don't get it
		types_50 = len(d)		#if token count is less than 49, avg type/token ratio defaults to flat number of types
	else:							#in a normal case
		denominator = tokens - (int(window_size) - 1) 	#denominator is going to be the number of windows/number of sets of 50
		types_50 = types_50_sums / denominator		#divide sum of types per 50 by number of 50s
	print>>outfile, "%s\t%s\t%s\t%.2f" % (book, tokens, total_types, types_50)

window_size = sys.argv[1]
target = 'tagged'

d = {}
l = []
types_50_sums = float(0)
types = 0
tokens = 0
total_types = 0

pathstump = "/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Analysis/"

for dirname, dirs, files in os.walk('.'):
    if target in dirname:
        #author = re.findall("..(.*?)\\\\tagged", dirname)[0]
        author = dirname.split(os.sep)[1]
        #print author
        output = os.path.join(dirname, '..', author + "_MAT_" + str(window_size) + ".txt")
        outfile = open(output, 'w')
        # .\James\tagged\..\James_MAT_50.txt
        for filename in files:
            d = {}
            l = []
            types_50_sums = float(0)
            types = 0
            total_types = 0
            tokens = 0
            if '_tagged.txt' in filename: 
                book = filename.replace('_tagged.txt', '')
                data = open(pathstump + author + "/" + "tagged/" + filename, 'r')
                for line in data:
                    line = line.rstrip('\n')
                    line = line.split('\t')
                    lemma = line[2]
                    tokens += 1
                    l.append(lemma)				#add lemma to list
                    if lemma in d:
                        d[lemma] += 1			#add lemma to dictionary or increase value
                    else:
                        d[lemma] = 1
                        total_types += 1
                    if tokens >= int(window_size):
                        if tokens > int(window_size):			#not in first 50 words for book
                            chop_word = l[tokens - (int(window_size) + 1)] #chop_word becomes furthest left word in moving window
                            d[chop_word] -= 1			#find that word in d, decrease its value by 1
                            if d[chop_word] == 0:		#if that value reaches 0, delete word
                                del d[chop_word]		#dictionary token sum stays at 50 since it is all the values added up, basically
                        types = len(d)					#types is number of keys in dictionary
                        types_50_sums += types			#every set of 50, adds the number of keys to an accumulating total/sum
                calculate_mattr50()