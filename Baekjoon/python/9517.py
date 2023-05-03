# source : https://www.acmicpc.net/problem/9517

def main():
    # input
    k = int(input())
    n = int(input())
    problems = [input().split() for _ in range(n)]
    
    time = 0
    for p in problems:
        time += int(p[0])
        if time >= 210:
            print(k)
            break
        
        if p[1] == 'T':
            k = 8 if (k + 1) % 8 == 0 else (k + 1) % 8
    
if __name__ == '__main__':
    main()