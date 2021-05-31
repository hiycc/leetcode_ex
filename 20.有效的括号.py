#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        while '[]' in s or '{}' in s or '()' in s:
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
        return s==''
        '''
        '''堆栈
        91/91 cases passed (60 ms)
        Your runtime beats 6.94 % of python3 submissions
        Your memory usage beats 75.72 % of python3 submissions (14.8 MB)

        dic = {']':'[',')':'(','}':'{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:stack.pop()
                else:return False
            else:
                stack.append(i)
        return not stack
        
        '''
        
# @lc code=end

