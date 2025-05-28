# source : https://www.acmicpc.net/problem/20113

def main():
    # input
    N = int(input())
    votes = list(map(int, input().split()))
    
    result = [0] + [0] * N
    for n in votes:
        if n != 0:
            result[n] += 1
    
    if result.count(max(result)) >= 2 or max(result) == 0:
        print('skipped')
    else:
        print(result.index(max(result)))

if __name__ == '__main__':
    main()