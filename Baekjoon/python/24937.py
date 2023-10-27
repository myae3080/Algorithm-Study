# source : https://www.acmicpc.net/problem/24937

def main():
    result = 'SciComLove'
    results = []
    for _ in range(len(result)):
        result = result[1:] + result[0]
        results.append(result)

    # input
    n = int(input())

    print(results[(n % 10) - 1])

if __name__ == '__main__':
    main()