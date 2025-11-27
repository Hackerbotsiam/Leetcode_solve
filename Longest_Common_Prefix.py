class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix=strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix=prefix[:-1]
                if prefix=="":
                    return ""
        return prefix

strs=["flowers","flow","flight"]
sol=Solution()
result=sol.longestCommonPrefix(strs)
print(f'"{result}"')