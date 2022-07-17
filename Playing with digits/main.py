def dig_pow(n, p):
    a = list()
    d = dict(zip([i for i in range(p, len(list(str(n)))+p)], [int(i) for i in list(str(n))]))
    for k, v in d.items():
        a.append(v ** k)
    if int(sum(a)/n) == float(sum(a)/n) : return int(sum(a)/n)
    return -1