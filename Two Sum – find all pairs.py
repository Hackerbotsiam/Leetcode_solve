class Solution:
    def TwoSum_all_pairs(self, nums,target):
        seen={}
        pairs=[]
        for i , group_o_num in enumerate(nums):
            need=target-group_o_num
            if need in seen:
                pairs.append([seen[need],i])
            seen[group_o_num]=i
        return pairs
nums=[1,5,7,1]
target=8
sol=Solution()
result=sol.TwoSum_all_pairs(nums,target)
print(result)