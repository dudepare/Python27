# kata eight conflicting ideas

# find six letter words in the 
# dictionary that is composed
# of two other letters



# create a bloom filter of all the
# six letter words in the dictionary

class CompoundWord:
    def __init__(self, word):
        self.word = word
        self.prefix = None
        self.suffix = None

    def setPrefix(self, pre):
        self.prefix = pre

    def setSuffix(self, suf):
        self.suffix = suf
        


with open("wordlist.dat") as f:
    sixletterwords= []
    worddb = []
    for line in f:
        line = line.strip()
        worddb.append(line)
        if len(line) == 6:
            sixletterwords.append(line)

    # filter the sixletterwords by prefix
    newlist=[]
    for word in worddb:
        for item in sixletterwords:
            appendToList = False
            if item.startswith(word) and len(word) < 6:
                appendToList = True
            elif item.endswith(word) and len(word) < 6:
                appendToList = True
            else:
                continue
            if item not in newlist and appendToList:
                newlist.append(item)
    sixletterwords = newlist
    print sixletterwords
    




    
