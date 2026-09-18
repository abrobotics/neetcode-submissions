class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = []
        for i, n in enumerate(nums):
            if (target - n) in nums[:i] + nums[i+1:]:
                pair.append(i)
                if len(pair) == 2:
                    break
        return pair
        # # brute force
        # i = 0
        # j = 1
        # while(i < len(nums) - 1):
        #     while (j < len(nums)):
        #         if ((nums[i] + nums[j]) != target):
        #             j+=1
        #         else:
        #             return [i, j]
        #     i+=1
        #     j=i+1
