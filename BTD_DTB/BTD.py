def binary_to_decimal(b):
    l = []
    a = 0
    x = []
    for i in str(b):
        l.append(i)
    x = l[::-1]
    for j in range(len(x)):
        a = ((int(x[j])) * (2 ** j)) + a
    return a
