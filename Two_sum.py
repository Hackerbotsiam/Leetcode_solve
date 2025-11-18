class Solution:
    def twoSum(self, nums, target):
        seen = {}  # number : index
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
        return []

# ---------- Example list assignment ----------
nums = [2, 7, 11, 15]   
target = 9

# ---------- Call the class function ----------
sol = Solution()
result = sol.twoSum(nums, target)

# ---------- Print Result ----------
print(result)
