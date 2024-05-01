file = open('./datasets/rosalind_gc.txt','r')

def computeGCContent(dnaString):
    res = 0
    total = 0
    for char in dnaString:
        if char == 'C' or char == 'G':
            res += 1
            total += 1
        elif char =='T' or char == 'A':
            total += 1
    
    return res, total


results = {}

line = file.readline()

identifier = str()
while line:
    if line[0] == '>':
        identifier = line[1:]
        results[identifier] = [0,0]
    else:
        res, total = computeGCContent(line)
        results[identifier][0] += res
        results[identifier][1] += total
    line = file.readline()

bestId = str()
highestContent = 0
for res in results:
    content = results[res][0]/results[res][1]
    if content > highestContent:
        highestContent = content
        bestId = res
print(bestId)
print(highestContent*100)