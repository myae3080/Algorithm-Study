# source : https://www.acmicpc.net/problem/26531

def main():
    # input
    inputs = list(input().split())
    
    print('YES' if int(inputs[0]) + int(inputs[2]) == int(inputs[4]) else 'NO')

if __name__ == '__main__':
    main()