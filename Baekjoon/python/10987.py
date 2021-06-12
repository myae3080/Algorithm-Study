# string

vowel_list = ['a', 'e', 'i', 'o', 'u']
count = 0

for ch in input():
    if ch in vowel_list:
        count += 1

print(count)