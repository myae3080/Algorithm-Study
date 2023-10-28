# source : https://www.acmicpc.net/problem/1703

def main():
    while 1:
        # input
        tree = list(map(int, input().split()))

        if tree[0] == 0:
            break

        result = 1
        for i in range(tree[0]):
            result = result * tree[2 * i + 1] - tree[2 * i + 2]
        
        print(result)

if __name__ == '__main__':
    main()