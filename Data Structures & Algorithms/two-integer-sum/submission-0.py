class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            comp = target - val
            if comp in seen:
                j = seen[comp]
                return [min(i, j), max(i, j)]
            seen[val] = i
