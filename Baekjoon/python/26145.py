# source : https://www.acmicpc.net/problem/26145

def main():
    # input
    n, m = map(int, input().split())
    pay = list(map(int, input().split()))
    
    result = pay + [0] * m
    for i in range(n):
        # input
        temp_pay = list(map(int, input().split()))
        
        for j in range(n + m):
            result[i] -= temp_pay[j]
            result[j] += temp_pay[j]
    
    print(' '.join([str(num) for num in result]))

if __name__ == '__main__':
    main()