import re
import os
import sys

target = 'tagged'
pathstump = "/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Analysis/"

lemmalist = []
POSlist = []

lemmaStringList = []
POSstringList = []

tokendict = {}

verbtags = ['VB', 'VBD', 'VBG', 'VBN', 'VBZ', 'VBP', 'VD', 'VDD', 'VDG', 'VDN', 'VDZ', 'VDP', 'VH', 'VHD', 'VHG', 'VHN', 'VHZ', 'VHP', 'VV', 'VVD', 'VVG', 'VVN', 'VVP', 'VVZ']
adjtags = ['JJ', 'JJR', 'JJS']
advtags = ['RB', 'RBR', 'RBS']

for dirname, dirs, files in os.walk('.'):
    if target in dirname:
        author = dirname.split(os.sep)[1]
        print author
        output = os.path.join(dirname, '..', author + "_it-verb-adj-to_that_relative.txt")
        outfile = open(output, 'w')
        lemmaStringList = []
        POSstringList = []
        tokendict = {}
        # .\James\tagged\..\James_MAT_50.txt
        for filename in files:
            lemmalist = []
            POSlist = []
            tokens = 0
            if '_tagged.txt' in filename: 
                novel = filename.replace('_tagged.txt', '')
                data = open(pathstump + author + "/" + "tagged/" + filename, 'r')
                for line in data:
                    line = line.rstrip('\r\n')
                    first_char = line[0]
                    line = line.split('\t')
                    POS = line[1]
                    if POS in verbtags:
                        POS = "VERB"
                    if POS in adjtags:
                        POS = "ADJ"
                    if POS in advtags:
                        POS = "ADV"
                    if POS == "IN/that":
                        POS = "THAT"
                    lemma = line[2]
                    if lemma == "it":
                        POS = "IT"
                    tokens += 1

                    lemmalist.append(lemma)
                    POSlist.append(POS)
                #print tokens
                #print novel
                tokendict[novel] = tokens
                #print tokendict
                #print tokendict[novel]

                item = []
                item.append(novel)
                item.append(' '.join(lemmalist))
                lemmaStringList.append(item)

                item = []
                item.append(novel)
                item.append(' '.join(POSlist))
                POSstringList.append(item)
        print>>outfile, "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % ("Novel", "IT VERB ADJ THAT", "IT MD VERB ADJ THAT", "IT VERB ADV ADJ THAT", "IT MD VERB ADV ADJ THAT", "IT VERB ADJ TO", "IT MD VERB ADJ TO", "IT VERB ADV ADJ TO", "IT MD VERB ADV ADJ TO")
        #testfile = open("test_strings.txt", 'w')
        #print>>testfile, POSstringList
        #print>>testfile, lemmaStringList
        for x,item in enumerate(POSstringList):
            novel = item[0]
            print novel
            #print tokendict[novel]
            # POSconstructionMatches = re.findall("(IT (?:MD )?VERB (?:ADV )?ADJ (?:TO|THAT))", item[1])
            POSconstructionIndices = list(re.finditer("(IT (?:MD )?VERB (?:ADV )?ADJ (?:TO|THAT))", item[1]))
            thatSolo = 0.
            thatWithModal = 0.
            thatWithAdv = 0.
            thatWithBoth = 0.
            toSolo = 0.
            toWithModal = 0.
            toWithAdv = 0.
            toWithBoth = 0.

            d_thatSolo = {}
            d_thatWithModal = {}
            d_thatWithAdv = {}
            d_thatWithBoth = {}
            d_toSolo = {}
            d_toWithModal = {}
            d_toWithAdv = {}
            d_toWithBoth = {}

            for match in POSconstructionIndices:
                startIndex = match.start()
                matchLength = len(match.group().split())
                currentLemmaString = lemmaStringList[x][1]
                currentPOSstring = item[1]
                begindex = len(currentPOSstring[:startIndex].split())
                antiBegindex = begindex + matchLength
                correspondingLemmaString = ' '.join(currentLemmaString.split()[begindex:antiBegindex])
                if match.group() == "IT VERB ADJ THAT":
                    thatSolo += 1
                    if correspondingLemmaString in d_thatSolo:
                        d_thatSolo[correspondingLemmaString] += 1
                    else:
                        d_thatSolo[correspondingLemmaString] = 1
                if match.group() == "IT MD VERB ADJ THAT":
                    thatWithModal += 1
                    if correspondingLemmaString in d_thatWithModal:
                        d_thatWithModal[correspondingLemmaString] += 1
                    else:
                        d_thatWithModal[correspondingLemmaString] = 1
                if match.group() == "IT VERB ADV ADJ THAT":
                    thatWithAdv += 1
                    if correspondingLemmaString in d_thatWithAdv:
                        d_thatWithAdv[correspondingLemmaString] += 1
                    else:
                        d_thatWithAdv[correspondingLemmaString] = 1
                if match.group() == "IT MD VERB ADV ADJ THAT":
                    thatWithBoth += 1
                    if correspondingLemmaString in d_thatWithBoth:
                        d_thatWithBoth[correspondingLemmaString] += 1
                    else:
                        d_thatWithBoth[correspondingLemmaString] = 1
                if match.group() == "IT VERB ADJ TO":
                    toSolo += 1
                    if correspondingLemmaString in d_toSolo:
                        d_toSolo[correspondingLemmaString] += 1
                    else:
                        d_toSolo[correspondingLemmaString] = 1
                if match.group() == "IT MD VERB ADJ TO":
                    toWithModal += 1
                    if correspondingLemmaString in d_toWithModal:
                        d_toWithModal[correspondingLemmaString] += 1
                    else:
                        d_toWithModal[correspondingLemmaString] = 1
                if match.group() == "IT VERB ADV ADJ TO":
                    toWithAdv += 1
                    if correspondingLemmaString in d_toWithAdv:
                        d_toWithAdv[correspondingLemmaString] += 1
                    else:
                        d_toWithAdv[correspondingLemmaString] = 1
                if match.group() == "IT MD VERB ADV ADJ TO":
                    toWithBoth += 1
                    if correspondingLemmaString in d_toWithBoth:
                        d_toWithBoth[correspondingLemmaString] += 1
                    else:
                        d_toWithBoth[correspondingLemmaString] = 1

            all_constructions = thatSolo + thatWithModal + thatWithAdv + thatWithBoth + toSolo + toWithModal + toWithAdv + toWithBoth
            #print>>outfile, "%s\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i" % (novel, thatSolo, thatWithModal, thatWithAdv, thatWithBoth, toSolo, toWithModal, toWithAdv, toWithBoth, all_constructions)
            #raw ^
            print>>outfile, "%s\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % (novel, float(thatSolo/tokendict[novel] * 1000000), float(thatWithModal/tokendict[novel] * 1000000), float(thatWithAdv/tokendict[novel] * 1000000), float(thatWithBoth/tokendict[novel] * 1000000), float(toSolo/tokendict[novel] * 1000000), float(toWithModal/tokendict[novel] * 1000000), float(toWithAdv/tokendict[novel] * 1000000), float(toWithBoth/tokendict[novel] * 1000000), float(all_constructions/tokendict[novel] * 1000000))
            #relative ^
           
            # print "THAT"
            # for entry in sorted(d_thatSolo.items(), key=lambda x: (-x[1],x[0])):
            # 	print "%s\t%i" % (entry[0], entry[1])
            # print "THAT with MODAL"
            # for entry in sorted(d_thatWithModal.items(), key=lambda x: (-x[1],x[0])):
            # 	print "%s\t%i" % (entry[0], entry[1])
            # print "THAT with ADV"
            # for entry in sorted(d_thatWithAdv.items(), key=lambda x: (-x[1],x[0])):
            # 	print "%s\t%i" % (entry[0], entry[1])
            # print "THAT with BOTH"
            # for entry in sorted(d_thatWithBoth.items(), key=lambda x: (-x[1],x[0])):
            # 	print "%s\t%i" % (entry[0], entry[1])
            # print "TO"
            # for entry in sorted(d_toSolo.items(), key=lambda x: (-x[1],x[0])):
            # 	print "%s\t%i" % (entry[0], entry[1])
            # print "TO with MODAL"
            # for entry in sorted(d_toWithModal.items(), key=lambda x: (-x[1],x[0])):
            # 	print "%s\t%i" % (entry[0], entry[1])
            # print "TO with ADV"
            # for entry in sorted(d_toWithAdv.items(), key=lambda x: (-x[1],x[0])):
            # 	print "%s\t%i" % (entry[0], entry[1])
            # print "TO with BOTH"
            # for entry in sorted(d_toWithBoth.items(), key=lambda x: (-x[1],x[0])):
            # 	print "%s\t%i" % (entry[0], entry[1])
