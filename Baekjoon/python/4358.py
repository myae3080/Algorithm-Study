# source : https://www.acmicpc.net/problem/4358

from collections import defaultdict
import sys
input = sys.stdin.readline

trees = defaultdict(int)
total = 0

while True:
    # input
    tree = input().rstrip()
    if not tree:
        break

    total += 1
    trees[tree] += 1

[print(tree[0], '{:.4f}'.format((int(tree[1]) / total) * 100)) for tree in sorted(trees.items())]