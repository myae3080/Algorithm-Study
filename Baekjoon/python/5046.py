# source : https://www.acmicpc.net/problem/5046

def main():
    # input
    N, B, H, W = map(int, input().split())
    
    price = []
    available = []
    for _ in range(H):
        # input
        price.append(int(input()))
        available.append(list(map(int, input().split())))
    
    result = []
    for i in range(H):
        for a in available[i]:
            if a >= N:
                result.append(N * price[i])
    
    if len(result) == 0 or min(result) > B:
        print('stay home')
    else:
        print(min(result))    

if __name__ == '__main__':
    main()