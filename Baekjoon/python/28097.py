# source : https://www.acmicpc.net/problem/28097

def main():
    # input
    n = int(input())
    plans = list(map(int, input().split()))
    
    whole_time = sum(plans) + (n - 1) * 8
    
    print(whole_time // 24, whole_time % 24)
    
if __name__ == '__main__':
    main()