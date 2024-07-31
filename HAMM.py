file = open('./datasets/rosalind_hamm.txt','r')
string1 = file.readline()
string2 = file.readline()

total = 0
for i, char1 in enumerate(string2):
    char2 = string1[i]
    if char1 != char2:
        total += 1

print(total)