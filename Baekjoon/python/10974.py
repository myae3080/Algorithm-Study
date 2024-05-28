# source : https://www.acmicpc.net/problem/10974

def main():
    # input
    n = int(input())
    
    backTracking([], n)

def backTracking(arr: list, n: int):
    if len(arr) == n:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            backTracking(arr, n)
            arr.pop()

if __name__ == '__main__':
    main()