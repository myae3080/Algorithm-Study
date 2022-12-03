# source : https://www.acmicpc.net/problem/13717

total_evol, max_evol = 0, 0
result_pokemon = ''
for _ in range(int(input())):
    # input
    pokemon = input()
    needed, total = map(int, input().split())
    
    count = 0
    while total >= needed:
        total -= needed
        total += 2
        count += 1

    total_evol += count
    if count > max_evol:
        result_pokemon = pokemon
    max_evol = max(max_evol, count)

print(total_evol)
print(result_pokemon)