# source : https://www.acmicpc.net/problem/10474

while 1:
    # input
    a, b = map(int, input().split())
    
    if a == b == 0:
        break
    
    print('{0} {1} / {2}'.format(a // b, a % b, b))