def hanoi(n, from_tower: str, to_tower: str, temp_tower: str):
    if n == 1:
        print(from_tower, ' ===> ', to_tower)
        return
    else:
        hanoi(n - 1, from_tower, temp_tower, to_tower)
        print(from_tower, ' ===> ', to_tower)
        hanoi(n - 1, temp_tower, to_tower, from_tower)

hanoi(4, 'A', 'B', 'C')