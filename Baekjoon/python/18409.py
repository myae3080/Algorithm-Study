# source : https://www.acmicpc.net/problem/18409

def main():
    # input
    N, S = int(input()), input()

    vowels = ['a', 'e', 'i', 'o', 'u']
    result = 0
    for c in S:
        if c in vowels:
            result += 1
    
    print(result)

if __name__ == '__main__':
    main()