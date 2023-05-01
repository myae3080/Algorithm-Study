# source : https://www.acmicpc.net/problem/17509

def main():
    # input
    times = [list(map(int, input().split())) for _ in range(11)]
    times.sort()
    
    time, penalty = 0, 0
    for t in times:
        time += t[0]
        penalty += (time + 20 * t[1])
        
    print(penalty)

if __name__ == '__main__':
    main()