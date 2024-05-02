class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert integer to string
        x_str = str(x)
        # Compare the string with its reverse
        return x_str == x_str[::-1]

