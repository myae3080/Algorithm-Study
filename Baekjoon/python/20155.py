# source : https://www.acmicpc.net/problem/20155

def main():
    # input
    n, m = map(int, input().split())
    cons = list(map(int, input().split()))
    
    result = [0] * (m + 1)
    for i in cons:
        result[i] += 1
    
    print(max(result))

if __name__ == '__main__':
    main()