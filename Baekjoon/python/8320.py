# source : https://www.acmicpc.net/problem/8320

def main():
    # input
    n = int(input())
    
    result = 0
    for w in range(1, n + 1):
        for h in range(w, n + 1):
            if w * h <= n:
                result += 1
    
    print(result)

if __name__ == '__main__':
    main()