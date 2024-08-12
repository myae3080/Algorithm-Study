# source : https://www.acmicpc.net/problem/26162

def main():
    size = 200
    sieve = [True] * size
    sieve[0], sieve[1] = False, False
    for i in range(2, int(size ** 0.5) + 1):
        if sieve[i]:           
            for j in range(i + i, size, i): 
                sieve[j] = False
    
    prime = [i for i in range(len(sieve)) if sieve[i]]
    
    # input
    for _ in range(int(input())):
        # input
        atomic_num = int(input())
        
        is_possible = False
        for p1 in prime:
            if p1 < atomic_num:
                for p2 in prime:
                    if p1 + p2 == atomic_num:
                        is_possible = True
                        break
                    elif p1 + p2 > atomic_num:
                        break
            
            if is_possible:
                break
        
        print('Yes' if is_possible else 'No')

if __name__ == '__main__':
    main()