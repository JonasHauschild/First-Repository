class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        liste = list(s)
        test = [dic.get(n, n) for n in liste]
        n = len(test)
        for i in range(1,n):
            if test[i] > test[i-1]:
                test[i] = test[i] - test[i-1]
                test[i-1]=0
        return(sum(test))

a = Solution()

s = 'VIII'

print(a.romanToInt(s))

