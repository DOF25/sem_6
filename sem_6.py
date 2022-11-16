#Ссылка: https://leetcode.com/problems/3sum/
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        if len(nums) < 3:
            return []
        if (all(num == 0 for num in nums)):
            return [[0, 0, 0]]
        nums = sorted(nums)
        for ind, value in enumerate(nums):
            start = ind + 1
            end = len(nums) - 1
            while start < end:
                current = (value, nums[start], nums[end])
                total = sum(current)
                if total == 0:
                    if current not in d:
                        d[current] = True
                    end -= 1
                elif total > 0:
                    end -= 1
                else:
                    start += 1
        return list(d.keys())
    
#Ссылка: https://leetcode.com/problems/3sum-closest/
class Solution2:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if (all(num == 0 for num in nums)):
            return 0
        nums = sorted(nums)
        closest = nums[0] + nums[1] + nums[len(nums)-1]
        for ind, value in enumerate(nums):
            start = ind + 1
            end = len(nums) - 1
            while start < end:
                total = value + nums[start] + nums[end]
                if total == target:
                    return total
                if total > target:
                    end -= 1
                else:
                    start += 1
                if abs(closest - target) > abs(total - target):
                    closest = total
        return closest

#Ссылка: https://leetcode.com/problems/longest-common-prefix/
class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for char in zip(*strs):
            if len(set(char)) == 1:
                prefix += char[0]
            else:
                break
        return prefix
        