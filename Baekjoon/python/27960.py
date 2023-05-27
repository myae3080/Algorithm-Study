# source : https://www.acmicpc.net/problem/27960

def main():
    # input
    a, b = map(int, input().split())
    
    a_bin, b_bin = bin(a)[2:].zfill(10), bin(b)[2:].zfill(10)
    multiplier = 9
    score = 0
    for i in range(10):
        if not (a_bin[i] == b_bin[i]):
            score += 2 ** (multiplier - i)

    print(score)
    
if __name__ == '__main__':
    main()