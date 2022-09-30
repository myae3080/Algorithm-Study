# source : https://www.acmicpc.net/problem/17362

finger_numbers = {
    0: 2,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 4,
    7: 3,
    8: 2,
    9: 1
}

# input
n = int(input())

print(finger_numbers[n % 8])