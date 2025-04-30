# source : https://www.acmicpc.net/problem/32642

def main():
    # input
    N = int(input())
    days = list(map(int, input().split()))

    condition = 0
    conditions = [0] * N
    for i in range(N):
        if days[i] == 1:
            condition += 1
        else:
            condition -= 1
        
        conditions[i] = condition
    
    print(sum(conditions))

if __name__ == '__main__':
    main()