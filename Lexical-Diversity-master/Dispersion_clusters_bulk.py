import os
import sys
import re

#stop_words = ["the", "be", "and", "of", "a"] #most common words in English
stop_words = ["the", "be", "and", "to", "a"] #most common words in my data, gathered from stop_words_finder.py

window_size = sys.argv[1]
target = 'tagged'

pathstump = "/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Analysis/"

for dirname, dirs, files in os.walk('.'):
    if target in dirname:
        #author = re.findall("..(.*?)\\\\tagged", dirname)[0]
        author = dirname.split(os.sep)[1]
        #print author
        output = os.path.join(dirname, '..', author + "_Dispersion_" + str(window_size) + ".txt")
        outfile = open(output, 'w')
        # .\James\tagged\..\James_MAT_50.txt
        for filename in files:
            d = {}
            tokens = 0
            clusters = 0
            if '_tagged.txt' in filename: 
                book = filename.replace('_tagged.txt', '')
                data = open(pathstump + author + "/" + "tagged/" + filename, 'r')
                for line in data:
                    line = line.rstrip('\n')
                    line = line.split('\t')
                    lemma = line[2]
                    tokens += 1
                    if lemma not in stop_words:
                        if lemma not in d:
                            d[lemma] = tokens
                        else:
                            if (tokens - d[lemma]) < int(window_size):				######Make sure you change this number to reflect the cluster size.
                                clusters += 1
                                #cluster_words.append(lemma)
                            d[lemma] = tokens
                clusters = float(clusters)
                density = (clusters / tokens) * 100
            print>>outfile, "%s\t%.0f\t%.0f\t%.2f" % (book, tokens, clusters, density)