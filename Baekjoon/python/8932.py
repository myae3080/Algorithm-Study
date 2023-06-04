# source : https://www.acmicpc.net/problem/8932

def main():
    constants = [
        [9.23076, 26.7, 1.835],
        [1.84523, 75, 1.348],
        [56.0211, 1.5, 1.05],
        [4.99087, 42.5, 1.81],
        [0.188807, 210, 1.41],
        [15.9803, 3.8, 1.04],
        [0.11193, 254, 1.88]
    ]
    
    # input
    n = int(input())
    for _ in range(n):
        # input
        scores = list(map(int, input().split()))
        
        result = 0
        for i in range(7):
            result += int(constants[i][0] * (abs(constants[i][1] - scores[i])) ** constants[i][2])
        
        print(result)

if __name__ == '__main__':
    main()