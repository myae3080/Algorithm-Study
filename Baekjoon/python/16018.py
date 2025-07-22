# source : https://www.acmicpc.net/problem/16018

def main():
    # input
    N = int(input())
    yesterday = list(input())
    today = list(input())
    
    result = 0
    for i in range(N):
        if 'C' == yesterday[i] == today[i]:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()