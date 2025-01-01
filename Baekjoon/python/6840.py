# source : https://www.acmicpc.net/problem/6840

def main():
    #input
    nums = [int(input()) for _ in range(3)]

    print(sorted(nums)[1])

if __name__ == '__main__':
    main()