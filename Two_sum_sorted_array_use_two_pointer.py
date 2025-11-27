class Solution:
    def Two_Sum_sorted_arr(self, nums,target):
        left=0
        right=len(nums)-1
        while left<right:
            current_sum=nums[left]+ nums[right]
            if current_sum==target:
                return[nums[left],nums[right]]
            elif current_sum<target:
                left=left+1
            else:
                right=right-1
        return []

nums = [2,7,11,15]
target = 9
sol=Solution()
result=sol.Two_Sum_sorted_arr(nums,target)
print(result)