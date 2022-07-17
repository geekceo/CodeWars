from collections import Counter

def find_uniq(arr):
    return Counter(arr).most_common()[-1][0]