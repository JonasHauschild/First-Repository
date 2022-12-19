class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        # Der Funktion wird ein String (Roman) übergeben, woraufhin ein Integer zurückgegeben wird
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        liste= list(s)
        print(liste)
        test = [dic.get(n, n) for n in liste]
        # methode get() gibt den Wert eines dictionaries für bestimmte Values zurück
        n = len(test)
        for i in range(1,n):
            if test[i] > test[i-1]:
                test[i] = test[i] - test[i-1]
                test[i-1] = 0
        return (sum(test))

s = 'XLIV'
print(Solution.romanToInt(s))
