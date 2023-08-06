# source : https://www.acmicpc.net/problem/28289

def main():
    students = [0, 0, 0, 0]
    
    # input
    for _ in range(int(input())):
        # input
        # 학년 / 반 / 번호
        g, c, n = map(int, input().split())
        
        if g == 1:
            students[3] += 1
        elif c == 1 or c == 2:
            students[0] += 1
        elif c == 3:
            students[1] += 1
        elif c == 4:
            students[2] += 1
            
    [print(s) for s in students]

if __name__ == '__main__':
    main()