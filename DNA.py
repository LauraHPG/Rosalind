file = open('./datasets/rosalind_dna.txt','r')
content = file.read()

As = 0
Cs = 0
Gs = 0
Ts = 0
for char in content:
    if char == 'A':
        As += 1
    if char == 'C':
        Cs += 1
    if char == 'G':
        Gs += 1
    if char == 'T':
        Ts += 1

print(As, Cs, Gs, Ts)