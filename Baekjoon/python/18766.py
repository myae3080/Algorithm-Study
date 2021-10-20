# source : https://www.acmicpc.net/problem/18766
# sorting

for _ in range(int(input())):
    # input
    index = int(input())
    a = sorted(list(input().split()))
    b = sorted(list(input().split()))
    
    is_cheater = False

    print('CHEATER') if a != b else print('NOT CHEATER')
