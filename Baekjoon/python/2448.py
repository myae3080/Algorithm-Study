# star, recursion

import math

star_list = ['  *   ', ' * *  ', '***** ']

def print_star(shift):
    length = len(star_list)

    for i in range(length):
        star_list.append(star_list[i] + star_list[i])
        # 해당 배열의 요소에 공백 적용.
        star_list[i] = '   ' * shift + star_list[i] + '   ' * shift

# input
n = int(input())
# 정확한 이유는 모르겠지만, 일반 연산으로 값을 세팅했을 시, 메모리 초과가 떠서 math 함수를 이용해서 값 세팅.
k = int(math.log(int(n / 3), 2))

for i in range(k):
    print_star(int(math.pow(2, i)))

print(star_list)

for i in range(n):
    print(star_list[i])