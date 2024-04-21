# source : https://www.acmicpc.net/problem/3048

def main():
    # input
    n1, n2 = map(int, input().split())
    group1, group2 = list(input()), list(input())
    t = int(input())
    
    result = group1[::-1] + group2
    for _ in range(t):
        for i in range(n1 + n2 - 1):
            if (result[i] in group1) and (result[i + 1] in group2):
                result[i], result[i + 1] = result[i + 1], result[i]
                
                if result[i + 1] == group1[0]:
                    break
        
    print(''.join(result))
    
if __name__ == '__main__':
    main()