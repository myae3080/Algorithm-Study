# source : https://www.acmicpc.net/problem/6246

def main():
    # input
    N, Q = map(int, input().split())
    methods = [list(map(int, input().split())) for _ in range(Q)]

    slots = [0] * (N + 1)
    for m in methods:
        for i in range(m[0], N + 1, m[1]):
            slots[i] = 1
    
    print(slots[1:].count(0))

if __name__ == '__main__':
    main()