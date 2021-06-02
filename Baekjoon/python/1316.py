# String

# input
word_num = int(input())

word_list = []

for i in range(word_num):
    word_list.append(input())

result_num = word_num

for word in word_list:
    for index in range(len(word) - 1):
        if word[index] != word[index + 1]:
            temp_str = word[index + 1:]
            
            if temp_str.find(word[index]) != -1:
                result_num -= 1
                break

print(result_num)