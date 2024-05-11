class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        
        hex_map = '0123456789abcdef'
        
       
        if num < 0:
            num += 2 ** 32
        
        hex_string = ''
        
        while num:
           
            remainder = num % 16
           
            hex_string = hex_map[remainder] + hex_string
           
            num //= 16
        
        return hex_string


