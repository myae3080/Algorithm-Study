# source : https://www.acmicpc.net/problem/18322

def main():
    # input
    N, K = map(int, input().split())
    words = list(input().split())
    
    curr_idx = 0
    results = []
    while curr_idx < N:
        length = 0
        temp = []
        for i in range(curr_idx, N):
            if length + len(words[i]) <= K:
                temp.append(words[i])
                length += len(words[i])
                curr_idx = i + 1
            else:
                break
        
        results.append(' '.join(temp))
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()