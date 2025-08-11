# source : https://www.acmicpc.net/problem/20125

def main():
    # input
    N = int(input())
    coordinates = [list(input()) for _ in range(N)]

    head = (0, 0)
    for i in range(N):
        if coordinates[i].count('*') == 1:
            head = (i, coordinates[i].index('*'))

            break
    
    arms = coordinates[head[0] + 1]
    left_arm = sum([1 for i in range(head[1]) if arms[i] == '*'])
    right_arm = sum([1 for i in range(head[1] + 1, N) if arms[i] == '*'])

    waist = 0
    for i in range(head[0] + 2, N):
        if coordinates[i][head[1]] == '*':
            waist += 1
        else:
            break
    
    left_leg, right_leg = 0, 0
    for i in range(head[0] + 1 + waist, N):
        if coordinates[i][head[1] - 1] == '*':
            left_leg += 1
        if coordinates[i][head[1] + 1] == '*':
            right_leg += 1
    
    print(head[0] + 2, head[1] + 1)
    print(left_arm, right_arm, waist, left_leg, right_leg)

if __name__ == '__main__':
    main()