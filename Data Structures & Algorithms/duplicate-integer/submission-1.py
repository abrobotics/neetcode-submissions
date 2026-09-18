class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False
        # Not optimized, O(n²)
        # i = 0
        # j = 1
        # while i < (len(nums) - 1):
        #     while j < len(nums):
        #         if (nums[i] != nums[j]):
        #             j+=1
        #         else:
        #             return True
        #     i+=1
        #     j=i+1

