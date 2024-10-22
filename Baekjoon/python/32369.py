# source : https://www.acmicpc.net/problem/32369

def main():
    # input
    N, A, B = map(int, input().split())
    
    compliment_onion, blame_onion = 1, 1
    for _ in range(N):
        compliment_onion += A
        blame_onion += B
        
        if compliment_onion == blame_onion:
            blame_onion -= 1
        elif blame_onion > compliment_onion:
            compliment_onion, blame_onion = blame_onion, compliment_onion
    
    print(compliment_onion, blame_onion)

if __name__ == '__main__':
    main()