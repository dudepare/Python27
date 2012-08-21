# this is the daily weather data for Morristown, NJ analyser
import os.path
import string
import datamunger
    
# data format is: [league, for, against]
def extractFields(row):
    return [row[1], row[6], row[8]]

def removeUnwantedData(fileContents):
    newContents = []
    for line in fileContents:
        line = string.strip(line)
        brokenline = line.split()
        if len(brokenline) == 0:
            continue
        first = brokenline[0]
        first = string.rstrip(first, '.')
        if datamunger.isNumber(first):
            brokenline = datamunger.cleanData(extractFields(brokenline))
            newContents.append(brokenline)
    return newContents

# check if the file exists
filename = "football.dat"
if not os.path.exists(filename):
    exit()

# load the file here
with open(filename) as f:
    # read the file contents
    contents = f.readlines()

    # weed out the unneeded data
    contents = removeUnwantedData(contents)

    # write algo to determine the smallest temperature spread
    mapOfLeagues = datamunger.computeDifference(contents)

    # display to the user which day has the smallest temperature spread
    print """Team %s has the least goal difference of: %d """ % datamunger.getLeastEntry(mapOfLeagues)


    
    
