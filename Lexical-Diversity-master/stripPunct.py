def stripToOut(filename):

    import re
    import string
    import codecs

    outputname = filename + '.subbed'
    #outputname = 'subbed_' + filename
    toss = re.compile("[^\w\s\'\-@]+", re.UNICODE)
    #tossnum = re.compile("[\d]", re.UNICODE)

    infile = codecs.open(filename, 'r', 'utf-8')

    unistring = infile.read()

    unistring = unistring.replace(u"\u2019", "'")

    unistring = toss.sub('', unistring)
    #unistring = tossnum.sub('', unistring)

    outfile = codecs.open(outputname, 'w', 'utf-8')
    outfile.write(unistring)