# source : https://www.acmicpc.net/problem/21867

def main():
    # input
    N = int(input())
    S = input()
    
    remove_chars = ['J', 'A', 'V']
    
    result = S
    for c in remove_chars:
        result = result.replace(c, '')
    
    print('nojava' if len(result) == 0 else result)

if __name__ == '__main__':
    main()