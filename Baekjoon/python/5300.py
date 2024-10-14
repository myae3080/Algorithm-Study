# source : https://www.acmicpc.net/problem/5300

def main():
    # input
    N = int(input())
    
    results = []
    for i in range(1, N + 1):
        if i != 1 and (i - 1) % 6 == 0:
            results.append('Go!')
        
        results.append(str(i))
        
        if (i - 1) % 6 != 0 and i == N:
            results.append('Go!')
    
    print(' '.join(results))

if __name__ == '__main__':
    main()