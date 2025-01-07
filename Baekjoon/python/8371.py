# source : https://www.acmicpc.net/problem/8371

def main():
    # input
    n = int(input())
    a, b = input(), input()
    
    result = 0
    for i in range(n):
        if a[i] != b[i]:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()