# source : https://www.acmicpc.net/problem/31908

import sys
input = sys.stdin.readline

def main():
    names_by_ring = {}
    
    # input
    for _ in range(int(input())):
        # input
        name, ring = input().rstrip().split()
        
        if ring == '-':
            continue
        
        if ring in names_by_ring:
            names_by_ring[ring].append(name)
        else:
            names_by_ring[ring] = [name]
    
    couple_count = 0
    result = []
    for ring in names_by_ring.keys():
        if len(names_by_ring[ring]) == 2:
            couple_count += 1
            result.append(' '.join(names_by_ring[ring]))
    
    print(couple_count)
    for couple in result:
        print(couple)

if __name__ == '__main__':
    main()