# math, number theory, prime number, Sieve of Eratosthenes

# input
n, m = map(int, input().split())

num_list = [0] * (n + 2)

for i in range(2, n + 1):
    if num_list[i] == 0:
        for j in range(i, n + 1):
            if j % i == 0 and num_list[j] == 0:
                num_list[j] = 1
                m-= 1

            if m == 0:
                print(j)
                break