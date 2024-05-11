class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        
        while i >= 0 or j >= 0:
            digit_sum = carry
            if i >= 0:
                digit_sum += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                digit_sum += ord(num2[j]) - ord('0')
                j -= 1
            
            carry = digit_sum // 10
            digit_sum %= 10
            result.append(str(digit_sum))
        
        if carry:
            result.append(str(carry))
        
        return ''.join(result[::-1])

