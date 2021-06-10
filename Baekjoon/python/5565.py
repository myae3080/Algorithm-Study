# math

rest = 0

for i in range(10):
    price = int(input())

    if i == 0:
        rest = price
    else:
        rest -= price

print(rest)