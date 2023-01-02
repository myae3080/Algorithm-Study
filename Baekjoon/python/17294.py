# source : https://www.acmicpc.net/problem/17294

# input
num = input()

is_cute = True
for i in range(2, len(num)):
    if int(num[i]) - int(num[i - 1]) != int(num[i - 1]) - int(num[i - 2]):
        is_cute = False
        break

print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!') if is_cute else print('흥칫뿡!! <(￣ ﹌ ￣)>')