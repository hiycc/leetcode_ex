#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        res,y = 0,x
        while y!=0:
            res = res*10 + y%10
            y//=10
        if res == x:
            return True
        else:
            return False
# @lc code=end

