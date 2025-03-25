# source : https://www.acmicpc.net/problem/11608

def main():
    # input
    s = input()
    
    alpha = [0] * 26
    for c in s:
        alpha[ord(c) - 97] += 1
        
    alpha.sort(reverse=True)
    
    print(sum(alpha[2:]))

if __name__ == '__main__':
    main()