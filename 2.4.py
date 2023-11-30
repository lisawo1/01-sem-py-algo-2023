def revarray(array):
  return array[::-1]

a = int(input("Введите размер массива: "))
array = []
for i in range(a):
    array.append(int(input()))
print(revarray(array))
