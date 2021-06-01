# 너무 느림
class Solution:
    def getKth(this, lo: int, hi: int, k:int) -> int:
        num_list = []
        count_dict = {}

        for i in range(lo, hi + 1):
            num_list.append(i)

        for idx, num in enumerate(num_list):
            count = 0
            temp_num = num

            while num != 1:
                count += 1

                if num % 2 == 0:
                    num /= 2
                else:
                    num = num * 3 + 1
            
            count_dict[temp_num] = count

        test = sorted(count_dict.items(), key=lambda x : x[1])
        
        return test[k-1][0]

print(Solution.getKth(Solution, 7, 11, 4))
