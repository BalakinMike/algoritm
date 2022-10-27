def sum_recurs(arr):
    if len(arr) == 1:
        res = arr[0]
        return res
    else:
        arr_1 = arr[1:len(arr)]
        res = arr[0] + sum_recurs(arr_1)
        return res

arr = [1, 2, 3, 4, 5, 6]

print (sum_recurs(arr))