from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                ranges.append(self.formatRange(start, nums[i - 1]))
                start = nums[i]
        
        ranges.append(self.formatRange(start, nums[-1]))
        
        return ranges
    
    def formatRange(self, start, end):
        if start == end:
            return str(start)
        else:
            return str(start) + "->" + str(end)

