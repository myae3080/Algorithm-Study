# source : https://www.acmicpc.net/problem/1337

def main():
    # input
    n = int(input())
    arr = sorted([int(input()) for _ in range(n)])

    result = 4
    for i in range(n):
        start = arr[i]

        need = 4
        correct_arr = [start + a for a in range(1, 5)]
        for j in range(i + 1, i + 5):
            if j >= n:
                break

            if arr[j] in correct_arr:
                need -= 1
        
        result = min(result, need)
    
    print(result)

if __name__ == '__main__':
    main()