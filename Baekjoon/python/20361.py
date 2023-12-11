# source : https://www.acmicpc.net/problem/20361

def main():
    # input
    n, x, k = map(int, input().split())
    
    cups = [0] * (n + 1)
    cups[x] = 1
    
    for _ in range(k):
        # input
        a, b = map(int, input().split())
        
        cups[a], cups[b] = cups[b], cups[a]
    
    print(cups.index(1))

if __name__ == '__main__':
    main()