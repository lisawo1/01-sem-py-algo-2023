def evaluate_expression(a, b, m):
    binary_b = bin(b)[2:]  # перевожу в двоичную
    result = 0

    for digit in binary_b:
        result = (result * a + int(digit)) % m

    return result

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
m = int(input("Enter the value of m: "))

result = evaluate_expression(a, b, m)
print("Result:", result)
