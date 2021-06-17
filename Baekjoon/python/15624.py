# fibonacci, dp

# input
n = int(input())

num1, num2, num3 = 1, 1, 2
result = 0

'''
    재귀는 시간 초과로 당연히 안되고 배열로 했을 때는 메모리 초과의 문제가 있어,
    세 변수를 가지고 변화시키면서 시도함.
    시간 초과로 통과하지 못 해 질문 검색을 통해 정확한 이유는 아직 모르지만 너무 큰 수를 한 번에 나누는 것 보다 그때 그때 나눠서 처리하는 것이 더 빨라서 다음과 같이 해결.
'''
if n != 0:
    for i in range(n):
        if i == 0 or i == 1:
            result = 1
        else:
            result = num3 = (num1 + num2) % 1000000007
            num1 = num2 % 1000000007
            num2 = num3 % 1000000007

print(result)