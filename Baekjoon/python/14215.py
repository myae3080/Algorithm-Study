# source : https://www.acmicpc.net/problem/14215

def main():
    # input
    sides = sorted(list(map(int, input().split())))
    
    if sides[0] + sides[1] > sides[2]:
        print(sum(sides))
    else:
        two_sides_sum = sum(sides[:2])
        print(2 * two_sides_sum - 1)
    
if __name__ == '__main__':
    main()