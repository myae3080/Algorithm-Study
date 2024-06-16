# source : https://www.acmicpc.net/problem/30403

def main():
    # input
    n = int(input())
    string = input()
    
    lower_rainbow = ['r', 'o', 'y', 'g', 'b', 'i', 'v']
    upper_rainbow = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']
    lower, upper = [0] * n, [0] * n
    
    for c in string:
        if c in lower_rainbow:
            lower[lower_rainbow.index(c)] = 1
        
        if c in upper_rainbow:
            upper[upper_rainbow.index(c)] = 1
    
    if lower.count(1) == 7 and upper.count(1) == 7:
        print('YeS')
    elif lower.count(1) == 7:
        print('yes')
    elif upper.count(1) == 7:
        print('YES')
    else:
        print('NO!')

if __name__ == '__main__':
    main()