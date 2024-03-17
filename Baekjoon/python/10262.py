# source : https://www.acmicpc.net/problem/10262

def main():
    # input
    g = sum(list(map(int, input().split())))
    e = sum(list(map(int, input().split())))

    if g == e:
        print('Tie')
    elif g > e:
        print('Gunnar')
    else:
        print('Emma')
    
if __name__ == '__main__':
    main()