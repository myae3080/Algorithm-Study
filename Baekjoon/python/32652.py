# source : https://www.acmicpc.net/problem/32652

def main():
    # input
    K = int(input())
    
    result = 'AKARAKA'
    for _ in range(1, K):
        result += 'RAKA'

    print(result)

if __name__ == '__main__':
    main()