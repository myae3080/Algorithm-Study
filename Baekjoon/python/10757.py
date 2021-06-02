# math

"""
python3에서는 숫자 정수형이 integer뿐이고, integer의 경우 overflow를 고려하지 않아도 됨.
"""

"""
두 번째 풀이
"""
# input
print(sum(map(int, input().split())))

"""
첫 번째 풀이
"""
# input
a, b = map(int, input().split())

print(a + b)