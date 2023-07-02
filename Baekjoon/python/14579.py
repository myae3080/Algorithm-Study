# source : https://www.acmicpc.net/problem/14579

def main():
    # input
    a, b = map(int, input().split())
    
    base_sum = sum([i for i in range(1, a + 1)])
    result = base_sum
    for j in range(a + 1, b + 1):
        base_sum += j
        result *= base_sum
        
    print(result % 14579)
    
if __name__ == '__main__':
    main()