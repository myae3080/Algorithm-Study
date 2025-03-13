# source : https://www.acmicpc.net/problem/3512

def main():
    # input
    n, c = map(int, input().split())
    
    
    total_metre, total_bedrooms, total_cost  = 0, 0, 0
    for _ in range(n):
        # input
        m, type = input().split()
        
        total_metre += int(m)
        
        if type == 'bedroom':
            total_bedrooms += int(m)
            
        if type == 'balcony':
            total_cost += ((int(m) / 2) * c)
        else:
            total_cost += (int(m) * c)
    
    print(total_metre)
    print(total_bedrooms)
    print(total_cost)

if __name__ == '__main__':
    main()