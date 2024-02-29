# source : https://www.acmicpc.net/problem/25630

def main():
    # input
    n = int(input())
    st = input()
    
    result = 0
    for i in range(n // 2):
        if st[i] != st[n - i - 1]:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()