class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left, right = 2, num // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_square = mid * mid
            
            if mid_square == num:
                return True
            elif mid_square < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

