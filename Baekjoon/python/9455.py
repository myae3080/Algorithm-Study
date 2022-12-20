# source : https://www.acmicpc.net/problem/9455

for _ in range(int(input())):
    # input
    row, col = map(int, input().split())
    boxes = [input().split() for __ in range(row)]
    
    result = 0
    for i in range(col):
        space = 0
        
        # 열 별 계산
        for j in range(row - 1, -1, -1):
            if boxes[j][i] == '1':
                result += space
            else:
                space += 1
        
    print(result)