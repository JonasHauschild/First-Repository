def longest_prefix(strs):
    if len(strs) == 0:
        return ''
    strs = sorted(strs)     # Wenn liste mit Wörtern sortiert wird, muss ein Abgleich nur zwischen dem ersten und dem letzten Wort der Liste erfolgen
    res = ''

    for i in strs[0]:
        if strs[-1].startswith(res + i):
            res += i
        else:
            break
    return res


strs = ['Schreiben', 'Saufen', 'Schießen']

print(longest_prefix(strs))
