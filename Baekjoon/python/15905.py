# source : https://www.acmicpc.net/problem/15905

def main():
    # input
    n = int(input())
    students = sorted([list(map(int, input().split())) for _ in range(n)], reverse=True)
    
    if n <= 5:
        print(0)
    else:
        target_rank = students[4][0]
        result = 0
        for std in students[5:]:
            if target_rank == std[0]:
                result += 1
        
        print(result)

if __name__ == '__main__':
    main()