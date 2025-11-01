# source : https://www.acmicpc.net/problem/20186

def main():
    # input
    N, K = map(int, input().split())
    seq = sorted(list(map(int, input().split())), reverse=True)

    print(sum(seq[:K]) - sum(range(1, K))) 

if __name__ == '__main__':
    main()