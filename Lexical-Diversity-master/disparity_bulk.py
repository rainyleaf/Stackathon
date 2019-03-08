import os
import sys
import re

def calculate_disparity():
    sense_tokens = 0
    sense_types = 0
    for line in sense_index:
        line = line.rstrip('\r\n')
        line = line.split('\t')
        word = line[0]
        if word in d:
            for n in range(2, len(line)):
                sense_id = line[n]
                if sense_id in sense_dict:
                    sense_dict[sense_id] += 1
                else:
                    sense_dict[sense_id] = 1
                sense_tokens += 1
    types = len(d)
    sense_types = float(len(sense_dict))
    if sense_types == 0:
        semantic_disp = 1
    else:
        semantic_disp = float(sense_tokens/sense_types)
    print>>outfile, "%s\t%s\t%s\t%.3f" % (book, tokens, types, semantic_disp)

target = 'tagged'

sense_index = open("/Users/Torri/Documents/Grad Stuff/Thesis stuff/Data - Novels/Analysis/senseindex(condensed).txt", 'r').readlines()
#sense_index = open("/Users/Leaf/Documents/Analysis/senseindex(condensed).txt", 'r').readlines()

data = open("/Users/Torri/Documents/Grad Stuff/Thesis stuff/Data - Novels/Analysis/Christie/tagged/And_Then_There_Were_None_tagged.txt", 'r').readlines() #not real filename, find actual

d = {}
sense_dict = {}
tokens = 0
types = 0
semantic_disp = 0


pathstump = "/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Analysis/"

for dirname, dirs, files in os.walk('.'):
    if target in dirname:
        #author = re.findall("..(.*?)\\\\tagged", dirname)[0]
        author = dirname.split(os.sep)[1]
        print author
        output = os.path.join(dirname, '..', author + "_sem_disp.txt")
        outfile = open(output, 'w')
        print>>outfile, "Book\tTokens\tTypes\tSemantic Disparity"
        for filename in files:
            d = {}
            sense_dict = {}
            tokens = 0
            types = 0
            semantic_disp = 0
            if '_tagged.txt' in filename: 
                book = filename.replace('_tagged.txt', '')
                data = open(pathstump + author + "/" + "tagged/" + filename, 'r')
                for line in data:
                    for line in data:
                        line = line.rstrip('\r\n')
                        line = line.split('\t')
                        lemma = line[2]
                        lexeme = line[0]
                        if lemma in d:
                            d[lemma] += 1
                        else:
                            d[lemma] = 1
                        tokens += 1
                calculate_disparity()
