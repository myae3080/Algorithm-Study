# source : https://www.acmicpc.net/problem/2992

from itertools import permutations

def main():
    # input
    num = int(input())

    str_nums = list(str(num))

    has_result = False
    for n in sorted([int(''.join(c)) for c in permutations(str_nums, len(str_nums))]):
        if n > num:
            has_result = True

            print(n)

            break
    
    if not has_result:
        print(0)

if __name__ == '__main__':
    main()