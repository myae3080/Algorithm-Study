# source : https://www.acmicpc.net/problem/17127

def main():
    # input
    n = int(input())
    cherry_blossom = list(map(int, input().split()))
    
    result = 0
    a_sum = 1
    for a in range(n - 3):
        a_sum *= cherry_blossom[a]
        b_sum = 1
        
        for b in range(a + 1, n - 2):
            b_sum *= cherry_blossom[b]
            c_sum = 1
            
            for c in range(b + 1, n - 1):
                c_sum *= cherry_blossom[c]
                d_sum = 1
                
                for d in range(c + 1, n):
                    d_sum *= cherry_blossom[d]
                    
                    result = max(result, a_sum + b_sum + c_sum + d_sum)
    
    print(result)

if __name__ == '__main__':
    main()