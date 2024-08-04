# source : https://www.acmicpc.net/problem/17211

def main():
    # input
    n, mood = map(int, input().split())
    gg, gb, bg, bb = map(float, input().split())
    
    if mood == 0:
        good, bad = gg, gb
    else:
        good, bad = bg, bb

    for _ in range(1, n):
        prev_good = good
        good = good * gg + bad * bg
        bad = bad * bb + prev_good * gb

    print(round(good * 1000))
    print(round(bad * 1000))

if __name__ == '__main__':
    main()