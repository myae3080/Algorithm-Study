# source : https://www.acmicpc.net/problem/13456

def main():
    # input
    for _ in range(int(input())):
        # input
        n = int(input())
        v, u = input().split(), input().split()

        hamming_distance = 0
        for i in range(n):
            if v[i] != u[i]:
                hamming_distance += 1
        
        print(hamming_distance)

if __name__ == '__main__':
    main()