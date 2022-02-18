# https://leetcode.com/problems/valid-parentheses/

# Solution 1

class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        brackets = []
        for b in s:
            if b in matching.values():
                brackets.append(b)
            elif b in matching.keys() and (not len(brackets) or matching[b] != brackets[-1]):
                return False
            else:
                brackets.pop()
        if len(brackets):
            return False
        return True
