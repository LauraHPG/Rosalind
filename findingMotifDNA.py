string = input("String: ")
subString = input("Substring: ")

positions = []
for i, char in enumerate(string):
    if char == subString[0]:
        if string[i:i+len(subString)] == subString:
            positions.append(i+1)

print(positions)