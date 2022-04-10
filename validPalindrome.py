# https://leetcode.com/problems/valid-palindrome/submissions/

# Solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphanum(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))

        l = 0
        r = len(s) - 1

        while(l < r):
            while l < r and not alphanum(s[r]):
                r -= 1
            while l < r and not alphanum(s[l]):
                l += 1

            if s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1
        return True
