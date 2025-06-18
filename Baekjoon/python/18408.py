# source : https://www.acmicpc.net/problem/18408

def main():
    # input
    nums = list(map(int, input().split()))
    
    print(1 if nums.count(1) > 1 else 2)

if __name__ == '__main__':
    main()