import os
import subprocess
#target = '-Processing'

for dirname, dirs, files in os.walk('./temp'):
    #if target in dirname and 'tagged' not in dirname: 
        #if 'tagged' not in dirs:
        #    os.makedirs(os.path.join(dirname, 'tagged'))   # If tagged doesn't exist, make it
    for filename in files:
        if 'split.txt' in filename: # Find the files we're working on
            #output = os.path.join('tagged', filename.replace('split.txt', 'tagged.txt'))
            command = 'tree-tagger-english ' + os.path.join(dirname, filename)# + ' ' + os.path.join("./temp", output)
            #os.system(command)
            newFilename = filename.replace('split.txt', 'tagged.txt')
            print(newFilename)
            print('~Second-split-here~')
            print(subprocess.check_output(['tree-tagger-english', os.path.join(dirname, filename)]).decode('utf-8'))
            print("~~~~~~~~~SPLIT~HERE~~~~~~~~~~")