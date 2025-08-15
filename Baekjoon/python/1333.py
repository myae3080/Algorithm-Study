# source : https://www.acmicpc.net/problem/1333

def main():
    # input
    N, L, D = map(int, input().split())

    total = N * L + (N - 1) * 5
    time = [0] * (total + 1)
    
    for i in range(N - 1):
        quiet = L * (i + 1) + i * 5
        for j in range(quiet, quiet + 5):
            time[j] = 1

    ring = D
    while ring < total:
        if time[ring]:
            break

        ring += D
    
    print(ring)

if __name__ == '__main__':
    main()