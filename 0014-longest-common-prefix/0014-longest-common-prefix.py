from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
       
        for i, char in enumerate(strs[0]):
            # Check if the character matches in all other strings
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    # Return the prefix found so far
                    return strs[0][:i]
        
       
        return strs[0]



        