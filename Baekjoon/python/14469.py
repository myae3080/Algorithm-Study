# source : https://www.acmicpc.net/problem/14469

def main():
    # input
    n = int(input())
    time = [tuple(map(int, input().split())) for _ in range(n)]

    time.sort(key=lambda t: (t[0], t[1]))

    total_time = sum(time[0])
    for i in range(1, len(time)):
        if total_time <= time[i][0]:
            total_time = sum(time[i])
        else:
            total_time += time[i][1]
    
    print(total_time)

if __name__ == '__main__':
    main()