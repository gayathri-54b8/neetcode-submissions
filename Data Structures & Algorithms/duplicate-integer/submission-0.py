class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        obj={}
        for i in nums:
            obj[i]=(obj.get(i,) or 0)+1
        for i in obj:
            if obj[i]>1:
                return True
        return False