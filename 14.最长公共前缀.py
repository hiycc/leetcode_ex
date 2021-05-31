#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''zip方法
        if not strs: return ''
        res = ''
        ss = list(map(set,zip(*strs)))
        for i,x in enumerate(ss):
            x = list(x)
            if len(x)>1:break
            res = res+x[0]
        return res
        '''
        if not strs: return ''
        x1 = min(strs)
        x2 = max(strs)
        for i,x in enumerate(x1):
            if x != x2[i]:
                return x2[:i]
        return x1
        
                
# @lc code=end

