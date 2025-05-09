# source : https://www.acmicpc.net/problem/16406

def main():
    # input
    k = int(input())
    mine = list(input())
    friend = list(input())

    same = 0
    for i in range(len(mine)):
        if mine[i] == friend[i]:
            same += 1
    
    print(len(mine) - abs(k - same))

if __name__ == '__main__':
    main()