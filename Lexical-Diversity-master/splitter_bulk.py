import os

target_names = ['-to-process.txt.subbed', '_to_process.txt.subbed', '_to-process.txt.subbed', '-to_process.txt.subbed', '-tp.txt.subbed', '_tp.txt.subbed']
target = "-Processing"

for dirname, dirs, files in os.walk('.'):
    if target in dirname and 'tagged' not in dirname: 
        for filename in files:
            if any(filename.endswith(ending) for ending in target_names):
                inputname = "/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Processing/" + dirname + "/" + filename
                inputfile = open(inputname, 'r')
                for ending in target_names:
                    if filename.endswith(ending):
                        new_filename = filename.replace(ending, '_split.txt')
                new_filename = new_filename.replace(' ', '_')
                new_filename = new_filename.replace(',', '')
                new_filename = new_filename.replace('!', '')
                print dirname + new_filename

                new_file = open("/Users/Torri/Documents/Grad stuff/Thesis stuff/Data - Novels/Processing/" + dirname + "/" + new_filename, 'w')              
                for line in inputfile:
	                for word in line.split():

		            #word = word.lower()
		            word = word.rstrip('-\n\r\'.')
		            word = word.lstrip("\'")
		            print >>new_file, word

                inputfile.close()