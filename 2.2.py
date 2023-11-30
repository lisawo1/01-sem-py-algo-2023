def sieveOfEratosthenes(x):
    primes=[]
    for i in range (x+1):
        primes.append(i)
    primes[1] = 0
    i = 2
    while i <= x:
        if primes[i] != 0:
            j = i + i
            while j <= x:
                primes[j] = 0
                j = j + i
        i += 1
    primes = [i for i in primes if i != 0]
    return primes


def divisor(x):
    primes = sieveOfEratosthenes(x)
    gr_divisor = 1
    for prime in primes:
        if x % prime == 0:
            gr_divisor = prime

    return gr_divisor


x = int(input("Введите число: "))
gr_divisor = divisor(x)
print(f"наибольший простой делитель - {gr_divisor}")


