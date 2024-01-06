# source : https://www.acmicpc.net/problem/30088

def main():
    # input
    n = int(input())
    
    times = []
    for _ in range(n):
        # input
        info = list(map(int, input().split()))
        
        times.append(sum(info[1:]))
    
    times.sort()
    result = 0
    for i in range(n):
        result += sum(times[:i + 1])

    print(result)

if __name__ == '__main__':
    main()