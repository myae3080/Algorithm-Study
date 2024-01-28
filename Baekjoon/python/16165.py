# source : https://www.acmicpc.net/problem/16165

def main():
    # input
    n, m = map(int, input().split())
    
    data = {'group': {}, 'member': {}}
    
    # data setting
    # input
    for _ in range(n):
        # input
        team = input()
        total = int(input())
        
        data['group'][team] = []
        
        # input
        for __ in range(total):
            # input
            member = input()
            
            data['group'][team].append(member)
            data['member'][member] = team
    
    # quiz
    # input
    for _ in range(m):
        # input
        info, type = input(), input()
        
        if type == '1':
            print(data['member'][info])
        else:
            for m in sorted(data['group'][info]):
                print(m)

if __name__ == '__main__':
    main()