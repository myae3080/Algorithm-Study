# source : https://www.acmicpc.net/problem/13333

def main():
    # input
    n = int(input())
    indexes = sorted(list(map(int, input().split())), reverse=True)
    
    k = n
    while k > -1:
        if k == 0:
            print(k)

            break 
        
        over = len([i for i in indexes if i >= k])
        under = len([i for i in indexes if i <= k])

        if over >= k and under <= k:
            print(k)

            break
        else:
            k -= 1

if __name__ == '__main__':
    main()