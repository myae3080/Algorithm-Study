# source : https://www.acmicpc.net/problem/5567

import sys 

input = sys.stdin.readline

def main():
    # input
    n, m = int(input()), int(input())

    friends = []
    friend_by_friend = {}

    for _ in range(m):
        # input
        a, b = map(int, input().split())

        if a == 1 or b == 1:
            friends.append(b if a == 1 else a)
        else:
            if a in friend_by_friend:
                friend_by_friend[a].append(b)
            else:
                friend_by_friend[a] = [b]
            
            if b in friend_by_friend:
                friend_by_friend[b].append(a)
            else:
                friend_by_friend[b] = [a]

    invited = [0] * (n + 1)
    for f in friends:
        if not invited[f]:
            invited[f] = 1
        
        if f in friend_by_friend:
            for ff in friend_by_friend[f]:
                if not invited[ff]:
                    invited[ff] = 1

    print(invited.count(1))

if __name__ == '__main__':
    main()