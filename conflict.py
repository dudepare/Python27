# kata eight conflicting ideas
class CompoundWord:
    def __init__(self, word):
        self.word = word
        self.prefix = None
        self.suffix = None
        
def filterByPrefix(worddb, sixletterwords):
    newlist=[]
    for word in worddb:
        for item in sixletterwords:
            if item.startswith(word) and len(word) < 6:
                cw = CompoundWord(item)
                cw.prefix = word
                newlist.append(cw)
    return newlist

def filterBySuffix(worddb, sixletterwords):
    newlist = []
    for word in worddb:
        for item in sixletterwords:
            if item.word.endswith(word) and len(word) < 6:
                item.suffix = word
                newlist.append(item)
    return newlist

def filterByLength(sixletterwords):
    newlist = []
    for item in sixletterwords:
        if (len(item.prefix) + len(item.suffix)) == 6:
            newlist.append(item)
    return newlist

with open("wordlist.dat") as f:
    sixletterwords= []
    worddb = []
    for line in f:
        line = line.strip()
        if len(line) < 6:
            worddb.append(line)
        if len(line) == 6:
            sixletterwords.append(line)
    print len(sixletterwords)

    # filter the sixletterwords by prefix  
    sixletterwords = filterByPrefix(worddb, sixletterwords)
    print len(sixletterwords)
    
    # filter the sixletterwords by suffix
    sixletterwords = filterBySuffix(worddb, sixletterwords)

    sixletterwords = filterByLength(sixletterwords)
    for word in sixletterwords:
        print "%s + %s = %s" %(word.prefix, word.suffix, word.word)

    print len(sixletterwords)
    




    
