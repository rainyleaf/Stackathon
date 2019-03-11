#doesn't actually contain any bulk functionality as the only input is the specialwords list, but the specialwords list
#was derived from a bulk script, so the naming has been kept consistent

from nltk.corpus import wordnet as wn
import sys
import os
import re
reload(sys)
sys.setdefaultencoding('UTF8')

infile = open("/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Analysis/nouns_and_verbs.txt").readlines()
outfile = open("/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Analysis/novels_hypernym_paths.txt", 'w')

path_lengths = []
avg_depths = []
max_depths = []

onNouns = False

for line in infile:
	line = line.rstrip('\r\n')
	word = line
	if word == "Verbs":
		print>>outfile, "@Verbs"
		continue
	if word == "Nouns":
		onNouns = True
		print>>outfile, "@Nouns"
		continue
	for synset in wn.synsets(word):
		if onNouns == False:
			if synset.pos() == "v":
				hypernymPaths = synset.hypernym_paths()
				for item in hypernymPaths:
					path_lengths.append(len(item))
				avgHypDepth = sum(path_lengths)/len(path_lengths) - 1
				avg_depths.append(avgHypDepth)
				depth = synset.max_depth()
				max_depths.append(depth)


		if onNouns == True:
			if synset.pos() == "n":
				hypernymPaths = synset.hypernym_paths()
				for item in hypernymPaths:
					path_lengths.append(len(item))
				avgHypDepth = sum(path_lengths)/len(path_lengths) - 1
				avg_depths.append(avgHypDepth)
				depth = synset.max_depth()
				max_depths.append(depth)

		path_lengths = []

	if len(max_depths) == 0:
		avgMaxDepth = 0
	else:
		avgMaxDepth = sum(max_depths)/len(max_depths)
	if len(max_depths) == 0:
		avgPathDepths = 0
	else:
		avgPathDepths = sum(avg_depths)/len(avg_depths)

	print>>outfile, "%s\t%s\t%s" % (word, avgPathDepths, avgMaxDepth)

	avg_depths = []
	max_depths = []
