def find_saddle_point(arr):
    rows = len(arr)
    columns = len(arr[0])

    for i in range(rows):
        max_row_x = i
        max_row_y = 0

        for j in range(1, columns):
            if arr[i][j] > arr[i][max_row_y]:
                max_row_y = j

        is_saddle_point = True
        for k in range(rows):
            if arr[k][max_row_y] < arr[i][max_row_y]:
                is_saddle_point = False
                break
        
        if is_saddle_point:
            return arr[i][max_row_y]

    return None

rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))

arr = []
for z in range(rows):
    arr.append(list(map(int, input().split())))

print(find_saddle_point(arr))
