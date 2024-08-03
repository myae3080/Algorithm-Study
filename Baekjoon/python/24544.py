# source : https://www.acmicpc.net/problem/24544

def main():
    # input
    n = int(input())
    interest = list(map(int, input().split()))
    registration = list(input().split())
    
    print(sum(interest))
    
    not_registered = 0
    for i in range(n):
        if registration[i] == '0':
            not_registered += interest[i]
    
    print(not_registered)

if __name__ == '__main__':
    main()