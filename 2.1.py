def maxk(arr, k):
    n = len(arr)
    max_sum = float('-inf')  
    for i in range(n - k + 1):
        current_sum = sum(arr[i:i+k])  

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum



size = int(input("введите длину массива: "))
arr = list(map(int, input("введите элементы массива: ").split()))
k = int(input("введите число последовательных элементов: "))


result = maxk(arr, k)
print("макс сумма", k, "последовательных элементов:", result)

