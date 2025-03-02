# source : https://www.acmicpc.net/problem/2896

def main():
    # input
    A, B, C = map(int, input().split())
    I, J, K = map(int, input().split())
    
    ratio = min(A / I, B / J, C / K)
    
    print(A - I * ratio, B - J * ratio, C - K * ratio)

if __name__ == '__main__':
    main()