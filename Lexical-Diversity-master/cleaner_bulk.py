import stripPunct
import os
print("in cleaner_bulk")
target_names = ['to-process.txt', 'to_process.txt', '-tp.txt', '_tp.txt']
#target = "-Processing"

for dirname, dirs, files in os.walk('./temp'):
    #if target in dirname and 'tagged' not in dirname:
    for filename in files:
        print(filename)
        #if any(filename.endswith(ending) for ending in target_names):
        inputfile = "temp/" + filename
        #print(dirname + "/" + filename)
        stripPunct.stripToOut(inputfile)