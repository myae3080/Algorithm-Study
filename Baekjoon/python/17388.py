# source : https://www.acmicpc.net/problem/17388

universities = ['Soongsil', 'Korea', 'Hanyang']

# input
participation = list(map(int, input().split()))

if sum(participation) >= 100:
    print('OK')
else:
    print(universities[participation.index(min(participation))])