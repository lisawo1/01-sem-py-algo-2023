def sieveOfEratosthenes(limit):
    isPrime = [True] * (limit + 1)
    primes = []

    for i in range(2, int(limit ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, limit + 1, i):
                isPrime[j] = False

    for i in range(2, limit + 1):
        if isPrime[i]:
            primes.append(i)

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
