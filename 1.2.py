def evaluate_expression(a, b, m):
    bb = bin(b)[2:]  # перевожу в двоичную
    result = 0

    for i in bb:
        result = (result * a + int(i)) % m

    return result

a = int(input("введите a "))
b = int(input("введите b "))
m = int(input("введите m "))

result = evaluate_expression(a, b, m)
print("Result:", result)
