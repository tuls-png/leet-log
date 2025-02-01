'''
3151. Special Array I
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

'''

class Solution:
    def isArraySpecial(self, nums):
        bool_check = True
        if len(nums) == 1:
            return bool_check
        else:
            for i in range(0, len(nums)-1):
                rem1 = nums[i]%2
                rem2 = nums[i+1]%2
                if (rem1 == 0 and rem2 == 0) or (rem1 != 0 and rem2 != 0):
                    bool_check = False
                    break
                else:
                    bool_check = True
            return bool_check

nums = [1]
print(Solution().isArraySpecial(nums=nums))
