# source : https://www.acmicpc.net/problem/16944

def main():
    # input
    N = int(input())
    S = input()
    
    special = '!@#$%^&*()-+'
    rules = [0, 0, 0, 0]
    
    for s in S:
        if s.isnumeric():
            rules[0] += 1
        elif s.islower():
            rules[1] += 1
        elif s.isupper():
            rules[2] += 1
        elif s in special:
            rules[3] += 1
    
    print(max(rules.count(0), max(6 - N, 0)))

if __name__ == '__main__':
    main()