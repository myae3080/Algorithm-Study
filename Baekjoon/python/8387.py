# source : https://www.acmicpc.net/problem/8387

def main():
    # input
    n = int(input())
    first, second = input(), input()
    
    result = 0
    for i in range(n):
        if first[i] == second[i]:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()