# source : https://www.acmicpc.net/problem/31306

def main():
    # input
    s = input()
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = 0
    
    for v in vowels:
        result += s.count(v)
    
    print(result, result + s.count('y'))

if __name__ == '__main__':
    main()