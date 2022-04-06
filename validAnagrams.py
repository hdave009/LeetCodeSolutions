# https://leetcode.com/problems/valid-anagram/submissions/

# Solution 1 - Mine
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        for i in s:
            if i in s_count:
                s_count[i] += 1
            else:
                s_count[i] = 1

        for i in t:
            if i in t_count:
                t_count[i] += 1
            else:
                t_count[i] = 1

        if len(s_count) == len(t_count):
            for c in s_count:
                if not (c in s_count and c in t_count and t_count[c] == s_count[c]):
                    return False
            return True
        return False

# Solution 2 - Neet Code


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
