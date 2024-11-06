class Solution:
    def canSortArray(self, nums) -> bool:
        result = False
        binary_mapping = {}
        for i in nums:
            binary_rep = bin(i).replace("0b", "") 
            set_bit = binary_rep.count('1')
            binary_mapping[i] = set_bit
        
        actual_sorted = sorted(nums)
        for j in range(len(nums)-1):
            for i in range(len(nums)-1):
                if binary_mapping[nums[i]] == binary_mapping[nums[i+1]]:
                    if nums[i]>nums[i+1]:
                        temp = nums[i]
                        nums[i] = nums[i+1]
                        nums[i+1] = temp
                    else:
                        continue
                    
                else:
                    continue
        
        if nums == actual_sorted:
            result = True
        
        return result



nums = [3,16,8,4,2]
print (Solution().canSortArray(nums))