import os
import sys
import math

target = 'tagged'
pathstump = "/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Analysis/"

d = {}
tokens = 0
types = 0
proportion = 0
shannon = 0
evenness = 0
evenness2 = 0
effective = 0

for dirname, dirs, files in os.walk('.'):
    if target in dirname:
        author = dirname.split(os.sep)[1]
        print author
        output = os.path.join(dirname, '..', author + "_shannon_evenness.txt")
        outfile = open(output, 'w')
        print>>outfile, "Book\tTokens\tTypes\tEffective Types\tShannon\tEvenness\tEvenness2"
        # .\James\tagged\..\James_MAT_50.txt
        for filename in files:
            d = {}
            tokens = 0
            types = 0
            proportion = 0
            shannon = 0
            evenness = 0
            evenness2 = 0
            effective = 0
            if '_tagged.txt' in filename: 
                book = filename.replace('_tagged.txt', '')
                data = open(pathstump + author + "/" + "tagged/" + filename, 'r')
                for line in data:
                    line = line.rstrip('\r\n')
                    line = line.split('\t')  
                    lemma = line[2]
                    tokens += 1
                    if lemma in d:
                        d[lemma] += 1
                    else:
                        d[lemma] = 1
                        types += 1
                for key in d:
                    toks_of_this_type = int(d[key])
                    proportion = float(toks_of_this_type) / tokens
                    shannon = shannon + (proportion * math.log(proportion))
                shannon = shannon * -1
                evenness = shannon / math.log(types)
                effective = math.exp(shannon)
                evenness2 = effective / types
                print>>outfile, "%s\t%s\t%s\t%.2f\t%.3f\t%.3f\t%.3f" % (book, tokens, types, effective, shannon, evenness, evenness2)