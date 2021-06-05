# math, prime number

# input
count = int(input())

num_list = list(map(int, input().split()))
prime_count = 0

for num in num_list:
    if num == 1:
        continue
    elif num == 2:
        prime_count += 1
    else:
        for i in range(2, num + 1):
            if num % i == 0:
                if i != num:
                    break
                else:
                    prime_count += 1

print(prime_count)