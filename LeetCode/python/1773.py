# https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        dic = {"type": 0, "color": 1, "name": 2}
        count = 0
        
        for i in range(len(items)):
            if items[i][dic[ruleKey]] ==  ruleValue:
                count += 1
                
        return count