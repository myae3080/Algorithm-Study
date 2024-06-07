# source : https://www.acmicpc.net/problem/2622
# PyPy3

def main():
    # input
    match = int(input())

    result = 0
    for a in range(1, match - 1):
        for b in range(a, match):
            c = match - a - b

            if c >= a + b:
                continue
            else:
                if b > c:
                    break

                result += 1

    print(result)

if __name__ == '__main__':
    main()