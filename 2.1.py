def maxk(arr, k):
    max_sum = float('-inf')
    if k<len(arr):
        for i in range(len(arr) - k + 1):
            cursum = sum(arr[i:i+k])  

        if cursum > max_sum:
            max_sum = cursum
        return max_sum
    

arr = list(map(int, input("введите элементы массива: ").split()))
k = int(input("введите число последовательных элементов: "))

if k<len(arr):
    result = maxk(arr, k)
    print("макс сумма", k, "последовательных элементов:", result)
else:
    print("введите другие значения")
