# source : https://www.acmicpc.net/problem/25325

def main():
    # input
    n = int(input())
    students = input().split()
    
    scores_by_names = {}
    for name in students:
        scores_by_names[name] = 0
    
    for _ in range(n):
        # input
        names = input().split()
        
        for name in names:
            scores_by_names[name] += 1
    
    results = sorted(scores_by_names.items(), key=lambda x:x[1], reverse=True)
    
    for tu in results:
        print(tu[0], tu[1])

if __name__ == '__main__':
    main()