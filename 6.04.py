def egcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, q =egcd(b, a%b)
    x, y = y, (x-a//y * b)
    return x, y, q


from egcd import egcd


def teorem_chinese(pairs):
    nd1, nd2 = [p[0] for p in pairs], [p[1] for p in pairs]
    M1 = nd2[1] * nd2[2]
    M2 = nd2[2] * nd2[0]
    M3 = nd2[0] * nd2[1]
    x1 = egcd(M1, nd2[0])[1] % nd2[0]
    x2 = egcd(M2, nd2[1])[1] % nd2[1]
    x3 = egcd(M3, nd2[2])[1]% nd2[2]
    sz = nd2[0]*nd2[1]*nd2[2]
    x = (x1*nd1[0]*M1+x2*nd1[1]*M2+x3*nd1[2]*M3)%sz
    return x

print(teorem_chinese([(2,3),(1,4), (3,5)]))