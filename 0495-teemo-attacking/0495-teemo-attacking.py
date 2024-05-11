from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total_duration = 0
        for i in range(1, len(timeSeries)):
            diff = timeSeries[i] - timeSeries[i - 1]
            total_duration += min(diff, duration)
        
        # Add duration for the last attack
        total_duration += duration
        
        return total_duration

