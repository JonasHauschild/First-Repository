class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        res = ''
        strs = sorted(strs)     # Wenn liste mit Wörtern sortiert wird, muss ein Abgleich nur zwischen dem ersten und dem letzten Wort der Liste erfolgen
        for i in strs[0]:
            if strs[-1].startswith(res+i):
                res += i
            else:
                break
        return res


liste = ['Schreiben', 'Saufen', 'Schreibe']

a = Solution()

print(a.longestCommonPrefix(liste))