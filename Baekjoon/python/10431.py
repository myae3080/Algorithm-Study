# source : https://www.acmicpc.net/problem/10431

def main():
    # input
    for _ in range(int(input())):
        # input
        case = list(map(int, input().split()))
        
        count = 0
        for prev in range(1, len(case) - 1):
            for next in range(prev + 1, len(case)):
                if case[prev] > case[next]:
                    case[prev], case[next] = case[next], case[prev]
                    count += 1
        
        print(case[0], count)

if __name__ == '__main__':
    main()