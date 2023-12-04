def polinomial(arr, x):
    result=arr[0]*x+arr[1]
    for i in range(2,len(arr)):
        result = result * x + arr[i]
    return result

def derivative(arr, x):
    proizv=n*arr[0]
    for i in range(1, n):
         proizv= proizv * x + (n-i) * arr[i]
    
    return proizv

arr = []
n = int(input("введите n: "))
x = int(input("введите x: "))
for a in range(n + 1):
    b = "Введите коэф перед x^" +str(n - a)+" "
    arr.append(int(input(b)))





print("значение многочлена = ",polinomial(arr, x))
print("производная = ", derivative(arr, x))
