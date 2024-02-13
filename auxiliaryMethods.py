import re

def readFasta(folder):
    content = open(folder, 'r')

    line = content.readline()
    result = {}

    identifier = line[1:]
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
            result[identifier] = str()
            line = content.readline()

    return result