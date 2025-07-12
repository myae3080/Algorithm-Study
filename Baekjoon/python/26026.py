# source : https://www.acmicpc.net/problem/26026

def main():
    # input
    n = int(input())
    halls = input()
    
    result = int(halls[0])
    for i in range(1, n):
        if halls[i] == '1' or halls[i - 1] == '1' or (i - 2 >= 0 and  halls[i - 2] == '1'):
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()