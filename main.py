arr1 = [1, 2, 3]


def arr_new_plus_1(arr1: list) -> list:
    arr = [1 * (10 ** num) for num in range(len(arr1) - 1, 0, -1)]
    arr.append(1)

    number = 0
    for item in range(len(arr1)):
        if item == len(arr1) - 1:
            number += (arr1[item] + 1) * arr[item]
        else:
            number += arr1[item] * arr[item]

    new_arr = [0 * num for num in range(len(arr1))]

    for item in range(len(new_arr)):
        item_number = number % 10
        number = number // 10
        new_arr[item] = item_number

    new_arr.sort()
    return new_arr

print(arr_new_plus_1(arr1))
