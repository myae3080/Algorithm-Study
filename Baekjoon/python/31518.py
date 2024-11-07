# source : https://www.acmicpc.net/problem/31518

def main():
    # input
    n = int(input())
    
    seven = 0
    for _ in range(3):
        # input
        digits = list(map(int, input().split()))
        
        if 7 in digits:
            seven += 1
    
    print(777 if seven == 3 else 0)

if __name__ == '__main__':
    main()