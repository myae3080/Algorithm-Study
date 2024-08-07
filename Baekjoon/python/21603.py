# source : https://www.acmicpc.net/problem/21603

def main():
    # input
    N, K = map(int, input().split())
    
    fn = K % 10
    fn2 = (2 * K) % 10
    
    result = []
    for i in range(1, N + 1):
        one_digit = i % 10
        
        if one_digit != fn and one_digit != fn2:
            result.append(i)
    
    print(len(result))
    print(*result)

if __name__ == '__main__':
    main()