# source : https://www.acmicpc.net/problem/2606

import sys
input = sys.stdin.readline

def main():
    # input
    coms = int(input())
    pairs = int(input())
    
    network = {}
    for _ in range(pairs):
        # input
        a, b = map(int, input().split())
        
        if a in network:
            network[a].add(b)
        else:
            network[a] = {b}
        
        if b in network:
            network[b].add(a)
        else:
            network[b] = {a}

    visited = [0] * (coms + 1)
    def checkVirus(start):
        visited[start] = 1
        if start in network:
            for c in network[start]:
                if visited[c] == 0:
                    checkVirus(c)
    
    checkVirus(1)
    
    print(visited.count(1) - 1)
    
if __name__ == '__main__':
    main()