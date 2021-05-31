#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# class Solution:
#     def reverse(self, x: int) -> int:
#         str_x = str(x)
#         if str_x[0] != '-':
#             str_x = str_x[::-1]
#             x = int(str_x)
#         else:
#             str_x = str_x[1:][::-1]
#             x = int(str_x)
#             x = -x
#         if x>=-2**31 and x<= 2**31-1:
#             return x
#         else:
#             return 0

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        y,res = abs(x),0
        b = 1<<31 if x<0 else (1<<31)-1
        while y!=0:
            res = res*10 + y%10
            y //= 10
        res = res if res<b else 0
        res = res if x>0 else -res
        return res

# @lc code=end
