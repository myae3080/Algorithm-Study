# source : https://www.acmicpc.net/problem/25905

def main():
    # input
    odds = sorted([float(input()) for _ in range(10)], reverse=True)
    
    result = 1
    for i in range(9):
        result *= (odds[i] / (i + 1))
    
    print(round(result * (10 ** 9), 6))

if __name__ == '__main__':
    main()