# this will hold all of the common functions in katafour exercise
import exceptions
import string

def isNumber(value):
    try:
        int(value)
        return True
    except exceptions.ValueError:
        return False

def getLeastEntry(mapData):
    keylist = mapData.keys()
    sortedKeylist = sorted(keylist, key=mapData.__getitem__)
    leastKey = sortedKeylist[0]
    return (leastKey, mapData[leastKey])

def cleanData(row, unwantedChar=None):
    newRow = []
    for field in row:
        field = string.rstrip(field, unwantedChar)
        if isNumber(field):
            field = int(field)
        newRow.append(field)
    return newRow

# data format is: [key, maxData, minData] -- all numbers
def computeDifference(rows):
    mapResult = {}
    for row in rows:
        key = row[0]
        maxVal = row[1]
        minVal = row[2]
        mapResult[key] = abs(maxVal - minVal)
    return mapResult
