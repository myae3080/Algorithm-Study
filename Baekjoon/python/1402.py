# source : https://www.acmicpc.net/problem/1402

for _ in range(int(input())):
    # input
    a, b = map(int, input().split())

    '''
        처음엔 소인수 분해로 생각하고 풀어, 시간 초과 발생.
    '''
    print('yes')