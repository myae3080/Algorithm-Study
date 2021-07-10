# math, brute forcing, number theory, prime number, Sieve of Eratosthenes

# Sieve of Eratosthenes
n = 1010000
sieve = [True] * n

m = int(n ** 0.5)

for i in range(2, m + 1):
    if sieve[i] == True:           
        for j in range(i + i, n, i): 
            sieve[j] = False

sieve[1] = False

# input
input_num = int(input())

for i in range(input_num, n + 1):
    if sieve[i] == True:
        temp_str = str(i)
        is_palindrome = True

        mid = len(temp_str) // 2

        for j in range(mid):
            if temp_str[j] != temp_str[len(temp_str) - j - 1]:
                is_palindrome = False
                break

        if is_palindrome:
            print(i)
            break