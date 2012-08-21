import bloom

def checkWordsAgainstFilter(filename, bloomFilter):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if bloomFilter.find(line):
                print line, "Yes"
            else:
                print line, "No"

def main():
    wordDb = "wordlist.dat"
    searchWords = "words.dat"
    hashFunctions = 4
    filterSize = 2**18
    
    # create the filter, populate with the words
    bloomFilter = bloom.BloomFilter(wordDb, hashFunctions, filterSize)

    # check if the word subset is a member of the word database
    checkWordsAgainstFilter(searchWords, bloomFilter)

if __name__ == "__main__":
    main()


