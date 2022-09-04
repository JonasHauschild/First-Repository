class Solution:
    def isPalindrome(self, x: int) -> bool:
        liste = list(str(x))
        n = len(liste)
        neu = []
        index = n - 1
        while index >= 0:
            neu.append(liste[index])
            index = index - 1
        if liste == neu:
            return True
        else:
            return False

a = Solution()

print(a.isPalindrome(66666666666666))