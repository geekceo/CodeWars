def tribonacci(signature, n):
    a = signature
    for i in range(len(signature), n):
        a.append(sum(signature[i-3:i]))
    return a[:n]