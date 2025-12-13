class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        count = set()
        for num in nums:
            if num in count:
                return num
            else:
                count.add(num)
        return 0
