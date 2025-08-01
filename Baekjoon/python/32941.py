# source : https://www.acmicpc.net/problem/32941

def main():
    # input
    T, X = map(int, input().split())

    is_possible = True
    
    # input
    for _ in range(int(input())):
        # input
        K = int(input())
        A = list(map(int, input().split()))

        if X not in A:
            is_possible = False
    
    print('YES' if is_possible else 'NO')

if __name__ == '__main__':
    main()