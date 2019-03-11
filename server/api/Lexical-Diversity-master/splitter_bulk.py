import os
#from nltk.stem import WordNetLemmatizer 
#lemmatizer = WordNetLemmatizer() 

#target_names = ['-to-process.txt.subbed', '_to_process.txt.subbed', '_to-process.txt.subbed', '-to_process.txt.subbed', '-tp.txt.subbed', '_tp.txt.subbed']
#target = "-Processing"
print("in splitter")
for dirname, dirs, files in os.walk('./server/api/temp'):
    #if target in dirname and 'tagged' not in dirname: 
    for filename in files:
        print(filename)
        if filename.endswith('.txt.subbed'):
            inputname = "./server/api/temp/" + filename
            inputfile = open(inputname, 'r')
            # for ending in target_names:
            #if filename.endswith('.subbed'):
            new_filename = filename.replace('.txt.subbed', '_split.txt')
            new_filename = new_filename.replace(' ', '_')
            new_filename = new_filename.replace(',', '')
            new_filename = new_filename.replace('!', '')
            #print(dirname + new_filename)
            new_filename= "./server/api/temp/" + new_filename

            new_file = open(new_filename, 'w')              
            for line in inputfile:
                for word in line.split():

                #word = word.lower()
                    word = word.rstrip('-\n\r\'.')
                    word = word.lstrip("\'")
                    #word = lemmatizer.lemmatize(word)
                    print(word, file=new_file)

            inputfile.close()