def maxk(massiv, k):
    n=len(massiv)
    if k>n:
        return None
    nsum=0
    for i in range(k):
        nsum=nsum+massiv[i]

    msum = nsum
    for i in range(k, n):
        nsum=nsum+massiv[i]- massiv[i - k]
        if msum>nsum:
            msum=msum
        else:
            msum=nsum
    return msum

n = int(input("длина массива: "))
massiv= []
for b in range(n):
    massiv.append(int(input()))

k = int(input("k="))
print("макс сумма=", maxk(massiv, k))
