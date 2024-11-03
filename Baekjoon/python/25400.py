# source : https://www.acmicpc.net/problem/25400

def main():
    # input
    N = int(input())
    cards = list(map(int, input().split()))
    
    order = 1
    result = 0
    for num in cards:
        if order != num:
            result += 1
        else:
            order += 1
    
    print(result)

if __name__ == '__main__':
    main()