def getprimefactors(n):
    primfactorlist = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfactorlist.append(d)  # Assuming you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfactorlist.append(n)
    return primfactorlist
