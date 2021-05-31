#
# @lc app=leetcode.cn id=13 lang=python3
#



# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace('IV','Q')
        s = s.replace('IX','W')
        s = s.replace('XL','E')
        s = s.replace('XC','R')
        s = s.replace('CD','T')
        s = s.replace('CM','Y')
        
        keys = {
            'Q':4,
            'W':9,
            'E':40,
            'R':90,
            'T':400,
            'Y':900,
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        res = 0
        for i in s:
            res +=  keys[i]
        return res
# @lc code=end

