import bitarray
import os.path
import hashlib

def hashFunctionBiggie(what, bitlen):
    if bitlen == 0:
        return 0
    m = hashlib.md5()
    m.update(what)
    result = m.hexdigest()
    result = int(result, 16)
    result = int(result % bitlen)
    return result

def hashFunctionMedium(what, bitlen):
    if bitlen == 0:
        return 0
    result = ~hash(what) % bitlen
    return result
    
def hashFunctionSmall(what, bitlen):
    if bitlen == 0:
        return 0
    result = hash(what) % bitlen
    return result

def getHashIndexes(item, bitlen):
    return [hashFunctionBiggie(item, bitlen),
            hashFunctionMedium(item, bitlen),
            hashFunctionSmall(item, bitlen)]
    
def setIndexesInBloomFilter(bloomFilter, indexes):
    sizeBloomFilter = len(bloomFilter)
    for index in indexes:
        if index < sizeBloomFilter:
            bloomFilter[index] = 1

def loadWordsToBloomFilter(filename, sizeBloomFilter):
    # initialise our bloom filter
    bloomFilter = bitarray.bitarray(sizeBloomFilter)
    bloomFilter.setall(False)

    # open the file with the word list
    with open(filename) as f:
        for line in f:
            hashedIndexes = getHashIndexes(line.strip(), sizeBloomFilter)
            setIndexesInBloomFilter(bloomFilter, hashedIndexes)

    # return the initialised filter
    return bloomFilter

def isWordInBloom(key, bloomFilter):
    keyindexes = getHashIndexes(key.strip(), len(bloomFilter))
    result = True
    for index in keyindexes:
        if bloomFilter[index] != 1:
            result = False
            break
    return result

def checkWordsAgainstFilter(filename, bloomFilter):
    with open(filename) as f:
        for line in f:
            if isWordInBloom(line.strip(), bloomFilter):
                print line.strip(), "Yes"
            else:
                print line.strip(), "No"
            

def main():
    database = "wordlist.dat"
    randomwords = "words.dat"
    bitlen = 2**18

    # load the database of valid words
    bloomFilter = loadWordsToBloomFilter(database, bitlen)

    print bloomFilter

    # check a subset of words if they are in the database
    checkWordsAgainstFilter(randomwords, bloomFilter)

if __name__ == "__main__":
    main()


