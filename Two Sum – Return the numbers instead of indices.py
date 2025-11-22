class Solution:
    def Two_sum(self,nums,target):
        seen={}
        for i,group_o_num in enumerate(nums):
            need= target-group_o_num
            if need in seen:
                return [seen[need],group_o_num]
            seen[group_o_num]=group_o_num
        return []

nums=[2, 7, 11, 15]
target=9
sol=Solution()
result=sol.Two_sum(nums,target)
print(result)