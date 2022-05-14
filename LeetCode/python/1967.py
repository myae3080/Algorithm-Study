# source : https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        return len([pattern for pattern in patterns if pattern in word])