class Word:
    def __init__(self, strword):
        self.length = len(strword)
        self.strword = strword
        self.letters = sorted([char for char in strword])
        self.anagram = False
 
    def isAnagram(self, word):
        if word.length != self.length:
            self.anagram = False
            return self.anagram
        if self.letters == word.letters:
            self.anagram = True
        else:
            self.anagram = False
        return self.anagram
  
    def toString(self):
        return self.strword
 
def itemExists(l, item):
    try:
        l.index(item)
        return True
    except ValueError:
        return False
   
def findAnagrams00(wordlist):
    # this holds the list of anagrams found
    anagramlist = []
    # flat list of anagrams
    anagrams = []
    # iterate through all the word database
    for i in range(len(wordlist)):
        # get the first element in the word database
        key = wordlist[i]

        # create a set from the anagrams found
        foundwords = set(anagrams)

        # check if the set is valid
        if len(foundwords) > 0:
            # check if the word we are looking at is
            # already marked as an anagram, skip it
            if key.strword in foundwords:
                continue
        # check for anagrams from the remaining list
        words = wordlist[:i] + wordlist[i+1:]
        anagram = []
        # iterate through the new wordlist
        for word in words:
            if key.isAnagram(word):
                anagram.append(word.strword)
                if not itemExists(anagram, key.strword):
                    anagram.append(key.strword)
        if len(anagram) > 0:
            anagrams += anagram
            anagramlist.append(anagram)
    # return the anagrams found
    return anagramlist


def printAnagrams(anagrams):
    count = 0
    sortedanagrams = sorted(anagrams.values())
    for anagramlist in sortedanagrams:
        if len(anagramlist) > 1:
            count += 1
            print " ".join(anagramlist)
    print ">> found %d anagrams" % (count)
        
def main():
    anagrams = {}
    with open("wordlist.dat") as f:
        for line in f:
            line = line.strip()
            sortedword = sorted(line)
            key = "".join(sortedword)
            anagram = anagrams.setdefault(key,[])
            anagram.append(line)
        printAnagrams(anagrams)

def _main():
    with open("wordlist.dat") as f:
        worddata = [Word(line.strip()) for line in f]
        anagrams = findAnagrams00(worddata)
        print "found %d anagrams: " % len(anagrams)
        for anagram in anagrams:
            print " ".join(anagram)

if __name__ == "__main__":
    main()
