#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber>0:
            columnNumber -=1
            res = chr(65+columnNumber%26)+res
            columnNumber //=26
        return res
        
        '''
        18/18 cases passed (44 ms)
        Your runtime beats 27.41 % of python3 submissions
        Your memory usage beats 54.03 % of python3 submissions (14.8 MB)
        '''
# @lc code=end

