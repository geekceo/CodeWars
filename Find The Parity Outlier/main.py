from collections import Counter

def find_outlier(integers):
    return integers[[i % 2 == 0 for i in integers].index(Counter([i % 2 == 0 for i in integers]).most_common()[-1][0])]