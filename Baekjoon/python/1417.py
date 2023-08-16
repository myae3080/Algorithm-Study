# source : https://www.acmicpc.net/problem/1417

def main():
    # input
    n = int(input())
    votes = [int(input()) for _ in range(n)]
    
    count = 0
    while 1:
        max_val = max(votes)
        max_index = votes.index(max_val)
        if votes.count(max_val) == 1 and max_index == 0:
            break
        else:
            for i in range(1, len(votes)):
                if votes[i] == max_val:
                    votes[i] -= 1
                    break
                
            votes[0] += 1
            count += 1
        
    print(count)

if __name__ == '__main__':
    main()