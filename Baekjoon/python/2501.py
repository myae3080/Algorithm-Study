# math, bruteforcing

# input
n, k = map(int, input().split())

divisor_set = set()

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        divisor_set.add(i)
        divisor_set.add(n // i)

if len(divisor_set) < k:
    print(0)
else:
    print(list(sorted(divisor_set))[k - 1])