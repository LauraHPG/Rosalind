import auxiliaryMethods as fnc

strings = fnc.readFasta("./datasets/rosalind_grph.txt")
matrix = dict()

def hasOverlap(id1, id2, string1, string2, n):
    if string1 != string2:
        lenS1 = len(string1)
        subString1 = string1[lenS1-n:lenS1]
        subString2 = string2[0:n]
        if subString1 == subString2:
            if id1 in matrix:
                matrix[id1].append(id2)
            else:
                matrix[id1] = [id2]
    

for id1 in strings:
    for id2 in strings:
        hasOverlap(id1, id2, strings[id1], strings[id2], 3)

for id1 in matrix:
    for id2 in matrix[id1]:
        print(id1,id2)
