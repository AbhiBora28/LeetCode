from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_length = 0
        
        for word in words:
            word_count = Counter(word)
            valid_word = True
            for char, count in word_count.items():
                if char not in chars_count or count > chars_count[char]:
                    valid_word = False
                    break
            if valid_word:
                total_length += len(word)
        
        return total_length

\