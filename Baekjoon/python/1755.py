# math, string, sorting

# input
m, n = map(int, input().split())

num_str_dict = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

result_list = []
[result_list.append((i, ' '.join(num_str_dict[s] for s in str(i)))) for i in range(m, n + 1)]
result_list.sort(key=lambda x: x[1])

[print(result_list[i][0]) if (i + 1) % 10 == 0 else print(result_list[i][0], end=' ') for i in range(len(result_list))]