# source : https://www.acmicpc.net/problem/14649

def main():
    stones = [0] * 100
    
    # input
    P, N = int(input()), int(input())
    
    for _ in range(N):
        # input
        num, direction = input().split()
        
        if direction == 'R':
            for i in range(int(num), 100):
                stones[i] += 1
        else:
            for i in range(int(num) - 1):
                stones[i] += 1
    
    b, r, g = 0, 0, 0
    for i in range(100):
        if stones[i] % 3 == 0:
            b += 1
        elif stones[i] % 3 == 1:
            r += 1
        else:
            g += 1
    
    print('{:.2f}'.format((P * (b / 100))))
    print('{:.2f}'.format((P * (r / 100))))
    print('{:.2f}'.format((P * (g / 100))))

if __name__ == '__main__':
    main()