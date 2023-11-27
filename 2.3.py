def find_saddle_point(arr):
    rows = len(arr)
    columns = len(arr[0])

    for i in range(rows):
        saddle_point_row = i
        saddle_point_columns = 0

        for j in range(1, columns):
            if arr[i][j] < arr[saddle_point_row][saddle_point_columns]:
                saddle_point_row = i
                saddle_point_columns = j

        for k in range(rows):
            if arr[k][saddle_point_columns] > arr[saddle_point_row][saddle_point_columns]:
                saddle_point_row = -1
                break

        if saddle_point_row != -1:
            return saddle_point_row, saddle_point_columns

    return None

rows=int(input())
columns = int(input())

arr = []
for z in range(rows):
    arr.append(list(map(int, input().split())))

print(find_saddle_point(arr))

