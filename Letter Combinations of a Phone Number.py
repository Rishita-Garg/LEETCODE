# Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Approach: Backtracking using digit-letter mapping
# Time Complexity: O(4^n), Space Complexity: O(n)

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append("".join(path))
                return
            for letter in phone_map[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return res
