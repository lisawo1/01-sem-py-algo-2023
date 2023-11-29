def resheto(x = int): 
    array = [i for i in range(2, x + 1)]
    for i in range(2, (x // 2) + 1):
        p = 2
        if array:
            while max(array) >= (i * p):
                if (i * p) in array:
                    array.remove(i * p)
                p += 1
                if not array:
                    break
    return array

def found_prime_div(x = int):
    array = resheto(x)
    for i in array[::-1]:
        if (x % i) == 0:
            return i

if __name__ == "__main__":
    x = int(input())
    print(found_prime_div(x))
