# source : https://www.acmicpc.net/problem/29615

def main():
    # input
    n, m = map(int, input().split())
    order = input().split()
    friends = input().split()
    
    result = 0
    for i in range(m):
        if order[i] not in friends:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()