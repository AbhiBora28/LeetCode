class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_number(num):
            next_num = 0
            while num > 0:
                digit = num % 10
                next_num += digit * digit
                num //= 10
            return next_num
        
        slow_ptr = n
        fast_ptr = get_next_number(n)
        
        while fast_ptr != 1 and slow_ptr != fast_ptr:
            slow_ptr = get_next_number(slow_ptr)
            fast_ptr = get_next_number(get_next_number(fast_ptr))
        
        return fast_ptr == 1


