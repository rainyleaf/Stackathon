#not doing 'override' due to number of weird smashed-together words in list

from nltk.corpus import wordnet as wn
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

infile = open("/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Analysis/novels_hypernym_paths.txt").readlines()
cocaFile1000 = open("/Users/Torri/pythonstuff/COCA-top1000.txt").read().splitlines()
cocaFile900 = open("/Users/Torri/pythonstuff/COCA-top900.txt").read().splitlines()
cocaFile5000 = open("/Users/Torri/pythonstuff/COCA-top5000.txt").read().splitlines()

specialwords = []
onNouns = False

for line in infile[1:]:
	line = line.rstrip('\r\n')
	first_char = line[0]
	line = line.split('\t')
	if first_char == "@":
		onNouns = True
	else:
		word = line[0]
		depth = line[1]
		if onNouns == False:	#if doing verbs
			if (int(depth) >= 2) and (word not in cocaFile900):
				specialwords.append(word)
			#elif word not in cocaFile5000 and ("\'" not in word):	#'override'
				#specialwords.append(word)
		if onNouns == True:
			if (int(depth) >= 7) and (word not in cocaFile1000):
				specialwords.append(word)

for word in specialwords:
	print word
