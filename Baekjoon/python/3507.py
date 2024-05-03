# source : https://www.acmicpc.net/problem/3507

def main():
    # input
    n = int(input())
    
    result = 0
    for a in range(100):
        for b in range(100):
            if n - a - b == 0:
                result += 1
    
    print(result)

if __name__ == '__main__':
    main()