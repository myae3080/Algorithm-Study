# 입력 받은 한 줄을 string으로 할당.
data = input()

print('data : ', data)

# space가 포함된 입력을 분리해서 int형으로 할당.
data1, data2 = map(int, input().split())

print('data1 : ', data1, 'data2 : ', data2)

# space가 포함됨 입력을 분리해서 int형의 list로 할당.
# 입력 받은 값에 따른 type 지정?
data_list = list(map(int, input().split()))

print('data_list : ', data_list)