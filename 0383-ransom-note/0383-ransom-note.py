from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = dict(Counter(ransomNote))
        magazine = dict(Counter(magazine))
        for a, c in ransomNote.items():
            if a in magazine:
                if magazine[a] < c:
                    return False
            else:
                return False
        return True
            
