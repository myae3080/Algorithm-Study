# source : https://www.acmicpc.net/problem/31776

def main():
    result = 0
    
    # input
    for _ in range(int(input())):
        # input
        times = list(map(int, input().split()))
        
        if times.count(-1) == 3:
            continue
        
        for i in range(3):
            if times[i] == -1:
                times[i] = 121
        
        if times[0] <= times[1] <= times[2]:
            result += 1
        
    print(result)

if __name__ == '__main__':
    main()