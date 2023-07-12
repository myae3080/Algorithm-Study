# source : https://www.acmicpc.net/problem/13073

def main():
    # input
    for _ in range(int(input())):
        # input
        n = int(input())
        
        s1 = n * (n + 1) // 2
        s2 = n ** 2
        s3 = n ** 2 + n
        
        print(s1, s2, s3)

if __name__ == '__main__':
    main()