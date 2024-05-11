class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        # Define a mapping for hexadecimal digits
        hex_map = '0123456789abcdef'
        
        # Convert negative numbers to their two's complement representation
        if num < 0:
            num += 2 ** 32
        
        hex_string = ''
        
        while num:
            # Get the remainder when dividing by 16
            remainder = num % 16
            # Append the corresponding hexadecimal digit to the front of the string
            hex_string = hex_map[remainder] + hex_string
            # Update num by integer division by 16
            num //= 16
        
        return hex_string


