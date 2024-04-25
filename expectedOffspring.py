dataset = input()
values = dataset.split(' ')

prob ={
    1: 2.0,
    2: 2.0,
    3: 2.0,
    4: 1.5,
    5: 1.0,
    6: 0
}

sumValues = 0

for i, val in enumerate(values):
    sumValues += float(val)*prob[i+1]

print(sumValues)