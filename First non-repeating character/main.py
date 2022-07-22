from collections import Counter

def first_non_repeating_letter(string):
    d = Counter(string)
    for k in d.keys():
        if k.islower() and k.upper() in d.keys():
            d[k] += d[k.upper()]
            d[k.upper()] = d[k]
    return [i for i in string if d[i] == 1][0] if string and (1 in d.values()) else ''