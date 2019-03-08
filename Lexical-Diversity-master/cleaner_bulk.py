import stripPunct
import os

target_names = ['to-process.txt', 'to_process.txt', '-tp.txt', '_tp.txt']
target = "-Processing"

for dirname, dirs, files in os.walk('.'):
    if target in dirname and 'tagged' not in dirname: # Only want James-Processing for now, change target to just -Processing for all processing folders
        for filename in files:
            if any(filename.endswith(ending) for ending in target_names):
                inputfile = "/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Processing/" + dirname + "/" + filename
                print dirname + filename
                stripPunct.stripToOut(inputfile)