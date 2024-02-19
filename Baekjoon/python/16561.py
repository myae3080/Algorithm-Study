# source : https://www.acmicpc.net/problem/16561

def main():
    # input
    n = int(input())
    
    count = 0
    for i in range(3, n + 1, 3):
        for j in range(3, n + 1, 3):
            if (n - i - j) < 3:
                continue
            else:
                count += 1
    
    print(count)

if __name__ == '__main__':
    main()