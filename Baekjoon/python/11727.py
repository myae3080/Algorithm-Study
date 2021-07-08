# dp

tile_list = [0, 1, 3]

# input
n = int(input())

if n > 2:
    for i in range(3, n + 1):
        tile_list.append((tile_list[i - 2] * 2) + tile_list[i - 1])

print(tile_list[n] % 10007)