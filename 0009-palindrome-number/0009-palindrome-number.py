class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        i = 0
        while i < len(y) // 2:
            if y[i] == y[-i - 1]:
                i += 1
            else:
                return False
        return True
