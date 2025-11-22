class  Solution:
    def Two_sum_count_pair(self, nums,target):
        seen={}
        count=0
        for group_o_num in nums:
            need=target-group_o_num
            if need in seen:
                count=count+seen[need]
            if group_o_num in seen:
                seen[group_o_num]=seen[group_o_num]+1
            else:
                seen[group_o_num]=1
        return count

nums=[1, 7, 11, 1]
target=8
sol=Solution()
result=sol.Two_sum_count_pair(nums,target)
print(result)