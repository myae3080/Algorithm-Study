# number theory, prime number, Sieve of Eratosthenes

# prime number setting(Sieve of Eratosthenes)
n = 250000
prime_num_list = [True] * n

m = int(n ** 0.5)
for i in range(2, m + 1):
    if prime_num_list[i] == True:           
        for j in range(i + i, n, i):
            prime_num_list[j] = False

while True:
    input_num = int(input())

    if input_num == 0:
        break

    count = 0

    if input_num == 1:
        print(1)
    else:
        for i in range(input_num + 1, input_num * 2 + 1):
            if prime_num_list[i] == True:
                count += 1

        print(count)