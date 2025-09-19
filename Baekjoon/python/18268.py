# source : https://www.acmicpc.net/problem/18268

def main():
    # input
    K, N = map(int, input().split())

    d = {}
    for _ in range(K):
        # input
        cows = list(map(int, input().split()))

        for i in range(N):
            for j in range(i + 1, N):
                if (cows[j], cows[i]) in d:
                    d[(cows[j], cows[i])] += 1
                else:
                    d[(cows[j], cows[i])] = 1
    
    print(list(d.values()).count(K))

if __name__ == '__main__':
    main()