# source : https://www.acmicpc.net/problem/31867

def main():
    # input
    N = int(input())
    K = input()
    
    odd, even = 0, 0
    for num in K:
        if int(num) % 2 == 1:
            odd += 1
        else:
            even += 1
    
    print(1 if odd > even else -1 if odd == even else 0)

if __name__ == '__main__':
    main()