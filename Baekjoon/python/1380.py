# source : https://www.acmicpc.net/problem/1380

def main():
    results = []
    while 1:
        # input
        n = int(input())
        
        if n == 0:
            break
        
        # input
        students = [input() for _ in range(n)]
        
        earings_by_studs = {}
        for _ in range(2 * n - 1):
            # input
            num, check = input().split()
            
            if num not in earings_by_studs:
                earings_by_studs[num] = [check]
            else:
                earings_by_studs[num].append(check)
        
        for k, v in earings_by_studs.items():
            if len(v) == 1:
                results.append(students[int(k) - 1])
    
    for i in range(len(results)):
        print(i + 1, results[i])

if __name__ == '__main__':
    main()