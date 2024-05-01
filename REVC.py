file = open('./datasets/rosalind_revc.txt','r')
content = file.read()

result = str()
for char in content:
    if char == 'A':
        result += 'T'
    if char == 'T':
        result += 'A'
    if char == 'C':
        result += 'G'
    if char == 'G':
        result += 'C'

print(result[::-1])