# source : https://www.acmicpc.net/problem/31859

def main():
    # input
    num, s = input().split()
    
    result = ''
    # rule 1
    for c in s:
        if c not in result:
            result += c
    
    # rule 2
    result += str(len(s) - len(result) + 4)

    # rule 3
    result = str(int(num) + 1906) + result
    
    # rule 4
    result = result[::-1]
    
    # rule 5
    result = 'smupc_' + result
    
    print(result)

if __name__ == '__main__':
    main()