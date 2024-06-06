# source : https://www.acmicpc.net/problem/16283

def main():
    # input
    a, b, n, w = map(int, input().split())

    answer = []
    for i in range(1, n):
        if (a * i) + (b * (n - i)) == w:
            answer.append((i, n - i))

            if len(answer) == 2:
                break
    
    if len(answer) == 1:
        print(answer[0][0], answer[0][1])
    else:
        print(-1)
    
if __name__ == '__main__':
    main()