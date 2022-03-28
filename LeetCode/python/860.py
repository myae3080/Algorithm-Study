# source : https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        dic = {
            5: 0,
            10: 0,
            20: 0,
        }

        for bill in bills:
            dic[bill] += 1

            if bill != 5:
                change = bill - 5
                
                if change == 5 and dic[5] == 0:
                    print(dic, change)
                    return False
                elif change == 15:
                    if not ((dic[5] >= 3) or (dic[5] >= 1 and dic[10] >= 1)):
                        return False
                    else:
                        if dic[5] >= 1 and dic[10] >= 1:
                            dic[5] -= 1
                            dic[10] -= 1
                        else:
                            dic[5] -= 3
                else:
                    dic[5] -= 1
            
        return True