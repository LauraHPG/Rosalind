file = open("./datasets/prova.txt", 'r')

identifier = file.readline()
string = file.readline()

n = len(string)-1

matrix = {}
matrix['A'] = [0]*n
matrix['C'] = [0]*n
matrix['G'] = [0]*n
matrix['T'] = [0]*n

while string:
    for i, char in enumerate(string):
        if char != '\n':
           matrix[char][i] += 1

    identifier = file.readline()
    string = file.readline()

consensusString = str()

for i in range(0,n):
    maxNumChar = matrix['A'][i]
    char = 'A'

    if matrix['C'][i] > maxNumChar:
        maxNumChar = matrix['C'][i]
        char = 'C'

    if matrix['G'][i] > maxNumChar:
        maxNumChar = matrix['G'][i]
        char = 'G'

    if matrix['T'][i] > maxNumChar:
        maxNumChar = matrix['T'][i]
        char = 'T'
    
    consensusString += char

print(consensusString)
print('A:', end="")
for num in matrix['A']:
    print(' ', num, end="")
print()
print('C:', end="")
for num in matrix['C']:
    print(' ', num, end="")
print()
print('G:', end="")
for num in matrix['G']:
    print(' ', num, end="")
print()
print('T:', end="")
for num in matrix['T']:
    print(' ', num, end="")
print()


