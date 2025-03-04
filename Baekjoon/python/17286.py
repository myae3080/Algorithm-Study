# source : https://www.acmicpc.net/problem/17286

from itertools import permutations 
import sys

def main():
    # input
    yumi = list(map(int, input().split()))
    coordinates = permutations([list(map(int, input().split())) for _ in range(3)], 3)

    min_distance = sys.maxsize
    for co_list in coordinates:
        prev = yumi
        curr_d = 0
        for co in co_list:
            curr_d += ((prev[0] - co[0]) ** 2 + (prev[1] - co[1]) ** 2) ** 0.5
            
            prev = co
        
        min_distance = min(min_distance, curr_d)
    
    print(int(min_distance))

if __name__ == '__main__':
    main()