# source : https://www.acmicpc.net/problem/21955

def main():
    # input
    num = input()
    
    half_idx = len(num) // 2
    
    print(num[:half_idx], num[half_idx:])

if __name__ == '__main__':
    main()