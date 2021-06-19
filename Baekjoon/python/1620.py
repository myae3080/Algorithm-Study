# data structure, string, map, dictionary

import sys

# input
input = sys.stdin.readline

pokemon_num, find_num = map(int, input().split())

pokemon_dict = {}
reverse_pokemon_dict = {}

for i in range(1, pokemon_num + 1):
    pokemon_dict[str(i)] = input().rstrip()

reverse_pokemon_dict = {v:k for k,v in pokemon_dict.items()}

for i in range(find_num):
    input_str = input().rstrip()

    if pokemon_dict.get(input_str) != None:
        print(pokemon_dict.get(input_str))
    else:
        print(reverse_pokemon_dict.get(input_str))