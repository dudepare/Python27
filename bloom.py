import hashlib
import bitarray

class BloomFilter:
    """my version of a bloom filter"""
    def __init__(self, filename, numhash, bitlen):
        self.datafile = filename
        self.numHashes = numhash
        self.arraysize = bitlen
        self.bloomFilter = bitarray.bitarray(self.arraysize)
        self.bloomFilter.setall(False)
	self.create()

    def hash(self, what):
        if self.arraysize == 0:
            result = [0] * self.numHashes
            return result
        
        m = hashlib.md5()
        m.update(what)
        result = m.hexdigest()
        hashlen = len(result) / self.numHashes

        hashlist = []

        for i in range(self.numHashes):
            hashlist.append(result[i*hashlen:hashlen*(i+1)])

        result = [int(int(hash, 16) % self.arraysize) for hash in hashlist]
        return result

    def setIndexes(self, indexes):
        for index in indexes:
            self.bloomFilter[index] = True

    def create(self):
        #load data file
        with open(self.datafile) as f:
            for line in f:
                hashedIndexes = self.hash(line.strip())
                self.setIndexes(hashedIndexes)
            print self.bloomFilter

    def find(self, item):
        hashIndexes = self.hash(item.strip())
        result = True
        for index in hashIndexes:
            if not self.bloomFilter[index]:
                result = False
                break
        return result
