# https://leetcode.com/problems/length-of-last-word/submissions/

# Solution 1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])

# Solution 2


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        charFound = False
        length = 0
        for i in range(len(s) - 1, -1, -1):
            print(s[i])
            if s[i] != ' ' and not charFound:
                charFound = True
                length += 1
            elif s[i] == ' ' and charFound:
                break
            elif s[i] != ' ':
                length += 1
        return length
