class Solution:
    def isValid(self, str) -> bool:

        dic = {'(' : 1, ')' : 2,'[' : 3,']' : 4, '{' : 5, '}' : 6}

        n = len(str)
        liste = list()
        liste_1_2 = list()
        liste_3_4 = list()
        liste_5_6 = list()

        if n % 2 != 0:
            print(False)
        else:
            for i in range(0,n):
                if str[i] in dic.keys():
                    liste.append(dic.get(str[i]))
        m = len(liste)

        for i in range(0,m):
            if liste[i] == 1:
                liste_1_2.append(liste[i])
            elif liste[i] == 2:
                liste_1_2.append(liste[i])
            elif liste[i] == 3:
                liste_3_4.append(liste[i])
            elif liste[i] == 4:
                liste_3_4.append(liste[i])
            elif liste[i] == 5:
                liste_5_6.append(liste[i])
            elif liste[i] == 6:
                liste_5_6.append(liste[i])
        a = len(liste_1_2)
        b = len(liste_3_4)
        c = len(liste_5_6)
        ergebnis_1_2 = 0
        ergebnis_3_4 = 0
        ergebnis_5_6 = 0
        for i in range(0,a-1):
            if liste_1_2[i] + liste_1_2[i+1] == 3:
                ergebnis_1_2 += 1
        for i in range(0,b-1):
            if liste_3_4[i] + liste_3_4[i+1] == 7:
                ergebnis_3_4 += 1
        for i in range(0,c-1):
            if liste_5_6[i] + liste_5_6[i+1] == 11:
                ergebnis_5_6 += 1
        if ergebnis_1_2 == a-1:
            if ergebnis_3_4 == b-1:
                if ergebnis_5_6 == c-1:
                    return True
                else:
                    return False

a = Solution()

str = '()'

print(a.isValid(str))