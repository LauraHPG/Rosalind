file = open('./datasets/rosalind_rna.txt','r')
content = file.read()

result = str()
for char in content:
    if char == 'T':
        result += 'U'
    else:
        result += char

print(result)