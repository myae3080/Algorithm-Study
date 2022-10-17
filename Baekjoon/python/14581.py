# source : https://www.acmicpc.net/problem/14581

# input
hj = input()

fans = ':fan::%s::fan:'
for i in range(3):
    if i % 2:
        print(fans % hj)
    else:
        print(fans % 'fan')