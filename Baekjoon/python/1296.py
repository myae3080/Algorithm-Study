# source : https://www.acmicpc.net/problem/1296

def main():
    # input
    name = input()
    n = int(input())
    
    if n == 1:
        # input
        print(input())
        return
    
    L, O, V, E = name.count('L'), name.count('O'), name.count('V'), name.count('E')
    
    result = {}
    for i in range(n):
        # input
        team_name = input()
        
        result[team_name] = getProbability(
            L + team_name.count('L'),
            O + team_name.count('O'),
            V + team_name.count('V'),
            E + team_name.count('E')
        )
    sorted_result = sorted(result.items(), key = lambda item: (-item[1], item[0]))
    
    print(sorted_result[0][0])
        
def getProbability(L, O, V, E):
    return ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    
if __name__ == '__main__':
    main()