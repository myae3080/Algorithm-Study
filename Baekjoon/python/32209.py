# source : https://www.acmicpc.net/problem/32209

def main():
    # input
    events = [list(map(int, input().split())) for _ in range(int(input()))]
    
    q = 0
    has_next = True
    for event in events:
        if event[0] == 1:
            q += event[1]
        else:
            if q >= event[1]:
                q -= event[1]
            else:
                has_next = False
                break
    
    print('See you next month' if has_next else 'Adios')

if __name__ == '__main__':
    main()