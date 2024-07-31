import re

def readFasta(folder):
    '''
    returns map of {identifier: string}
    '''
    content = open(folder, 'r')

    line = content.readline()
    result = {}

    identifier = line[1:]

    identifier = re.sub(r'[^\w]', ' ', identifier)
    identifier = re.sub(r"\s+", "", identifier)
    
    result[identifier] = str()
    
    line = content.readline()

    while line:

        cleanString = re.sub(r'[^\w]', ' ', line)
        cleanString = re.sub(r"\s+", "", cleanString)
        
        result[identifier] += cleanString

        line = content.readline()
        if not line:
            break 
        if line[0] == '>':
            
            identifier = line[1:]

            identifier = re.sub(r'[^\w]', ' ', identifier)
            identifier = re.sub(r"\s+", "", identifier)

            result[identifier] = str()
            line = content.readline()

    return result

def getOnlyStrings(folder):
    '''
    returns a list with all the strings
    '''
    return list(readFasta(folder).values())
