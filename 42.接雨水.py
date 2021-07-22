#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # ans = 0
        # for i in range(1,len(height)-1):
        #     left_high = max(height[:i])
        #     right_high = max(height[i+1:])
        #     low = min(left_high,right_high)
        #     if low-height[i] > 0 :
        #         ans += (low-height[i])
        # return ans
        '''
        Accepted
            320/320 cases passed (1236 ms)
            Your runtime beats 5.03 % of python3 submissions
            Your memory usage beats 70.41 % of python3 submissions (15.1 MB)
        '''
        # ans = 0
        # max_left = [x*0 for x in range(1,len(height)+1)]
        # max_right = [x*0 for x in range(1,len(height)+1)]
        # for i in range(1,len(height)-1):
        #     max_left[i] = max(max_left[i-1],height[i-1])
        # for i in range(len(height)-2,-1,-1):
        #     max_right[i] = max(max_right[i+1],height[i+1])
        # for i in range(1,len(height)-1):
        #     low = min(max_left[i],max_right[i])
        #     if low - height[i] > 0 :
        #         ans += (low - height[i])
        # return ans
        '''
        Accepted
            320/320 cases passed (40 ms)
            Your runtime beats 87.27 % of python3 submissions
            Your memory usage beats 10.27 % of python3 submissions (15.5 MB)
        '''
        stack = []
        ans = 0
        i = 0
        while i<len(height):
            if not stack:
                stack.append(height[i])
                i += 1
            else:
                while stack:
                    if height[i] < stack[0]:
                        stack.append(height[i])
                        i += 1
                        if i == len(height):
                            break
                    else:
                        ans += (min(stack[0],height[i])-stack.pop())
        return ans
            
# @lc code=end

