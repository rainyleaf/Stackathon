import os
import sys
import re

target = 'tagged'

verbtags = ['VB', 'VBD', 'VBG', 'VBN', 'VBZ', 'VBP', 'VD', 'VDD', 'VDG', 'VDN', 'VDZ', 'VDP', 'VH', 'VHD', 'VHG', 'VHN', 'VHZ', 'VHP', 'VV', 'VVD', 'VVG', 'VVN', 'VVP', 'VVZ']
nountags = ['NN', 'NNS']

verblist = []
nounlist = []

pathstump = "/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Analysis/"

output = open(pathstump + "nouns_and_verbs.txt", 'w')

for dirname, dirs, files in os.walk('.'):
    if target in dirname:
        #author = re.findall("..(.*?)\\\\tagged", dirname)[0]
        author = dirname.split(os.sep)[1]
        #print author
        for filename in files:
            if '_tagged.txt' in filename: 
                book = filename.replace('_tagged.txt', '')
                data = open(pathstump + author + "/" + "tagged/" + filename, 'r')
                for line in data:
                    line = line.rstrip('\r\n')
                    line = line.split('\t')
                    pos = line[1]
                    lemma = line[2]
                    if pos in verbtags:
                        if lemma not in verblist:
                            verblist.append(lemma)
                    if pos in nountags:
                        if lemma not in nounlist:
                            nounlist.append(lemma)
print>>output, "Verbs"
for verb in verblist:
    print>>output, verb
print>>output, "Nouns"
for noun in nounlist:
    print>>output, noun
