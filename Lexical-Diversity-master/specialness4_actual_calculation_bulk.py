from nltk.corpus import wordnet as wn
import sys
import os
import re
reload(sys)
sys.setdefaultencoding('UTF8')

pathstump = "/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Analysis/"
target = 'tagged'

specialwords = open("/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Analysis/novels_special_words.txt").read().splitlines()
cocaFile1000 = open("/Users/Torri/pythonstuff/COCA-top1000.txt").read().splitlines()

advTags = ['RB', 'RBR', 'RBS']
adjTags = ['JJ', 'JJR', 'JJS']


for dirname, dirs, files in os.walk('.'):
    if target in dirname:
        #author = re.findall("..(.*?)\\\\tagged", dirname)[0]
        author = dirname.split(os.sep)[1]
        print author
        #print author
        output = os.path.join(dirname, '..', author + "_specialness.txt")
        outfile = open(output, 'w')
        print "%s\t%s\t%s" % ("Novel", "special types", "relative specialness")
        print>>outfile, "%s\t%s\t%s" % ("Novel", "special types", "relative specialness")
        # .\James\tagged\..\James_MAT_50.txt
        for filename in files:
            specialtypes = 0
            specialwordlist = []
            tokens = 0.
            if '_tagged.txt' in filename: 
                book = filename.replace('_tagged.txt', '')
                data = open(pathstump + author + "/" + "tagged/" + filename, 'r')
                for line in data:
                    line = line.rstrip('\r\n')
                    first_char = line[0]
                    line = line.split('\t')
                    pos = line[1]
                    lemma = line[2]
                    tokens += 1
                    if lemma in specialwords:
                        if lemma not in specialwordlist:
                            specialwordlist.append(lemma)
                            specialtypes += 1
                    if pos == "IN":										#prepositions
                        if lemma not in specialwordlist:
                            specialwordlist.append(lemma)
                            specialtypes += 1
                    if pos == "MD":									#modals
                        if lemma not in specialwordlist:
                            specialwordlist.append(lemma)
                            specialtypes += 1
                    if (pos in advTags) and (lemma not in cocaFile1000):	#adverbs
                        if lemma not in specialwordlist:
                            specialwordlist.append(lemma)
                            specialtypes += 1
                    if (pos in adjTags) and (lemma not in cocaFile1000):	#adjectives
                        if lemma not in specialwordlist:
                            specialwordlist.append(lemma)
                            specialtypes += 1
                relativeSpecial = (specialtypes/tokens) * 100
                print "%s\t%s\t%.2f" % (book, specialtypes, relativeSpecial)
                print>>outfile, "%s\t%s\t%.2f" % (book, specialtypes, relativeSpecial)