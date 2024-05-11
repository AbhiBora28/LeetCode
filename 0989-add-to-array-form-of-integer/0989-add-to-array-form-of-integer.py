class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        carry = 0
        i = len(num) - 1
        
        while i >= 0 or k > 0:
            digit_sum = carry
            if i >= 0:
                digit_sum += num[i]
                i -= 1
            if k > 0:
                digit_sum += k % 10
                k //= 10
            
            carry = digit_sum // 10
            digit_sum %= 10
            result.append(digit_sum)
        
        if carry:
            result.append(carry)
        
        return result[::-1]

