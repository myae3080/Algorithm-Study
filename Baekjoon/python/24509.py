# source : https://www.acmicpc.net/problem/24509

import sys
input = sys.stdin.readline

def main():
    # input
    N = int(input())
    stu_infos = [list(map(int, input().split())) for _ in range(N)]
    
    result = []
    
    stu_infos.sort(key=lambda info: (-info[1], info[0]))
    
    result.append(stu_infos[0][0])
    
    stu_infos.sort(key=lambda info: (-info[2], info[0]))
    for i in range(N):
        if stu_infos[i][0] not in result:
            result.append(stu_infos[i][0])
            break
            
    stu_infos.sort(key=lambda info: (-info[3], info[0]))
    for i in range(N):
        if stu_infos[i][0] not in result:
            result.append(stu_infos[i][0])
            break
            
    stu_infos.sort(key=lambda info: (-info[4], info[0]))
    for i in range(N):
        if stu_infos[i][0] not in result:
            result.append(stu_infos[i][0])
            break

    print(*result)
    
if __name__ == '__main__':
    main()