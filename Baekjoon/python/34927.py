# source : https://www.acmicpc.net/problem/34927

def main():
    # input
    N = int(input())
    box_weights = sorted(list(map(int, input().split())))

    s = box_weights[0]
    i = 1
    result = 1
    while i < N:
        if box_weights[i] >= s:
            s += box_weights[i]
            result += 1
        
        i += 1
    
    print(result)

if __name__ == '__main__':
    main()