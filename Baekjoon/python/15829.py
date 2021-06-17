# string, hasing

# input
leng = int(input())
input_str = input()

sum_list = [(ord(input_str[i]) - 96) * (31 ** i) for i in range(leng)]

print(sum(sum_list) % 1234567891)