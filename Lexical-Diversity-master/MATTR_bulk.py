import os
import sys
import re
import json

def calculate_mattr50(text, tokens, total_types, types_50_sums, d):		#moving average type token ratio for window size of words
	if tokens < (int(window_size) - 1):	#further comments in context of a size 50 window
		types_50 = len(d)		#if token count is less than 49, avg type/token ratio defaults to flat number of types
	else:							#in a normal case
		denominator = tokens - (int(window_size) - 1) 	#denominator is going to be the number of windows/number of sets of 50
		types_50 = types_50_sums / denominator		#divide sum of types per 50 by number of 50s
	print(f"{text}\t{tokens}\t{total_types}\t{types_50}\n")

window_size = sys.argv[1]
taggedFiles = sys.argv[2]

taggedFiles = json.loads(taggedFiles)


def traverseData(taggedFiles):       #will be an array of two-item arrays: eachFile: [filename, filecontents]
    for eachFile in taggedFiles:
        d = {}
        t = {}
        l = []
        types_50_sums = float(0)
        types = 0
        total_types = 0
        tokens = 0
        filename = eachFile[0]
        if '_tagged.txt' in filename: 
            text = filename.replace('_tagged.txt', '')
            data = eachFile[1]
            print(filename)
            for line in data.split('\n'):
                
            #     line = line.rstrip('\n')
                line = line.split('\t')
                if (len(line) != 3):
                    line = ["'s", "POS", "'s"]
                #print(line)
                lemma = line[2]
                tokens += 1
                l.append(lemma)				#add lemma to list
                if lemma in d:
                    d[lemma] += 1			#add lemma to dictionary or increase value
                else:
                    d[lemma] = 1
                if lemma in t:
                    t[lemma] += 1			#add lemma to dictionary or increase value
                else:
                    t[lemma] = 1
                    total_types += 1
                if tokens >= int(window_size):
                    if tokens > int(window_size):			#not in first 50 words for book
                        chop_word = l[tokens - (int(window_size) + 1)] #chop_word becomes furthest left word in moving window
                        d[chop_word] -= 1			#find that word in d, decrease its value by 1
                        if d[chop_word] == 0:		#if that value reaches 0, delete word
                            del d[chop_word]		#dictionary token sum stays at 50 since it is all the values added up, basically
                    types = len(d)					#types is number of keys in dictionary
                    types_50_sums += types			#every set of 50, adds the number of keys to an accumulating total/sum
            calculate_mattr50(text, tokens, total_types, types_50_sums, d)
traverseData(taggedFiles)