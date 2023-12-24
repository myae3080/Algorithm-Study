# source : https://www.acmicpc.net/problem/27736

def main():
    # input
    n = int(input())
    votes = list(map(int, input().split()))
    
    approved, rejected, invalid = 0, 0, 0
    for v in votes:
        if v == 1:
            approved += 1
        elif v == -1:
            rejected += 1
        else:
            invalid += 1
    
    if invalid >= n / 2:
        print('INVALID')
    else:
        if approved > rejected:
            print('APPROVED')
        else:
            print('REJECTED')

if __name__ == '__main__':
    main()