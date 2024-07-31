import auxiliaryMethods as fnc

strings = fnc.getOnlyStrings("./datasets/rosalind_lcsm.txt")
# strings = fnc.getOnlyStrings("./datasets/prova.txt")

def findSharedMotif(string1, string2):

    bestSubstring = ""
    allSubstrings = []

    for i in range(0,len(string1)):
        
        actLen = 1

        j = 0

        startString1 = i
        endString1 = i + actLen

        if endString1 < len(string1):

            startString2 = j
            endString2 = j + actLen

            while endString2 < len(string2):

                if string1[startString1:endString1] == string2[startString2:endString2]:

                    actSubstring = string1[startString1:endString1]

                    if len(bestSubstring) < len(actSubstring):
                        bestSubstring = actSubstring
                        allSubstrings.clear()
                        allSubstrings.append(bestSubstring)

                    if len(bestSubstring) == len(actSubstring) and actSubstring not in allSubstrings:
                        allSubstrings.append(actSubstring)
                        
                    actLen += 1

                else:
                    j = j + 1
                    actLen = 1
                
                startString1 = i
                endString1 = i + actLen

                startString2 = j
                endString2 = j + actLen


    return allSubstrings

firstRes = findSharedMotif(strings[0], strings[1])
result = firstRes

for i in range(2, len(strings)):
    auxRes = []
    largestSubstringSize = 0
    for res in result:
        allSubstrings = findSharedMotif(res, strings[i])
        for subString in allSubstrings:
            if largestSubstringSize < len(subString):
                auxRes = [subString]
                largestSubstringSize = len(subString)
            elif largestSubstringSize == len(subString):
                auxRes += subString

    result = auxRes

print(list(set(result)))

    
