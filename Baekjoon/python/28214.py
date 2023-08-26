# source : https://www.acmicpc.net/problem/28214

def main():
    # input
    n, k, p = map(int, input().split())
    breads = list(map(int, input().split()))
    
    result = 0
    cnt, no_cream = 0, 0
    for bread in breads:
        if bread == 0:
            no_cream += 1
            
        cnt += 1
        
        if cnt == k:
            if no_cream < p:
                result += 1
                
            cnt, no_cream = 0, 0
            
    print(result)

if __name__ == '__main__':
    main()