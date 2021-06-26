# string

resistance_list = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white'
]

result = 0

for i in range(3):
    # input
    color = input()

    idx = resistance_list.index(color)

    if i == 0:
        result += idx * 10
    elif i == 1:
        result += idx
    else:
        result *= (10 ** idx)

print(result)