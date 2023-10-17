class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        if n == 4 or n < 10:
            return False

        happy = 0
        while True:
            for i in str(n):
                happy += int(i) ** 2
            
            if happy == 1 or happy == 7:
                return True
            if happy == 4 or happy < 10:
                return False
            
            n, happy = happy, 0