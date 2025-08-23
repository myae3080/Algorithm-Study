# source : https://www.acmicpc.net/problem/1449

def main():
    # input
    N, L = map(int, input().split())
    locations = list(map(int, input().split()))

    repair = {}
    locations.sort()

    result = 0
    for l in locations:
        is_need_repair = False
        for i in range(2):
            check = l + i * 0.5 - 0.5

            if check not in repair:
                is_need_repair = True

        if not is_need_repair:
            continue

        for i in range(L * 2 + 1):
            target = l + i * 0.5 - 0.5
            if target not in repair:
                repair[target] = 1
        
        result += 1
    
    print(result)

if __name__ == '__main__':
    main()