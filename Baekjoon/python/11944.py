# string

# input
n, m = input().split()

result = n * int(n)

print(result[:int(m)]) if len(result) > int(m) else print(result)