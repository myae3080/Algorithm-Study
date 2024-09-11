# source : https://www.acmicpc.net/problem/6794

def main():
    # input
    n = int(input())
    
    result = 0
    for l in range(6):
        for r in range(l, 6):
            if l + r == n:
                result += 1
    
    print(result)

if __name__ == '__main__':
    main()