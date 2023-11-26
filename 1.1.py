def polinomial(arr, x):
    result=arr[0]*x
    result+=arr[1]
    for num in range(2,len(arr)):
        result = result * x + arr[num]

    return result

def derivative(arr, x):
    proizv=n*arr[0]
    for i in range(1, n):
         proizv= proizv * x + (n-i) * arr[i]
    
    return proizv
arr = []
n = int(input("n: "))
x = int(input("x: "))
for a in range(n + 1):
    b = "Введите коэф " + "x в степени " +str(n - a)
    arr.append(int(input(b)))





print("f(x) = ",polinomial(arr, x))
print("f'(x) = ", derivative(arr, x))
